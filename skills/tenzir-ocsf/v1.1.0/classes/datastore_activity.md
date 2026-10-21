# Datastore Activity (datastore_activity)

Datastore events describe general activities (Read, Update, Query, Delete, etc.) which affect datastores or data within those datastores, e.g. (AWS RDS, AWS S3).

- **Class UID**: `6005`
- **Category**: Application Activity
- **Extends**: [Application Activity (application)](application.md)
- **Profiles**: [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md)

## Constraints

- **At least one of**: `database`, `databucket`, `table`

## Inherited attributes

**From Base Event:**
- `category_uid` (required)
- `metadata` (required)
- `severity_id` (required)
- `time` (required)
- `message` (recommended)
- `status_id` (recommended)
- `timezone_offset` (recommended)

## Attributes

### `activity_id`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `activity_name`

#### Enum values

- `0`: `Unknown` - The event activity is unknown.
- `1`: `Read` - The datastore activity in the event pertains to a 'Read' operation.
- `2`: `Update` - The datastore activity in the event pertains to a 'Update' operation.
- `3`: `Connect` - The datastore activity in the event pertains to a 'Connect' operation.
- `4`: `Query` - The datastore activity in the event pertains to a 'Query' operation.
- `5`: `Write` - The datastore activity in the event pertains to a 'Write' operation.
- `6`: `Create` - The datastore activity in the event pertains to a 'Create' operation.
- `7`: `Delete` - The datastore activity in the event pertains to a 'Delete' operation.
- `99`: `Other` - The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

The normalized identifier of the activity that triggered the event.

### `database`

- **Type**: [`database`](../objects/database.md)
- **Requirement**: recommended
- **Group**: primary

The database object is used for databases which are typically datastore services that contain an organized collection of structured and unstructured data or a types of data.

### `databucket`

- **Type**: [`databucket`](../objects/databucket.md)
- **Requirement**: recommended
- **Group**: primary

The data bucket object is a basic container that holds data, typically organized through the use of data partitions.

### `table`

- **Type**: [`table`](../objects/table.md)
- **Requirement**: optional
- **Group**: primary

The table object represents a table within a structured relational database or datastore, which contains columns and rows of data that are able to be create, updated, deleted and queried.

### `type`

- **Type**: `string_t`
- **Requirement**: optional

The datastore resource type (e.g. database, datastore, or table).

### `type_id`

- **Type**: `integer_t`
- **Requirement**: recommended
- **Sibling**: `type`

#### Enum values

- `0`: `Unknown` - The datastore resource type is unknown.
- `1`: `Database`
- `2`: `Databucket`
- `3`: `Table`
- `99`: `Other` - The datastore resource type is not mapped.

The normalized datastore resource type identifier.

### `query_info`

- **Type**: [`query_info`](../objects/query_info.md)
- **Requirement**: optional
- **Group**: primary

The query info object holds information related to data access within a datastore. To access, manipulate, delete, or retrieve data from a datastore, a database query must be written using a specific syntax.

### `dst_endpoint`

- **Type**: [`network_endpoint`](../objects/network_endpoint.md)
- **Requirement**: optional
- **Group**: primary

Details about the endpoint hosting the datastore application or service.

### `http_request`

- **Type**: [`http_request`](../objects/http_request.md)
- **Requirement**: optional
- **Group**: primary

Details about the underlying http request.

### `actor`

- **Type**: [`actor`](../objects/actor.md)
- **Requirement**: required
- **Group**: primary

The actor object describes details about the user/role/process that was the source of the activity.

### `src_endpoint`

- **Type**: [`network_endpoint`](../objects/network_endpoint.md)
- **Requirement**: required
- **Group**: primary

Details about the source of the activity.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `6005`: `Datastore Activity` - Datastore events describe general activities (Read, Update, Query, Delete, etc.) which affect datastores or data within those datastores, e.g. (AWS RDS, AWS S3).

The unique identifier of a class. A Class describes the attributes available in an event.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `600500`: `Datastore Activity: Unknown`
- `600501`: `Datastore Activity: Read` - The datastore activity in the event pertains to a 'Read' operation.
- `600502`: `Datastore Activity: Update` - The datastore activity in the event pertains to a 'Update' operation.
- `600503`: `Datastore Activity: Connect` - The datastore activity in the event pertains to a 'Connect' operation.
- `600504`: `Datastore Activity: Query` - The datastore activity in the event pertains to a 'Query' operation.
- `600505`: `Datastore Activity: Write` - The datastore activity in the event pertains to a 'Write' operation.
- `600506`: `Datastore Activity: Create` - The datastore activity in the event pertains to a 'Create' operation.
- `600507`: `Datastore Activity: Delete` - The datastore activity in the event pertains to a 'Delete' operation.
- `600599`: `Datastore Activity: Other`

The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
