# Web Resource Access Activity (web_resource_access_activity)

Web Resource Access Activity events describe successful/failed attempts to access a web resource over HTTP.

- **Class UID**: `6004`
- **Category**: Application Activity
- **Extends**: [Application Activity (application)](application.md)
- **Profiles**: [Host](../profiles/host.md), [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md)

## Inherited attributes

**From Base Event:**
- `category_uid` (required)
- `metadata` (required)
- `severity_id` (required)
- `time` (required)
- `message` (recommended)
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
- `1`: `Access Grant` - The incoming request has permission to the web resource.
- `2`: `Access Deny` - The incoming request does not have permission to the web resource.
- `3`: `Access Revoke` - The incoming request's access has been revoked due to security policy enforcements.
- `4`: `Access Error` - An error occurred during processing the request.
- `99`: `Other` - The event activity is not mapped.

The normalized identifier of the activity that triggered the event.

### `http_request`

- **Type**: [`http_request`](../objects/http_request.md)
- **Requirement**: required
- **Group**: context

Details about the underlying HTTP request.

### `http_response`

- **Type**: [`http_response`](../objects/http_response.md)
- **Requirement**: optional
- **Group**: context

Details about the HTTP response, if available.

### `proxy`

- **Type**: [`network_proxy`](../objects/network_proxy.md)
- **Requirement**: optional
- **Group**: context

Details about the proxy service, if available.

### `web_resources`

- **Type**: [`web_resource`](../objects/web_resource.md)
- **Requirement**: required
- **Group**: primary

Details about the resource that is the target of the activity.

### `src_endpoint`

- **Type**: [`network_endpoint`](../objects/network_endpoint.md)
- **Requirement**: recommended
- **Group**: primary

Details about the source endpoint of the request.

### `tls`

- **Type**: [`tls`](../objects/tls.md)
- **Requirement**: optional
- **Group**: context

The Transport Layer Security (TLS) attributes, if available.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `6004`: `Web Resource Access Activity` - Web Resource Access Activity events describe successful/failed attempts to access a web resource over HTTP.

The unique identifier of a class. A Class describes the attributes available in an event.

### `type_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `600400`: `Web Resource Access Activity: Unknown`
- `600401`: `Web Resource Access Activity: Access Grant` - The incoming request has permission to the web resource.
- `600402`: `Web Resource Access Activity: Access Deny` - The incoming request does not have permission to the web resource.
- `600403`: `Web Resource Access Activity: Access Revoke` - The incoming request's access has been revoked due to security policy enforcements.
- `600404`: `Web Resource Access Activity: Access Error` - An error occurred during processing the request.
- `600499`: `Web Resource Access Activity: Other`

The event type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
