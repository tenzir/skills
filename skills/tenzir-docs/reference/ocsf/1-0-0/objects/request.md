# Request Elements

> The Request Elements object describes characteristics of an API request.


The Request Elements object describes characteristics of an API request.

## Attributes

**`uid`**

* **Type**: `string_t`
* **Requirement**: required

The unique request identifier.

**`flags`**

* **Type**: `string_t`
* **Requirement**: optional

The list of communication flags, normalized to the captions of the flag\_ids values. In the case of ‘Other’, they are defined by the event source.

## Used By

* [`rdp_activity`](../classes/rdp_activity.md)