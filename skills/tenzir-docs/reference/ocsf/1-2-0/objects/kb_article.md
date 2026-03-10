# KB Article

> The KB Article object contains metadata that describes the patch or update.


The KB Article object contains metadata that describes the patch or update.

## Attributes

**`uid`**

* **Type**: `string_t`
* **Requirement**: required

The unique identifier for the kb article.

**`os`**

* **Type**: [`os`](os.md)
* **Requirement**: recommended

The operating system the kb article applies.

**`severity`**

* **Type**: `string_t`
* **Requirement**: recommended

The severity of the kb article.

**`title`**

* **Type**: `string_t`
* **Requirement**: recommended

The title of the kb article.

**`bulletin`**

* **Type**: `string_t`
* **Requirement**: optional

The kb article bulletin identifier.

**`classification`**

* **Type**: `string_t`
* **Requirement**: optional

The vendors classification of the kb article.

**`created_time`**

* **Type**: `timestamp_t`
* **Requirement**: optional

The date the kb article was released by the vendor.

**`created_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The date the kb article was released by the vendor.

**`is_superseded`**

* **Type**: `boolean_t`
* **Requirement**: optional

The kb article has been replaced by another.

**`product`**

* **Type**: [`product`](product.md)
* **Requirement**: optional

The product details the kb article applies.

**`size`**

* **Type**: `long_t`
* **Requirement**: optional

The size in bytes for the kb article.

**`src_url`**

* **Type**: `url_t`
* **Requirement**: optional

The kb article link from the source vendor.

## Used By

* [`patch_state`](../classes/patch_state.md)