# Related Event

> The Related Event object describes an event related to a finding or detection as identified by the security product.


The Related Event object describes an event related to a finding or detection as identified by the security product.

## Attributes

**`uid`**

* **Type**: `string_t`
* **Requirement**: required

The unique identifier of the related event.

**`type_uid`**

* **Type**: `integer_t`
* **Requirement**: recommended

The unique identifier of the related event type. For example: 100701.

**`product_uid`**

* **Type**: `string_t`
* **Requirement**: optional

The unique identifier of the product that reported the related event.

**`type`**

* **Type**: `string_t`
* **Requirement**: optional

The type of the related event. For example: Process Activity: Launch.