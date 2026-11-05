---
title: "Overview"
description: "Persist events for later search, replay, and analysis."
canonical: https://tenzir.com/docs/guides/store
source: https://tenzir.com/docs/guides/store.md
section: "Docs"
---

# Overview

> Persist events for later search, replay, and analysis.

Storage keeps events beyond the lifetime of a running pipeline. Tenzir can write partitioned files to object storage, import events into a node, or write them to an external database such as ClickHouse.

Learn how to [write partitioned files](store/write-partitioned-files.md), [import into a node](store/import-into-a-node.md), [inspect stored schemas](store/show-available-schemas.md), and [transform data at rest](store/transform-data-at-rest.md). To store OCSF events in ClickHouse, follow our tutorial on [building an OCSF lake with ClickHouse](../tutorials/build-an-ocsf-lake-with-clickhouse.md).
