# User

Information about a user.

- **Full name**: `google.backstory.User`
- **Fields**: `34`
- **Nested enums**: `2`

## Nested enums

- [User.AccountType](../enums/user_account_type.md)
- [User.Role](../enums/user_role.md)

## Fields

### `productObjectId`

- Type: `string` (singular)

A vendor-specific identifier to uniquely identify the entity (e.g. a GUID, LDAP, OID, or similar). This field can be used as an entity indicator for user entities.

### `userid`

- Type: `string` (singular)

The ID of the user. This field can be used as an entity indicator for user entities.

### `userDisplayName`

- Type: `string` (singular)

The display name of the user (e.g. "John Locke").

### `firstName`

- Type: `string` (singular)

First name of the user (e.g. "John").

### `middleName`

- Type: `string` (singular)

Middle name of the user.

### `lastName`

- Type: `string` (singular)

Last name of the user (e.g. "Locke").

### `phoneNumbers`

- Type: `string` (repeated)

Phone numbers for the user.

### `personalAddress`

- Type: [`Location`](location.md) (singular)

Personal address of the user.

### `attribute`

- Type: [`Attribute`](attribute.md) (singular)

Generic entity metadata attributes of the user.

### `firstSeenTime`

- Type: `google.protobuf.Timestamp` (singular)

The first observed time for a user. The value is calculated on the basis of the first time the identifier was observed.

### `accountType`

- Type: [`User.AccountType`](../enums/user_account_type.md) (singular)

Type of user account (for example, service, domain, or cloud). This is somewhat aligned to: [https://attack.mitre.org/techniques/T1078/](https://attack.mitre.org/techniques/T1078/)

### `groupid`

- Type: `string` (singular)
- Deprecated: `true`

The ID of the group that the user belongs to. Deprecated in favor of the repeated groupIdentifiers field.

### `groupIdentifiers`

- Type: `string` (repeated)

Product object identifiers of the group(s) the user belongs to A vendor-specific identifier to uniquely identify the group(s) the user belongs to (a GUID, LDAP OID, or similar).

### `windowsSid`

- Type: `string` (singular)

The Microsoft Windows SID of the user. This field can be used as an entity indicator for user entities.

### `emailAddresses`

- Type: `string` (repeated)

Email addresses of the user. This field can be used as an entity indicator for user entities.

### `employeeId`

- Type: `string` (singular)

Human capital management identifier. This field can be used as an entity indicator for user entities.

### `title`

- Type: `string` (singular)

User job title.

### `companyName`

- Type: `string` (singular)

User job company name.

### `department`

- Type: `string` (repeated)

User job department

### `officeAddress`

- Type: [`Location`](location.md) (singular)

User job office location.

### `managers`

- Type: [`User`](user.md) (repeated)

User job manager(s).

### `hireDate`

- Type: `google.protobuf.Timestamp` (singular)

User job employment hire date.

### `terminationDate`

- Type: `google.protobuf.Timestamp` (singular)

User job employment termination date.

### `timeOff`

- Type: [`TimeOff`](time_off.md) (repeated)

User time off leaves from active work.

### `lastLoginTime`

- Type: `google.protobuf.Timestamp` (singular)

User last login timestamp.

### `lastPasswordChangeTime`

- Type: `google.protobuf.Timestamp` (singular)

User last password change timestamp.

### `passwordExpirationTime`

- Type: `google.protobuf.Timestamp` (singular)

User password expiration timestamp.

### `accountExpirationTime`

- Type: `google.protobuf.Timestamp` (singular)

User account expiration timestamp.

### `accountLockoutTime`

- Type: `google.protobuf.Timestamp` (singular)

User account lockout timestamp.

### `lastBadPasswordAttemptTime`

- Type: `google.protobuf.Timestamp` (singular)

User last bad password attempt timestamp.

### `userAuthenticationStatus`

- Type: [`Authentication.AuthenticationStatus`](../enums/authentication_authentication_status.md) (singular)

System authentication status for user.

### `roleName`

- Type: `string` (singular)
- Deprecated: `true`

System role name for user. Deprecated: use attribute.roles.

### `roleDescription`

- Type: `string` (singular)
- Deprecated: `true`

System role description for user. Deprecated: use attribute.roles.

### `userRole`

- Type: [`User.Role`](../enums/user_role.md) (singular)
- Deprecated: `true`

System role for user. Deprecated: use attribute.roles.

## Guidance

Population guidance from the Google UDM usage guide.

### `User.emailAddresses`

- **Purpose**: Stores the email addresses for the user.
- **Encoding**: Repeated String.
- **Example**: johnlocke@company.example.com

#### Examples

- johnlocke@company.example.com

### `User.employeeId`

- **Purpose**: Stores the human resources employee ID for the user.
- **Encoding**: String.
- **Example**: 11223344.

#### Examples

- 11223344.

### `User.firstName`

- **Purpose**: Stores the first name for the user.
- **Encoding**: String.
- **Example**: John.

#### Examples

- John.

### `User.groupIdentifiers`

- **Purpose**: Stores the group ID(s) (a GUID, LDAP OID, or similar) associated with a user.
- **Encoding**: Repeated String.
- **Example**: admin-users.

#### Examples

- admin-users.

### `User.lastName`

- **Purpose**: Stores the last name for the user.
- **Encoding**: String.
- **Example**: Locke.

#### Examples

- Locke.

### `User.middleName`

- **Purpose**: Stores the middle name for the user.
- **Encoding**: String.
- **Example**: Anthony.

#### Examples

- Anthony.

### `User.phoneNumbers`

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

### `User.userDisplayName`

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

### `User.windowsSid`

- **Purpose**: Stores the Microsoft Windows security identifier (SID) associated with a user.
- **Encoding**: String.
- **Example**: S-1-5-21-1180649209-123456789-3582944384-1064

#### Examples

- S-1-5-21-1180649209-123456789-3582944384-1064
