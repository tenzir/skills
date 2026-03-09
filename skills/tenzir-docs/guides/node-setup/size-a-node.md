# Size a node


This guide helps you determine the CPU, RAM, and storage resources needed for a Tenzir node. Use the [calculator](#calculator) below to get concrete estimates based on your deployment scenario.

## Calculator

Adjust the sliders to match your expected workload:

<!-- Data Volume Section -->

Data Volume

GB/day EPS

432.0 GB/day 232 EPS

<!-- GB/day mode inputs (shown by default) -->

Ingest GB

10 10

Bytes/event

500 500

<!-- EPS mode inputs (hidden by default) -->

Events/sec

10000 10,000

Bytes/event

500 500

***

<!-- Sources Row -->

Sources

1 1

<!-- Destinations Row -->

Destinations

1 1

<!-- Edge Storage Row -->

Edge Storage

3 3 months

***

<!-- Workloads Row -->

Workloads

\[x] Normalization \[ ] Enrichment \[ ] Detection

<!-- Context Size Row (conditional) -->

Context Size

2 2 GB

***

<!-- Output Cards -->

CPU 2 cores

RAM 1.0 GB

Storage 0.09 TB

## Input factors

The calculator considers the following factors to estimate resource requirements.

### Data volume

The amount of data flowing through your node is the primary driver for resource requirements. You can specify your ingest rate either as **GB/day** or as **events per second (EPS)**. The calculator converts between these units based on the average bytes per event.

Typical event sizes vary by source:

* Firewall logs: 300–800 bytes
* EDR telemetry: 500–2,000 bytes
* Cloud audit logs: 1,000–5,000 bytes

### Sources

The number of distinct data sources feeding into your node. Each source requires parsing incoming data (typically JSON) and maintaining input buffers. The calculator assumes approximately 10 different log types per source, which is typical for firewalls, EDRs, and cloud providers.

### Destinations

The number of outputs where your node sends data. Each destination requires serializing data (e.g., to Parquet or JSON) and maintaining output buffers. Common destinations include cloud storage, SIEMs, and data lakes.

### Edge storage

How long data stays in the node’s edge storage before deletion or archival. This determines your **storage** requirements. Tenzir uses Zstd compression, achieving roughly 10× reduction of the raw input volume.

Note that this refers to data stored *on the node itself*, not data forwarded to external destinations like a data lake.

## Workloads

Optional workloads add overhead to the base resource requirements.

### Normalization

Normalization parses and transforms raw data into structured events with a common schema. This adds **CPU** overhead proportional to the number of sources and log types.

### Enrichment

[Enriching](../../explanations/enrichment.md) events with context data requires holding lookup tables in memory. The **Context Size** slider lets you specify how much data you plan to use for enrichment. This directly affects your **RAM** requirements.

### Detection

Running detection rules, correlations, or analytics adds **CPU** overhead for rule evaluation and **RAM** for maintaining state across events (e.g., for time-windowed correlations).