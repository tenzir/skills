# Test Lens

Use this lens when the change adds behavior, fixes a bug, or modifies branching
logic.

Focus on:

- coverage for new or changed code paths
- boundary cases and failure modes
- behavior-oriented assertions instead of implementation coupling
- deterministic, isolated tests
- test names that describe the verified behavior

Call out missing tests when the change could regress silently or when the fix is
hard to trust without coverage.
