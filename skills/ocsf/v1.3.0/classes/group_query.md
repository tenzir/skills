# Admin Group Query (group_query)

Admin Group Query events report information about administrative groups.

- **UID**: `9`
- **Category**: Discovery
- **Extends**: `discovery_result`

## Attributes

### `group`

- **Type**: `group`
- **Requirement**: required
- **Group**: primary

The administrative group.

### `users`

- **Type**: `user`
- **Requirement**: recommended
- **Group**: primary

The users that belong to the administrative group.
