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

A list of Data Classification objects, that include information about data classification levels and data category types, identified by a classifier.

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

**`role_id`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`: The role is unknown.
  * `1` - `Target`: The resource is the primary target or subject of the event/finding.
  * `2` - `Actor`: The resource is acting as the initiator or performer in the context of the event/finding.
  * `3` - `Affected`: The resource was impacted or affected by the event/finding.
  * `4` - `Related`: The resource is related to or associated with the event/finding.
  * `99` - `Other`: The role is not mapped. See the role attribute, which contains a data source specific value.

The normalized identifier of the resource’s role in the context of the event or finding.

**`uid`**

* **Type**: `resource_uid_t`
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

**`created_time`**

* **Type**: `timestamp_t`
* **Requirement**: optional

The time when the resource was created.

**`created_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The time when the resource was created.

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

**`is_backed_up`**

* **Type**: `boolean_t`
* **Requirement**: optional

Indicates whether the device or resource has a backup enabled, such as an automated snapshot or a cloud backup. For example, this is indicated by the `cloudBackupEnabled` value within JAMF Pro mobile devices or the registration of an AWS ARN with the AWS Backup service.

**`labels`**

* **Type**: `string_t`
* **Requirement**: optional

The list of labels associated to the resource.

**`modified_time`**

* **Type**: `timestamp_t`
* **Requirement**: optional

The time when the resource was last modified.

**`modified_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The time when the resource was last modified.

**`namespace`**

* **Type**: `string_t`
* **Requirement**: optional

The namespace is useful when similar entities exist that you need to keep separate.

**`region`**

* **Type**: `string_t`
* **Requirement**: optional

The cloud region of the resource.

**`resource_relationship`**

* **Type**: [`graph`](graph.md)
* **Requirement**: optional

A graph representation showing how this resource relates to and interacts with other entities in the environment. This can include parent/child relationships, dependencies, or other connections.

**`role`**

* **Type**: `string_t`
* **Requirement**: optional

The role of the resource in the context of the event or finding, normalized to the caption of the role\_id value. In the case of ‘Other’, it is defined by the event source.

**`tags`**

* **Type**: [`key_value_object`](key_value_object.md)
* **Requirement**: optional

The list of tags; `{key:value}` pairs associated to the resource.

**`type`**

* **Type**: `string_t`
* **Requirement**: optional

The resource type as defined by the event source.

**`uid_alt`**

* **Type**: `resource_uid_t`
* **Requirement**: optional

The alternative unique identifier of the resource.

**`version`**

* **Type**: `string_t`
* **Requirement**: optional

The version of the resource. For example `1.2.3`.

**`zone`**

* **Type**: `string_t`
* **Requirement**: optional

The specific availability zone within a cloud region where the resource is located.

## Constraints

At least one of: `name`, `uid`

## Used By

* [`api_activity`](../classes/api_activity.md)
* [`application_security_posture_finding`](../classes/application_security_posture_finding.md)
* [`cloud_resources_inventory_info`](../classes/cloud_resources_inventory_info.md)
* [`compliance_finding`](../classes/compliance_finding.md)
* [`data_security_finding`](../classes/data_security_finding.md)
* [`detection_finding`](../classes/detection_finding.md)
* [`group_management`](../classes/group_management.md)
* [`iam_analysis_finding`](../classes/iam_analysis_finding.md)
* [`security_finding`](../classes/security_finding.md)
* [`user_access`](../classes/user_access.md)
* [`vulnerability_finding`](../classes/vulnerability_finding.md)