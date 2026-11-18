---
title: "Overview"
description: "Persist events for later search, replay, and analysis."
canonical: https://tenzir.com/docs/guides/store
source: https://tenzir.com/docs/guides/store.md
section: "Docs"
---

# Overview

> Persist events for later search, replay, and analysis.

Storage keeps events beyond the lifetime of a running pipeline. A deployment holds no events of its own, so pipelines write them to object storage as partitioned files or to an external database such as ClickHouse.

Learn how to [write partitioned files](store/write-partitioned-files.md). To store OCSF events in ClickHouse, follow our tutorial on [building an OCSF lake with ClickHouse](../tutorials/build-an-ocsf-lake-with-clickhouse.md).
