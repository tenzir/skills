# SSH Activity (ssh)

SSH Activity events report remote client connections to a server using the Secure Shell (SSH) Protocol.

- **UID**: `7`
- **Category**: Network Activity
- **Extends**: `network_activity`

## Attributes

### `client_hassh`

- **Type**: `hassh`
- **Requirement**: recommended
- **Group**: primary

The Client HASSH fingerprinting object.

### `protocol_ver`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: context

The Secure Shell Protocol version.

### `server_hassh`

- **Type**: `hassh`
- **Requirement**: recommended
- **Group**: primary

The Server HASSH fingerprinting object.
