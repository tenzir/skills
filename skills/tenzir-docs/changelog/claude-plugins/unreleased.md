# Claude Marketplace Unreleased


## 💥 Breaking Changes

### C++ plugin removed from marketplace

Feb 12, 2026 · [@mavam](https://github.com/mavam), [@claude](https://github.com/claude)

The C++ plugin has been removed from the marketplace. Its contents have been migrated into a skill in the [tenzir/tenzir](https://github.com/tenzir/tenzir) repository, where the C++ coding conventions and language server integration live closer to the codebase they apply to.

## 🚀 Features

### Workaround for plugin skills and agents hooks not firing

Jan 28, 2026 · [@mavam](https://github.com/mavam), [@claude](https://github.com/claude)

Added a workaround for [Claude Code issue #17688](https://github.com/anthropics/claude-code/issues/17688) where frontmatter hooks in plugin skills and agents don’t fire.

The `link-plugin-components.sh` script copies plugin components that have hooks defined in their frontmatter to the project’s `.claude/` directory on session start. It uses `$CLAUDE_PLUGIN_ROOT` (set by Claude Code) to find the plugin, updates the `name:` field to include the plugin prefix, and resolves `$CLAUDE_PLUGIN_ROOT` paths to absolute paths in hook commands. The script skips files that already exist, so subsequent sessions are fast.

This workaround is triggered via a SessionStart hook. Currently affects the `dev:reviewing-changes` skill and `dev:docs-updater` agent.

This is a temporary workaround that should be removed once the upstream Claude Code bug is fixed.

## 🔧 Changes

### Improved guide subagent documentation and fallback behavior

Feb 1, 2026 · [@mavam](https://github.com/mavam), [@claude](https://github.com/claude)

The `tenzir:guide` subagent now provides clearer response guidelines and fallback behavior. The documentation has been reorganized to emphasize core principles for fact-checking and citation, while also documenting the fallback to online documentation when the local skill is unavailable. This ensures consistent, reliable guidance regardless of documentation availability.