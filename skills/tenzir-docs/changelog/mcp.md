# Tenzir MCP Server

> A Model Context Protocol (MCP) server that connects AI agents to Tenzir, generates data parsers, and creates OCSF mappings.


A Model Context Protocol (MCP) server that connects AI agents to Tenzir, generates data parsers, and creates OCSF mappings.

[ GitHub ](https://github.com/tenzir/mcp/releases)

[Download releases and artifacts](https://github.com/tenzir/mcp/releases)

[ RSS Feed ](/changelog/mcp.xml)

[Subscribe to release updates](/changelog/mcp.xml)

## Releases

* [Unreleased](mcp/unreleased.md)
* [v0.4.5 Dec 19, 2025](mcp/v0-4-5.md)

  [This release updates the embedded OCSF schemas and Tenzir documentation to their latest versions, ensuring AI agents have access to the most current reference material.](mcp/v0-4-5.md)
* [v0.4.4 Dec 12, 2025](mcp/v0-4-4.md)

  [This release fixes broken CI/CD workflows that were preventing successful publishing to PyPI. The workflows have been refactored with reusable composite actions and proper version verification after publishing.](mcp/v0-4-4.md)
* [v0.4.3 Dec 12, 2025](mcp/v0-4-3.md)

  [This patch release updates the server to use FastMCP's built-in logging infrastructure. The custom file-based logging has been removed, eliminating the creation of `tenzir-mcp.log` files in the working directory. Use `FASTMCP_LOG_LEVEL=DEBUG` for verbose output when troubleshooting.](mcp/v0-4-3.md)
* [v0.4.2 Dec 9, 2025](mcp/v0-4-2.md)

  [This release streamlines the prompts for the `make_parser` and `make_ocsf_mapping` tools, reducing model errors and speeding up agent completion.](mcp/v0-4-2.md)
* [v0.4.1 Nov 13, 2025](mcp/v0-4-1.md)
* [v0.4.0 Nov 10, 2025](mcp/v0-4-0.md)