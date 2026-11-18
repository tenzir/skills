---
title: "Glossary"
canonical: https://tenzir.com/docs/explanations/glossary
source: https://tenzir.com/docs/explanations/glossary.md
section: "Docs"
---

# Glossary

> This page defines the terms that name things you work with in Tenzir: the components, the entities a pipeline manipulates, and the units we ship. For the names of the transformations themselves, see Learn the data lifecycle.

This page defines the terms that name things you work with in Tenzir: the components, the entities a pipeline manipulates, and the units we ship. For the names of the transformations themselves, see [Learn the data lifecycle](../tutorials/learn-the-data-lifecycle.md).

Missing term?

If you are missing a term, please open a [GitHub Discussion](https://github.com/orgs/tenzir/discussions/new?category=questions-answers) or ping us in our [Discord server](https://discord.tenzir.com).

## Ad-hoc pipeline

A [pipeline](glossary.md#pipeline) that runs once on a [deployment](glossary.md#deployment) to show you data.

The Explorer in the [app](glossary.md#app), `tenzir run -r`, [MCP](glossary.md#mcp), and the [API](glossary.md#api) start ad-hoc pipelines. Their events stream to you through the [platform](glossary.md#platform), and the deployment never stores them, so a restart ends them.

* Read more about [where pipelines run](pipeline.md#where-pipelines-run)

## API

The REST interface to the [platform](glossary.md#platform) for your own scripts, CI jobs, and services.

It offers the same operations as the [app](glossary.md#app) and [MCP](glossary.md#mcp), under the same permissions. The `tenzir` command offers them too. A request authenticates with an [API key](glossary.md#api-key) that acts on behalf of the member who created it.

* [Connect to Tenzir](../guides/connect-to-tenzir.md)
* [API](../reference/api.md)

## API key

A credential that lets a script or service act on behalf of the member who created it, through the [API](glossary.md#api) or the `tenzir` command.

An API key carries a policy that narrows its member’s permissions to what the script needs, and it never exceeds them. The platform shows its secret only once, and revoking the key ends its access on the next request.

* [Control access](../guides/control-access.md#limit-what-a-script-may-do)
* [IAM](../reference/iam.md)

## App

The web interface to the [platform](glossary.md#platform), at [platform.tenzir.com](https://platform.tenzir.com).

Use the app to run [pipelines](glossary.md#pipeline) in the Explorer, edit and deploy the [configuration](glossary.md#configuration) of a [workspace](glossary.md#workspace), install [packages](glossary.md#package), and watch your [deployments](glossary.md#deployment). Everything it does is also available through the API, MCP, and the `tenzir` command.

* Read more about [the platform](platform.md)

## Configuration

The code that a [deployment](glossary.md#deployment) runs: its [pipelines](glossary.md#pipeline), [contexts](glossary.md#context), and the [packages](glossary.md#package) those pipelines use.

Each [workspace](glossary.md#workspace) keeps its configuration in a Git repository on the [platform](glossary.md#platform), so every change is a commit. A deployment tracks one branch of it through its [deployment tracker](glossary.md#deployment-tracker), and with auto deploy on, every commit on that branch deploys right away and restarts only the pipelines it changes.

* Read more about [configurations](configuration.md)
* [Change configurations](../guides/change-configurations.md)

## Context

A stateful object used for in-band enrichment.

Contexts come in various types, such as a lookup table, Bloom filter, and GeoIP database. A deployment’s configuration declares them, one file per context. Pipelines enrich events with them using [`context_enrich`](../reference/operators/context_enrich.md), and something has to keep them current.

* Read more about [enrichment](enrichment.md)
* [Declare contexts](../guides/enrich/declare-contexts.md)
* [Add enrichment contexts](../tutorials/add-enrichment-contexts.md)

## Deployment

A running Tenzir instance that runs the pipelines and contexts of one [configuration](glossary.md#configuration).

Besides its configuration, a deployment runs pipelines you start once to look at data. It keeps its state in an object store and connects outward to the [platform](glossary.md#platform), which delivers its configuration. Tenzir hosts it for you, or you run it yourself.

* Read more about [deployments](deployment.md)
* [Add a deployment](../guides/add-a-deployment.md)

## Deployment tracker

The setting of a [deployment](glossary.md#deployment) that selects the branch of its [configuration](glossary.md#configuration) it tracks, and whether new commits on that branch deploy automatically.

A new deployment tracks `main` with auto deploy on. With auto deploy off, the deployment keeps what it runs until you deploy a commit by hand, which is how you hold a deployment on an older commit.

* [Change configurations](../guides/change-configurations.md#choose-what-the-deployment-follows)
* See the [rules of trackers](../reference/cli.md#deployment-trackers)

## Destination

A [pipeline](glossary.md#pipeline) that ends in an [output](glossary.md#output) operator and starts with [`subscribe`](../reference/operators/subscribe.md).

* Learn more about [pipelines](pipeline.md)

## Draft

Your personal, uncommitted changes to one branch of a [configuration](glossary.md#configuration).

The [app](glossary.md#app) and [MCP](glossary.md#mcp) collect edits in a draft, which nobody else sees and which changes nothing until you commit it. Committing turns the draft into a commit on the branch, and discarding throws it away.

* Read why [every change is a commit](configuration.md#every-change-is-a-commit)
* [Change configurations](../guides/change-configurations.md#review-and-commit-the-change)

## Event

One record of typed data, and the unit that [pipelines](glossary.md#pipeline) move.

Think of an event as a JSON object with a stricter [type system](../reference/types.md): besides strings, numbers, and records, a field can be a timestamp, a duration, an IP address, or a subnet. The fields of an event and their types form its [schema](glossary.md#schema), and one pipeline can carry events of many schemas at once.

## Format

A data representation that Tenzir can read or write, such as JSON, CSV, Syslog, CEF, or PCAP.

Each format has a [parser](glossary.md#parser), a [printer](glossary.md#printer), or both. Formats are independent of where the bytes come from, so any format works with any connection.

* See available [operators for parsing](../reference/operators.md#parsing)
* See available [operators for printing](../reference/operators.md#printing)
* See available [functions for parsing](../reference/functions.md#parsing)
* See available [functions for printing](../reference/functions.md#printing)

## Function

Computes a value from other values, inside an expression.

A function acts on single values, while an [operator](glossary.md#operator) acts on a stream of [events](glossary.md#event). Examples of functions are `time.round(1s)` and `ip.is_v6()`, while `where` and `summarize` are operators.

* See available [functions](../reference/functions.md)

## Input

An [operator](glossary.md#operator) that only produces data, without consuming anything. A pipeline starts with one.

* Learn more about [pipelines](pipeline.md)

## Integration

Documentation and prebuilt TQL for working with one third-party product.

An integration tells you which operators to use for a given vendor, what to configure on their side, and which [package](glossary.md#package) provides operators for it if one exists.

* List of [all integrations](https://tenzir.com/product/integrations)
* [Does Tenzir have an integration for my system or format?](https://tenzir.com/faqs/does-tenzir-have-an-integration-for-x)

## Library

A public collection of [packages](glossary.md#package) that a [configuration](glossary.md#configuration) can depend on by version, browsable in our [library catalog](https://tenzir.com/product/library) and in the [app](glossary.md#app).

The library is [freely available on GitHub](https://github.com/tenzir/library), where we and the community maintain its packages and CI tests and tags every release. A [configuration](glossary.md#configuration) can also depend on packages from other public Git repositories.

* Read more about [the library](packages.md#the-library)
* [Manage packages](../guides/manage-packages.md#contribute-to-the-library)

## MCP

The [Model Context Protocol](https://modelcontextprotocol.io), through which an AI agent works with the [platform](glossary.md#platform).

The platform’s MCP server offers the same operations as the [API](glossary.md#api). An agent signs in through your browser and acts on your behalf, with the permissions of your roles.

* [Connect to Tenzir](../guides/connect-to-tenzir.md)
* [MCP](../reference/mcp.md)

## Metrics

Telemetry about [pipelines](glossary.md#pipeline) that a [deployment](glossary.md#deployment) reports to the [platform](glossary.md#platform).

Metrics answer operational questions: how many events and bytes a pipeline read and wrote, when it started, finished, or failed, and which diagnostics it reported. The platform shows them for each deployment.

* Read what [flows between deployment and platform](platform.md#how-deployments-connect)

## Module

A namespace for the [operators](glossary.md#operator) and [functions](glossary.md#function) of a [package](glossary.md#package), written with `::` as separator, as in `vendor::ocsf::map`.

Modules are exclusive to packages, and the package identifier is always the leading segment. Builtin operators and functions use flat names, such as [`ai_prompt`](../reference/operators/ai_prompt.md), so no builtin can shadow a package’s entities.

* Read more about [modules](packages.md#modules)
* [Manage packages](../guides/manage-packages.md#add-operators)

## OCSF

The [Open Cybersecurity Schema Framework](https://schema.ocsf.io), a vendor-neutral [schema](glossary.md#schema) for security events.

OCSF is the default target when we normalize data, because a detection written against an OCSF class works for every source that maps to it. Our [library](glossary.md#library) ships mappings for common sources, and dedicated operators derive and type-check the result.

* [Onboard a data source](../tutorials/onboard-a-data-source.md)

## Operator

The unit of computation in a [pipeline](glossary.md#pipeline), and one line of TQL.

An operator is an [input](glossary.md#input), a [transformation](glossary.md#transformation), or an [output](glossary.md#output). Packages add their own operators, which you call exactly like the builtin ones.

* See all available [operators](../reference/operators.md)

## Organization

The top level of the [platform](glossary.md#platform): it owns the [workspaces](glossary.md#workspace), the [deployments](glossary.md#deployment) in them, the subscription and its billing, and the list of its members.

Each member has one or more [roles](glossary.md#role) in the organization, which decide what that member, the member’s API keys, and the member’s agents may do.

* Read more about [organizations](platform.md#organizations)
* [Control access](../guides/control-access.md)

## Output

An [operator](glossary.md#operator) that only consumes data, without producing anything. A pipeline ends with one.

* Learn more about [pipelines](pipeline.md)

## Package

A reusable bundle of TQL for one use case, such as mapping the logs of one product: [operators](glossary.md#operator), constants, runnable examples, and tests.

Anyone can write one. A package can come from our [library](glossary.md#library), from any other Git repository, or from the `packages/` folder of your own [configuration](glossary.md#configuration). A package does nothing on its own: the configuration lists it as a dependency, and a [pipeline](glossary.md#pipeline) uses it only by calling its operators through the package’s [module](glossary.md#module).

* Read more about [packages](packages.md)
* [Onboard a data source](../tutorials/onboard-a-data-source.md)

## Parser

What turns bytes of a [format](glossary.md#format) into [events](glossary.md#event).

Parsers appear as the `read_*` operators, and as `parse_*` [functions](glossary.md#function) when the input is a string field instead of a byte stream. A parser is the dual of a [printer](glossary.md#printer).

* See available [operators for parsing](../reference/operators.md#parsing)
* See available [functions for parsing](../reference/functions.md#parsing)

## Pipeline

A sequence of [operators](glossary.md#operator) that data flows through, written in [TQL](glossary.md#tql).

A pipeline can run once and return a result, or run continuously until you stop it. Pipelines connect to each other through topics with [`publish`](../reference/operators/publish.md) and [`subscribe`](../reference/operators/subscribe.md), which is how a deployment ends up as many small pipelines rather than one large one.

* Learn more about [pipelines](pipeline.md)
* [Where pipelines run](pipeline.md#where-pipelines-run)

## Platform

The control plane that your [deployments](glossary.md#deployment) connect to, reachable through the app, the `tenzir` command, the API, and MCP.

The platform holds organizations, [workspaces](glossary.md#workspace), user access, secrets, and the [configuration](glossary.md#configuration) of every workspace, and it delivers configurations to deployments. Events stay on the deployment unless a pipeline sends them elsewhere. You can use ours or run your own.

* Read more about [the platform](platform.md)

## Printer

What turns [events](glossary.md#event) into bytes of a [format](glossary.md#format).

Printers appear as the `write_*` operators, and as `print_*` [functions](glossary.md#function) when you want a string field instead of a byte stream. A printer is the dual of a [parser](glossary.md#parser).

* See available [operators for printing](../reference/operators.md#printing)
* See available [functions for printing](../reference/functions.md#printing)

## Pushdown

Moving a requirement of a later [operator](glossary.md#operator) toward the [source](glossary.md#source) of a [pipeline](glossary.md#pipeline), so that upstream operators can act on it early.

Before a pipeline runs, Tenzir carries the predicates of `where`, the row limit of `head`, the fields that `select` keeps, and the ordering that downstream operators need upstream. A source such as `from_clickhouse` acts on what it understands, for example by adding a `WHERE` clause to the SQL query it sends, and a [parser](glossary.md#parser) that learns the order does not matter can split its work across several jobs. Results stay the same whether or not an operator acts on a pushed-down requirement.

* Learn more about [pipeline optimization](pipeline.md#optimization)

## Role

A named set of permissions that a member holds in an [organization](glossary.md#organization).

The built-in Owner role may do everything, and the built-in Member role may work with workspaces and deployments but not manage people, billing, or protected branches. A custom role grants exactly the permissions you choose.

* [Control access](../guides/control-access.md#give-members-the-roles-they-need)
* [IAM](../reference/iam.md)

## Schema

The type of an [event](glossary.md#event): a record type that lists the event’s fields in order, together with their types.

Every event has a schema. Some schemas are predefined and carry a name, such as `suricata.flow`, so that parsers can refer to them: the `schema` option of a `read_*` operator such as [`read_json`](../reference/operators/read_json.md) applies a predefined schema and sets the event’s `@name` to its name. The name itself is not part of the schema. It is internal metadata that every event carries, that pipelines can change freely, and that disappears when the event leaves Tenzir. `@name` can be used to tag/categorize events within Tenzir.

* Learn how the [data model](data-model.md#records-with-shapes) stores events of many schemas in one batch
* Read about `@name` and other [metadata fields](../reference/expressions.md#metadata)
* See the available [types](../reference/types.md)

## Sink

An operator that writes to an external resource.

A sink is the dual to a [source](glossary.md#source). It consumes events or bytes from the pipeline and has no output.

* Learn more about [pipelines](pipeline.md)

## Source

An [operator](glossary.md#operator) that reads from an external resource, or a [pipeline](glossary.md#pipeline) that starts with an [input](glossary.md#input) operator and ends in [`publish`](../reference/operators/publish.md).

The operator sense is the dual to a [sink](glossary.md#sink): it has no input and emits events or bytes into the pipeline. The pipeline sense is the counterpart to a [destination](glossary.md#destination).

* Learn more about [pipelines](pipeline.md)

## TQL

The Tenzir Query Language, in which you write [pipelines](glossary.md#pipeline).

TQL reads top to bottom, one [operator](glossary.md#operator) per line, and covers collection, transformation, analytics, and delivery in one language. It has no separate configuration dialect: what you type in the [app](glossary.md#app) is what a deployed pipeline contains.

* Learn more about the [language](language.md)
* [Learn idiomatic TQL](../tutorials/learn-idiomatic-tql.md)

## Transformation

An [operator](glossary.md#operator) that both consumes and produces data. Most operators are transformations.

* Learn more about [pipelines](pipeline.md)

## Workspace

A group of [deployments](glossary.md#deployment) on the [platform](glossary.md#platform) that share one [configuration](glossary.md#configuration) repository.

A workspace belongs to an organization and holds the configuration, the deployments that run it, and the secrets they may read. Separate workspaces keep teams or environments apart.

* Read more about [workspaces](platform.md#workspaces)
