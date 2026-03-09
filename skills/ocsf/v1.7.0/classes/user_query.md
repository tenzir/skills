# User Query (user_query)

User Query events report user data that have been discovered, queried, polled or searched. This event differs from User Inventory as it describes the result of a targeted search by filtering a subset of user attributes.

- **UID**: `18`
- **Category**: Discovery
- **Extends**: `discovery_result`

## Attributes

### `user`

- **Type**: `user`
- **Requirement**: required
- **Group**: primary

The user that pertains to the event or object.
