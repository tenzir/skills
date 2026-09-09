---
title: "Pipeline"
canonical: https://tenzir.com/docs/explanations/pipeline
source: https://tenzir.com/docs/explanations/pipeline.md
section: "Docs"
---

# Pipeline

> A Tenzir pipeline is a chain of operators that represents a dataflow. Operators are the atomic building blocks that produce, transform, or consume data. Think of them as Unix or Powershell commands where the result from one command is feeding into the next:

A Tenzir **pipeline** is a chain of **operators** that represents a dataflow. Operators are the atomic building blocks that produce, transform, or consume data. Think of them as Unix or Powershell commands where the result from one command is feeding into the next:

Our pipelines have 3 types of operators: **inputs** that produce data, **outputs** that consume data, and **transformations** that do both:

You write pipelines in the [Tenzir Query Language (TQL)](language.md), a language that we developed from the ground up to concisely describe such dataflows.

Learn TQL

Head over to our [language documentation](language.md) for an in-depth explanation of how TQL works. We’re continuing here with high-level architectural aspects of the pipeline execution model.

## Typed Operators

Tenzir pipelines operate both ond unstructured stream of bytes and typed event streams. The execution model ensures type safety while maintaining high performance through batching and parallel processing.

An operator has an **upstream** and **downstream** type:

This typing ensures pipelines are well-formed. Adjacent operators must have matching types: the downstream type of one operator must match the upstream type of the next, i.e., upstream/downstream types of adjacent operators have to match. Otherwise the pipeline is malformed.

With these operators as building blocks, you can create all kinds of pipelines, as long as they follow the two principal rules of (1) sequencing inputs, transformations, and outputs, and (2) ensuring that operator upstream/downstream types match. Here are examples of other valid pipeline variations:

## Multi-Schema Dataflows

As mentioned above, pipelines can transport both *bytes* and *events*. Let’s go deeper into the details of Tenzir represents events. Every event that flows through a pipeline is part of a *data frame* with a schema. Internally, these data frames are represented as Apache Arrow record batches, encoding potentially of tens of thousands of events in a single block of data. This innate batching is the reason why the pipelines can achieve high throughput.

Unique about Tenzir’s pipeline executor is that a single pipeline can process events with *multiple schemas*. When you typically work with data frames, your workload runs on input with a fixed schema, e.g., when you query a database table. In Tenzir, schemas can change dynamically during the execution of a pipeline, much like document-oriented engines that work on JSON or have one-event-at-a-time processing semantics. Tenzir is unique in that it gives the user the feeling of operating on a single event at a time while hiding the structured data frame batching behind the scenes. Thus, Tenzir combines the performance of structured query engines with the flexibility of document-oriented engines, making it perfect fit for processing *semi-structured data* at scale:

<!--?xml version="1.0" standalone="no"?-->

The schema variance begins early in the data flow, where parsers emit events with changing schemas as they encounter changing fields. If an operator detects a schema changes, it creates a new batch of events. In terms of performance, the worst case for Tenzir is a ordered stream of schema-switching events, with every event having a new schema than the previous one. But even for those scenarios operators can efficiently build homogeneous batches when the inter-event order does not matter. Similar to predicate pushdown, Tenzir operators support *ordering pushdown* to signal to upstream operators that the event order only matters intra-schema but not inter-schema. In this case the operator transparently “demultiplex” a heterogeneous event stream into N homogeneous streams. The [`sort`](https://tenzir.com/docs/reference/operators/sort.md) operator is an example of such an operator; it pushes its ordering requirements upstream, allowing parsers to efficiently create multiple streams events in parallel. The [Optimization](pipeline.md#optimization) section describes this and the other rewrites the optimizer performs.

Some operators only work with exactly one instance per schema internally, such as [`write_csv`](https://tenzir.com/docs/reference/operators/write_csv.md), which first writes a header and then all subsequent rows have to adhere to the emitted schema. Such operators cannot handle events with changing schemas.

It’s important to mention that most of the time you don’t have to worry about schemas. They are there for you when you want to work with them, but it’s often enough to just specified the fields that you want to work with, e.g., `where id.orig_h in 10.0.0.0/8`, or `select src_ip, dest_ip, proto`. Schemas are inferred automatically in parsers, but you can also seed a parser with a schema that you define explicitly.

## Parallel Execution

The operators of a pipeline always run concurrently: while one operator parses a batch, the next one already transforms the previous batch. Beyond that, Tenzir can run a *single* operator on multiple cores by replicating it into several instances that each process a share of the batches.

The planner rewrites the single chain of operators into several lanes that run side by side, fanning batches out across the instances, exchanging them where an operator needs it, and gathering them again at the end. An expensive operator then stops being a single-core bottleneck, because several cores work on it at once:

Which operators Tenzir replicates depends on what they need to see. An operator that treats every event on its own, such as [`where`](https://tenzir.com/docs/reference/operators/where.md), an assignment, or [`ocsf_cast`](https://tenzir.com/docs/reference/operators/ocsf_cast.md), works on any batch it receives, so Tenzir hands its instances whichever batches are available.

Operators that combine related events need more care. [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md), [`group`](https://tenzir.com/docs/reference/operators/group.md), and [`deduplicate`](https://tenzir.com/docs/reference/operators/deduplicate.md) only produce the right result if every event of a group reaches the same instance. Tenzir therefore partitions the stream by the operator’s key fields and routes each event to the instance that owns its key.

Parallelism is off by default. You opt in per pipeline with a `// parallelism:` comment, as the guide on [tuning performance](../guides/node-setup/tune-performance.md#parallelism) shows.

## Optimization

Before a pipeline runs, the **optimizer** rewrites it so that the source reads, transfers, and decodes only what the rest of the pipeline needs. It walks the pipeline from its last operator to its first and hands every operator a request from its downstream neighbor. The request captures four things:

* **Predicates** from [`where`](https://tenzir.com/docs/reference/operators/where.md) that filter the operator’s output.
* An **ordering** requirement: whether downstream depends on the event order.
* A **limit** from [`head`](https://tenzir.com/docs/reference/operators/head.md): how many events downstream needs at most.
* A **projection** from [`select`](https://tenzir.com/docs/reference/operators/select.md): the fields downstream reads.

An operator that does not affect a requirement passes it on. One that does, adjusts or stops it: [`set`](https://tenzir.com/docs/reference/operators/set.md) keeps a predicate that reads the field it assigns, [`sort`](https://tenzir.com/docs/reference/operators/sort.md) stops a limit because it needs all of its input, and any reference to `this` widens a projection to all fields. The source at the start receives what survived and acts on the parts it understands.

Take this pipeline:

```tql
from_clickhouse table="logs.events"
where severity > 3 or source == "fw"
select id, message
head 100
```

Read literally, it fetches every row and column, then discards most of them. Instead, [`from_clickhouse`](https://tenzir.com/docs/reference/operators/from_clickhouse.md) sends a single query that does all of that on the server:

```sql
SELECT id, message, severity, source
FROM logs.events
WHERE (severity > 3 OR source = 'fw')
LIMIT 100
```

Every rewrite preserves results. The `where`, `select`, and `head` stay in the pipeline, so a source that acts on a hint only partially, or not at all, still produces the same output. When only part of a predicate translates, for example because it calls a function the backend does not have, the source pushes what it can and evaluates the rest itself.

Which hints a source acts on depends on its backend. A source that acts on them, such as [`from_clickhouse`](https://tenzir.com/docs/reference/operators/from_clickhouse.md), has an *Optimizations* section on its reference page that states what it pushes and what stays in Tenzir. Parsers use the ordering requirement as described in [Multi-Schema Dataflows](pipeline.md#multi-schema-dataflows).

Federated Search

These optimizations reach any source, including operators that query remote storage, databases, or SIEMs, which is what makes **federated search** across distributed systems a transparent capability of the engine rather than a feature you configure.
