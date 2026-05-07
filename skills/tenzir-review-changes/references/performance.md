# Performance Lens

Use this lens when the diff touches hot paths, loops, queries, or large data
handling.

## Focus Areas

- **Algorithmic complexity.** An O(n²) loop over a collection that grows with
  user data is a real problem. An O(n²) loop over a 5-element config list is
  not. Consider realistic input sizes.
- **Unnecessary allocations or copies.** Large objects copied by value in a
  loop, string concatenation in a hot path, or repeated construction of
  objects that could be reused.
- **N+1 queries or repeated external calls.** Fetching related data one row at
  a time inside a loop instead of batching. Making the same API call on every
  iteration when the result is invariant.
- **Missing caching or memoization.** Expensive computations repeated with
  identical inputs, especially in request-handling or pipeline-processing
  paths.
- **Eager loading of data that could be deferred.** Reading entire files into
  memory when streaming would work, or loading all records when only the first
  N are needed.
- **Lock contention and synchronization overhead.** Holding locks across I/O
  operations, using a global mutex where a per-object lock would reduce
  contention.

## What a Real Finding Looks Like

```markdown
### 🟠 P2 · 🚀 PRF-1 · Quadratic scan in event matching · 88%

- **File:** src/matcher.cpp:95
- **Issue:** For each incoming event, the matcher iterates all registered
  rules. With 10k rules and high event throughput, this becomes a bottleneck.
- **Reasoning:** The inner loop is O(rules × events_per_second). At current
  deployment sizes (~5k rules), this path runs ~50M comparisons per second.
- **Evidence:** `for (auto& rule : rules_) { if (rule.matches(event)) ... }`
  with no early exit or indexing.
- **Suggestion:** Index rules by event type or field prefix so the inner loop
  only considers candidate rules. A hash-based dispatch reduced latency 10×
  in a similar pattern in `plugins/sigma/`.
```

## Common False Positives to Avoid

- Flagging micro-optimizations in code that runs once at startup or during
  configuration loading. Focus on steady-state hot paths.
- Suggesting `std::move` or `reserve()` in code paths that handle small,
  bounded collections — the readability cost outweighs the gain.
- Raising performance concerns without estimating realistic input sizes. "This
  could be slow" is not a finding; "This is O(n²) and n can reach 100k in
  production" is.
