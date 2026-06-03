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

### `display_name`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `displayName`

The user-friendly display name of the service.

### `service_type`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: [`Service.ServiceType`](../enums/service_service_type.md)
- **JSON name**: `serviceType`
- **Deprecated**: `true`

Deprecated: use service_types instead. The type of service.

### `service_types`

- **Number**: `6`
- **Cardinality**: `repeated`
- **Type**: [`Service.ServiceType`](../enums/service_service_type.md)
- **JSON name**: `serviceTypes`

The list of service types.

### `startup_type`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: [`Service.StartupType`](../enums/service_startup_type.md)
- **JSON name**: `startupType`

The startup type of the service.

### `state`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: [`Service.State`](../enums/service_state.md)
- **JSON name**: `state`

The status of the service.
