---
title: "Manage packages"
description: "Install, update, and override the packages your configuration uses, and create, release, and share packages of your own."
canonical: https://tenzir.com/docs/guides/manage-packages
source: https://tenzir.com/docs/guides/manage-packages.md
section: "Docs"
---

# Manage packages

> Install, update, and override the packages your configuration uses, and create, release, and share packages of your own.

Packages bundle the operators and constants that turn a use case, such as onboarding a firewall, into a few lines of TQL. This guide covers both sides: using packages in your configuration, from the first install to updates and rollbacks, and building packages of your own, from the first operator to a release that others install.

Before you begin

* To use packages, your role needs **Configuration** → **Read** and **Write**, plus **Configuration** → **Deploy** to take a change to a deployment. Our [IAM reference](../reference/iam.md#permissions-in-the-app) lists the details.
* On the command line, sign in, select a workspace with `tenzir use`, and clone its configuration with `tenzir config clone`. The package commands change nothing on the platform until you push.
* To build packages, install Git and [`uv`](https://docs.astral.sh/uv/), which runs `tenzir-test` and `tenzir-ship` through `uvx`.

## Install a package

You install a package by adding it to the dependencies of your workspace’s configuration. The configuration’s `package.yaml` lists the packages its pipelines use, `package.lock` pins their exact versions, and the next deploy ships them to your deployments.

### Find a package

Our [library catalog](https://tenzir.com/product/library) lists every released package of our library with the use cases it covers and its operators. You can also search from where you work:

* MCP

  Ask your agent:

  ```prompt
  Which packages of the Tenzir library help me onboard Suricata and map it to OCSF?
  ```

* App

  Open **Packages**. The **Available** tab shows the packages your configuration doesn’t use yet, and the search box filters them.

* CLI

  Search the library by id, name, description, and category:

  ```sh
  tenzir package search ocsf
  ```

  Without a query, the command lists every package.

### Add a package

Adding a package writes the dependency to `package.yaml` and locks it, and every package it needs, in `package.lock`:

* MCP

  Ask your agent:

  ```prompt
  Add the suricata package to my configuration on main, lock it, and commit the change.
  ```

  The agent adds the package to your draft of the branch and locks it there, as the app does. Review the draft in the app before the agent commits it.

* App

  1. Open **Packages** with the branch of your configuration selected.
  2. Select a package, and pick a version. The latest version accepts the compatible releases after it too, as in `^1.2.0`, while an older version pins your configuration to exactly that one, as in `=1.1.0`.
  3. Select **Add**. The platform writes the dependency to `package.yaml` and locks it in `package.lock`, both in your draft of the branch.
  4. Commit the draft from the top bar.

* CLI

  From inside your working copy, add the package:

  ```sh
  tenzir package add suricata
  ```

  A new workspace’s configuration starts empty. If your working copy has no `package.yaml` yet, create one that lists no dependencies first:

  ```sh
  echo 'dependencies: {}' > package.yaml
  ```

  The command accepts the newest release and the compatible ones after it, as in `^0.2.0`. To accept other versions, name a requirement:

  ```sh
  tenzir package add suricata@^0.1
  ```

  Then commit and push the change:

  ```sh
  tenzir config apply -m 'Add the suricata package'
  ```

A requirement has exactly one operator: `^` for compatible releases, `~` for patch releases, `=` for one exact version, or `*` for any. Our reference on [version requirements](../reference/dependencies.md#version-requirements) lists the rules, including how a caret behaves before version 1.0.

The commit alone changes nothing on a deployment. Deployments that track the branch with auto deploy on receive the package with the deploy that the commit starts. Any other deployment receives it once you deploy the commit, as our guide on [deploying the latest commit](change-configurations.md#deploy-the-latest-commit) shows.

### Verify the package

Check that your configuration locks the package and that a deployment can call its operators:

* MCP

  Ask your agent:

  ```prompt
  Which packages does my configuration on main use, at which versions? Then run an ad-hoc pipeline on edge-1 that calls suricata::ocsf::normalize on no events, to check that the deployment knows the operator.
  ```

* App

  The **Installed** tab of the **Packages** page lists the packages your configuration uses, with the version requirement, the locked version, and where each comes from. To check a deployment, run a pipeline that calls the package in the **Explorer**, such as `from {} | head 0 | suricata::ocsf::normalize`.

* CLI

  List what the lock holds:

  ```sh
  tenzir package list
  ```

  Then run a pipeline on the deployment that calls the package without sending it events:

  ```sh
  tenzir run -r 'from {} | head 0 | suricata::ocsf::normalize'
  ```

The pipeline ends without output once the deployment runs the package. Before that, it fails with an error that names the unknown operator. The pipelines of your configuration can now call the package’s operators, such as `suricata::ocsf::normalize`.

### Use a package from another repository

A package does not have to come from our library. Name a Git repository with `--git`, and the command takes the newest release of the package from there:

```sh
tenzir package add acme --git https://github.com/acme/tenzir-packages.git
```

The repository can hold a single package at its root or many packages in folders, and the package id finds the right one. In Tenzir 7.0, the platform fetches packages only from public repositories on GitHub.

A package that must stay private, or that you write for this configuration only, lives under `packages/` in the configuration itself. Declare it with `--path`:

```sh
tenzir package add myteam --path packages/myteam
```

The resulting `package.yaml` shows all three sources:

package.yaml

```yaml
dependencies:
  suricata: ^0.2.0
  acme:
    version: ^0.3.0
    git: https://github.com/acme/tenzir-packages.git
  myteam:
    path: packages/myteam
```

Our reference on [dependency entries](../reference/dependencies.md#entries) lists every key of these forms.

### Remove a package

Remove the calls to the package’s operators first, because a pipeline that still calls one no longer compiles after the next deploy. Then remove the package:

* MCP

  Ask your agent:

  ```prompt
  Remove the acme package from my configuration on main, after checking that no pipeline calls its operators any more.
  ```

* App

  Select **Remove** on the package, then commit the draft from the top bar.

* CLI

  ```sh
  tenzir package remove acme
  tenzir config apply -m 'Remove the acme package'
  ```

Removing drops the package from `package.yaml`, and from `package.lock` together with every package that only it needed.

### Run pipelines with packages locally

Pipelines that you run on your machine with `tenzir run` can call packages too. Run `tenzir package fetch` in your working copy to download the locked packages into a local cache. When you then run a pipeline anywhere inside the working copy, `tenzir run` finds the configuration’s `package.yaml` and reads the packages from the cache:

```sh
tenzir package fetch
tenzir run 'from {} | head 0 | suricata::ocsf::normalize'
```

Run `tenzir package fetch` again whenever the lock changes, such as after a `git pull`.

## Update packages

A new package release never reaches your deployments by itself. Your configuration’s `package.lock` pins every package to one version, and a new version takes an update of the lock, a commit, and a deploy. That way, you decide when a change reaches your pipelines, and you can roll it back.

### Find updates

Updates are the newer releases that a package’s requirement accepts:

* MCP

  Ask your agent:

  ```prompt
  Which packages of my configuration on main have updates?
  ```

* App

  The **Updates** tab of the **Packages** page lists the packages with a newer release that their requirement accepts. A release outside the requirement, such as a new major version, appears only in the version list of the package.

* CLI

  Update the lock in your working copy and look at what changed:

  ```sh
  tenzir package update
  git diff package.lock
  ```

  Nothing reaches a deployment until you push, so you can review the diff and discard it with `git checkout package.lock`.

### Apply updates

An update moves packages to the newest versions that their requirements in `package.yaml` accept, and only `package.lock` changes. Before you commit, read the release notes of each new version on its page in our [library catalog](https://tenzir.com/product/library). A requirement such as `^1.2` lets in data changes, such as a mapping that fills another OCSF attribute, and those can affect detections or dashboards that rely on the events.

* MCP

  Ask your agent:

  ```prompt
  Update the suricata package on main, show me its release notes, and commit the change once I agree.
  ```

* App

  Select **Update** on a package, or **Update all** above the tabs, then commit the draft from the top bar.

* CLI

  Update every package, or only the one you name and the packages it needs, then push:

  ```sh
  tenzir package update suricata
  tenzir config apply -m 'Update the suricata package'
  ```

### Move to an incompatible version

A requirement excludes versions that break the way pipelines call the package, so `^1.2` never updates to 2.0. Before 1.0, every minor version may break callers, so `^0.1` never updates to 0.2 either, and a package at `^0.0.1` takes the same step to reach any newer release. To move on, change the requirement:

* MCP

  Ask your agent:

  ```prompt
  Move the suricata package on main to version 0.2, and show me the breaking changes in its release notes.
  ```

* App

  Pick the new version in the package’s version list and select **Switch to**.

* CLI

  ```sh
  tenzir package add suricata@^0.2
  ```

Check the release notes for the breaking changes, and change the pipelines that call the package in the same commit, so that every pipeline compiles after the deploy. Our explanation of [what a version promises](../explanations/packages.md#what-a-version-promises) lists what counts as a breaking change.

### Pin a package to one version

To keep a package at one version until you decide otherwise, require exactly that version. In the app, picking a version other than the latest pins it. On the command line, name the version with `=`:

```sh
tenzir package add suricata@=0.1.0
```

Updates then leave the package alone until you change the requirement again.

### Roll out and roll back

A deploy compares what each pipeline compiles to and restarts only the pipelines whose compiled form changed with the new versions. A pipeline that doesn’t call an updated package keeps running. Our explanation of [what a deploy guarantees](../explanations/configuration.md#what-a-deploy-guarantees) covers the details.

If an update causes trouble, you have two ways back:

* **Deploy the previous commit** from the history, as our guide on [deploying a revision from history](change-configurations.md#deploy-a-revision-from-history) shows. This is the fast way back, and it sticks only while **Auto deploy** is off for that deployment, because with **Auto deploy** on, the next deploy takes the branch’s latest commit again. The app’s history dialog turns **Auto deploy** off for you; on the command line, turn it off first.
* **Revert the commit** on the branch, as our guide on [reverting a change](change-configurations.md#revert-a-change) shows. The revert restores the old `package.yaml` and `package.lock`, and **Auto deploy** delivers it like any other commit to every deployment that tracks the branch. If you deployed a revision from history first, turn **Auto deploy** on again afterwards.

## Override a package

Sometimes the latest release of a package isn’t what you need: a fix sits on a branch but isn’t released yet, or you need a change that its authors won’t make. You can run a package other than its release in three ways: pin a revision, use a fork, or copy the package into your configuration.

### Pin a revision

To take a package at a commit, tag, or branch instead of a release, name the revision with `--rev`. A branch or tag needs its exact name, and a commit its full 40-character id, because abbreviated ids don’t resolve:

```sh
tenzir package add suricata --rev main
```

Without `--git`, the revision comes from our library. The dependency in `package.yaml` then names the repository explicitly:

package.yaml

```yaml
dependencies:
  suricata:
    git: https://github.com/tenzir/library.git
    rev: main
```

The lock pins the commit that the revision named when you added it, with the version that the `version` field of the package’s `package.yaml` states at that commit. For a branch, `tenzir package update suricata` moves the lock to the branch’s latest commit, and nothing else does. To see which packages a branch holds, released or not, run `tenzir package search --rev main`.

When you’re done, go back to releases with `tenzir package add suricata@^0.2`, which replaces the pinned revision with a requirement.

### Use a fork

To run your own change to a package, fork its repository on GitHub, commit the change to a branch, and depend on the fork:

```sh
tenzir package add suricata \
  --git https://github.com/acme/library.git \
  --rev fix-dns-mapping
```

The fork must be public, because Tenzir 7.0 fetches packages only from public repositories on GitHub.

A source that your configuration names wins for every package that depends on the same package. When another package in your configuration uses `suricata::ocsf::normalize`, it calls the fork too, so one change fixes the operator everywhere. Those packages still check their version requirements against the fork. A revision that isn’t a release takes its version from the `version` field of its `package.yaml`, which still names the release that your branch started from. If a requirement of another package rejects that version, raise it in your fork, such as to `version: "2.0.0"`.

Open a pull request with your change against the original repository, and go back to its releases once it ships. The section on [contributing to the library](manage-packages.md#contribute-to-the-library) covers the pull request for library packages.

### Copy a package into your configuration

A package that you want to change freely, or keep private, can live in your configuration itself. Copy its folder to `packages/<id>/`, then declare it by its path:

```sh
tenzir package add suricata --path packages/suricata
```

The copy is now yours: it changes only when you change it, and every commit of the configuration carries it. Two limits apply:

* No other package may ask for it from a repository. When a package of the library depends on `suricata`, use a fork instead, so that both use the same code.
* You no longer receive releases. To catch up, copy a newer release over your folder and reapply your changes.

## Edit `package.yaml` by hand

The package commands and the app keep `package.yaml` and `package.lock` in step. When you change a requirement in `package.yaml` directly, such as in the app’s file editor, your own editor, or through an agent that edits files, the lock falls behind. The platform refuses to deploy a configuration whose lock doesn’t match its `package.yaml`, so bring the lock in line before you commit:

* MCP

  Ask your agent:

  ```prompt
  I changed package.yaml on main. Sync the package lock and commit both files.
  ```

* App

  The **Packages** page warns about a lock that doesn’t fit `package.yaml`. Select **Sync lock** in the warning, then commit the draft from the top bar.

* CLI

  ```sh
  tenzir package lock
  tenzir config apply -m 'Lock the edited requirements'
  ```

Syncing keeps every locked version that the new requirements still accept and resolves the rest. Our reference on [stale locks](../reference/lock.md#stale-locks) lists when a lock no longer fits.

## Create a package

A package of your own turns the TQL you would otherwise copy between pipelines into operators with names, arguments, and tests. You set up the folder, write the manifest, ship runnable examples, and use the package from a configuration.

### Set up the package folder

Create a folder named after the package’s id, with these files and folders:

* vendor/

  * package.yaml Manifest: descriptive fields, metadata, and dependencies

  * operators/ Reusable building blocks for pipelines

    * …

  * constants.tql Optional values that operators and pipelines share

  * examples/ Runnable snippets for users

    * …

  * tests/ Integration tests

    * inputs/ Sample data for test pipelines

      * …

  * changelog/ Changelog entries and release notes, which `tenzir-ship` writes

    * …

  * package.lock The lock of your dependencies, once you declare one

Only `package.yaml` is required. You create `changelog/` and `package.lock` not by hand: the first `tenzir-ship add` creates the changelog, as the section on [releasing a package](manage-packages.md#release-a-package) shows, and the first `tenzir package add` writes the lock, as the section on [using other packages](manage-packages.md#use-other-packages) shows. Our reference on the [package layout](../reference/directory-layout.md#package) lists what Tenzir reads from each file.

### Add the package manifest

The `package.yaml` file is the **package manifest**. It marks the folder as a package and declares the package’s identity, the metadata that our library catalog and the app’s **Packages** page show, and the other packages it depends on.

#### Add descriptive metadata

Start with the required and recommended metadata fields:

package.yaml

```yaml
# The unique ID of the package, which is also its module name, as in
# `vendor::ocsf::normalize`. Defaults to the name of the folder, but our
# release tool `tenzir-ship` needs it stated.
id: vendor


# The display name of the package (required) and a path to an icon for the
# package.
name: My Package
package_icon: https://example.com/icon.svg


# The display name of the package author and a path to a profile picture.
author: Your Name
author_icon: https://github.com/yourusername.png


# A user-facing description of the package.
description: |
  A brief description of what your package does and the use cases it supports.
  You can use **Markdown** formatting here.


# Tags that the Packages page and our library catalog filter by, such as
# sources, destinations, mappings, or detections.
categories:
  - sources
  - mappings
```

Leave out `version` for now. Cutting the first release with `tenzir-ship` sets it to the released version, as in `version: "0.1.0"`, and every later release raises it, as the section on [releasing a package](manage-packages.md#release-a-package) shows. Our reference on the [package manifest](../reference/manifest.md#package-manifest) lists every field.

#### Add external metadata

The top-level `metadata` field carries data for external tools. Tenzir accepts the field but never interprets its contents.

package.yaml

```yaml
metadata:
  vendor: Vendor
  source: https://github.com/vendor/tenzir-packages
```

Unknown top-level keys fail validation, so put anything Tenzir does not define under `metadata`.

#### Declare dependencies

When your operators call the operators of another package, list that package under `dependencies`, in the same form that a configuration uses:

package.yaml

```yaml
dependencies:
  stix: ^0.0.1
```

Your package sees only its own operators and those of the packages it lists here. The section on [using other packages](manage-packages.md#use-other-packages) shows how to add them with `tenzir package add`, lock them, and run your operators against them.

Write operators, not pipelines

A package provides operators and constants, and the pipelines that run belong to the configuration that uses the package. The deployment refuses a package that contains pipelines. Write an operator for each capability you want to offer, and let the configuration’s pipelines decide where events come from, where they go, and when the operator runs. Anything a caller might vary belongs in an operator argument, which is typed and checked every time the pipeline compiles. The section on [adding operators](manage-packages.md#add-operators) shows how.

### Add examples

The `examples` folder holds self-contained snippets that run after installation. For a package in our library, they appear in our [library catalog](https://tenzir.com/product/library), which makes them the first TQL most users see from your package, so they run on a literal event rather than on live credentials. Start with the shortest path through the package:

examples/basic-usage.tql

```tql
from {message: "2026-01-15T10:30:00Z auth alice success"}
vendor::ocsf::normalize message
```

Then show a snippet per use case the package supports:

examples/alert-on-high-severity.tql

```tql
from {message: "2026-01-15T10:31:00Z auth root failure"}
vendor::ocsf::normalize message
where severity_id >= 4
publish "alerts"
```

One example, one use case. An example that needs a paragraph of setup belongs in a test.

Contexts stay in the configuration

A package carries no contexts, because a context is state that the deployment holds. When your operators enrich events, they refer to contexts by name, and the deployment’s configuration declares them as our guide on [declaring contexts](enrich/declare-contexts.md) shows. Tell users which contexts your package expects, with their names and types, or take the name as an operator argument.

### Use the package in a configuration

A package does nothing until a configuration depends on it. To use it in your own configuration only, put its folder under `packages/` in the configuration and declare it with a `path`:

package.yaml

```yaml
dependencies:
  vendor:
    path: packages/vendor
```

To share it, [contribute it to our library](manage-packages.md#contribute-to-the-library), or [host it in a repository of your own](manage-packages.md#host-a-package-repository) and let configurations depend on it with `git`. Either way, the configuration’s pipelines can then call `vendor::ocsf::normalize`. Our explanation of [packages in a configuration](../explanations/packages.md#packages-in-a-configuration) describes how the platform locks and ships them.

## Add operators

User-defined operators are the heart of a package: each one turns a few lines of TQL into a named building block that pipelines call like a builtin, with typed arguments that the compiler checks. The examples here walk through the common patterns. Our reference on [operator files](../reference/directory-layout.md#operators) lists every frontmatter key, parameter field, type, and rule.

Our tutorial on onboarding a data source puts these patterns to work: it [creates a parser from a pipeline](../tutorials/onboard-a-data-source.md#create-the-parser), [composes a public mapper with internal mapping UDOs](../tutorials/onboard-a-data-source.md#create-the-mapper), and shows how the parse, map, and normalize [layers fit together](../tutorials/onboard-a-data-source.md#fit-it-into-the-data-lifecycle) behind one call.

### Create a user-defined operator

**User-defined operators (UDOs)** are reusable building blocks that you can use in your pipelines. Place operator files in the `operators` folder of your package.

Tenzir names operators using the convention `<package>::[dirs...]::<basename>`. For example, a file at `operators/ocsf/map.tql` in a package with ID `vendor` becomes the operator `vendor::ocsf::map`. The `::` separator forms a [module](../explanations/packages.md#modules), which only packages use, so no builtin can shadow your operators. Our reference on [module names](../reference/directory-layout.md#module-names) lists the rules.

operators/ocsf/auth.tql

```tql
// Normalize authentication logs to OCSF Authentication event class
class_uid = 3002
category_uid = 3
activity_id = 1 if outcome == "success" else 2
actor.user.name = username
actor.user.uid = user_id
src_endpoint.ip = src_ip
dst_endpoint.ip = dst_ip
drop username, user_id, src_ip, dst_ip, outcome
```

After installing the package, use the operator in any pipeline of the configuration:

```tql
from_file "auth.json"
vendor::ocsf::auth
publish "ocsf-events"
```

#### Choose a namespace

Name the package after the vendor and give each of the vendor’s products a folder below it, so operator names read `vendor::product::<operator>`. Our `amazon` package does this: `amazon::vpc_flow::parse_v2` sits next to `amazon::route53::ocsf::map`, and adding another AWS service means adding a folder rather than renaming anything.

Drop the product level when the vendor ships one thing, or when vendor and product are the same name. Our `zeek` package is `zeek::ocsf::map`, not `zeek::zeek::ocsf::map`.

Examples in this guide use the single-level form, as in `vendor::ocsf::map`, because a second placeholder segment adds length without teaching anything. Read them as the one-product case, and insert your product level where a vendor package needs it.

### Add parameters to operators

Operators can accept positional and named arguments, which lets you match the calling conventions of builtin operators. Define the parameters in a YAML frontmatter between two `---` lines at the beginning of the `.tql` file, and refer to each parameter as `$<name>` in the operator’s body. Each parameter takes a `name`, and optionally a `type`, a `description`, and a `default`, as our reference on [operator parameters](../reference/directory-layout.md#parameters) lists.

#### Define positional arguments

Positional arguments are passed in order when calling the operator. Define them under the `args.positional` key:

operators/tag.tql

```tql
---
args:
  positional:
    - name: field
      type: field
    - name: value
      type: string
---


$field = $value
```

Call this operator with positional arguments:

```tql
from {x: 1}
vendor::tag name, "Alice"
```

```tql
{x: 1, name: "Alice"}
```

#### Define named arguments

Named arguments use the `name=value` syntax. Define them under the `args.named` key. A named argument without a `default` is required, so give optional ones a default:

operators/tag.tql

```tql
---
args:
  positional:
    - name: field
      type: field
    - name: value
      type: string
  named:
    - name: prefix
      type: string
      default: ""
---


$field = f"{$prefix}{$value}"
```

Call this operator with both positional and named arguments:

```tql
from {x: 1}
vendor::tag name, "Alice", prefix="User: "
```

```tql
{x: 1, name: "User: Alice"}
```

#### Make arguments optional

Positional arguments with a `default` value become optional. Callers can omit them, and Tenzir substitutes the default. An optional positional parameter must come after the required ones:

operators/greet.tql

```tql
---
args:
  positional:
    - name: name
      type: string
      default: "World"
---


greeting = f"Hello, {$name}!"
```

Calling the operator without arguments uses the default value:

```tql
from {}
vendor::greet
```

```tql
{greeting: "Hello, World!"}
```

Passing an explicit argument overrides the default:

```tql
from {}
vendor::greet "Alice"
```

```tql
{greeting: "Hello, Alice!"}
```

#### Use field parameters

The `field` type enables dynamic field selection. The caller passes a field path, and the operator uses it to read or write data:

operators/double\_value.tql

```tql
---
args:
  positional:
    - name: target
      type: field
---


$target = $target * 2
```

Using the operator:

```tql
from {count: 5, score: 10}
vendor::double_value count
```

```tql
{count: 10, score: 10}
```

To update a child field of the selected target, access it like any other field. Use dot syntax for ordinary field names, string-literal bracket syntax for names with punctuation, or an index expression that resolves to a field name:

operators/tag\_nested.tql

```tql
---
args:
  positional:
    - name: target
      type: field
    - name: name
      type: string
    - name: value
      type: string
---


$target.status = $value
$target["mapped-status"] = $value
$target[$name] = $value
```

Using the operator:

```tql
from {event: {}}
vendor::tag_nested event, "dynamic-status", "ok"
```

```tql
{
  event: {
    status: "ok",
    "mapped-status": "ok",
    "dynamic-status": "ok",
  },
}
```

#### Default to a selector

Field parameters accept a selector as default value, such as `this`, `this.name`, or `foo.bar`. This lets an operator work on the entire event by default and on a specific field on demand:

operators/wrap.tql

```tql
---
args:
  named:
    - name: field
      type: field
      default: this
---


this = {wrapped: $field}
```

Calling the operator without arguments wraps the whole event:

```tql
from {name: "Alice"}
vendor::wrap
```

```tql
{
  wrapped: {
    name: "Alice",
  },
}
```

Passing an explicit selector wraps just that field:

```tql
from {name: "Alice"}
vendor::wrap field=name
```

```tql
{
  wrapped: "Alice",
}
```

#### Detect whether an argument was provided

Any typed parameter supports `default: null`, which makes it optional without a concrete fallback value. Inside the operator body, compare the parameter against `null` to check whether the caller provided it:

operators/tag.tql

```tql
---
args:
  positional:
    - name: field
      type: field
  named:
    - name: suffix
      type: string
      default: null
---


if $suffix != null {
  $field = f"{$field}{$suffix}"
}
```

When the caller omits `suffix`, the operator leaves the field alone:

```tql
from {name: "alice"}
vendor::tag name
```

```tql
{name: "alice"}
```

When the caller provides `suffix`, the operator appends it:

```tql
from {name: "alice"}
vendor::tag name, suffix="@acme"
```

```tql
{name: "alice@acme"}
```

The same works for a `field` parameter that the operator only reads, such as an optional field to take a label from:

operators/label.tql

```tql
---
args:
  named:
    - name: source
      type: field
      default: null
      description: "Optional field to take the label from"
---


label = $source if $source != null else "unknown"
```

Without `source`, the operator falls back to `"unknown"`:

```tql
from {host: "web-1"}
vendor::label
```

```tql
{host: "web-1", label: "unknown"}
```

With `source`, it takes the label from that field:

```tql
from {host: "web-1"}
vendor::label source=host
```

```tql
{host: "web-1", label: "web-1"}
```

The operator’s body can read such a parameter but not assign to it, because an omitted argument stands for `null`, which is no field. A caller can’t pass `null` for a `field` parameter explicitly either, as our reference on [null and type checks](../reference/directory-layout.md#null-and-type-checks) describes.

#### Call other operators

Parameterized operators can call other operators, including passing through their own parameters:

operators/transform.tql

```tql
---
args:
  positional:
    - name: field
      type: field
  named:
    - name: multiplier
      type: int
      default: 2
---


vendor::scale $field, factor=$multiplier
```

To call the operators of another package, declare it as the section on [using other packages](manage-packages.md#use-other-packages) shows.

## Add constants

Constants give the thresholds, enumerations, and lookup tables that your operators share one name and one place, instead of a copy in every operator. Pipelines that use your package can reference them too, so a consumer reuses your values rather than hardcoding its own. Our reference on [constant files](../reference/directory-layout.md#constants) lists the rules that each binding must satisfy.

Our tutorial on [onboarding a data source](../tutorials/onboard-a-data-source.md#create-the-parser) shows how package constants publish reusable classifiers, patterns, headers, and pattern definitions.

### Define constants

Place a `constants.tql` file at the root of your package. Each `let` binding defines a named constant:

constants.tql

```tql
let $threshold = 8
let $severities = {low: 2, medium: 3, high: 4, critical: 5}
```

A constant can be any value that doesn’t depend on events or on the time, such as a number, string, list, or record, which makes `constants.tql` a natural home for the lookup tables and magic numbers that would otherwise be copied across your operators.

### Reference constants

Reference a constant with `<package>::$name`, using your package’s ID as the prefix. In a package with ID `vendor`, the bindings above become `vendor::$threshold` and `vendor::$severities`.

Inside the package, operators reference constants so the same value lives in exactly one place:

operators/ocsf/map.tql

```tql
ocsf.severity_id = vendor::$severities[severity]
```

The pipelines of a configuration whose `package.yaml` lists the `vendor` package reference its constants the same way:

```tql
from {severity: 9}, {severity: 3}
where severity >= vendor::$threshold
```

```tql
{severity: 9}
```

A package that only another package depends on stays hidden from the configuration’s pipelines, as our reference on [visibility](../reference/dependencies.md#visibility) describes.

### Build on earlier constants

A binding may reference any constant declared before it, so you can derive one constant from another:

constants.tql

```tql
let $high_severity = 8
let $threshold = $high_severity + 1
```

References resolve in order. A binding that refers to a constant declared later in the file fails to load the package.

## Use other packages

A package can build on the operators of other packages, the way our `ismalicious` package calls the STIX operators of our `stix` package instead of copying them. You declare what your package uses, choose requirements that work for the configurations that install your package, and run your operators against their dependencies.

### Declare a dependency

Run `tenzir package add` from inside your package’s folder. The command edits the nearest `package.yaml`, which is your package’s own:

```sh
cd acme
tenzir package add stix
```

Your manifest now lists the package, and your operators can call it:

acme/package.yaml

```yaml
name: ACME
dependencies:
  stix: ^0.0.1
```

acme/operators/ocsf/normalize.tql

```tql
stix::ocsf::normalize
```

Your package sees only the packages it declares. A package that one of your dependencies uses stays hidden from your operators until you declare it too.

Where the lock goes

Where the command locks the dependency depends on where your package lives:

* **In a configuration**: A package under a configuration’s `packages/` folder belongs to that configuration, and its dependencies go into the configuration’s own `package.lock`, next to everything else the configuration uses. Such a package can also use another package of the same configuration by its path, such as `tenzir package add shared --path ../shared`.
* **In its own repository**: Any other package is a root of its own, and the command writes `package.lock` next to its `package.yaml`. Commit the lock, so that your tests and local runs use the same versions everywhere.

A configuration that installs your package ignores your package’s lock. It resolves your `dependencies` together with its own requirements and those of its other packages, and locks one version of each. Our reference on [lock locations](../reference/lock.md#location) lists each case.

Choose requirements that combine

A configuration uses exactly one version of each package. If your package requires `=1.2.3` of a helper and another package requires `^1.3`, no configuration can install both. Keep your requirements as broad as your operators allow:

* Require the oldest release that has what you call, such as `^1.0`, and let configurations pick a newer compatible one.
* Avoid exact versions and pinned revisions in a package you release, because they force every configuration that installs your package onto that one version.
* Depend on packages from our library, or from other public repositories on GitHub. A package can’t use a package by its path unless both live in the same configuration.

Our reference on [package dependencies](../reference/dependencies.md) lists the requirement syntax and the rules that resolving follows.

### Run your operators locally

Download the locked packages once, then run pipelines from inside your package’s folder:

```sh
tenzir package fetch
tenzir run 'from {message: "test"} | acme::ocsf::map'
```

The `tenzir run` command finds your package’s `package.yaml`, loads your package with the packages it declares, and lets the pipeline call all of them. Run `tenzir package fetch` again whenever the lock changes.

Keep dependencies current

The `tenzir package update` command moves your lock to the newest versions that your requirements accept. Run your tests after an update. When a dependency releases an incompatible version, raise your requirement with `tenzir package add stix@<versions>`, adapt your operators, and release your package with a changelog entry for the change.

## Test a package

Tests keep your operators honest from one release to the next: each test runs a pipeline against your package and compares its output with a saved baseline. Put them in your package’s `tests/` folder and run them from the package’s root with our test harness:

```sh
uvx tenzir-test
```

The harness detects the package, runs every test with `tenzir run`, and downloads the packages that your `package.lock` pins before the first test. Our guide on [testing packages](write-tests.md#test-packages) walks through writing tests, saving baselines, and testing a package that uses other packages, and the section on [testing packages in CI](manage-packages.md#test-packages-in-ci) runs them on every pull request.

## Release a package

A release gives a state of your package a version that configurations can depend on. It consists of release notes, the version in your `package.yaml`, and a Git tag on the released commit. You record each change as you make it, then cut, version, and tag the release with our release tool [`tenzir-ship`](https://tenzir.com/docs/reference/ship-framework/).

### Record each change

Every change that users notice gets a changelog entry. Run `tenzir-ship` from your package’s folder, where it finds the `package.yaml` and works on the package’s `changelog/` folder:

```sh
uvx tenzir-ship add \
  --title "Map DNS answers to OCSF" \
  --type feature
```

The command writes the entry to `changelog/unreleased/`, where you can edit its description in Markdown. Write it for the people who call your operators: what changed for them and what they need to do. The first entry also creates the `changelog/` folder.

### Pick the type of a change

The type of each entry decides the next version number, and with it which configurations receive the release with their next update. Judge a change by what it does to the pipelines that call your package:

| Type       | When                                                                                                                                                             | Example                                                     |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| `breaking` | The way callers use your operators changes: you remove or rename an operator or a constant, remove, rename, or retype an argument, or make an argument required. | `vendor::parse` becomes `vendor::parse_json`.               |
| `change`   | Only the data changes: an operator emits different events, while every call stays valid.                                                                         | The mapping fills `src_endpoint.hostname` from a new field. |
| `feature`  | You add an operator, a constant, or an optional argument.                                                                                                        | `vendor::fetch` gains an optional `limit`.                  |
| `bugfix`   | You fix a defect.                                                                                                                                                | The parser no longer drops lines with a trailing space.     |

A `change` can still matter downstream, for example to a detection that matches on a field you renamed in the output. Say so in the entry, so that users read it before they update.

### Cut the release

1. Preview the release from your package’s folder:

   ```sh
   uvx tenzir-ship release create
   ```

   Without `--yes`, the command only lists what it would change, such as the version, the entries it moves, and the version file it updates, and exits with an error. It derives the version from the entries since the last release:

   | Highest entry type  | Before 1.0 | From 1.0 on |
   | ------------------- | ---------- | ----------- |
   | `bugfix`            | Patch      | Patch       |
   | `feature`, `change` | Minor      | Minor       |
   | `breaking`          | Minor      | Major       |

2. Create the release:

   ```sh
   uvx tenzir-ship release create --yes
   ```

   The command moves the entries into `changelog/releases/v<version>/` and writes the release notes there. Before 1.0, every minor version may break callers. Once your operators are stable, declare 1.0.0 with `uvx tenzir-ship release create --major --yes`.

3. Check the `version` field in your `package.yaml`. The command sets it to the released version, quoted and without the `v`:

   package.yaml

   ```yaml
   version: "0.3.0"
   ```

   The field keeps this value until the next release, so a branch or a fork of your package still says which release it builds on.

4. Commit the release notes and the manifest together, and tag that commit. A package at the root of its repository takes a tag such as `v0.3.0`, and a package in a folder takes the folder as a prefix:

   ```sh
   git tag -a acme/v0.3.0 -m "acme 0.3.0"
   git push origin acme/v0.3.0
   ```

   In our library, CI creates the tag for you once the pull request merges, as the section on [contributing to the library](manage-packages.md#contribute-to-the-library) explains.

The release is now available. The `tenzir package search` command and the app’s **Packages** page list it, and configurations whose requirements accept it receive it with their next update. Our reference on [releases](../reference/dependencies.md#releases) lists how Tenzir finds them.

Never change a release

Treat a tag as permanent. Configurations lock the commit that a tag named when they resolved it, so moving the tag to another commit doesn’t change their locks, but sends new configurations to different code under the same version. To fix a release, release a new version instead.

## Host a package repository

Not every package belongs in our library. A package for your organization’s own products, or one that you want to release on your own schedule, can live in a Git repository of your own, and configurations depend on it by its URL. You lay out the repository, release from it, test it in CI, and let configurations use its packages.

In Tenzir 7.0, the platform fetches packages only from public repositories on GitHub. A package that must stay private lives in the configuration that uses it, under `packages/`.

### Lay out the repository

A repository holds either one package at its root or several packages, each in a top-level folder named after its id:

* acme-packages/

  * .github/workflows/

    * test.yml

  * firewall/

    * package.yaml

    * operators/

      * …

    * tests/

      * …

  * proxy/

    * package.yaml

    * operators/

      * …

    * tests/

      * …

The layout decides the tags of your releases. A package in a folder takes the folder as a prefix, as in `firewall/v1.2.0`, while a package at the root takes plain tags such as `v1.2.0`, and its `package.yaml` must state the id that configurations ask for. Our reference on [packages in a repository](../reference/directory-layout.md#packages-in-a-repository) lists the rules of both layouts.

### Release from the repository

Releases work as in any package repository: record changes, cut the release with `tenzir-ship`, which also sets `version` in the package’s `package.yaml`, commit, and push a tag on the released commit:

```sh
uvx tenzir-ship --root firewall release create --yes
git add firewall
git commit -m "Release firewall 1.2.0"
git tag -a firewall/v1.2.0 -m "firewall 1.2.0"
git push origin HEAD firewall/v1.2.0
```

The section on [releasing a package](manage-packages.md#release-a-package) covers each step. To tag releases automatically once CI passes, adapt the [workflow](https://github.com/tenzir/library/blob/main/.github/workflows/tenzir-test.yml) and the [tagging script](https://github.com/tenzir/library/blob/main/.github/scripts/package-release-tags.py) of our library, which tag every release that a merge to the main branch adds.

### Test packages in CI

Run the tests of every package on each pull request and push:

.github/workflows/test.yml

```yaml
name: Tests


on:
  pull_request:
  push:
    branches: [main]


jobs:
  test:
    name: Test packages
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v4


      - name: Install uv
        uses: astral-sh/setup-uv@v5
        with:
          python-version: "3.13"


      - name: Cache locked packages
        uses: actions/cache@v4
        with:
          path: ~/.cache/tenzir/packages
          key: tenzir-packages-${{ hashFiles('**/package.lock') }}


      - name: Run package tests
        run: uvx tenzir-test firewall proxy
```

The job needs nothing but uv with Python 3.13, which `tenzir-test` requires. Without a `tenzir` on the runner’s `PATH`, the harness runs the pipelines with `uvx tenzir`, the latest Tenzir release. Before the tests of each package, it downloads the locked dependencies with `tenzir package fetch --locked`, which needs Git and network access but no sign-in, and the cache keeps them between runs. To learn early whether your packages work with the next Tenzir release, run the tests a second time with `TENZIR_BINARY: uvx --prerelease allow tenzir` in the step’s `env`, as our library does. Our reference on the [test framework](https://tenzir.com/docs/reference/test-framework/#binary-resolution) lists how the harness finds Tenzir.

With many packages, test only those a pull request touches, as the [detection script](https://github.com/tenzir/library/blob/main/.github/scripts/detect-touched-packages.sh) of our library does.

### Use the packages

Configurations add a package from your repository by naming its URL. The package id selects the folder:

```sh
tenzir package add firewall --git https://github.com/acme/acme-packages.git
```

The command takes the newest release and writes a caret requirement on its full version:

package.yaml

```yaml
dependencies:
  firewall:
    version: ^1.2.0
    git: https://github.com/acme/acme-packages.git
```

To see what your repository offers, search it like the library:

```sh
tenzir package search --git https://github.com/acme/acme-packages.git
```

## Contribute to the library

Our library at [github.com/tenzir/library](https://github.com/tenzir/library) collects the packages that we and the community maintain. A package in the library is one short line away for every Tenzir user, as in `suricata: ^1.2.0`, and appears in our [library catalog](https://tenzir.com/product/library) and on the app’s **Packages** page. Your package joins it through a pull request that CI and a maintainer check, and CI releases it once the pull request merges.

Get feedback first

Before you open a pull request, share your package in the `show-and-tell` channel on our [Discord server](https://discord.tenzir.com). Feedback from people who run the same product helps you shape the operators before others depend on them.

### Prepare the package

A package in the library lives in a folder at the root of the repository, named after its id:

* library/

  * your\_package/

    * package.yaml

    * package.svg the icon

    * changelog/

      * …

    * examples/

      * …

    * operators/

      * …

    * tests/

      * …

Check it against what the library expects:

* **Manifest**: The `package.yaml` has an `id`, a `name`, a Markdown `description` that says which product and use cases the package covers, an `author`, and `categories` such as `sources`, `mappings`, or `detections`. The `package_icon` points to the SVG in your folder through its raw GitHub URL, as the other packages in the library show.
* **Operators only**: The package provides operators and constants. It contains no pipelines and no contexts, because deployments refuse such packages.
* **Dependencies**: The package depends only on other packages of the library, in the short form that names nothing but a version requirement.
* **Examples**: Every use case has an example that runs on literal events, without credentials or network access.
* **Tests**: Tests cover the public operators and the examples, as our guide on [testing packages](write-tests.md#test-packages) shows. Run them with `uvx tenzir-test your_package` from the root of the repository.

### Open the pull request

1. Fork the [tenzir/library](https://github.com/tenzir/library) repository and add or change your package’s folder on a branch.

2. Record each user-visible change with a changelog entry, as the section on [recording each change](manage-packages.md#record-each-change) describes.

3. Cut the release in the same pull request, from the root of the repository:

   ```sh
   uvx tenzir-ship --root your_package release create --yes
   ```

   The command writes the release notes and sets `version` in `your_package/package.yaml` to the released version, such as `version: "0.1.0"`. Commit both.

4. Push the branch and open a pull request.

What CI checks

Every pull request runs the same checks:

* The changelogs of all packages are valid, and no released version changes afterwards.
* Every new release has its notes, and the `version` in its `package.yaml` states exactly the released version. A `version` that changes without a release fails too.
* Every TQL file in the library parses.
* The tests of every package that the pull request touches pass, against both the latest Tenzir release and the latest pre-release.

A maintainer reviews the operators, the examples, and the release notes.

After the merge

Once the pull request merges and the checks pass on the main branch, CI tags the release as `your_package/v0.1.0`. From then on, `tenzir package search` finds it, the **Packages** page offers it, and configurations add it with `tenzir package add your_package`.

Later changes follow the same path: a pull request with changelog entries and a release. Pick the entry types with care, because they decide whether configurations receive your release with their next update or only when they raise their requirement.

## See also

* [Packages](../explanations/packages.md)
* [Directory Layout](../reference/directory-layout.md)
* [Manifest](../reference/manifest.md)
* [Dependencies](../reference/dependencies.md)
* [Package lock file](../reference/lock.md)
* [CLI](../reference/cli.md)
* [Write tests](write-tests.md)
* [Onboard a data source](../tutorials/onboard-a-data-source.md)
