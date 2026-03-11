# Security Lens

Use this lens when the diff touches user input, authentication, networking,
filesystems, secrets, or external command execution.

## Focus Areas

- **Input validation and sanitization.** Trace user-controlled data from entry
  point to where it's consumed. Watch for unescaped interpolation into shell
  commands, SQL, TQL pipelines, URLs, or file paths.
- **Injection risks.** String concatenation to build queries or commands is the
  most common vector. Look for `f"..."`, template strings, or `.format()` that
  embed user input without escaping.
- **Credentials and secrets exposure.** Hardcoded tokens, API keys logged at
  info level, secrets passed via CLI arguments (visible in `ps`), or
  credentials committed in config files.
- **Authentication and authorization checks.** New endpoints or commands that
  skip auth, or changes that widen access without explicit justification.
- **Unsafe defaults.** TLS verification disabled, permissive CORS, world-
  readable file permissions, or debug modes left on.
- **Path traversal.** User-supplied filenames joined to a base path without
  canonicalization (e.g., `../../../etc/passwd`).

## What a Real Finding Looks Like

```markdown
### 🔴 P1 · 🛡️ SEC-1 · Unsanitized input in shell command · 95%

- **File:** src/connectors/shell.cpp:142
- **Issue:** User-provided `--command` argument is interpolated directly into
  a shell invocation without escaping.
- **Reasoning:** An attacker-controlled string can inject arbitrary commands
  via `;`, `&&`, or backtick sequences.
- **Evidence:** `std::format("sh -c '{}'", user_command)` — no quoting or
  allow-listing.
- **Suggestion:** Use `execvp` with an argument vector instead of shell
  interpolation, or at minimum apply POSIX shell escaping.
```

## Common False Positives to Avoid

- Flagging parameterized queries or prepared statements as injection risks.
- Reporting internal-only debug endpoints that are already gated behind a
  feature flag or build configuration.
- Raising concerns about secrets in test fixtures that use well-known dummy
  values (e.g., `password: test`).
