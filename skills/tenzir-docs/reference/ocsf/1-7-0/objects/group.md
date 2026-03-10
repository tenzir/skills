# Group

> The Group object represents a collection or association of entities, such as users, policies, or devices.


The Group object represents a collection or association of entities, such as users, policies, or devices. It serves as a logical grouping mechanism to organize and manage entities with similar characteristics or permissions within a system or organization, including but not limited to purposes of access control.

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

* [`admin_group_query`](../classes/admin_group_query.md)
* [`application_security_posture_finding`](../classes/application_security_posture_finding.md)
* [`authorize_session`](../classes/authorize_session.md)
* [`compliance_finding`](../classes/compliance_finding.md)
* [`data_security_finding`](../classes/data_security_finding.md)
* [`detection_finding`](../classes/detection_finding.md)
* [`group_management`](../classes/group_management.md)
* [`iam_analysis_finding`](../classes/iam_analysis_finding.md)
* [`incident_finding`](../classes/incident_finding.md)
* [`vulnerability_finding`](../classes/vulnerability_finding.md)