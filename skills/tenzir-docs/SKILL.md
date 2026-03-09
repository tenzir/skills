---
name: tenzir-docs
description: Answer questions using the Tenzir documentation. Use when the user asks about TQL, operators, pipelines, packages, nodes, the platform, MCP tools, or documented integrations.
---

# Tenzir Documentation Map

> The low-code data pipeline solution for security teams

Tenzir is a data pipeline engine for security teams. Run pipelines to collect,
parse, transform, and route security data. Deploy nodes on-prem or in the cloud,
and manage them via the Tenzir Platform.

## [Guides](guides.md)

Practical step-by-step explanations to help you achieve a specific goal.
Start here when you're trying to get something done.

### Get Started

#### [Quickstart](guides/quickstart.md)

Drowning in logs, alerts, and rigid tools? Meet Tenzir—your engine for taming security data. In just a few minutes, you’ll be ingesting, transforming, and enriching data on your terms, with full control. Here’s what you’ll accomplish:

#### [Installation](guides/installation.md)

This guide shows you how to install the Tenzir CLI to run pipelines locally or deploy a persistent node. The package includes two binaries:

### Setup

#### [Node Setup](guides/node-setup.md)

The Tenzir Node is the vehicle to run pipelines. It is light-weight server application that can be deployed on-premises or in the cloud.

#### [Platform Setup](guides/platform-setup.md)

The Tenzir Platform acts as a fleet management control plane for Tenzir Nodes. Use its web interface to explore data, create pipelines, and build dashboards.

#### [AI Workbench](guides/ai-workbench.md)

Build your own AI Workbench by bringing an AI agent and configuring it according to the guides in this section. Once set up, use it to write TQL pipelines, understand OCSF schemas, generate parsers, and create data mappings.

### Work with Data

#### [Collecting](guides/collecting.md)

This guide provides an overview of data collection in TQL. You’ll learn about the different approaches for ingesting data from various sources.

#### [Normalization](guides/normalization.md)

This guide provides an overview of data normalization in TQL. Normalization transforms raw, inconsistent data into a clean, standardized format that’s ready for analysis, storage, and sharing.

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

## [Integrations](integrations.md)

Turn-key packages and native connectors for security tools.
Start here to connect Tenzir with Splunk, Elastic, CrowdStrike, etc.

### Cloud Providers

#### [Amazon](integrations/amazon.md)

Tenzir integrates with the services from Amazon Web Services (AWS) listed below.

### Messaging

#### [AMQP](integrations/amqp.md)

The Advanced Message Queuing Protocol (AMQP) is an open standard application layer protocol for message-oriented middleware.

#### [Fluent Bit](integrations/fluent-bit.md)

Fluent Bit is a an open source observability pipeline. Tenzir embeds Fluent Bit, exposing all its inputs via from_fluent_bit and outputs via to_fluent_bit

#### [Kafka](integrations/kafka.md)

Apache Kafka is a distributed open-source message broker. The Tenzir integration can publish (send messages to a topic) or subscribe (receive) messages from a topic.

#### [ZeroMQ](integrations/zeromq.md)

ZeroMQ (0mq) is a light-weight messaging framework with various socket types. Tenzir supports writing to PUB sockets and reading from SUB sockets, both in server (listening) and client (connect) mode.

### Protocols

#### [Email](integrations/email.md)

Tenzir supports sending events as email using the save_email operator. To this end, the operator establishes a connection with an SMTP server that sends the message on behalf of Tenzir.

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
