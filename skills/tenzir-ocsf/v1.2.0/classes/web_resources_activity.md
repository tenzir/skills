# Web Resources Activity (web_resources_activity)

Web Resources Activity events describe actions executed on a set of Web Resources.

- **Class UID**: `6001`
- **Category**: Application Activity
- **Extends**: [Base Event (base_event)](base_event.md)
- **Profiles**: [Host](../profiles/host.md), [Network Proxy](../profiles/network_proxy.md), [Security Control](../profiles/security_control.md), [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md)

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
- `1`: `Create` - One or more web resources were created.
- `2`: `Read` - One or more web resources were read / viewed.
- `3`: `Update` - One or more web resources were updated.
- `4`: `Delete` - One or more web resources were deleted.
- `5`: `Search` - A search was performed on one or more web resources.
- `6`: `Import` - One or more web resources were imported into an Application.
- `7`: `Export` - One or more web resources were exported from an Application.
- `8`: `Share` - One or more web resources were shared.
- `99`: `Other` - The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

The normalized identifier of the activity that triggered the event.

### `dst_endpoint`

- **Type**: [`network_endpoint`](../objects/network_endpoint.md)
- **Requirement**: recommended
- **Group**: primary

Details about server providing the web resources.

### `http_request`

- **Type**: [`http_request`](../objects/http_request.md)
- **Requirement**: recommended
- **Group**: context

Details about the underlying HTTP request.

### `http_response`

- **Type**: [`http_response`](../objects/http_response.md)
- **Requirement**: optional
- **Group**: context

Details about the HTTP response, if available.

### `src_endpoint`

- **Type**: [`network_endpoint`](../objects/network_endpoint.md)
- **Requirement**: recommended
- **Group**: primary

Details about the endpoint from which the request originated.

### `tls`

- **Type**: [`tls`](../objects/tls.md)
- **Requirement**: optional
- **Group**: context

The Transport Layer Security (TLS) attributes, if available.

### `web_resources`

- **Type**: [`web_resource`](../objects/web_resource.md)
- **Requirement**: required
- **Group**: primary

Describes details about web resources that were affected by an activity/event.

### `web_resources_result`

- **Type**: [`web_resource`](../objects/web_resource.md)
- **Requirement**: recommended
- **Group**: primary

The results of the activity on web resources. It should contain the new values of the changed attributes of the web resources.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `6001`: `Web Resources Activity` - Web Resources Activity events describe actions executed on a set of Web Resources.

The unique identifier of a class. A class describes the attributes available in an event.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `600100`: `Web Resources Activity: Unknown`
- `600101`: `Web Resources Activity: Create` - One or more web resources were created.
- `600102`: `Web Resources Activity: Read` - One or more web resources were read / viewed.
- `600103`: `Web Resources Activity: Update` - One or more web resources were updated.
- `600104`: `Web Resources Activity: Delete` - One or more web resources were deleted.
- `600105`: `Web Resources Activity: Search` - A search was performed on one or more web resources.
- `600106`: `Web Resources Activity: Import` - One or more web resources were imported into an Application.
- `600107`: `Web Resources Activity: Export` - One or more web resources were exported from an Application.
- `600108`: `Web Resources Activity: Share` - One or more web resources were shared.
- `600199`: `Web Resources Activity: Other`

The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
