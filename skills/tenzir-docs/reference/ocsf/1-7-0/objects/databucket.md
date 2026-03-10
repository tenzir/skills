# Databucket

> The databucket object is a basic container that holds data, typically organized through the use of data partitions.


The databucket object is a basic container that holds data, typically organized through the use of data partitions.

* **Extends**: `_resource`

## Attributes

**`type_id`**

* **Type**: `integer_t`

* **Requirement**: required

* **Values**:

  * `0` - `Unknown`: The type is unknown.
  * `1` - `S3`
  * `2` - `Azure Blob`
  * `3` - `GCP Bucket`
  * `99` - `Other`: The type is not mapped. See the `type` attribute, which contains a data source specific value.

The normalized identifier of the databucket type.

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

The fully qualified hostname of the databucket.

**`ip`**

* **Type**: `ip_t`
* **Requirement**: recommended

The IP address of the resource, in either IPv4 or IPv6 format.

**`is_public`**

* **Type**: `boolean_t`
* **Requirement**: recommended

Indicates if the databucket is publicly accessible.

**`name`**

* **Type**: `string_t`
* **Requirement**: recommended

The databucket name.

**`owner`**

* **Type**: [`user`](user.md)
* **Requirement**: recommended

The identity of the service or user account that owns the databucket.

**`type`**

* **Type**: `string_t`
* **Requirement**: recommended

The databucket type.

**`uid`**

* **Type**: `resource_uid_t`
* **Requirement**: recommended

The unique identifier of the databucket.

**`agent_list`**

* **Type**: [`agent`](agent.md)
* **Requirement**: optional

A list of `agent` objects associated with a device, endpoint, or resource.

**`cloud_partition`**

* **Type**: `string_t`
* **Requirement**: optional

The logical grouping or isolated segment within a cloud provider’s infrastructure where the databucket is located.

**`created_time`**

* **Type**: `timestamp_t`
* **Requirement**: optional

The time when the databucket was known to have been created.

**`created_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The time when the databucket was known to have been created.

**`criticality`**

* **Type**: `string_t`
* **Requirement**: optional

The criticality of the databucket as defined by the event source.

**`data`**

* **Type**: `json_t`
* **Requirement**: optional

Additional data describing the resource.

**`desc`**

* **Type**: `string_t`
* **Requirement**: optional

The description of the databucket.

**`encryption_details`**

* **Type**: [`encryption_details`](encryption_details.md)
* **Requirement**: optional

The encryption details of the databucket. Should be populated if the databucket is encrypted.

**`file`**

* **Type**: [`file`](file.md)
* **Requirement**: optional

Details about the file/object within a databucket.

**`group`**

* **Type**: [`group`](group.md)
* **Requirement**: optional

The name of the related resource group.

**`groups`**

* **Type**: [`group`](group.md)
* **Requirement**: optional

The group names to which the databucket belongs.

**`is_backed_up`**

* **Type**: `boolean_t`
* **Requirement**: optional

Indicates whether the device or resource has a backup enabled, such as an automated snapshot or a cloud backup. For example, this is indicated by the `cloudBackupEnabled` value within JAMF Pro mobile devices or the registration of an AWS ARN with the AWS Backup service.

**`is_encrypted`**

* **Type**: `boolean_t`
* **Requirement**: optional

Indicates if the databucket is encrypted.

**`labels`**

* **Type**: `string_t`
* **Requirement**: optional

The list of labels associated to the resource.

**`modified_time`**

* **Type**: `timestamp_t`
* **Requirement**: optional

The most recent time when any changes, updates, or modifications were made within the databucket.

**`modified_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The most recent time when any changes, updates, or modifications were made within the databucket.

**`namespace`**

* **Type**: `string_t`
* **Requirement**: optional

The namespace is useful when similar entities exist that you need to keep separate.

**`region`**

* **Type**: `string_t`
* **Requirement**: optional

The cloud region of the databucket.

**`resource_relationship`**

* **Type**: [`graph`](graph.md)
* **Requirement**: optional

A graph representation showing how this databucket relates to and interacts with other entities in the environment. This can include parent/child relationships, dependencies, or other connections.

**`size`**

* **Type**: `long_t`
* **Requirement**: optional

The size of the databucket in bytes.

**`tags`**

* **Type**: [`key_value_object`](key_value_object.md)
* **Requirement**: optional

The list of tags; `{key:value}` pairs associated to the resource.

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

The specific availability zone within a cloud region where the databucket is located.

## Constraints

At least one of: `name`, `uid`

## Used By

* [`cloud_resources_inventory_info`](../classes/cloud_resources_inventory_info.md)
* [`data_security_finding`](../classes/data_security_finding.md)
* [`datastore_activity`](../classes/datastore_activity.md)