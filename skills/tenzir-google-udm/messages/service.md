# Service

Information about a Windows service.

## Fields

### `display_name` / `displayName`

- Type: `string` (singular)

The user-friendly display name of the service.

### `service_type` / `serviceType`

- Type: [`ServiceType`](../enums/service_service_type.md) (singular)
- Deprecated: `true`

Deprecated: use service_types instead. The type of service.

### `service_types` / `serviceTypes`

- Type: [`ServiceType`](../enums/service_service_type.md) (repeated)

The list of service types.

### `startup_type` / `startupType`

- Type: [`StartupType`](../enums/service_startup_type.md) (singular)

The startup type of the service.

### `state`

- Type: [`Service.State`](../enums/service_state.md) (singular)

The status of the service.
