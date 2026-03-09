# SSH Activity (ssh_activity)

SSH Activity events report remote client connections to a server using the Secure Shell (SSH) Protocol.

- **UID**: `7`
- **Category**: Network Activity
- **Extends**: `network`

## Attributes

### `activity_id`

- **Type**: `integer_t`
- **Sibling**: `activity_name`

#### Enum values

- `1`: `Open` - A new network connection was opened.
- `2`: `Close` - The network connection was closed.
- `3`: `Reset` - The network connection was abnormally terminated or closed by a middle device like firewalls.
- `4`: `Fail` - The network connection failed. For example a connection timeout or no route to host.
- `5`: `Refuse` - The network connection was refused. For example an attempt to connect to a server port which is not open.
- `6`: `Traffic` - Network traffic report.
- `7`: `Listen` - A network endpoint began listening for new network connections.

The normalized identifier of the activity that triggered the event.

### `auth_type`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: primary

The SSH authentication type, normalized to the caption of 'auth_type_id'. In the case of 'Other', it is defined by the event source.

### `auth_type_id`

- **Type**: `integer_t`
- **Requirement**: recommended
- **Group**: primary
- **Sibling**: `auth_type`

#### Enum values

- `0`: `Unknown`
- `1`: `Certificate Based` - Authentication using digital certificates.
- `2`: `GSSAPI` - GSSAPI for centralized authentication.
- `3`: `Host Based` - Authentication based on the client host's identity.
- `4`: `Keyboard Interactive` - Multi-step, interactive authentication.
- `5`: `Password` - Password Authentication.
- `6`: `Public Key` - Paired public key authentication.
- `99`: `Other`

The normalized identifier of the SSH authentication type.

### `client_hassh`

- **Type**: `hassh`
- **Requirement**: recommended
- **Group**: primary

The Client HASSH fingerprinting object.

### `file`

- **Type**: `file`
- **Requirement**: optional
- **Group**: context

The file that is the target of the SSH activity.

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
