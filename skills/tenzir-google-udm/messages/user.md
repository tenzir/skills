# User

Information about a user.

## Fields

### `product_object_id` / `productObjectId`

- Type: `string` (singular)

A vendor-specific identifier to uniquely identify the entity (e.g. a GUID, LDAP, OID, or similar). This field can be used as an entity indicator for user entities.

### `userid`

- Type: `string` (singular)

The ID of the user. This field can be used as an entity indicator for user entities.

### `user_display_name` / `userDisplayName`

- Type: `string` (singular)

The display name of the user (e.g. "John Locke").

### `first_name` / `firstName`

- Type: `string` (singular)

First name of the user (e.g. "John").

### `middle_name` / `middleName`

- Type: `string` (singular)

Middle name of the user.

### `last_name` / `lastName`

- Type: `string` (singular)

Last name of the user (e.g. "Locke").

### `phone_numbers` / `phoneNumbers`

- Type: `string` (repeated)

Phone numbers for the user.

### `personal_address` / `personalAddress`

- Type: [`Location`](location.md) (singular)

Personal address of the user.

### `attribute`

- Type: [`Attribute`](attribute.md) (singular)

Generic entity metadata attributes of the user.

### `first_seen_time` / `firstSeenTime`

- Type: `timestamp` (singular)

The first observed time for a user. The value is calculated on the basis of the first time the identifier was observed.

### `account_type` / `accountType`

- Type: [`AccountType`](../enums/user_account_type.md) (singular)

Type of user account (for example, service, domain, or cloud). This is somewhat aligned to: [https://attack.mitre.org/techniques/T1078/](https://attack.mitre.org/techniques/T1078/)

### `groupid`

- Type: `string` (singular)
- Deprecated: `true`

The ID of the group that the user belongs to. Deprecated in favor of the repeated group_identifiers field.

### `group_identifiers` / `groupIdentifiers`

- Type: `string` (repeated)

Product object identifiers of the group(s) the user belongs to A vendor-specific identifier to uniquely identify the group(s) the user belongs to (a GUID, LDAP OID, or similar).

### `windows_sid` / `windowsSid`

- Type: `string` (singular)

The Microsoft Windows SID of the user. This field can be used as an entity indicator for user entities.

### `email_addresses` / `emailAddresses`

- Type: `string` (repeated)

Email addresses of the user. This field can be used as an entity indicator for user entities.

### `employee_id` / `employeeId`

- Type: `string` (singular)

Human capital management identifier. This field can be used as an entity indicator for user entities.

### `title`

- Type: `string` (singular)

User job title.

### `company_name` / `companyName`

- Type: `string` (singular)

User job company name.

### `department`

- Type: `string` (repeated)

User job department

### `office_address` / `officeAddress`

- Type: [`Location`](location.md) (singular)

User job office location.

### `managers`

- Type: [`User`](user.md) (repeated)

User job manager(s).

### `hire_date` / `hireDate`

- Type: `timestamp` (singular)

User job employment hire date.

### `termination_date` / `terminationDate`

- Type: `timestamp` (singular)

User job employment termination date.

### `time_off` / `timeOff`

- Type: [`TimeOff`](time_off.md) (repeated)

User time off leaves from active work.

### `last_login_time` / `lastLoginTime`

- Type: `timestamp` (singular)

User last login timestamp.

### `last_password_change_time` / `lastPasswordChangeTime`

- Type: `timestamp` (singular)

User last password change timestamp.

### `password_expiration_time` / `passwordExpirationTime`

- Type: `timestamp` (singular)

User password expiration timestamp.

### `account_expiration_time` / `accountExpirationTime`

- Type: `timestamp` (singular)

User account expiration timestamp.

### `account_lockout_time` / `accountLockoutTime`

- Type: `timestamp` (singular)

User account lockout timestamp.

### `last_bad_password_attempt_time` / `lastBadPasswordAttemptTime`

- Type: `timestamp` (singular)

User last bad password attempt timestamp.

### `user_authentication_status` / `userAuthenticationStatus`

- Type: [`AuthenticationStatus`](../enums/authentication_authentication_status.md) (singular)

System authentication status for user.

### `role_name` / `roleName`

- Type: `string` (singular)
- Deprecated: `true`

System role name for user. Deprecated: use attribute.roles.

### `role_description` / `roleDescription`

- Type: `string` (singular)
- Deprecated: `true`

System role description for user. Deprecated: use attribute.roles.

### `user_role` / `userRole`

- Type: [`User.Role`](../enums/user_role.md) (singular)
- Deprecated: `true`

System role for user. Deprecated: use attribute.roles.

## Guidance

Population guidance from the Google UDM usage guide.

### `email_addresses` / `emailAddresses`

- **Purpose**: Stores the email addresses for the user.
- **Encoding**: Repeated String.
- **Example**: johnlocke@company.example.com

#### Examples

- johnlocke@company.example.com

### `employee_id` / `employeeId`

- **Purpose**: Stores the human resources employee ID for the user.
- **Encoding**: String.
- **Example**: 11223344.

#### Examples

- 11223344.

### `first_name` / `firstName`

- **Purpose**: Stores the first name for the user.
- **Encoding**: String.
- **Example**: John.

#### Examples

- John.

### `group_identifiers` / `groupIdentifiers`

- **Purpose**: Stores the group ID(s) (a GUID, LDAP OID, or similar) associated with a user.
- **Encoding**: Repeated String.
- **Example**: admin-users.

#### Examples

- admin-users.

### `last_name` / `lastName`

- **Purpose**: Stores the last name for the user.
- **Encoding**: String.
- **Example**: Locke.

#### Examples

- Locke.

### `middle_name` / `middleName`

- **Purpose**: Stores the middle name for the user.
- **Encoding**: String.
- **Example**: Anthony.

#### Examples

- Anthony.

### `phone_numbers` / `phoneNumbers`

- **Purpose**: Stores the phone numbers for the user.
- **Encoding**: Repeated String.
- **Example**: 800-555-0101

#### Examples

- 800-555-0101

### `title`

- **Purpose**: Stores the job title for the user.
- **Encoding**: String.
- **Example**: Customer Relationship Manager.

#### Examples

- Customer Relationship Manager.

### `user_display_name` / `userDisplayName`

- **Purpose**: Stores the display name for the user.
- **Encoding**: String.
- **Example**: John Locke.

#### Examples

- John Locke.

### `userid`

- **Purpose**: Stores the user ID.
- **Encoding**: String.
- **Example**: jlocke.

#### Examples

- jlocke.

### `windows_sid` / `windowsSid`

- **Purpose**: Stores the Microsoft Windows security identifier (SID) associated with a user.
- **Encoding**: String.
- **Example**: S-1-5-21-1180649209-123456789-3582944384-1064

#### Examples

- S-1-5-21-1180649209-123456789-3582944384-1064
