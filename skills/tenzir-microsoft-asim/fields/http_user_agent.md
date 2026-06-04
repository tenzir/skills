# `HttpUserAgent`

- **Schema occurrences**: `4`
- **Raw fragment/source occurrences**: `2`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [AuditEvent](../schemas/audit_event.md) | `Optional` | `string` |  |  | inherited from Acting application entity as Acting |
| [Authentication](../schemas/authentication.md) | `Optional` | `string` |  |  | inherited from Acting application entity as Acting |
| [FileEvent](../schemas/file_event.md) | `Optional` | `string` |  |  | local |
| [User Management](../schemas/user_management.md) | `Optional` | `string` |  |  | inherited from Acting application entity as Acting |

## Raw sources

- `ASIM/schemas/ASimFileEvent.yaml`
- `ASIM/schemas/entities/ASimApp.yaml`

## Details by schema

### AuditEvent

#### `HttpUserAgent`

- **Class**: `Optional`
- **Type**: `string`
- **For roles**: `Actor`, `Src`, `Acting`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimApp.yaml`; include `Acting application entity`; role `Acting`

The user agent header accosiated with the application, when communicating using HTTP or HTTPS.

### Authentication

#### `HttpUserAgent`

- **Class**: `Optional`
- **Type**: `string`
- **For roles**: `Actor`, `Src`, `Acting`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimApp.yaml`; include `Acting application entity`; role `Acting`

The user agent header accosiated with the application, when communicating using HTTP or HTTPS.

### FileEvent

#### `HttpUserAgent`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Local: `ASIM/schemas/ASimFileEvent.yaml`

When the operation is initiated by a remote system using HTTP or HTTPS, the user agent used.

#### Examples

- `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)`

### User Management

#### `HttpUserAgent`

- **Class**: `Optional`
- **Type**: `string`
- **For roles**: `Actor`, `Src`, `Acting`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimApp.yaml`; include `Acting application entity`; role `Acting`

The user agent header accosiated with the application, when communicating using HTTP or HTTPS.
