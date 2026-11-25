---
title: "Overview"
description: "Add context that the original event does not contain."
canonical: https://tenzir.com/docs/guides/enrich
source: https://tenzir.com/docs/guides/enrich.md
section: "Docs"
---

# Overview

> Add context that the original event does not contain.

Enrichment adds context such as asset ownership, threat intelligence, and model-generated labels to events as they pass through a pipeline.

Use [lookup tables](enrich/use-lookup-tables.md), [asset inventory](enrich/enrich-with-asset-inventory.md), [threat intelligence](enrich/enrich-with-threat-intel.md), [AI enrichment](enrich/enrich-events-with-ai.md), or [event-stream joins](enrich/join-event-streams.md) to supply the context your downstream systems need. Lookup tables and other stateful sources live in contexts, which you [declare in your deployment’s configuration](enrich/declare-contexts.md), while [`join`](../reference/operators/join.md) correlates events against a finite source directly inside a single pipeline.
