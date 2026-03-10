# Databucket

> The databucket object is a basic container that holds data, typically organized through the use of data partitions.


The databucket object is a basic container that holds data, typically organized through the use of data partitions.

* **Extends**: `_entity`

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

**`name`**

* **Type**: `string_t`
* **Requirement**: recommended

The databucket name.

**`type`**

* **Type**: `string_t`
* **Requirement**: recommended

The databucket type.

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The unique identifier of the databucket.

**`created_time`**

* **Type**: `timestamp_t`
* **Requirement**: optional

The time when the databucket was known to have been created.

**`created_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The time when the databucket was known to have been created.

**`desc`**

* **Type**: `string_t`
* **Requirement**: optional

The description of the databucket.

**`file`**

* **Type**: [`file`](file.md)
* **Requirement**: optional

A file within a databucket.

**`groups`**

* **Type**: [`group`](group.md)
* **Requirement**: optional

The group names to which the databucket belongs.

**`modified_time`**

* **Type**: `timestamp_t`
* **Requirement**: optional

The most recent time when any changes, updates, or modifications were made within the databucket.

**`modified_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The most recent time when any changes, updates, or modifications were made within the databucket.

**`size`**

* **Type**: `long_t`
* **Requirement**: optional

The size of the databucket in bytes.

## Constraints

At least one of: `name`, `uid`

## Used By

* [`data_security_finding`](../classes/data_security_finding.md)
* [`datastore_activity`](../classes/datastore_activity.md)