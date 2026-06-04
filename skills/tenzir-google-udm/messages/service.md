# Service

Information about a Windows service.

- **Full name**: `google.backstory.Service`
- **Fields**: `5`
- **Nested enums**: `3`

## Nested enums

- [Service.ServiceType](../enums/service_service_type.md)
- [Service.StartupType](../enums/service_startup_type.md)
- [Service.State](../enums/service_state.md)

## Fields

### `displayName`

- Type: `string` (singular)

The user-friendly display name of the service.

### `serviceType`

- Type: [`Service.ServiceType`](../enums/service_service_type.md) (singular)
- Deprecated: `true`

Deprecated: use serviceTypes instead. The type of service.

### `serviceTypes`

- Type: [`Service.ServiceType`](../enums/service_service_type.md) (repeated)

The list of service types.

### `startupType`

- Type: [`Service.StartupType`](../enums/service_startup_type.md) (singular)

The startup type of the service.

### `state`

- Type: [`Service.State`](../enums/service_state.md) (singular)

The status of the service.
