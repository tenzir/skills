# Readability Lens

Use this lens when code clarity, naming, or local comprehension is the main
concern. This lens is the baseline — load it for every review.

## Focus Areas

- **Naming quality.** Do variable, function, and type names reveal intent? A
  name like `process_data` tells you nothing; `aggregate_hourly_metrics` tells
  you everything. Flag names that force the reader to look at the
  implementation to understand the purpose.
- **Language-idiomatic patterns.** Code should follow the conventions of its
  language and the surrounding codebase. Using raw loops where standard
  algorithms apply, reinventing RAII in C++, or ignoring error returns in Go
  are readability problems because they break reader expectations.
- **Control-flow clarity.** Deeply nested conditionals, early returns mixed
  with late returns in the same function, or boolean logic that requires a
  truth table to understand. Prefer guard clauses and flat control flow.
- **Comments.** Flag comments that are missing where the code does something
  non-obvious, misleading where the code has drifted, or redundant where they
  just restate the code. A good comment explains _why_, not _what_.
- **Function length and cohesion.** Functions that do multiple unrelated things
  or exceed ~50 lines usually benefit from extraction — but only if the
  extracted pieces are meaningful on their own.

## What a Real Finding Looks Like

```markdown
### 🟡 P3 · 👁️ RDY-1 · Opaque boolean parameter · 82%

- **File:** src/pipeline/builder.cpp:203
- **Issue:** `create_operator(spec, true, false)` — the boolean arguments
  are meaningless without checking the signature.
- **Reasoning:** Callers of this function cannot understand what `true, false`
  means at the call site. This will cause mistakes when someone adds a third
  boolean or swaps the order.
- **Evidence:** Three call sites in the diff all pass different combinations
  of booleans with no named constants or comments.
- **Suggestion:** Replace with an enum or a struct:
  `create_operator(spec, {.lazy = true, .validated = false})`.
```

## Common False Positives to Avoid

- Nitpicking formatting, brace style, or whitespace — these are the
  formatter's job.
- Suggesting renames for well-established conventions in the codebase, even if
  you'd have named it differently in isolation.
- Flagging short variable names in tight scopes (e.g., `i` in a 3-line loop)
  where brevity is the convention and intent is obvious.
