# Group

Information about an organizational group.

## Fields

### `product_object_id` / `productObjectId`

- Type: `string` (singular)

Product globally unique user object identifier, such as an LDAP Object Identifier.

### `creation_time` / `creationTime`

- Type: `timestamp` (singular)
- Deprecated: `true`

Group creation time. Deprecated: creation_time should be populated in Attribute as generic metadata.

### `group_display_name` / `groupDisplayName`

- Type: `string` (singular)

Group display name. e.g. "Finance".

### `attribute`

- Type: [`Attribute`](attribute.md) (singular)

Generic entity metadata attributes of the group.

### `email_addresses` / `emailAddresses`

- Type: `string` (repeated)

Email addresses of the group.

### `windows_sid` / `windowsSid`

- Type: `string` (singular)

Microsoft Windows SID of the group.

## Guidance

Population guidance from the Google UDM usage guide.

### `Group.creation_time` / `Group.creationTime`

- **Purpose**: Group creation time.
- **Encoding**: RFC 3339 timestamp.

### `Group.email_addresses` / `Group.emailAddresses`

- **Purpose**: Group contact information.
- **Encoding**: Email.

### `Group.group_display_name` / `Group.groupDisplayName`

- **Purpose**: Group display name.
- **Encoding**: String.

#### Examples

- Finance
- HR
- Marketing

### `Group.product_object_id` / `Group.productObjectId`

- **Purpose**: Globally unique user object identifier for the product, such as an LDAP object identifier.
- **Encoding**: String.

### `Group.windows_sid` / `Group.windowsSid`

- **Purpose**: Microsoft Windows Security Identifier (SID) group attribute field.
- **Encoding**: String.
