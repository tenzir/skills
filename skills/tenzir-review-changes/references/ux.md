# User Experience Lens

Use this lens when the diff changes user-facing behavior, CLI output, error
messages, setup flows, or defaults.

## Focus Areas

- **Clarity of messages and prompts.** Error messages should tell the user what
  went wrong, why, and what to do next. "Connection failed" is useless;
  "Connection to 10.0.0.1:5158 refused — is the Tenzir node running?" is
  actionable.
- **Discoverability.** Can users find the new or changed behavior through
  normal exploration? New options should appear in `--help`, new operators in
  documentation, new config keys in example configs.
- **Consistency with existing behavior.** Terminology, flag naming, output
  formatting, and exit codes should match what the rest of the product does.
  Introducing `--no-verify` when existing flags use `--skip-X` is a
  consistency break.
- **Feedback during long-running or risky operations.** Progress indicators,
  confirmation prompts for destructive actions, and clear indication of what's
  happening during multi-second operations.
- **Sensible defaults.** The common path should work without configuration.
  Defaults should be safe (don't delete data, don't expose services) and
  performant for typical workloads.

## What a Real Finding Looks Like

```markdown
### 🟠 P2 · 🎨 UXD-1 · Silent data truncation on export · 90%

- **File:** src/export.cpp:182
- **Issue:** When the export exceeds the row limit, the command silently
  truncates output without any warning or exit code.
- **Reasoning:** Users relying on the exported data for downstream processing
  will silently get incomplete results. This is worse than a hard failure
  because it's invisible.
- **Evidence:** `if (rows > limit) break;` — no warning, no stderr message,
  exit code remains 0.
- **Suggestion:** Emit a warning to stderr: `"Warning: output truncated to
{limit} rows. Use --limit to increase."` and consider a non-zero exit code.
```

## Common False Positives to Avoid

- Suggesting UX improvements to internal-only developer tools or debug
  commands that aren't user-facing.
- Flagging output format differences in machine-readable output modes (JSON,
  CSV) where the format is defined by spec, not human readability.
- Demanding confirmation prompts for non-destructive, easily reversible
  operations.
