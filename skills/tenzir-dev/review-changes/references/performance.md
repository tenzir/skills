# Performance Lens

Use this lens when the diff touches hot paths, loops, queries, or large data
handling.

Focus on:

- algorithmic complexity
- unnecessary allocations or copies
- N+1 queries or repeated external calls
- missing caching or reuse of expensive work
- eager loading of data that could be deferred

Call out performance issues only when the impact is plausible for real usage,
not just theoretically possible.
