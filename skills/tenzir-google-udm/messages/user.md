# User

Information about a user.

- **Full name**: `google.backstory.User`
- **Fields**: `34`
- **Nested enums**: `2`

## Nested enums

- [User.AccountType](../enums/user_account_type.md)
- [User.Role](../enums/user_role.md)

## Fields

### `product_object_id`

- **Number**: `7`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `productObjectId`

A vendor-specific identifier to uniquely identify the entity (e.g. a GUID, LDAP, OID, or similar). This field can be used as an entity indicator for user entities.

### `userid`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `userid`

The ID of the user. This field can be used as an entity indicator for user entities.

### `user_display_name`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `userDisplayName`

The display name of the user (e.g. "John Locke").

### `first_name`

- **Number**: `100`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `firstName`

First name of the user (e.g. "John").

### `middle_name`

- **Number**: `101`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `middleName`

Middle name of the user.

### `last_name`

- **Number**: `102`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `lastName`

Last name of the user (e.g. "Locke").

### `phone_numbers`

- **Number**: `103`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `phoneNumbers`

Phone numbers for the user.

### `personal_address`

- **Number**: `104`
- **Cardinality**: `singular`
- **Type**: [`Location`](location.md)
- **JSON name**: `personalAddress`

Personal address of the user.

### `attribute`

- **Number**: `8`
- **Cardinality**: `singular`
- **Type**: [`Attribute`](attribute.md)
- **JSON name**: `attribute`

Generic entity metadata attributes of the user.

### `first_seen_time`

- **Number**: `10`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp` (imported)
- **JSON name**: `firstSeenTime`

The first observed time for a user. The value is calculated on the basis of the first time the identifier was observed.

### `account_type`

- **Number**: `9`
- **Cardinality**: `singular`
- **Type**: [`User.AccountType`](../enums/user_account_type.md)
- **JSON name**: `accountType`

Type of user account (for example, service, domain, or cloud). This is somewhat aligned to: [https://attack.mitre.org/techniques/T1078/](https://attack.mitre.org/techniques/T1078/)

### `groupid`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `groupid`
- **Deprecated**: `true`

The ID of the group that the user belongs to. Deprecated in favor of the repeated group_identifiers field.

### `group_identifiers`

- **Number**: `200`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `groupIdentifiers`

Product object identifiers of the group(s) the user belongs to A vendor-specific identifier to uniquely identify the group(s) the user belongs to (a GUID, LDAP OID, or similar).

### `windows_sid`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `windowsSid`

The Microsoft Windows SID of the user. This field can be used as an entity indicator for user entities.

### `email_addresses`

- **Number**: `5`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `emailAddresses`

Email addresses of the user. This field can be used as an entity indicator for user entities.

### `employee_id`

- **Number**: `6`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `employeeId`

Human capital management identifier. This field can be used as an entity indicator for user entities.

### `title`

- **Number**: `601`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `title`

User job title.

### `company_name`

- **Number**: `602`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `companyName`

User job company name.

### `department`

- **Number**: `603`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `department`

User job department

### `office_address`

- **Number**: `604`
- **Cardinality**: `singular`
- **Type**: [`Location`](location.md)
- **JSON name**: `officeAddress`

User job office location.

### `managers`

- **Number**: `605`
- **Cardinality**: `repeated`
- **Type**: [`User`](user.md)
- **JSON name**: `managers`

User job manager(s).

### `hire_date`

- **Number**: `606`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp` (imported)
- **JSON name**: `hireDate`

User job employment hire date.

### `termination_date`

- **Number**: `607`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp` (imported)
- **JSON name**: `terminationDate`

User job employment termination date.

### `time_off`

- **Number**: `608`
- **Cardinality**: `repeated`
- **Type**: [`TimeOff`](time_off.md)
- **JSON name**: `timeOff`

User time off leaves from active work.

### `last_login_time`

- **Number**: `609`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp` (imported)
- **JSON name**: `lastLoginTime`

User last login timestamp.

### `last_password_change_time`

- **Number**: `610`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp` (imported)
- **JSON name**: `lastPasswordChangeTime`

User last password change timestamp.

### `password_expiration_time`

- **Number**: `611`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp` (imported)
- **JSON name**: `passwordExpirationTime`

User password expiration timestamp.

### `account_expiration_time`

- **Number**: `612`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp` (imported)
- **JSON name**: `accountExpirationTime`

User account expiration timestamp.

### `account_lockout_time`

- **Number**: `613`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp` (imported)
- **JSON name**: `accountLockoutTime`

User account lockout timestamp.

### `last_bad_password_attempt_time`

- **Number**: `614`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp` (imported)
- **JSON name**: `lastBadPasswordAttemptTime`

User last bad password attempt timestamp.

### `user_authentication_status`

- **Number**: `701`
- **Cardinality**: `singular`
- **Type**: [`Authentication.AuthenticationStatus`](../enums/authentication_authentication_status.md)
- **JSON name**: `userAuthenticationStatus`

System authentication status for user.

### `role_name`

- **Number**: `702`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `roleName`
- **Deprecated**: `true`

System role name for user. Deprecated: use attribute.roles.

### `role_description`

- **Number**: `703`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `roleDescription`
- **Deprecated**: `true`

System role description for user. Deprecated: use attribute.roles.

### `user_role`

- **Number**: `704`
- **Cardinality**: `singular`
- **Type**: [`User.Role`](../enums/user_role.md)
- **JSON name**: `userRole`
- **Deprecated**: `true`

System role for user. Deprecated: use attribute.roles.
