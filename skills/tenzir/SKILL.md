---
name: tenzir
description: >-
  Answer questions using the documentation of Tenzir 7.0.0. Use whenever the
  user asks about TQL syntax, pipeline operators, functions, data parsing or
  transformation, normalization, OCSF mapping, enrichment, lookup tables,
  contexts, packages, nodes, platform setup, deployment, configuration,
  integrations with tools like Splunk, Kafka, S3, Elasticsearch, or any other
  Tenzir feature. Also use when the user asks how to collect, route, filter,
  aggregate, or export security data with Tenzir, or needs help writing or
  debugging TQL pipelines, even if they don't mention 'Tenzir' explicitly but
  are clearly working in a Tenzir context. Also use for questions about Tenzir
  the company or product, release notes and changelog, blog posts, and
  solution use cases.
---

# Tenzir Documentation Map

> The security data pipeline platform.

This map covers the documentation of Tenzir 7.0.0, the newest version, which is in preview.
If the user works with an older version, read that version's index at <https://tenzir.com/docs/v<version>/llms.txt> instead; <https://tenzir.com/docs/versions.json> lists the published versions.
Every link below is relative to <https://tenzir.com/docs/> and leads to the Markdown version of a page, which you can read on its own.

## How to use this skill

Navigate the documentation based on the type of question:

| Question type | Where to look |
|---|---|
| "How do I…" tasks | [Guides](guides.md) — step-by-step instructions organized by task |
| Operator or function syntax | [Operator Index](reference/operators.md) or [Function Index](reference/functions.md), then the specific page |
| Integration setup (Splunk, Kafka, S3…) | <https://tenzir.com/product/integrations.md> — per-product setup and pipeline examples |
| Concepts (nodes, pipelines, deployment) | [Explanations](explanations.md) — architecture and design |
| Learning from scratch | [Tutorials](tutorials.md) — guided lessons |
| TQL language rules | [Language](explanations/language.md), [Expressions](reference/expressions.md), [Statements](reference/statements.md) |

Always read the relevant page before answering. Prefer TQL examples from the
documentation over inventing syntax.

## Beyond the docs

This map covers only the documentation of Tenzir nodes. For anything else
about Tenzir, fetch these live pages on demand instead of answering from
memory:

| Topic | Where to look |
|---|---|
| Release notes, "when was X added/changed" | <https://tenzir.com/changelog.md> |
| Integrations with third-party products | <https://tenzir.com/product/integrations.md> |
| The platform, its API, the Helm chart, and the test and ship frameworks | <https://tenzir.com/docs/llms.txt> — they ship on their own schedule, so only the current documentation has them |
| Blog posts and announcements | <https://tenzir.com/blog.md> |
| Solution use cases | <https://tenzir.com/solutions.md> |
| Company, product, events, everything else | <https://tenzir.com/llms.txt> — the full site index with per-page Markdown links |

## Answer patterns

**Operator syntax question** — *"How does `where` work?"*
→ Read [where](reference/operators/where.md), explain the syntax, show the doc's TQL examples.

**Integration question** — *"How do I send data to Splunk?"*
→ Read <https://tenzir.com/product/integrations/splunk.md> and [to_splunk](reference/operators/to_splunk.md), provide the pipeline example from the page.

**Task question** — *"How do I parse syslog?"*
→ Read [Parse delimited text](guides/parse/parse-delimited-text.md) and
[read_syslog](reference/operators/read_syslog.md). Combine the guide's approach
with the operator reference.

## [Guides](guides.md)

Guides are practical step-by-step explanation to help you achieve a specific goal.

### Get started

#### [Quickstart](guides/quickstart.md)

See live security events flow through Tenzir within minutes, from your AI agent, the app, or a terminal.

#### [Install Tenzir](guides/installation.md)

Install the tenzir command on macOS or Linux with Homebrew, a Debian or RPM package, a static tarball, Docker, or uv, and run your first pipeline.

#### [Connect to Tenzir](guides/connect-to-tenzir.md)

Connect your AI agent via MCP, sign in with the tenzir command, or create an API key for your scripts.

#### [Set up your agent](guides/set-up-your-agent.md)

Give an AI agent what it needs to operate your deployments, write and test pipelines on your machine, and map events to security schemas.

### Operate

#### [Add a deployment](guides/add-a-deployment.md)

Add a deployment that runs your pipelines, hosted by Tenzir or on your own machine or server, keep it running and up to date, find out why it doesn't connect, and delete it when you no longer need it.

#### [Change configurations](guides/change-configurations.md)

Change what your deployments run, review the change, take it to a deployment automatically or by hand, try it on a staging branch, and roll it back when it goes wrong.

#### [Manage packages](guides/manage-packages.md)

Install, update, and override the packages your configuration uses, and create, release, and share packages of your own.

#### [Write tests](guides/write-tests.md)

Write and run tests for your pipelines and packages, with fixtures, custom runners, and project hooks when tests need more than TQL.

#### [Control access](guides/control-access.md)

Invite members and give them the roles they need, limit what scripts and AI agents may do, protect production branches, and remove access you no longer trust.

### Collect

#### [Overview](guides/collect.md)

Read events and bytes from files, APIs, brokers, stores, and networks.

##### [Read and watch files](guides/collect/read-and-watch-files.md)

##### [Fetch via HTTP and APIs](guides/collect/fetch-via-http-and-apis.md)

##### [Read from message brokers](guides/collect/read-from-message-brokers.md)

##### [Read from data stores](guides/collect/read-from-data-stores.md)

##### [Get data from the network](guides/collect/get-data-from-the-network.md)

##### [Receive events with ingest endpoints](guides/collect/receive-events-with-ingest-endpoints.md)

### Parse

#### [Overview](guides/parse.md)

Turn byte streams and text fields into structured events.

##### [Parse delimited text](guides/parse/parse-delimited-text.md)

##### [Parse binary data](guides/parse/parse-binary-data.md)

##### [Parse string fields](guides/parse/parse-string-fields.md)

##### [Clean up values](guides/parse/clean-up-values.md)

### Shape

#### [Overview](guides/shape.md)

Prepare event fields and records for downstream processing.

##### [Transform values](guides/shape/transform-values.md)

##### [Manipulate strings](guides/shape/manipulate-strings.md)

##### [Normalize event timestamps](guides/shape/normalize-event-timestamps.md)

##### [Repair out-of-order events](guides/shape/repair-out-of-order-events.md)

##### [Calculate with time](guides/shape/calculate-with-time.md)

##### [Shape lists](guides/shape/shape-lists.md)

##### [Shape records](guides/shape/shape-records.md)

##### [Reshape complex data](guides/shape/reshape-complex-data.md)

##### [Convert data formats](guides/shape/convert-data-formats.md)

### Normalize

#### [Overview](guides/normalize.md)

Map source-specific events into a shared schema.

##### [Map to ASIM](guides/normalize/map-to-asim.md)

##### [Map to CIM](guides/normalize/map-to-cim.md)

##### [Map to ECS](guides/normalize/map-to-ecs.md)

##### [Map to OCSF](guides/normalize/map-to-ocsf.md)

##### [Map to UDM](guides/normalize/map-to-udm.md)

### Optimize

#### [Overview](guides/optimize.md)

Reduce data volume and processing work in a pipeline.

##### [Filter and select data](guides/optimize/filter-and-select-data.md)

##### [Slice and sample data](guides/optimize/slice-and-sample-data.md)

##### [Deduplicate events](guides/optimize/deduplicate-events.md)

### Protect

#### [Overview](guides/protect.md)

Limit sensitive-data exposure while preserving useful structure.

##### [Mask sensitive data](guides/protect/mask-sensitive-data.md)

##### [Encrypt sensitive data](guides/protect/encrypt-sensitive-data.md)

### Enrich

#### [Overview](guides/enrich.md)

Add context that the original event does not contain.

##### [Declare contexts](guides/enrich/declare-contexts.md)

##### [Use lookup tables](guides/enrich/use-lookup-tables.md)

##### [Enrich with asset inventory](guides/enrich/enrich-with-asset-inventory.md)

##### [Enrich with threat intel](guides/enrich/enrich-with-threat-intel.md)

##### [Enrich events with AI](guides/enrich/enrich-events-with-ai.md)

##### [Join event streams](guides/enrich/join-event-streams.md)

### Analyze

#### [Overview](guides/analyze.md)

Summarize event streams and compare current activity with prior behavior.

##### [Aggregate event streams](guides/analyze/aggregate-event-streams.md)

##### [Shape aggregation results](guides/analyze/shape-aggregation-results.md)

##### [Window event streams](guides/analyze/window-event-streams.md)

##### [Calculate aggregate statistics](guides/analyze/calculate-aggregate-statistics.md)

##### [Find unseen and rare values](guides/analyze/find-unseen-and-rare-values.md)

##### [Set adaptive thresholds from a baseline](guides/analyze/set-adaptive-thresholds-from-a-baseline.md)

##### [Identify distribution drift](guides/analyze/identify-distribution-drift.md)

##### [Find cardinality spikes](guides/analyze/find-cardinality-spikes.md)

### Detect

#### [Overview](guides/detect.md)

Match security activity and model the resulting findings.

##### [Match events with TQL](guides/detect/match-events-with-tql.md)

##### [Model detections in OCSF](guides/detect/model-detections-in-ocsf.md)

##### [Detect over time windows](guides/detect/detect-over-time-windows.md)

##### [Baseline behavior from stored events](guides/detect/baseline-from-stored-events.md)

##### [Detect periodic behavior](guides/detect/detect-periodic-behavior.md)

##### [Create multi-stage detectors](guides/detect/create-multi-stage-detectors.md)

##### [Execute Sigma rules](guides/detect/execute-sigma-rules.md)

##### [Check Sigma rule compatibility with OCSF](guides/detect/check-sigma-rule-compatibility-with-ocsf.md)

##### [Scan bytes with YARA](guides/detect/scan-bytes-with-yara.md)

### Store

#### [Overview](guides/store.md)

Persist events for later search, replay, and analysis.

##### [Write partitioned files](guides/store/write-partitioned-files.md)

### Search

#### [Overview](guides/search.md)

Push selective queries to data stores, search across heterogeneous backends in one pipeline, and scan Parquet archives in place.

##### [Push queries to data stores](guides/search/push-queries-to-data-stores.md)

##### [Search across data stores](guides/search/search-across-data-stores.md)

##### [Query open archives in place](guides/search/query-open-archives-in-place.md)

### Route

#### [Overview](guides/route.md)

Deliver event streams to the systems that need them.

##### [Send to destinations](guides/route/send-to-destinations.md)

##### [Expose data as a server](guides/route/expose-data-as-server.md)

##### [Split and merge streams](guides/route/split-and-merge-streams.md)

##### [Fan out with subpipelines](guides/route/fan-out-with-subpipelines.md)

##### [Load-balance pipelines](guides/route/load-balance-pipelines.md)

### Replay

#### [Overview](guides/replay.md)

Run stored events through live pipelines again.

##### [Replay historical events](guides/replay/replay-historical-events.md)

### Contribute

#### [Code of Conduct](guides/contribution/code-of-conduct.md)

In the interest of fostering an open and welcoming environment, we as contributors and maintainers pledge to make participation in our project and our community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, sex characteristics, gender identity and expression, level of experience, education, socio-economic status, nationality, personal appearance, race, religion, or sexual identity and orientation.

#### [Git and GitHub Workflow](guides/contribution/workflow.md)

The following diagram visualizes our branching model:

#### [Security Policy](guides/contribution/security.md)

Security is a serious matter for us.

#### [Setup syntax highlighting](guides/development/setup-syntax-highlighting.md)

Install TQL language extensions for syntax highlighting in your editor

#### [Build from source](guides/development/build-from-source.md)

Tenzir uses CMake as build system with a C++23 compiler.

### Other

#### [Work with time](guides/shape/work-with-time.md)

We split this guide into focused tasks.

## [Tutorials](tutorials.md)

Tutorials are learning-oriented lessons that take you through a series of steps to complete a project.

### Fundamentals

#### [Learn the data lifecycle](tutorials/learn-the-data-lifecycle.md)

Security data arrives as somebody else’s text and has to end up as something a detection, a dashboard, or an auditor can use.

#### [Learn idiomatic TQL](tutorials/learn-idiomatic-tql.md)

This tutorial teaches you to write TQL that is clear, efficient, and maintainable.

### Development

#### [Onboard a data source](tutorials/onboard-a-data-source.md)

Onboarding a data source means turning one product’s output into events that every later stage of the data lifecycle can use.

#### [Add enrichment contexts](tutorials/add-enrichment-contexts.md)

A context is state, not code.

### Analytics

#### [Build an OCSF lake with ClickHouse](tutorials/build-an-ocsf-lake-with-clickhouse.md)

Store OCSF events in ClickHouse, from a table that accepts anything to a tuned lake with typed columns, skip indexes, codecs, and per-class retention.

## [Explanations](explanations.md)

Explanations are big-picture explanations of higher-level Tenzir concepts.

### Architecture

#### [Platform](explanations/platform.md)

Understand how the platform organizes organizations, workspaces, deployments, and ingest endpoints, how deployments connect to it, and which data it sees.

#### [Configuration](explanations/configuration.md)

Understand how a workspace keeps its pipelines, contexts, and packages in a Git repository, and what a deploy guarantees when a commit reaches a deployment.

#### [Deployment](explanations/deployment.md)

Understand what a deployment runs, which states its pipelines go through, how it survives restarts, and how it keeps working when the platform is unreachable.

#### [Pipeline](explanations/pipeline.md)

A Tenzir pipeline is a chain of operators that represents a dataflow.

#### [Language](explanations/language.md)

Understand TQL's dataflow model, streaming and batch semantics, and support for events with different schemas.

#### [Executor](explanations/executor.md)

Understand how Tenzir compiles TQL into an execution plan and runs operators with fused handoffs, channels, subpipelines, and parallel jobs.

#### [Data model](explanations/data-model.md)

Understand how Tenzir stores events in columnar batches, keeps events of different shapes and types side by side, and selects rows with bitmaps instead of slicing batches apart.

### Concepts

#### [Secrets](explanations/secrets.md)

Operators and functions accept secrets as arguments for sensitive values, such as authentication tokens, passwords, keys, or even URLs.

#### [Normalization](explanations/normalization.md)

Why Tenzir maps every source to OCSF first and translates from there

#### [Enrichment](explanations/enrichment.md)

Enrichment means adding contextual data to events.

#### [Detections](explanations/detections.md)

Understand how Tenzir matches, correlates, and models security evidence as detection results

#### [Packages](explanations/packages.md)

Understand what a package contains, how a configuration and its packages depend on each other by version, how releases work, and what our library offers.

#### [Encryption](explanations/encryption.md)

Encryption turns a value into ciphertext that only the holders of a key can turn back into the original.

#### [Transpilation](explanations/transpilation.md)

Understand how Tenzir compiles TQL operators after a remote source into the target's native query language, how native semantics differ from TQL, and when operators stay in Tenzir.

### Help

#### [Glossary](explanations/glossary.md)

This page defines the terms that name things you work with in Tenzir: the components, the entities a pipeline manipulates, and the units we ship.

## [Reference](reference.md)

The reference has nitty-gritty technical descriptions of how Tenzir works.

### Language (TQL)

#### [Type System](reference/types.md)

This page explains TQL’s type system, which provides strong typing with automatic inference.

#### [Expressions](reference/expressions.md)

Expressions form the computational core of TQL.

#### [Statements](reference/statements.md)

TQL programs are a sequence of statements.

#### [Programs](reference/programs.md)

TQL programs compose statements into complete data processing workflows that can execute.

#### [Overview](reference/optimizations.md)

This reference lists which operators each source pushes down, compares what the query-language targets compute, and links a page per remote target with its native spellings and semantic differences.

### Configuration

#### [Directory Layout](reference/directory-layout.md)

A configuration and a package are both folders of plain files in fixed places.

#### [Contexts](reference/contexts.md)

A deployment declares its contexts in its configuration, one YAML file per context.

#### [Manifest](reference/manifest.md)

Every package and every configuration has a package.yaml at its root, its manifest.

#### [Dependencies](reference/dependencies.md)

The dependencies key of a manifest lists the packages that a configuration or a package uses, by id.

#### [Package lock file](reference/lock.md)

The package.lock file pins every package that a configuration uses to one version, one commit, and a hash of its files, including the packages that these use in turn.

### Tools

#### [Test Framework](reference/test-framework.md)

The tenzir-test harness discovers and runs integration tests for pipelines, fixtures, and custom runners.

#### [Ship Framework](reference/ship-framework.md)

tenzir-ship ships as a Python package that requires Python 3.12 or later.

### Security

#### [AWS Authentication](reference/aws-authentication.md)

Tenzir’s AWS operators authenticate with AWS using the AWS SDK’s default credential chain, an OIDC web identity token, or static credentials.

#### [Azure Authentication](reference/azure-authentication.md)

Tenzir’s Azure operators authenticate with Microsoft Entra ID using the Azure SDK’s default credential chain, a shared account key, an application client secret, or workload identity federation.

#### [IAM](reference/iam.md)

The platform decides every request with role-based access control: a member’s roles grant actions on resources, an API key’s policy narrows its member’s actions, and an agent connected via MCP acts with its user’s actions.

### Interfaces

#### [MCP](reference/mcp.md)

The platform’s MCP server lets an AI agent do what you do in the app, with your permissions: run pipelines, read diagnostics, change the configuration, and manage deployments.

#### [CLI](reference/cli.md)

The tenzir command runs pipelines on your machine and on your deployments, runs a deployment on your machine, and does everything the platform offers from a terminal, under the same permissions as the app, the API, and the MCP server.

### API

#### [Overview](reference/api.md)

The platform’s REST API offers everything that the app, the MCP server, and the CLI do, under the same permissions, for your own scripts and tools.

### Operators

#### [Operators](reference/operators.md)

Tenzir comes with a wide range of built-in pipeline operators.

### Functions

#### [Functions](reference/functions.md)

Functions appear in expressions and take positional and/or named arguments, producing a value as a result of their computation.

### Indexes

For the complete operator listing by category, read [Operator Index](reference/operators.md).

For the complete function listing by category, read [Function Index](reference/functions.md).

#### Overview Index

- [Axiom](reference/optimizations/axiom.md)
- [ClickHouse](reference/optimizations/clickhouse.md)
- [CloudWatch Logs](reference/optimizations/cloudwatch.md)
- [DuckDB](reference/optimizations/duckdb.md)
- [KQL](reference/optimizations/kql.md)
- [Microsoft Graph](reference/optimizations/microsoft-graph.md)
- [Microsoft SQL Server](reference/optimizations/microsoft-sql.md)
- [MySQL](reference/optimizations/mysql.md)
- [SentinelOne](reference/optimizations/sentinelone.md)
- [SPL](reference/optimizations/spl.md)
