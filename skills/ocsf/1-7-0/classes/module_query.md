# Module Query (module_query)

Module Query events report information about loaded modules.

- **UID**: `11`
- **Category**: Discovery
- **Extends**: `discovery_result`

## Attributes

### `module`

- **Type**: `module`
- **Requirement**: required
- **Group**: primary

The module that pertains to the event.

### `process`

- **Type**: `process`
- **Requirement**: required
- **Group**: primary

The process that loaded the module.
