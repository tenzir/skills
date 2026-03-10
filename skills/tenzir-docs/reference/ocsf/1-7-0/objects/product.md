# Product

> The Product object describes characteristics of a software product.


The Product object describes characteristics of a software product.

* **Extends**: `_entity`

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

The name of the product.

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The unique identifier of the product.

**`vendor_name`**

* **Type**: `string_t`
* **Requirement**: recommended

The name of the vendor of the product.

**`version`**

* **Type**: `string_t`
* **Requirement**: recommended

The version of the product, as defined by the event source. For example: `2013.1.3-beta`.

**`cpe_name`**

* **Type**: `string_t`
* **Requirement**: optional

The Common Platform Enumeration (CPE) name as described by ([NIST](https://nvd.nist.gov/products/cpe)) For example: `cpe:/a:apple:safari:16.2`.

**`feature`**

* **Type**: [`feature`](feature.md)
* **Requirement**: optional

The feature that reported the event.

**`lang`**

* **Type**: `string_t`
* **Requirement**: optional

The two letter lower case language codes, as defined by [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1). For example: `en` (English), `de` (German), or `fr` (French).

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
* [`software_info`](../classes/software_info.md)