# Database

> The database object is used for databases which are typically datastore services that contain an organized collection of structured and unstructured data or a types of data.


The database object is used for databases which are typically datastore services that contain an organized collection of structured and unstructured data or a types of data.

* **Extends**: `_entity`

## Attributes

**`type_id`**

* **Type**: `integer_t`

* **Requirement**: required

* **Values**:

  * `0` - `Unknown`: The type is unknown.
  * `1` - `Relational`
  * `2` - `Network`
  * `3` - `Object Oriented`
  * `4` - `Centralized`
  * `5` - `Operational`
  * `6` - `NoSQL`
  * `99` - `Other`: The type is not mapped. See the `type` attribute, which contains a data source specific value.

The normalized identifier of the database type.

**`data_classification`**

* **Type**: [`data_classification`](data_classification.md)
* **Requirement**: recommended

The Data Classification object includes information about data classification levels and data category types.

**`name`**

* **Type**: `string_t`
* **Requirement**: recommended

The database name, ordinarily as assigned by a database administrator.

**`type`**

* **Type**: `string_t`
* **Requirement**: recommended

The database type.

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The unique identifier of the database.

**`created_time`**

* **Type**: `timestamp_t`
* **Requirement**: optional

The time when the database was known to have been created.

**`created_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The time when the database was known to have been created.

**`desc`**

* **Type**: `string_t`
* **Requirement**: optional

The description of the database.

**`groups`**

* **Type**: [`group`](group.md)
* **Requirement**: optional

The group names to which the database belongs.

**`modified_time`**

* **Type**: `timestamp_t`
* **Requirement**: optional

The most recent time when any changes, updates, or modifications were made within the database.

**`modified_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The most recent time when any changes, updates, or modifications were made within the database.

**`size`**

* **Type**: `long_t`
* **Requirement**: optional

The size of the database in bytes.

## Constraints

At least one of: `name`, `uid`

## Used By

* [`data_security_finding`](../classes/data_security_finding.md)
* [`datastore_activity`](../classes/datastore_activity.md)