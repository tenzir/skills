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
- **Type**: `google.protobuf.Timestamp`
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

## Guidance

Population guidance from the Google UDM usage guide.

### `Group.creation_time`

- **Purpose**: Group creation time.
- **Encoding**: RFC 3339, as appropriate for JSON or Proto3 timestamp format.

### `Group.email_addresses`

- **Purpose**: Group contact information.
- **Encoding**: Email.

### `Group.group_display_name`

- **Purpose**: Group display name.
- **Encoding**: String.

#### Examples

- Finance
- HR
- Marketing

### `Group.product_object_id`

- **Purpose**: Globally unique user object identifier for the product, such as an LDAP object identifier.
- **Encoding**: String.

### `Group.windows_sid`

- **Purpose**: Microsoft Windows Security Identifier (SID) group attribute field.
- **Encoding**: String.
