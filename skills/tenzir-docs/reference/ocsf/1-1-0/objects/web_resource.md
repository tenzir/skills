# Web Resource

> The Web Resource object describes characteristics of a web resource that was affected by the activity/event.


The Web Resource object describes characteristics of a web resource that was affected by the activity/event.

* **Extends**: `_resource`

## Attributes

**`url_string`**

* **Type**: `url_t`
* **Requirement**: recommended

The URL pointing towards the source of the web resource.

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

The list of labels/tags associated to a resource.

**`name`**

* **Type**: `string_t`
* **Requirement**: optional

The name of the web resource.

**`type`**

* **Type**: `string_t`
* **Requirement**: optional

The web resource type as defined by the event source.

**`uid`**

* **Type**: `string_t`
* **Requirement**: optional

The unique identifier of the web resource.

## Constraints

At least one of: `name`, `uid`

## Used By

* [`web_resource_access_activity`](../classes/web_resource_access_activity.md)
* [`web_resources_activity`](../classes/web_resources_activity.md)