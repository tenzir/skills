# Response Elements

> The Response Elements object describes characteristics of an API response.


The Response Elements object describes characteristics of an API response.

## Attributes

**`code`**

* **Type**: `integer_t`
* **Requirement**: recommended

The numeric response sent to a request.

**`error`**

* **Type**: `string_t`
* **Requirement**: recommended

Error Code

**`error_message`**

* **Type**: `string_t`
* **Requirement**: recommended

Error Message

**`message`**

* **Type**: `string_t`
* **Requirement**: recommended

The description of the event, as defined by the event source.

**`flags`**

* **Type**: `string_t`
* **Requirement**: optional

The list of communication flags, normalized to the captions of the flag\_ids values. In the case of ‘Other’, they are defined by the event source.

## Used By

* [`rdp_activity`](../classes/rdp_activity.md)
* [`smb_activity`](../classes/smb_activity.md)