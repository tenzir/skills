# Software Component

> The Software Component object describes characteristics of a software component within a software package.


The Software Component object describes characteristics of a software component within a software package.

## Attributes

**`name`**

* **Type**: `string_t`
* **Requirement**: required

The software component name.

**`version`**

* **Type**: `string_t`
* **Requirement**: required

The software component version.

**`author`**

* **Type**: `string_t`
* **Requirement**: recommended

The author(s) who published the software component.

**`purl`**

* **Type**: `string_t`
* **Requirement**: recommended

The Package URL (PURL) to identify the software component. This is a URL that uniquely identifies the component, including the component’s name, version, and type. The URL is used to locate and retrieve the component’s metadata and content.

**`related_component`**

* **Type**: `string_t`
* **Requirement**: recommended

The package URL (PURL) of the component that this software component has a relationship with.

**`relationship_id`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`: The relationship is unknown.
  * `1` - `Depends On`: The component is a dependency of another component. Can be used to define both direct and transitive dependencies.
  * `99` - `Other`: The relationship is not mapped. See the `relationship` attribute, which contains a data source specific value.

The normalized identifier of the relationship between two software components.

**`type_id`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`: The type is unknown.
  * `1` - `Framework`: A software framework.
  * `2` - `Library`: A software library.
  * `3` - `Operating System`: An operating system. Useful for SBOMs of container images.
  * `99` - `Other`: The type is not mapped. See the `type` attribute, which contains a data source specific value.

The type of software component.

**`hash`**

* **Type**: [`fingerprint`](fingerprint.md)
* **Requirement**: optional

Cryptographic hash to identify the binary instance of a software component.

**`license`**

* **Type**: `string_t`
* **Requirement**: optional

The software license applied to this component.

**`relationship`**

* **Type**: `string_t`
* **Requirement**: optional

The relationship between two software components, normalized to the caption of the `relationship_id` value. In the case of ‘Other’, it is defined by the source.

**`type`**

* **Type**: `string_t`
* **Requirement**: optional

The type of software component, normalized to the caption of the `type_id` value. In the case of ‘Other’, it is defined by the source.