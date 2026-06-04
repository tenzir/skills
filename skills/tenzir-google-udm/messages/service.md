# Service

Information about a Windows service.

## Fields

### `displayName`

- Type: `string` (singular)

The user-friendly display name of the service.

### `serviceType`

- Type: [`ServiceType`](../enums/service_service_type.md) (singular)
- Deprecated: `true`

Deprecated: use serviceTypes instead. The type of service.

### `serviceTypes`

- Type: [`ServiceType`](../enums/service_service_type.md) (repeated)

The list of service types.

### `startupType`

- Type: [`StartupType`](../enums/service_startup_type.md) (singular)

The startup type of the service.

### `state`

- Type: [`Service.State`](../enums/service_state.md) (singular)

The status of the service.
