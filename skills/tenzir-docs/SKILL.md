---
name: tenzir-docs
description: >-
  Answer questions using the Tenzir documentation. Use whenever the user asks
  about TQL syntax, pipeline operators, functions, data parsing or
  transformation, normalization, OCSF mapping, enrichment, lookup tables,
  contexts, packages, nodes, platform setup, deployment, configuration,
  integrations with tools like Splunk, Kafka, S3, Elasticsearch, or any other
  Tenzir feature. Also use when the user asks how to collect, route, filter,
  aggregate, or export security data with Tenzir, or needs help writing or
  debugging TQL pipelines, even if they don't mention 'Tenzir' explicitly but
  are clearly working in a Tenzir context.
---

# Tenzir Documentation Map

> The low-code data pipeline solution for security teams

Tenzir is a data pipeline engine for security teams. Run pipelines to collect,
parse, transform, and route security data. Deploy nodes on-prem or in the cloud,
and manage them via the Tenzir Platform.

## How to use this skill

Navigate the documentation based on the type of question:

| Question type | Where to look |
|---|---|
| "How do I…" tasks | [Guides](guides.md) — step-by-step instructions organized by task |
| Operator or function syntax | [Operator Index](reference/operators-index.md) or [Function Index](reference/functions-index.md), then the specific page |
| Integration setup (Splunk, Kafka, S3…) | [Integrations](integrations.md) — per-product setup and pipeline examples |
| Concepts (nodes, pipelines, deployment) | [Explanations](explanations.md) — architecture and design |
| Learning from scratch | [Tutorials](tutorials.md) — guided lessons |
| TQL language rules | [Language](explanations/language.md), [Expressions](reference/expressions.md), [Statements](reference/statements.md) |

Always read the relevant page before answering. Prefer TQL examples from the
documentation over inventing syntax.

## Answer patterns

**Operator syntax question** — *"How does `where` work?"*
→ Read [where](reference/operators/where.md), explain the syntax, show the doc's TQL examples.

**Integration question** — *"How do I send data to Splunk?"*
→ Read [Splunk](integrations/splunk.md), provide the pipeline example from the page.

**Task question** — *"How do I parse syslog?"*
→ Read [Parse delimited text](guides/parsing/parse-delimited-text.md) and
[read_syslog](reference/operators/read_syslog.md). Combine the guide's approach
with the operator reference.

## [Guides](guides.md)

Practical step-by-step explanations to help you achieve a specific goal.
Start here when you're trying to get something done.

### Get Started

#### [Quickstart](guides/quickstart.md)

Drowning in logs, alerts, and rigid tools? Meet Tenzir—your engine for taming security data. In just a few minutes, you’ll be ingesting, transforming, and enriching data on your terms, with full control. Here’s what you’ll accomplish:

#### [Installation](guides/installation.md)

This guide shows you how to install the Tenzir CLI to run pipelines locally or deploy a persistent node. The package includes two binaries:

##### [Create account](guides/installation/create-account.md)

#### Basic Usage

##### [Run pipelines](guides/basic-usage/run-pipelines.md)

##### [Manage a pipeline](guides/basic-usage/manage-a-pipeline.md)

### Setup

#### [Node Setup](guides/node-setup.md)

The Tenzir Node is the vehicle to run pipelines. It is light-weight server application that can be deployed on-premises or in the cloud.

##### [Provision a node](guides/node-setup/provision-a-node.md)

##### [Size a node](guides/node-setup/size-a-node.md)

##### [Deploy a node](guides/node-setup/deploy-a-node.md)

##### [Configure a node](guides/node-setup/configure-a-node.md)

##### [Configure TLS](guides/node-setup/configure-tls.md)

##### [Start the API](guides/node-setup/start-the-api.md)

##### [Tune performance](guides/node-setup/tune-performance.md)

#### [Platform Setup](guides/platform-setup.md)

The Tenzir Platform acts as a fleet management control plane for Tenzir Nodes. Use its web interface to explore data, create pipelines, and build dashboards.

##### [Deploy on AWS](guides/platform-setup/deploy-on-aws.md)

##### [Choose a scenario](guides/platform-setup/choose-a-scenario.md)

##### [Configure reverse proxy](guides/platform-setup/configure-reverse-proxy.md)

##### [Configure internal services](guides/platform-setup/configure-internal-services.md)

##### [Configure identity provider](guides/platform-setup/configure-identity-provider.md)

##### [Configure database](guides/platform-setup/configure-database.md)

##### [Configure blob storage](guides/platform-setup/configure-blob-storage.md)

##### [Configure secret store](guides/platform-setup/configure-secret-store.md)

##### [Run the platform](guides/platform-setup/run-the-platform.md)

#### Platform Management

##### [Configure workspaces](guides/platform-management/configure-workspaces.md)

##### [Configure dashboards](guides/platform-management/configure-dashboards.md)

##### [Use ephemeral nodes](guides/platform-management/use-ephemeral-nodes.md)

#### [AI Workbench](guides/ai-workbench.md)

Build your own AI Workbench by bringing an AI agent and configuring it with Tenzir’s agent skills. Once set up, use it to write TQL pipelines, understand OCSF schemas, generate parsers, and create data mappings.

##### [Use agent skills](guides/ai-workbench/use-agent-skills.md)

### Work with Data

#### [Collecting](guides/collecting.md)

This guide provides an overview of data collection in TQL. You’ll learn about the different approaches for ingesting data from various sources.

##### [Read and watch files](guides/collecting/read-and-watch-files.md)

##### [Fetch via HTTP and APIs](guides/collecting/fetch-via-http-and-apis.md)

##### [Read from message brokers](guides/collecting/read-from-message-brokers.md)

##### [Get data from the network](guides/collecting/get-data-from-the-network.md)

#### Parsing

##### [Parse delimited text](guides/parsing/parse-delimited-text.md)

##### [Parse binary data](guides/parsing/parse-binary-data.md)

##### [Parse string fields](guides/parsing/parse-string-fields.md)

#### Transformation

##### [Filter and select data](guides/transformation/filter-and-select-data.md)

##### [Transform values](guides/transformation/transform-values.md)

##### [Manipulate strings](guides/transformation/manipulate-strings.md)

##### [Work with time](guides/transformation/work-with-time.md)

##### [Shape lists](guides/transformation/shape-lists.md)

##### [Shape records](guides/transformation/shape-records.md)

##### [Reshape complex data](guides/transformation/reshape-complex-data.md)

##### [Convert data formats](guides/transformation/convert-data-formats.md)

#### [Normalization](guides/normalization.md)

This guide provides an overview of data normalization in TQL. Normalization transforms raw, inconsistent data into a clean, standardized format that’s ready for analysis, storage, and sharing.

##### [Clean up values](guides/normalization/clean-up-values.md)

##### [Map to OCSF](guides/normalization/map-to-ocsf.md)

##### [Map to other schemas](guides/normalization/map-to-other-schemas.md)

#### Enrichment

##### [Work with lookup tables](guides/enrichment/work-with-lookup-tables.md)

##### [Enrich with network inventory](guides/enrichment/enrich-with-network-inventory.md)

##### [Enrich with threat intel](guides/enrichment/enrich-with-threat-intel.md)

##### [Execute Sigma rules](guides/enrichment/execute-sigma-rules.md)

#### Optimization

##### [Slice and sample data](guides/optimization/slice-and-sample-data.md)

##### [Deduplicate events](guides/optimization/deduplicate-events.md)

#### Routing

##### [Send to destinations](guides/routing/send-to-destinations.md)

##### [Split and merge streams](guides/routing/split-and-merge-streams.md)

##### [Load-balance pipelines](guides/routing/load-balance-pipelines.md)

#### Analytics

##### [Aggregate and summarize data](guides/analytics/aggregate-and-summarize.md)

##### [Collect metrics](guides/analytics/collect-metrics.md)

#### Edge Storage

##### [Import into a node](guides/edge-storage/import-into-a-node.md)

##### [Export from a node](guides/edge-storage/export-from-a-node.md)

##### [Show available schemas](guides/edge-storage/show-available-schemas.md)

##### [Transform data at rest](guides/edge-storage/transform-data-at-rest.md)

### Build

#### Packages

##### [Install a package](guides/packages/install-a-package.md)

##### [Create a package](guides/packages/create-a-package.md)

##### [Test packages](guides/packages/test-packages.md)

##### [Add operators](guides/packages/add-operators.md)

##### [Add pipelines](guides/packages/add-pipelines.md)

##### [Add contexts](guides/packages/add-contexts.md)

##### [Configure inputs](guides/packages/configure-inputs.md)

##### [Maintain a changelog](guides/packages/maintain-a-changelog.md)

##### [Publish a package](guides/packages/publish-a-package.md)

#### Testing

##### [Run tests](guides/testing/run-tests.md)

##### [Write tests](guides/testing/write-tests.md)

##### [Run fixtures](guides/testing/run-fixtures.md)

##### [Create fixtures](guides/testing/create-fixtures.md)

##### [Add custom runners](guides/testing/add-custom-runners.md)

### Contribute

#### Contribution

##### [Code of Conduct](guides/contribution/code-of-conduct.md)

##### [Git and GitHub Workflow](guides/contribution/workflow.md)

##### [Documentation](guides/contribution/documentation.md)

##### [Security Policy](guides/contribution/security.md)

#### Development

##### [Setup syntax highlighting](guides/development/setup-syntax-highlighting.md)

##### [Build from source](guides/development/build-from-source.md)

##### [Write a node plugin](guides/development/write-a-node-plugin.md)

## [Tutorials](tutorials.md)

Learning-oriented lessons that take you through a series of steps.
Start here when you want to get started with Tenzir.

### Fundamentals

#### [Learn idiomatic TQL](tutorials/learn-idiomatic-tql.md)

This tutorial teaches you to write TQL that is clear, efficient, and maintainable. It assumes you already know basic TQL syntax and operators, and shows you how experienced TQL developers approach common patterns.

#### [Write a package](tutorials/write-a-package.md)

This tutorial teaches you how packages bundle pipelines, operators, contexts, and examples. You’ll build a package for an SSL blacklist that detects malicious certificates. You can then install packages from the Tenzir Library or deploy them as code.

#### [Map data to OCSF](tutorials/map-data-to-ocsf.md)

In this tutorial you’ll learn how to map events to Open Cybersecurity Schema Framework (OCSF). We walk you through an example of events from a network monitor and show how you can use Tenzir pipelines to transform them into OCSF-compliant events.

### Analytics

#### [Plot data with charts](tutorials/plot-data-with-charts.md)

In this tutorial, you will learn how to use pipelines to plot data as charts.

## [Explanations](explanations.md)

Big-picture explanations of higher-level concepts.
Start here to build understanding of a particular topic.

### Architecture

#### [Deployment](explanations/deployment.md)

This page explains Tenzir’s deployment architecture, which separates data processing from management through a layered design. Three primary abstractions work together:

#### [Pipeline](explanations/pipeline.md)

A Tenzir pipeline is a chain of operators that represents a dataflow. Operators are the atomic building blocks that produce, transform, or consume data. Think of them as Unix or Powershell commands where the result from one command is feeding into the next:

#### [Node](explanations/node.md)

A node is a running process that manages and executes pipelines.

#### [Platform](explanations/platform.md)

The platform provides fleet management for nodes. With an API and web interface, the platform offers user and workspace administration, authentication via external identity providers (IdP), and dashboards consisting of pipeline-powered charts.

#### [Language](explanations/language.md)

The Tenzir Query Language (TQL) is a dataflow language designed for processing of unstructured byte-streams and semi-structured events.

### Concepts

#### [Configuration](explanations/configuration.md)

This page explains how to configure the Tenzir CLI and Node. Configuration flows through four layers, sorted by precedence:

#### [Secrets](explanations/secrets.md)

Operators accept secrets as parameters for sensitive values, such as authentication tokens, passwords, or even URLs.

#### [Enrichment](explanations/enrichment.md)

Enrichment means adding contextual data to events. The purpose of this added context is to allow for making better decisions, e.g., to triage alerts and weed out false positive, to leverage country information to classify logins as malicious, or to flag a sighting of an indicator of compromise.

#### [Packages](explanations/packages.md)

This page explains how packages bundle pipelines, operators, contexts, and examples into a deployable unit. You’ll learn about package design principles and how the components fit together.

### Help

#### [Glossary](explanations/glossary.md)

This page defines central terms in the Tenzir ecosystem.

#### [FAQs](explanations/faqs.md)

This page answers frequently asked questions about Tenzir.

## [Reference](reference.md)

Nitty-gritty technical descriptions of how Tenzir works.
Start here when you need detailed information about building blocks.

### Language (TQL)

#### [Type System](reference/types.md)

This page explains TQL’s type system, which provides strong typing with automatic inference. You get type safety without requiring explicit declarations. Key characteristics include:

#### [Expressions](reference/expressions.md)

Expressions form the computational core of TQL. They range from simple literals to complex evaluations.

#### [Statements](reference/statements.md)

TQL programs are a sequence of statements. Operator statements perform various actions on data streams. Each operator statement can be thought of as a modular unit that processes data and can be combined with other operators to create complex dataflows.

#### [Programs](reference/programs.md)

TQL programs compose statements into complete data processing workflows that can execute. Valid TQL programs adhere to the following rules:

#### [Operators](reference/operators.md)

Tenzir comes with a wide range of built-in pipeline operators.

#### [Functions](reference/functions.md)

Functions appear in expressions and take positional and/or named arguments, producing a value as a result of their computation.

### Tools

#### [Test Framework](reference/test-framework.md)

The `tenzir-test` harness discovers and runs integration tests for pipelines, fixtures, and custom runners. Use this page as a reference for concepts, configuration, and CLI details. For step-by-step walkthroughs, see the guides for running tests, writing tests, creating fixtures, and adding custom runners.

#### [Ship Framework](reference/ship-framework.md)

`tenzir-ship` helps you ship faster with automated release engineering. Manage changelogs, generate release notes, and publish GitHub releases. Use this page as a reference for concepts, configuration, and CLI details. For step-by-step walkthroughs, see the guide for maintaining a changelog.

### Workflows

#### [Create a parser package](reference/workflows/create-parser-package.md)

This workflow guides you through creating a package to parse and clean log events. To this end, you scaffold a Tenzir package and build user-defined operators.

#### [Create an OCSF mapping](reference/workflows/create-ocsf-mapping.md)

This workflow guides you through creating an OCSF mapping for a parser package. It builds on a parser package, adding OCSF-specific mapping and validation steps.

#### Node Index

- [Node Configuration](reference/node/configuration.md)

#### Platform Index

- [Platform command line interface](reference/platform/command-line-interface.md)
- [Platform Configuration](reference/platform/configuration.md)

### Indexes

For the complete operator listing by category, read [Operator Index](reference/operators-index.md).

For the complete function listing by category, read [Function Index](reference/functions-index.md).

## [Integrations](integrations.md)

Turn-key packages and native connectors for security tools.
Start here to connect Tenzir with Splunk, Elastic, CrowdStrike, etc.

### Cloud Providers

#### [Amazon](integrations/amazon.md)

Tenzir integrates with the services from Amazon Web Services (AWS) listed below.

##### [MSK](integrations/amazon/msk.md)

##### [S3](integrations/amazon/s3.md)

##### [Security Lake](integrations/amazon/security-lake.md)

##### [SQS](integrations/amazon/sqs.md)

#### Google

##### [Cloud Logging](integrations/google/cloud-logging.md)

##### [Cloud Storage](integrations/google/cloud-storage.md)

##### [Cloud Pub/Sub](integrations/google/cloud-pubsub.md)

##### [SecOps](integrations/google/secops.md)

#### Microsoft

##### [Azure Blob Storage](integrations/microsoft/azure-blob-storage.md)

##### [Azure Event Hubs](integrations/microsoft/azure-event-hubs.md)

##### [Defender](integrations/microsoft/defender.md)

##### [Sentinel & Log Analytics](integrations/microsoft/sentinel-log-analytics.md)

##### [Windows Event Logs](integrations/microsoft/windows-event-logs.md)

### Messaging

#### [AMQP](integrations/amqp.md)

The Advanced Message Queuing Protocol (AMQP) is an open standard application layer protocol for message-oriented middleware.

#### [Fluent Bit](integrations/fluent-bit.md)

Fluent Bit is a an open source observability pipeline. Tenzir embeds Fluent Bit, exposing all its inputs via `from_fluent_bit` and outputs via `to_fluent_bit`

#### [Kafka](integrations/kafka.md)

Apache Kafka is a distributed open-source message broker. The Tenzir integration can publish (send messages to a topic) or subscribe (receive) messages from a topic.

#### [ZeroMQ](integrations/zeromq.md)

ZeroMQ (0mq) is a light-weight messaging framework with various socket types. Tenzir supports writing to PUB sockets and reading from SUB sockets, both in server (listening) and client (connect) mode.

### Protocols

#### [Email](integrations/email.md)

Tenzir supports sending events as email using the `save_email` operator. To this end, the operator establishes a connection with an SMTP server that sends the message on behalf of Tenzir.

#### [File](integrations/file.md)

Tenzir supports reading from and writing to files, including non-regular files, such as Unix domain sockets, standard input, standard output, and standard error.

#### [FTP](integrations/ftp.md)

Tenzir supports the File Transfer Protocol (FTP), both downloading and uploading files.

#### [HTTP](integrations/http.md)

Tenzir supports HTTP and HTTPS, both as sender and receiver.

#### [Network Interface](integrations/nic.md)

Tenzir supports reading packets from a network interface card (NIC).

#### [Syslog](integrations/syslog.md)

Tenzir supports parsing and emitting Syslog messages across multiple transport protocols, including both UDP and TCP. This enables seamless integration with Syslog-based systems for ingesting or exporting logs.

#### [TCP](integrations/tcp.md)

The Transmission Control Protocol (TCP) offers a bi-directional byte stream between applications that communicate via IP. Tenzir supports writing to and reading from TCP sockets, both in server (listening) and client (connect) mode.

#### [UDP](integrations/udp.md)

The User Datagram Protocol (UDP) is a connection-less protocol to send messages on an IP network. Tenzir supports writing to and reading from UDP sockets, both in server (listening) and client (connect) mode.

### Data Tools

#### [ClickHouse](integrations/clickhouse.md)

ClickHouse is an open-source analytical database that enables its users to generate powerful analytics, using SQL queries, in real-time.

#### [Elasticsearch](integrations/elasticsearch.md)

Elasticsearch is a search and observability suite for unstructured data. Tenzir can send events to Elasticsearch and emulate and Elasticsearch Bulk API endpoint.

#### [Graylog](integrations/graylog.md)

Graylog is a log management solution based on top of OpenSearch. Tenzir can send data to and receive data from Graylog.1

#### [OpenSearch](integrations/opensearch.md)

OpenSearch is a search and observability suite for unstructured data. Tenzir can send events to OpenSearch and emulate and OpenSearch Bulk API endpoint.

#### [Snowflake](integrations/snowflake.md)

Snowflake is a multi-cloud data warehouse. Tenzir can send events from a pipeline to Snowflake databases.

#### [Splunk](integrations/splunk.md)

Splunk is a SIEM solution for storing and processing logs. Tenzir can send data to Splunk via HEC.

### Security Tools

#### [SentinelOne Data Lake](integrations/sentinelone-data-lake.md)

SentinelOne is a cybersecurity platform that provides endpoint protection and threat detection. The SentinelOne Singularity Data Lake allows you to store and analyze security events at scale. Tenzir provides bidirectional integration with the SentinelOne Data Lake via its REST API.

#### [Suricata](integrations/suricata.md)

Suricata is network monitor with a rule matching engine to detect threats. Use Tenzir to acquire, process, and store Suricata logs.

#### [Velociraptor](integrations/velociraptor.md)

Velociraptor is a digital forensics and incident response (DFIR) tool for interrogating endpoints.

#### [Zeek](integrations/zeek.md)

The Zeek network monitor translates raw packets into structured logs. Tenzir supports various Zeek use cases, such as continuous ingestion, ad-hoc log file processing, and even generating Zeek logs.

#### [Zscaler](integrations/zscaler.md)

Zscaler’s Nanolog Streaming Service (NSS) is a family of products that enable Zscaler cloud communication with third-party security solution devices for exchanging event logs. You can either use Zscaler’s Cloud NSS or deploy an on-prem NSS server to obtain the logs. Tenzir can receive Zscaler logs in either case.
