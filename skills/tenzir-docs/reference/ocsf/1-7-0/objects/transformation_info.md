# Transformation Info

> The transformation_info object represents the mapping or transformation used.


The transformation\_info object represents the mapping or transformation used.

* **Extends**: `_entity`

## Attributes

**`name`**

* **Type**: `string_t`
* **Requirement**: recommended

The name of the transformation or mapping.

**`time`**

* **Type**: `timestamp_t`
* **Requirement**: recommended

Time of the transformation.

**`url_string`**

* **Type**: `url_t`
* **Requirement**: recommended

The Uniform Resource Locator String where the mapping or transformation exists.

**`lang`**

* **Type**: `string_t`
* **Requirement**: optional

The transformation language used to transform the data.

**`product`**

* **Type**: [`product`](product.md)
* **Requirement**: optional

The product or instance used to make the transformation

**`time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

Time of the transformation.

**`uid`**

* **Type**: `string_t`
* **Requirement**: optional

The unique identifier of the mapping or transformation.

## Constraints

At least one of: `name`, `uid`