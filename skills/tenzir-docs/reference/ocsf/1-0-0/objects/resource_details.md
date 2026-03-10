# Resource Details

> The Resource Details object describes details about resources that were affected by the activity/event.


The Resource Details object describes details about resources that were affected by the activity/event.

* **Extends**: `_resource`

## Attributes

**`owner`**

* **Type**: [`user`](user.md)
* **Requirement**: recommended

The identity of the service or user account that owns the resource.

**`cloud_partition`**

* **Type**: `string_t`
* **Requirement**: optional

The canonical cloud partition name to which the region is assigned (e.g. AWS Partitions: aws, aws-cn, aws-us-gov).

**`criticality`**

* **Type**: `string_t`
* **Requirement**: optional

The criticality of the resource as defined by the event source.

**`data`**

* **Type**: `json_t`
* **Requirement**: optional

Additional data describing the resource.

**`group`**

* **Type**: [`group`](group.md)
* **Requirement**: optional

The name of the related resource group.

**`labels`**

* **Type**: `string_t`
* **Requirement**: optional

The list of labels/tags associated to a resource.

**`name`**

* **Type**: `string_t`
* **Requirement**: optional

The name of the resource.

**`region`**

* **Type**: `string_t`
* **Requirement**: optional

The cloud region of the resource.

**`type`**

* **Type**: `string_t`
* **Requirement**: optional

The resource type as defined by the event source.

**`uid`**

* **Type**: `string_t`
* **Requirement**: optional

The unique identifier of the resource.

**`version`**

* **Type**: `string_t`
* **Requirement**: optional

The version of the resource. For example `1.2.3`.

## Constraints

At least one of: `name`, `uid`

## Used By

* [`api_activity`](../classes/api_activity.md)
* [`group_management`](../classes/group_management.md)
* [`security_finding`](../classes/security_finding.md)
* [`user_access`](../classes/user_access.md)