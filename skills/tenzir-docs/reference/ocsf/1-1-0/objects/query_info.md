# Query Information

> The query info object holds information related to data access within a datastore.


The query info object holds information related to data access within a datastore. To access, manipulate, delete, or retrieve data from a datastore, a query must be written using a specific syntax.

* **Extends**: `_entity`

## Attributes

**`query_string`**

* **Type**: `string_t`
* **Requirement**: required

A string representing the query code being run. For example: `SELECT * FROM my_table`

**`name`**

* **Type**: `string_t`
* **Requirement**: recommended

The query name for a saved or scheduled query.

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The unique identifier of the query.

**`bytes`**

* **Type**: `long_t`
* **Requirement**: optional

The size of the data returned from the query.

**`data`**

* **Type**: `json_t`
* **Requirement**: optional

The data returned from the query execution.

**`query_time`**

* **Type**: `timestamp_t`
* **Requirement**: optional

The time when the query was run.

**`query_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The time when the query was run.

## Constraints

At least one of: `name`, `uid`

## Used By

* [`datastore_activity`](../classes/datastore_activity.md)