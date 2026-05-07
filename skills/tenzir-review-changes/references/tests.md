# Test Lens

Use this lens when the change adds behavior, fixes a bug, or modifies branching
logic.

## Focus Areas

- **Coverage for new or changed code paths.** Every new branch, error case, or
  feature should have at least one test that exercises it. If a bug is fixed,
  there should be a regression test that would have caught it.
- **Boundary cases and failure modes.** Empty inputs, zero-length collections,
  maximum values, malformed data, permission errors, network timeouts. These
  are where bugs hide.
- **Behavior-oriented assertions.** Tests should assert on observable outcomes
  (output values, side effects, error messages), not implementation details
  (which internal function was called, how many times).
- **Determinism and isolation.** Tests that depend on wall-clock time, random
  values, network state, or shared mutable state are flaky by nature. Look for
  these dependencies and flag them.
- **Test names.** Names should describe the scenario and expected behavior, not
  the function under test. `test_empty_input_returns_error` beats
  `test_parse`.

## What a Real Finding Looks Like

```markdown
### 🟠 P2 · 🧪 TST-1 · No test for the fixed race condition · 90%

- **File:** src/scheduler.cpp:210
- **Issue:** The fix adds a mutex around shared state but no test reproduces
  the race that motivated it.
- **Reasoning:** Without a regression test, a future refactor could reintroduce
  the same race silently. Concurrent tests are hard, but even a stress test
  with a tight loop increases confidence.
- **Evidence:** PR description says "fixes intermittent crash in scheduler" but
  `tests/` has no new or modified test files.
- **Suggestion:** Add a test that spawns two threads both calling
  `scheduler::submit()` in a tight loop and asserts no crash or data
  corruption.
```

## Common False Positives to Avoid

- Demanding 100% line coverage. Focus on behavioral coverage of code that
  matters — not getters, trivial constructors, or logging statements.
- Flagging missing tests for pure refactors that don't change behavior and
  already have passing tests.
- Suggesting integration tests when a unit test would suffice, or vice versa,
  without considering the test suite's existing structure and conventions.
