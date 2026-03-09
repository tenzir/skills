# HTTP Activity (http)

HTTP Activity events report HTTP connection and traffic information.

- **Class UID**: `4002`
- **Category**: Network Activity
- **Extends**: [network_activity (network_activity)](network_activity.md)

## Attributes

### `activity_id`

- **Type**: `integer_t`
- **Sibling**: `activity_name`

#### Enum values

- `99`: `Other` - The event activity is not mapped.
- `0`: `Unknown` - The event activity is unknown.

The normalized identifier of the activity that triggered the event.

### `http_status`

- **Type**: `integer_t`
- **Group**: primary

The Hypertext Transfer Protocol (HTTP) [status code](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml) returned to the client.

### `http_request`

- **Type**: [`http_request`](../objects/http_request.md)
- **Requirement**: required
- **Group**: primary

The HTTP Request Object documents attributes of a request made to a web server.

### `http_response`

- **Type**: [`http_response`](../objects/http_response.md)
- **Requirement**: required
- **Group**: primary

The HTTP Response from a web server to a requester.
