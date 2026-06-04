# Group Field Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`

## Schema

- [Group](../messages/group.md)

## Fields

### `Group.creation_time`

- **Purpose**: Group creation time.
- **Encoding**: RFC 3339, as appropriate for JSON or Proto3 timestamp format.

### `Group.email_addresses`

- **Purpose**: Group contact information.
- **Encoding**: Email.

### `Group.group_display_name`

- **Purpose**: Group display name.
- **Encoding**: String.
- **Examples**: Finance HR Marketing

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
