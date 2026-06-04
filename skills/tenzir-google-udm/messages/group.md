# Group

Information about an organizational group.

## Fields

### `productObjectId`

- Type: `string` (singular)

Product globally unique user object identifier, such as an LDAP Object Identifier.

### `creationTime`

- Type: `timestamp` (singular)
- Deprecated: `true`

Group creation time. Deprecated: creationTime should be populated in Attribute as generic metadata.

### `groupDisplayName`

- Type: `string` (singular)

Group display name. e.g. "Finance".

### `attribute`

- Type: [`Attribute`](attribute.md) (singular)

Generic entity metadata attributes of the group.

### `emailAddresses`

- Type: `string` (repeated)

Email addresses of the group.

### `windowsSid`

- Type: `string` (singular)

Microsoft Windows SID of the group.

## Guidance

Population guidance from the Google UDM usage guide.

### `Group.creationTime`

- **Purpose**: Group creation time.
- **Encoding**: RFC 3339 timestamp.

### `Group.emailAddresses`

- **Purpose**: Group contact information.
- **Encoding**: Email.

### `Group.groupDisplayName`

- **Purpose**: Group display name.
- **Encoding**: String.

#### Examples

- Finance
- HR
- Marketing

### `Group.productObjectId`

- **Purpose**: Globally unique user object identifier for the product, such as an LDAP object identifier.
- **Encoding**: String.

### `Group.windowsSid`

- **Purpose**: Microsoft Windows Security Identifier (SID) group attribute field.
- **Encoding**: String.
