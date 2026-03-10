# Group

> The Group object represents a collection or association of entities, such as users, policies, or devices.


The Group object represents a collection or association of entities, such as users, policies, or devices. It serves as a logical grouping mechanism to organize and manage entities with similar characteristics or permissions within a system or organization.

* **Extends**: `_entity`

## Attributes

**`name`**

* **Type**: `string_t`
* **Requirement**: recommended

The group name.

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The unique identifier of the group. For example, for Windows events this is the security identifier (SID) of the group.

**`desc`**

* **Type**: `string_t`
* **Requirement**: optional

The group description.

**`domain`**

* **Type**: `string_t`
* **Requirement**: optional

The domain where the group is defined. For example: the LDAP or Active Directory domain.

**`privileges`**

* **Type**: `string_t`
* **Requirement**: optional

The group privileges.

**`type`**

* **Type**: `string_t`
* **Requirement**: optional

The type of the group or account.

## Constraints

At least one of: `name`, `uid`

## Used By

* [`authorize_session`](../classes/authorize_session.md)
* [`group_management`](../classes/group_management.md)
* [`incident_finding`](../classes/incident_finding.md)