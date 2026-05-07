# Architecture Lens

Use this lens when evaluating API shape, modularity, and complexity.

## Focus Areas

- **API design and public interface clarity.** Are new public functions or
  types named and shaped so that callers understand them without reading the
  implementation? Do they follow existing conventions in the codebase?
- **Separation of concerns.** Does the change mix layers (e.g., I/O logic in a
  data transformation, UI logic in a backend handler)?
- **Unnecessary complexity.** Is the solution simpler than the problem
  requires, or does it introduce abstractions that don't yet pay for
  themselves? A concrete function is better than a generic framework used once.
- **Hidden coupling.** Does the change create implicit dependencies between
  modules — shared global state, order-dependent initialization, or assumptions
  about another component's internals?
- **Breaking changes.** Does the diff alter a public API, config format, or
  wire protocol in a way that breaks existing consumers without a migration
  path?

## What a Real Finding Looks Like

```markdown
### 🟠 P2 · 🏗️ ARC-1 · Operator plugin leaks transport details · 88%

- **File:** plugins/kafka/src/operator.cpp:74
- **Issue:** The `kafka_read` operator directly constructs librdkafka consumer
  objects, coupling operator logic to a specific transport library.
- **Reasoning:** Other operators use the connector abstraction to separate
  transport from processing. Bypassing it here makes the operator untestable
  without a live Kafka broker and blocks future transport swaps.
- **Evidence:** `rd_kafka_consumer_new()` called directly in operator body
  instead of going through `connector::read()`.
- **Suggestion:** Inject a connector instance and delegate transport to it,
  matching the pattern in `plugins/amqp/`.
```

## Common False Positives to Avoid

- Demanding abstraction layers for code that has exactly one use case and no
  planned reuse. Wait for the second use before generalizing.
- Flagging tight coupling in test helpers or scripts — these are meant to be
  concrete and disposable.
- Suggesting design changes that amount to "I would have done it differently"
  without a concrete maintainability or correctness argument.
