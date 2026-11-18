---
title: "Overview"
description: "Query stored events and continue processing the results."
canonical: https://tenzir.com/docs/guides/search
source: https://tenzir.com/docs/guides/search.md
section: "Docs"
---

# Overview

> Query stored events and continue processing the results.

Search reads events that a data store already holds. Push selective work into the storage system, then continue processing the results in TQL.

The guide on [reading from data stores](collect/read-from-data-stores.md) covers tables, SQL queries, and new rows. Our reference on [optimizations](../reference/optimizations.md) lists the filters, field selections, and limits that each source hands to its data store. Our tutorial on building an OCSF lake with ClickHouse shows how to [read the stored events back](../tutorials/build-an-ocsf-lake-with-clickhouse.md#read-events-back).
