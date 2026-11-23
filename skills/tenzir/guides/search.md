---
title: "Overview"
description: "Push selective queries to data stores, search across heterogeneous backends in one pipeline, and scan Parquet archives in place."
canonical: https://tenzir.com/docs/guides/search
source: https://tenzir.com/docs/guides/search.md
section: "Docs"
---

# Overview

> Push selective queries to data stores, search across heterogeneous backends in one pipeline, and scan Parquet archives in place.

Search reads events where they already live and feeds the results straight into TQL. Instead of copying every log into one platform before you can ask a question, you query databases, SIEMs, EDRs, cloud APIs, and object-store archives directly, then normalize, enrich, correlate, or route the answers in the same pipeline.

Tenzir organizes search around three complementary workflows:

* Push work down to remote stores. Write standard TQL filters, projections, summaries, sorts, and limits after a remote source, and let each source transpile the supported leading work into its target’s native query language (such as ClickHouse, DuckDB, Splunk, Microsoft Defender, Azure Log Analytics, Axiom, SentinelOne, or CloudWatch Logs) while remaining filters and transforms run in Tenzir. Learn how to [push queries to data stores](search/push-queries-to-data-stores.md).
* Run federated search across heterogeneous stores. Query a SIEM, a data lake, an EDR, and an archive in a single pipeline, normalize their results into a shared schema such as OCSF, deduplicate overlapping sightings while keeping provenance, and let the optimizer rewrite filters written on normalized fields ahead of mappings so each target pushes down the leading portion it can express. Follow our guide on [searching across data stores](search/search-across-data-stores.md).
* Query open Parquet archives in place. Search partitioned Parquet files on local disk or object storage with row-group skipping, column projection, and HTTP range requests, or run SQL joins across archive files through embedded DuckDB, without rehydrating data back into a SIEM. Follow our guide on [querying open archives in place](search/query-open-archives-in-place.md).

For background on how Tenzir compiles TQL operators into native target queries and how target semantics differ from TQL, read our explanation of [transpilation](../explanations/transpilation.md). To understand how the optimizer rewrites predicates and propagates projections upstream, read our explanation of [pipeline optimization](../explanations/pipeline.md#optimization). To compare what each source pushes down and what each target computes, see our [optimizations reference](../reference/optimizations.md).

If you need to inspect database metadata, read full tables, or poll a table for new rows, see our guide on [reading from data stores](collect/read-from-data-stores.md). When you want to feed stored archives back through live detection pipelines with controlled timestamps and pacing, follow our guide on [replaying historical events](replay/replay-historical-events.md). Our tutorial on building an OCSF lake with ClickHouse also walks through [reading stored OCSF events back](../tutorials/build-an-ocsf-lake-with-clickhouse.md#read-events-back).
