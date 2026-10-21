# API Activity (api_activity)

API events describe general CRUD (Create, Read, Update, Delete) API activities, e.g. (AWS Cloudtrail)

- **Class UID**: `6003`
- **Category**: Application Activity
- **Extends**: [Application Activity (application)](application.md)
- **Profiles**: [Trace](../profiles/trace.md), [AI Operation](../profiles/ai_operation.md), [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md), [Host](../profiles/host.md), [OSINT](../profiles/osint.md), [Record Integrity](../profiles/record_integrity.md), [Security Control](../profiles/security_control.md)

## Inherited attributes

**From Base Event:**
- `category_uid` (required)
- `metadata` (required)
- `severity_id` (required)
- `time` (required)
- `message` (recommended)
- `observables` (recommended)
- `status` (recommended)
- `status_code` (recommended)
- `status_detail` (recommended)
- `status_id` (recommended)
- `timezone_offset` (recommended)

## Attributes

### `activity_id`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `activity_name`

#### Enum values

- `0`: `Unknown` - The event activity is unknown.
- `1`: `Create` - The API call in the event pertains to a 'create' activity.
- `2`: `Read` - The API call in the event pertains to a 'read' activity.
- `3`: `Update` - The API call in the event pertains to a 'update' activity.
- `4`: `Delete` - The API call in the event pertains to a 'delete' activity.
- `99`: `Other` - The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

The normalized identifier of the activity that triggered the event. Each event class defines its own set of activity values. Use `0` (Unknown) when the activity cannot be determined. Use `99` (Other) when the activity does not match any defined value, in which case `activity_name` must be populated with the source-specific label.

### `actor`

- **Type**: [`actor`](../objects/actor.md)
- **Requirement**: required
- **Group**: primary

The user, process, or service that initiated the activity on the host. For system-level events this is typically a process; for IAM events it is typically a user or role.

### `api`

- **Type**: [`api`](../objects/api.md)
- **Requirement**: required
- **Group**: primary

Describes details about a typical API (Application Programming Interface) call.

### `dst_endpoint`

- **Type**: [`network_endpoint`](../objects/network_endpoint.md)
- **Requirement**: recommended
- **Group**: primary

The network destination endpoint.

### `http_request`

- **Type**: [`http_request`](../objects/http_request.md)
- **Requirement**: recommended
- **Group**: primary

Details about the underlying http request.

### `http_response`

- **Type**: [`http_response`](../objects/http_response.md)
- **Requirement**: recommended
- **Group**: primary

Details about the underlying http response.

### `resources`

- **Type**: [`resource_details`](../objects/resource_details.md)
- **Requirement**: recommended
- **Group**: primary

Details about resources that were affected by the activity/event.

### `src_endpoint`

- **Type**: [`network_endpoint`](../objects/network_endpoint.md)
- **Requirement**: required
- **Group**: primary

Details about the source of the activity.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `6003`: `API Activity` - API events describe general CRUD (Create, Read, Update, Delete) API activities, e.g. (AWS Cloudtrail)

The unique identifier of a class. A class describes the attributes available in an event. Producers and mappers must set this to the `uid` defined in the event class definition. For example, `Detection Finding` is `2004`.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `600300`: `API Activity: Unknown`
- `600301`: `API Activity: Create` - The API call in the event pertains to a 'create' activity.
- `600302`: `API Activity: Read` - The API call in the event pertains to a 'read' activity.
- `600303`: `API Activity: Update` - The API call in the event pertains to a 'update' activity.
- `600304`: `API Activity: Delete` - The API call in the event pertains to a 'delete' activity.
- `600399`: `API Activity: Other`

The event/finding type ID. It identifies the event's semantics and structure. Producers and mappers must compute this as `class_uid * 100 + activity_id`. It uniquely identifies the combination of event class and activity across the entire schema. For example, `Detection Finding: Create` is `200401`.
