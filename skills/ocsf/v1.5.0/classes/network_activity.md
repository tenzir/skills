# Network Activity (network_activity)

Network Activity events report network connection and traffic activity.

- **UID**: `1`
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

### `url`

- **Type**: `url`
- **Requirement**: recommended
- **Group**: primary

The URL details relevant to the network traffic.
