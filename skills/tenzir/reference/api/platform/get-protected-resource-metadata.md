---
title: "Get protected resource metadata"
description: "OAuth 2.0 Protected Resource Metadata (RFC 9728) for the MCP endpoint: which authorization server issues its tokens, and what resource identifier they must be bound to."
canonical: https://tenzir.com/docs/reference/api/platform/get-protected-resource-metadata
source: https://tenzir.com/docs/reference/api/platform/get-protected-resource-metadata.md
section: "Docs"
---

# Get protected resource metadata

> OAuth 2.0 Protected Resource Metadata (RFC 9728) for the MCP endpoint: which authorization server issues its tokens, and what resource identifier they must be bound to.

`GET /.well-known/oauth-protected-resource/mcp`

OAuth 2.0 Protected Resource Metadata (RFC 9728) for the MCP endpoint: which authorization server issues its tokens, and what resource identifier they must be bound to.

## Responses

### `200`: OAuth.ProtectedResourceMetadata

Media type: `application/json`

* `resource` (`string`, required)
* `authorization_servers` (`array<string>`, required)
* `bearer_methods_supported` (`array<string>`, required)
* `resource_name` (`string`, required)

### `400`: Validation

Media type: `application/json`

* `_tag` (`"Validation"`, required)
* `message` (`string`, required)

### `500`: InternalServerError

Media type: `application/json`

* `_tag` (`"InternalServerError"`, required)
