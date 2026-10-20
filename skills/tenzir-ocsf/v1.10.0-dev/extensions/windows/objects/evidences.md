# Windows Evidence Artifacts (evidences)

Extends the evidences object to add Windows specific fields

- **Extends**: [Evidence Artifacts (evidences)](../../../objects/evidences.md)

## Constraints

- **At least one of**: `actor`, `api`, `connection_info`, `data`, `database`, `databucket`, `device`, `dst_endpoint`, `email`, `file`, `process`, `query`, `src_endpoint`, `url`, `user`, `job`, `script`, `reg_key`, `reg_value`, `win_service`

## Inherited attributes

**From Evidence Artifacts:**
- `actor` (recommended)
- `ai_agent` (recommended)
- `api` (recommended)
- `connection_info` (recommended)
- `container` (recommended)
- `data` (recommended)
- `database` (recommended)
- `databucket` (recommended)
- `device` (recommended)
- `dst_endpoint` (recommended)
- `email` (recommended)
- `file` (recommended)
- `http_request` (recommended)
- `http_response` (recommended)
- `ja4_fingerprint_list` (recommended)
- `job` (recommended)
- `process` (recommended)
- `query` (recommended)
- `resources` (recommended)
- `script` (recommended)
- `src_endpoint` (recommended)
- `tls` (recommended)
- `url` (recommended)
- `user` (recommended)

## Attributes

### `reg_key`

- **Type**: `reg_key`
- **Requirement**: recommended

Describes details about the registry key that triggered the detection.

### `reg_value`

- **Type**: `reg_value`
- **Requirement**: recommended

Describes details about the registry value that triggered the detection.

### `win_service`

- **Type**: [`win_service`](../objects/win_service.md)
- **Requirement**: recommended

Describes details about the Windows service that triggered the detection.
