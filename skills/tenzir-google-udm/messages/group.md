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

### `creation_time` / `creationTime`

- **Purpose**: Group creation time.
- **Encoding**: RFC 3339 timestamp.

### `email_addresses` / `emailAddresses`

- **Purpose**: Group contact information.
- **Encoding**: Email.

### `group_display_name` / `groupDisplayName`

- **Purpose**: Group display name.
- **Encoding**: String.

#### Examples

- Finance
- HR
- Marketing

### `product_object_id` / `productObjectId`

- **Purpose**: Globally unique user object identifier for the product, such as an LDAP object identifier.
- **Encoding**: String.

### `windows_sid` / `windowsSid`

- **Purpose**: Microsoft Windows Security Identifier (SID) group attribute field.
- **Encoding**: String.
