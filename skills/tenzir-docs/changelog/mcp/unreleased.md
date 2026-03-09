# Tenzir MCP Server Unreleased


## 🔧 Changes

### Add smart Tenzir binary detection

Jan 6, 2026 · [@mavam](https://github.com/mavam), [@claude](https://github.com/claude) · [#14](https://github.com/tenzir/mcp/pull/14)

Pipeline execution now auto-detects the Tenzir binary: it first checks the `TENZIR_BINARY` environment variable, then looks for a local `tenzir` installation, and finally falls back to `uvx tenzir` if uv is available. This removes the requirement to have Tenzir pre-installed while still respecting existing installations.