# User Field Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`
- **License**: Content licensed under Creative Commons Attribution 4.0; code samples licensed under Apache 2.0, as stated in the Google Developers Site Policies.

## Schema

- [User](../messages/user.md)

## Fields

### `User.email_addresses`

- **Purpose**: Stores the email addresses for the user.
- **Encoding**: Repeated String.
- **Example**: johnlocke@company.example.com

#### Examples

- johnlocke@company.example.com

### `User.employee_id`

- **Purpose**: Stores the human resources employee ID for the user.
- **Encoding**: String.
- **Example**: 11223344.

#### Examples

- 11223344.

### `User.first_name`

- **Purpose**: Stores the first name for the user.
- **Encoding**: String.
- **Example**: John.

#### Examples

- John.

### `User.group_identifiers`

- **Purpose**: Stores the group ID(s) (a GUID, LDAP OID, or similar) associated with a user.
- **Encoding**: Repeated String.
- **Example**: admin-users.

#### Examples

- admin-users.

### `User.last_name`

- **Purpose**: Stores the last name for the user.
- **Encoding**: String.
- **Example**: Locke.

#### Examples

- Locke.

### `User.middle_name`

- **Purpose**: Stores the middle name for the user.
- **Encoding**: String.
- **Example**: Anthony.

#### Examples

- Anthony.

### `User.phone_numbers`

- **Purpose**: Stores the phone numbers for the user.
- **Encoding**: Repeated String.
- **Example**: 800-555-0101

#### Examples

- 800-555-0101

### `User.title`

- **Purpose**: Stores the job title for the user.
- **Encoding**: String.
- **Example**: Customer Relationship Manager.

#### Examples

- Customer Relationship Manager.

### `User.user_display_name`

- **Purpose**: Stores the display name for the user.
- **Encoding**: String.
- **Example**: John Locke.

#### Examples

- John Locke.

### `User.userid`

- **Purpose**: Stores the user ID.
- **Encoding**: String.
- **Example**: jlocke.

#### Examples

- jlocke.

### `User.windows_sid`

- **Purpose**: Stores the Microsoft Windows security identifier (SID) associated with a user.
- **Encoding**: String.
- **Example**: S-1-5-21-1180649209-123456789-3582944384-1064

#### Examples

- S-1-5-21-1180649209-123456789-3582944384-1064
