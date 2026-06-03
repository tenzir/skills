# Group

Information about an organizational group.

- **Full name**: `google.backstory.Group`
- **Fields**: `6`

## Fields

### `product_object_id`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `productObjectId`

Product globally unique user object identifier, such as an LDAP Object Identifier.

### `creation_time`

- **Number**: `100`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp` (imported)
- **JSON name**: `creationTime`
- **Deprecated**: `true`

Group creation time. Deprecated: creation_time should be populated in Attribute as generic metadata.

### `group_display_name`

- **Number**: `101`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `groupDisplayName`

Group display name. e.g. "Finance".

### `attribute`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: [`Attribute`](attribute.md)
- **JSON name**: `attribute`

Generic entity metadata attributes of the group.

### `email_addresses`

- **Number**: `2`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `emailAddresses`

Email addresses of the group.

### `windows_sid`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `windowsSid`

Microsoft Windows SID of the group.
