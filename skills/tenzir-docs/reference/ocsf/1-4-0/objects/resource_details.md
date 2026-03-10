# Resource Details

> The Resource Details object describes details about resources that were affected by the activity/event.


The Resource Details object describes details about resources that were affected by the activity/event.

* **Extends**: `_resource`

## Attributes

**`data_classification`**

* **Type**: [`data_classification`](data_classification.md)
* **Requirement**: recommended

The Data Classification object includes information about data classification levels and data category types.

**`data_classifications`**

* **Type**: [`data_classification`](data_classification.md)
* **Requirement**: recommended

A list of Data Classification objects, that include information about data classification levels and data category types, indentified by a classifier.

**`hostname`**

* **Type**: `hostname_t`
* **Requirement**: recommended

The fully qualified name of the resource.

**`ip`**

* **Type**: `ip_t`
* **Requirement**: recommended

The IP address of the resource, in either IPv4 or IPv6 format.

**`name`**

* **Type**: `string_t`
* **Requirement**: recommended

The name of the resource.

**`owner`**

* **Type**: [`user`](user.md)
* **Requirement**: recommended

The identity of the service or user account that owns the resource.

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The unique identifier of the resource.

**`agent_list`**

* **Type**: [`agent`](agent.md)
* **Requirement**: optional

A list of `agent` objects associated with a device, endpoint, or resource.

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

The list of labels associated to the resource.

**`namespace`**

* **Type**: `string_t`
* **Requirement**: optional

The namespace is useful when similar entities exist that you need to keep separate.

**`region`**

* **Type**: `string_t`
* **Requirement**: optional

The cloud region of the resource.

**`tags`**

* **Type**: [`key_value_object`](key_value_object.md)
* **Requirement**: optional

The list of tags; `{key:value}` pairs associated to the resource.

**`type`**

* **Type**: `string_t`
* **Requirement**: optional

The resource type as defined by the event source.

**`version`**

* **Type**: `string_t`
* **Requirement**: optional

The version of the resource. For example `1.2.3`.

## Constraints

At least one of: `name`, `uid`

## Used By

* [`api_activity`](../classes/api_activity.md)
* [`cloud_resources_inventory_info`](../classes/cloud_resources_inventory_info.md)
* [`compliance_finding`](../classes/compliance_finding.md)
* [`data_security_finding`](../classes/data_security_finding.md)
* [`detection_finding`](../classes/detection_finding.md)
* [`group_management`](../classes/group_management.md)
* [`security_finding`](../classes/security_finding.md)
* [`user_access`](../classes/user_access.md)
* [`vulnerability_finding`](../classes/vulnerability_finding.md)