# ASimApp

- **Source**: [`ASIM/schemas/entities/ASimApp.yaml`](https://github.com/Azure/Azure-Sentinel/blob/0db4cc9a326a610d44000d6af1b7035432db74ba/ASIM/schemas/entities/ASimApp.yaml)
- **Fields**: `6`

## Included by

- [AuditEvent](../schemas/audit_event.md) as `Target`
- [AuditEvent](../schemas/audit_event.md) as `Acting`
- [Authentication](../schemas/authentication.md) as `Acting`
- [Authentication](../schemas/authentication.md) as `Target`
- [FileEvent](../schemas/file_event.md) as `Target`
- [Notification](../schemas/notification.md)
- [User Management](../schemas/user_management.md) as `Acting`

## Raw fields

### `<<Role>>AppId`

- **Class**: `Optional`
- **Type**: `string`

The ID of the application, including a process, browser, or service.

### `<<Role>>AppName`

- **Class**: `Optional`
- **Type**: `string`

The name of the application, including a service, a URL, or a SaaS application.

#### Examples

- `Exchange 365`

### `<<Role>>AppType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [AppType](../enumerations.md#apptype)
- **Follows**: [`<<Role>>AppName`](../fields/role_app_name.md)

The type of the application.

### `<<Role>>OriginalAppType`

- **Class**: `Optional`
- **Type**: `string`

The application type as reported by the reporting device.

### `<<Role>>Url`

- **Class**: `Optional`
- **Type**: `string`
- **For roles**: `Target`, `Dst`

A URL associated with the application.

### `HttpUserAgent`

- **Class**: `Optional`
- **Type**: `string`
- **For roles**: `Actor`, `Src`, `Acting`

The user agent header accosiated with the application, when communicating using HTTP or HTTPS.
