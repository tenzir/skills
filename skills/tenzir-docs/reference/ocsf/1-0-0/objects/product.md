# Product

> The Product object describes characteristics of a software product.


The Product object describes characteristics of a software product.

* **Extends**: `_entity`

## Attributes

**`vendor_name`**

* **Type**: `string_t`
* **Requirement**: required

The name of the vendor of the product.

**`lang`**

* **Type**: `string_t`
* **Requirement**: recommended

The two letter lower case language codes, as defined by [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1). For example: `en` (English), `de` (German), or `fr` (French).

**`name`**

* **Type**: `string_t`
* **Requirement**: recommended

The name of the product.

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The unique identifier of the product.

**`version`**

* **Type**: `string_t`
* **Requirement**: recommended

The version of the product, as defined by the event source. For example: `2013.1.3-beta`.

**`feature`**

* **Type**: [`feature`](feature.md)
* **Requirement**: optional

The feature that reported the event.

**`path`**

* **Type**: `string_t`
* **Requirement**: optional

The installation path of the product.

**`url_string`**

* **Type**: `url_t`
* **Requirement**: optional

The URL pointing towards the product.

## Constraints

At least one of: `name`, `uid`

## Used By

* [`application_lifecycle`](../classes/application_lifecycle.md)