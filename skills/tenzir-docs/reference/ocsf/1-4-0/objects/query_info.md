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

* [`admin_group_query`](../classes/admin_group_query.md)
* [`datastore_activity`](../classes/datastore_activity.md)
* [`file_query`](../classes/file_query.md)
* [`folder_query`](../classes/folder_query.md)
* [`job_query`](../classes/job_query.md)
* [`kernel_object_query`](../classes/kernel_object_query.md)
* [`module_query`](../classes/module_query.md)
* [`network_connection_query`](../classes/network_connection_query.md)
* [`networks_query`](../classes/networks_query.md)
* [`peripheral_device_query`](../classes/peripheral_device_query.md)
* [`process_query`](../classes/process_query.md)
* [`service_query`](../classes/service_query.md)
* [`session_query`](../classes/session_query.md)
* [`startup_item_query`](../classes/startup_item_query.md)
* [`user_query`](../classes/user_query.md)