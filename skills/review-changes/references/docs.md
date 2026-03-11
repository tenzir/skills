# Documentation Lens

Use this lens when code changes affect docs, docstrings, examples, or README
content.

## Focus Areas

- **Accuracy.** Docs must match actual behavior. When a function's signature,
  default value, or return type changes, every doc that references it becomes a
  potential lie. Trace the change through docstrings, README, and `.docs/`.
- **Completeness.** New user-facing behavior needs documentation where users
  will look for it. A new CLI flag without a `--help` entry, a new operator
  without a docs page, or a new config option without a comment in the example
  config are all gaps.
- **Example validity.** Code examples in docs should still compile and produce
  the advertised output after the change. If the diff changes an API, grep for
  that API in doc examples.
- **Cross-links and references.** Linked pages, related-docs sections, and
  table-of-contents entries should stay coherent. Adding a new page without
  linking it from the parent index is a common miss.
- **Style.** Follow existing documentation conventions and the Tenzir
  technical-writing guide. Consistent terminology, active voice, and concrete
  examples over abstract descriptions.

## What a Real Finding Looks Like

```markdown
### 🟡 P3 · 📖 DOC-1 · New `--timeout` flag undocumented · 85%

- **File:** plugins/http/src/plugin.cpp:48
- **Issue:** The diff adds a `--timeout` flag to the `http` operator but
  neither the operator's docstring nor `docs/operators/http.md` mention it.
- **Reasoning:** Users discovering the flag via `--help` won't find
  explanation of units, default value, or interaction with retries unless
  the docs page is updated.
- **Evidence:** `parser.add("--timeout", ...)` added in plugin.cpp;
  `rg 'timeout' docs/operators/http.md` returns no matches.
- **Suggestion:** Add a row to the options table in `docs/operators/http.md`
  and include a brief example showing the flag in use.
```

## Common False Positives to Avoid

- Demanding documentation updates for internal refactors that don't change
  user-visible behavior.
- Flagging doc style issues (Oxford comma, heading capitalization) that aren't
  part of the project's established conventions.
- Insisting on docstrings for every private helper function — document public
  interfaces and non-obvious internals.
