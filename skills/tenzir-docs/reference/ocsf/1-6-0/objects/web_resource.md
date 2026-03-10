# Web Resource

> The Web Resource object describes characteristics of a web resource that was affected by the activity/event.


The Web Resource object describes characteristics of a web resource that was affected by the activity/event.

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

**`name`**

* **Type**: `string_t`
* **Requirement**: recommended

The name of the web resource.

**`uid`**

* **Type**: `resource_uid_t`
* **Requirement**: recommended

The unique identifier of the web resource.

**`url_string`**

* **Type**: `url_t`
* **Requirement**: recommended

The URL pointing towards the source of the web resource.

**`created_time`**

* **Type**: `timestamp_t`
* **Requirement**: optional

The time when the resource was created.

**`created_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The time when the resource was created.

**`data`**

* **Type**: `json_t`
* **Requirement**: optional

Details of the web resource, e.g, `file` details, `search` results or application-defined resource.

**`desc`**

* **Type**: `string_t`
* **Requirement**: optional

Description of the web resource.

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

**`tags`**

* **Type**: [`key_value_object`](key_value_object.md)
* **Requirement**: optional

The list of tags; `{key:value}` pairs associated to the resource.

**`type`**

* **Type**: `string_t`
* **Requirement**: optional

The web resource type as defined by the event source.

**`uid_alt`**

* **Type**: `resource_uid_t`
* **Requirement**: optional

The alternative unique identifier of the resource.

## Constraints

At least one of: `name`, `uid`

## Used By

* [`web_resource_access_activity`](../classes/web_resource_access_activity.md)
* [`web_resources_activity`](../classes/web_resources_activity.md)