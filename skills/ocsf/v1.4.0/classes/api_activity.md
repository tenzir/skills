# API Activity (api_activity)

API events describe general CRUD (Create, Read, Update, Delete) API activities, e.g. (AWS Cloudtrail)

- **UID**: `3`
- **Category**: Application Activity
- **Extends**: `application`

## Attributes

### `$include`

### `activity_id`

- **Type**: `integer_t`
- **Sibling**: `activity_name`

#### Enum values

- `1`: `Create` - The API call in the event pertains to a 'create' activity.
- `2`: `Read` - The API call in the event pertains to a 'read' activity.
- `3`: `Update` - The API call in the event pertains to a 'update' activity.
- `4`: `Delete` - The API call in the event pertains to a 'delete' activity.

The normalized identifier of the activity that triggered the event.

### `actor`

- **Type**: `actor`
- **Requirement**: required
- **Group**: primary

The actor object describes details about the user/role/process that was the source of the activity. Note that this is not the threat actor of a campaign but may be part of a campaign.

### `api`

- **Type**: `api`
- **Requirement**: required
- **Group**: primary

Describes details about a typical API (Application Programming Interface) call.

### `dst_endpoint`

- **Type**: `network_endpoint`
- **Requirement**: recommended
- **Group**: primary

The network destination endpoint.

### `http_request`

- **Type**: `http_request`
- **Requirement**: recommended
- **Group**: primary

Details about the underlying http request.

### `http_response`

- **Type**: `http_response`
- **Requirement**: recommended
- **Group**: primary

Details about the underlying http response.

### `resources`

- **Type**: `resource_details`
- **Requirement**: recommended
- **Group**: primary

Details about resources that were affected by the activity/event.

### `src_endpoint`

- **Type**: `network_endpoint`
- **Requirement**: required
- **Group**: primary

Details about the source of the activity.
