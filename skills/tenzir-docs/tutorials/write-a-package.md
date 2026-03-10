# Write a package


This tutorial teaches you how packages bundle pipelines, operators, contexts, and examples. You’ll build a package for an SSL blacklist that detects malicious certificates. You can then [install packages](../guides/packages/install-a-package.md) from the [Tenzir Library](https://app.tenzir.com/library) or deploy them as code.

## Map the use case

We’ll pick an example from the SecOps space: detect malicious certificates listed on the [SSLBL blocklist](https://sslbl.abuse.ch/).

This involves three primary actions:

1. Build a lookup table of SHA-1 hashes that mirror SSLBL data.
2. Extract SHA1 hashes of certificates in OCSF Network Activity events and compare them against the lookup table.
3. Tag matching events with the OCSF OSINT profile, so that downstream tools can escalate the match into an alert or detection finding.

We’ll begin with the managing the lookup table. But first we need to get the package scaffolding in place.

## Create the package scaffold

Create a directory named `sslbl` and add the standard package layout:

* sslbl/

  * changelog/ User-facing documentation of changes

    * …

  * examples/ Runnable snippets for users

    * …

  * operators/ Reusable building blocks for pipelines

    * …

  * pipelines/ Deployable pipelines

    * …

  * tests/ Integration tests

    * …

  * package.yaml Manifest: metadata, contexts, and inputs

## Add the package manifest

The [`package.yaml`](https://docs.tenzir.com/packages/sslbl/package.yaml) is the **package manifest**. I contains descriptive metadata, but also the definitions of contexts and inputs, as we shall see below.

### Add descriptive metadata

sslbl/package.yaml

```yaml
name: SSLBL
author: Tenzir
author_icon: https://github.com/tenzir.png
package_icon: |
  https://raw.githubusercontent.com/tenzir/library/main/sslbl/package.svg
description: |
  The [SSLBL](https://sslbl.abuse.ch/) package provides a lookup table with
  SHA1 hashes of blacklisted certificates for TLS monitoring use cases.
```

### Define the lookup table context

Next, add a lookup table context to the manifest. The node creates the context when you install the package.

sslbl/package.yaml

```yaml
contexts:
  sslbl:
    type: lookup-table
    description: |
      A table keyed by SHA1 hashes of SSL certificates on the SSL blocklist.
```

## Add user-defined operators

Packages give you the ability to implement **user-defined operators** that live right next to Tenzir’s [built-in operators](../reference/operators.md). These custom operators are an essential capability to scale your data processing, as you can break down complex operations into smaller, testable building blocks.

### Create the user-defined operators

First, we create an operator that fetches the latest SSL blocklist from the [SSLBL](https://sslbl.abuse.ch/) website. The operator in (/packages/sslbl/operators/fetch.tql) looks as follows:

operators/fetch.tql

```tql
from_http "https://sslbl.abuse.ch/blacklist/sslblacklist.csv" {
  read_csv comments=true, header="timestamp,SHA1,reason"
}
```

The relative path in the packagage defines the operator name. After installing the package, you can call this operator via `sslbl::fetch`. It will produce events of this shape:

```tql
{
  timestamp: 2014-05-04T08:09:56Z,
  SHA1: "b08a4939fb88f375a2757eaddc47b1fb8b554439",
  reason: "Shylock C&C",
}
```

Let’s create another operator to map this data to [OSINT objects](https://schema.ocsf.io/1.6.0/objects/osint)—the standardized representation of an indicators of compromise (IOCs) in OCSF.

operators/ocsf/to\_osint.tql

```tql
confidence = "High"
confidence_id = 3
created_time = move timestamp
malware = [{
  classification_ids: [3],
  classifications: ["Bot"],
  // The source lists the name as "$NAME C&C" and we drop the C&C suffix.
  name: (move reason).split(" ")[0],
}]
value = move SHA1
type = "Hash"
type_id = 4
```

This pipeline translates the original feed into this shape:

```tql
{
  confidence: "High",
  confidence_id: 3,
  created_time: 2014-05-04T08:09:56Z,
  malware: [
    {
      classification_ids: [
        3,
      ],
      classifications: [
        "Bot",
      ],
      name: "Shylock",
    },
  ],
  value: "b08a4939fb88f375a2757eaddc47b1fb8b554439",
  type: "Hash",
  type_id: 4,
}
```

OCSF Verbosity

You may notice that this shape is a lot more verbose than the original event. Don’t worry, it is absolutely normal when upgrading your raw data to a semantically richer representation like OCSF. You can always trim the feed down again later, either automatically with our [`ocsf::trim`](../reference/operators/ocsf/trim.md) operator or manually by [`drop`](../reference/operators/drop.md)ping fields. But while the data is in motion, the additional semantics unlock generic analytics when the context of the original source is long gone.

We’re not done yet. Let’s create one final operator that wraps a single fetch into an OCSF event that describes a single collection of IoCs: the [OSINT Inventory Info](https://schema.ocsf.io/1.6.0/classes/osint_inventory_info) event.

operators/ocsf/to\_osint\_inventory\_info.tql

```tql
// Collect a single fetch into an array of OSINT objects.
summarize osint=collect(this)
// Categorization
activity_id = 2
activity_name = "Collect"
category_uid = 5
category_name = "Discovery"
class_uid = 5021
class_name = "OSINT Inventory Info"
severity_id = 1
severity = "Informational"
type_uid = class_uid * 100 + activity_id
// Additional context attributes
actor = {
  app_name: "Tenzir"
}
metadata = {
  product: {
    name: "SSLBL SSL Certificate Blacklist",
    vendor_name: "abuse.ch",
  },
  version: "1.6.0",
}
// Occurence attributes
time = now()
// Apply Tenzir event metadata
@name = "ocsf.osint_inventory_info"
```

We can now call all three operators in one shot to construct an OCSF event:

```tql
sslbl::fetch
sslbl::ocsf::to_osint
sslbl::ocsf::to_osint_inventory_info
```

Now that we have building blocks, let’s combine them into something meaningful.

OCSF Mapping Tutorial

Mapping data to OCSF can feel like a daunting task. Check out our [dedicated tutorial OCSF mapping](map-data-to-ocsf.md) where we cover OCSF at great length.

### Add arguments to your operators

So far, our operators are static—they always do the same thing. You can make them more flexible with parameterized operators that accept positional and named arguments, just like built-in operators.

For example, an operator that tags events with threat metadata could accept a configurable confidence level and source name. See [Add operators](../guides/packages/add-operators.md) for the full parameter reference, including supported types and examples.

## Add deployable pipelines

With our operators in place, we can now create deployable pipelines. Packages that include pipelines execute on installation, which is useful for background tasks like periodic data fetching. To ship a pipeline as a template that users must explicitly enable, add `disabled: true` to the frontmatter. See [Add pipelines](../guides/packages/add-pipelines.md) for all frontmatter options.

The `sslbl::fetch` operator just downloads the blacklist entries once. But the remote data source changes periodically, and we want to always work with the latest version. So we turn the one-shot download into a continuous data feed using the [`every`](../reference/operators/every.md) operator:

sslbl/pipelines/publish-as-ocsf.tql

```tql
---
name: Publish SSLBL as OCSF
description: >
  Fetches the SSL blocklist hourly and publishes OCSF Inventory Info
  events to the `ocsf` topic.
disabled: true
---


every 1h {
  sslbl::fetch
}
sslbl::ocsf::to_osint
sslbl::ocsf::to_osint_inventory_info
publish "ocsf"
```

This is a closed pipeline, meaning, it has an input operator ([`every`](../reference/operators/every.md)) and an output operator ([`publish`](../reference/operators/publish.md)). The pipeline produces a new OCSF Inventory Info event every hour and publishes it to the `ocsf` topic so that other pipelines in the same node can consume it. This is a best-practice design pattern to expose data that you may reuse multiple times.

But instead of publishing the data as OCSF events and subscribing to it afterwards, we can directly update the lookup table from the plain OSINT objects:

sslbl/pipelines/update-lookup-table.tql

```tql
---
name: Update SSLBL Lookup Table
description: >
  Fetches the SSL blocklist hourly and updates the sslbl lookup table
  with OCSF OSINT objects keyed by indicator value.
disabled: true
---


every 1h {
  sslbl::fetch
}
sslbl::ocsf::to_osint
context::update "sslbl", key=value
```

Thanks to our user-defined operators, implementing these two different pipelines doesn’t take much effort.

## Add examples

To illustrate how others can use the package, we encourage package authors to add a few TQL snippets to the `examples` directory in the package.

### Example 1: One-shot lookup table update

Here’s a snippet that perform a single fetch followed by an update of the lookup table:

examples/one-shot-update.tql

```tql
---
description: |
  This example demonstrates how to fetch SSLBL data, convert it to OSINT format,
  and update the context with the new data.
---


sslbl::fetch
sslbl::ocsf::to_osint
context::update "sslbl", key=value
```

### Example 2: Enrich with the context

What do we do with feed of SHA1 hashes that correspond to bad certificates? One natural use case is to look at TLS traffic and compare these values with the SHA1 hashes in the feed.

Here’s a pipeline for this:

examples/enrich-network-activity.tql

```tql
---
description: |
  Subscribe to all OCSF events and extract those network events containing SHA-1
  certificate hashes. Correlate those events with the SSLBL database and attach
  the OSINT profile to matching events.
---


subscribe "ocsf"
where category_uid == 4
// Filter out network events that have SHA1 certificate hashes.
where not tls?.certificate?.fingerprints?.where(x => x.algorithm_id == 2).is_empty()
// Convert the list of SHA1 hashes into a record for enrichment. In the future,
// we'd want to enrich also within arrays. When we unroll we unfortunately lose
// all other certificate hash values, so this is sub-optimal.
unroll tls.certificate.fingerprints
enrich "sslbl",
  key=tls.certificate.fingerprints.value,
  into=_tmp
// Slap OSINT profile onto the event on match.
if _tmp != null {
  osint.add(move _tmp)
  metadata.profiles?.add("osint")
} else {
  drop _tmp
}
publish "ocsf-osint"
```

This pipelines hones in on OCSF Network Activity events (`category_uid == 4`) that come with a SHA1 TLS certificate fingerprint (`algorithm_id == 2`). If we have a matche, we add the `osint` profile to the event and publish it to separate topic `ocsf-osint` for further processing.

### Example 3: Show a summary of the dataset

examples/top-malware.tql

```tql
---
description: |
  Inspect all data in the context and count the different malware types,
  rendering the result as a pie chart.
---


context::inspect "sslbl"
select malware = value.malware[0].name
top malware
chart_pie x=malware, y=count
```

## Make your package configurable

**Inputs** let users customize package behavior without editing files. For example, to make the refresh interval configurable, replace the hard-coded value with `{{ inputs.refresh_interval }}`:

sslbl/pipelines/update-as-ocsf.tql

```tql
every {{ inputs.refresh_interval }} {
  sslbl::fetch
}
sslbl::ocsf::to_osint
context::update "sslbl", key=value
```

Define the input in `package.yaml` with a default value, then users can override it during installation. See [Configure inputs](../guides/packages/configure-inputs.md) for the full templating guide.

## Test your package

Testing ensures that you always have a working package during development. The earlier you start, the better!

### Add tests for your operators

Since our package ships with user-defined operators, we highly recommend to write tests for them:

1. You help users gain confidence in the functionality.
2. You provide illustrative input-output pairs.
3. You evolve faster with less regressions.

Each test consists of a `.tql` file with the test pipeline, an optional `.input` file with test data, and a `.txt` file with the expected output baseline. Access the input file via `from_file env("TENZIR_INPUT")`.

Let’s test the operator that maps our input to OCSF OSINT objects:

tests/ocsf/to\_osint.tql

```tql
from_file env("TENZIR_INPUT") {
  read_csv comments=true, header="timestamp,SHA1,reason"
}
sslbl::ocsf::to_osint
```

We first watch the terminal output it in passthrough mode:

```sh
uvx tenzir-test --passthrough
```

tests/ocsf/to\_osint.txt

```tql
{
  confidence: "High",
  confidence_id: 3,
  created_time: 2025-10-08T06:32:12Z,
  malware: [
    {
      classification_ids: [
        3,
      ],
      classifications: [
        "Bot",
      ],
      name: "Vidar",
    },
  ],
  value: "e8f4490420d0b0fc554d1296a8e9d5c35eb2b36e",
  type: "Hash",
  type_id: 4,
}
```

As expected, a valid OCSF OSINT object. Let’s confirm this as our new baseline:

```sh
uvx tenzir-test --update
```

This created a [`to_osint.txt`](https://docs.tenzir.com/packages/sslbl/tests/ocsf/to_osint.txt) file next to the [`to_osint.tql`](https://docs.tenzir.com/packages/sslbl/tests/ocsf/to_osint.tql.md) file. Future runs will use this baseline for comparisons.

Continue to test the remaining operators, or add additional tests for some examples.

### Test contexts and node interaction

Our package defines a context that lives in a node. To test node interactions, use a **suite** that spins up a fixture and runs tests sequentially against it. Add a `test.yaml` file to a subdirectory that represents the suite:

* sslbl/tests/context/

  * 01-context-list.tql
  * 02-context-update.tql
  * 03-context-inspect.tql
  * test.yaml

The suite updates the lookup table and verifies the expected values. See [Test packages](../guides/packages/test-packages.md) for suite configuration and [Add contexts](../guides/packages/add-contexts.md) for context-specific testing patterns.

## Add a changelog

Creating a package is rarely a one-time act. Vendors make upstream changes, you find corner cases, and users request new features. Do your users a favor and maintain a changelog!

From the package directory, create a new entry with [`tenzir-ship`](../reference/ship-framework.md):

```sh
uvx tenzir-ship add
```

The interactive wizard guides you through the process. See [Maintain a changelog](../guides/packages/maintain-a-changelog.md) for the full release workflow.

## Share and contribute

Phew, you made it! You now have a reusable package. 🎉

Now that you have a package, what’s next?

1. Join our [Discord server](https://docs.tenzir.com/discord) and showcase the package in the `show-and-tell` channel to gather feedback.
2. If you deem it useful for everyone, open a pull request in our [Community Library on GitHub](https://github.com/tenzir/library). Packages from this library appear automatically in the [Tenzir Library](https://app.tenzir.com/library).
3. Spread the word on social media and tag us so we can amplify it.

AI-based package creation

It’s quite a bit of work to manually create a package. In the age of AI and modern agentic tooling, you have powertools available to fully automate this task.