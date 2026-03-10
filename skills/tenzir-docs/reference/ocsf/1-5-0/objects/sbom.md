# Software Bill of Materials

> The Software Bill of Materials object describes characteristics of a generated SBOM.


The Software Bill of Materials object describes characteristics of a generated SBOM.

## Attributes

**`package`**

* **Type**: [`package`](package.md)
* **Requirement**: required

The software package or library that is being discovered or inventoried by an SBOM.

**`software_components`**

* **Type**: [`software_component`](software_component.md)
* **Requirement**: required

The list of software components used in the software package.

**`created_time`**

* **Type**: `timestamp_t`
* **Requirement**: recommended

The time when the SBOM was created.

**`product`**

* **Type**: [`product`](product.md)
* **Requirement**: recommended

Details about the upstream product that generated the SBOM e.g. `cdxgen` or `Syft`.

**`type_id`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`: The type is unknown.
  * `1` - `SPDX`: System Package Data Exchange (SPDX®) is an open standard capable of representing systems with software components in as SBOMs (Software Bill of Materials) and other AI, data and security references supporting a range of risk management use cases. The SPDX specification is a freely available international open standard (ISO/IEC 5692:2021).
  * `2` - `CycloneDX`: CycloneDX is an International Standard for Bill of Materials (ECMA-424).
  * `3` - `SWID`: The International Organization for Standardization (ISO) and the International Electrotechnical Commission (IEC) publishes, ISO/IEC 19770-2, a standard for software identification (SWID) tags that defines a structured metadata format for describing a software product. A SWID tag document is composed of a structured set of data elements that identify the software product
  * `99` - `Other`: The type is not mapped. See the `type` attribute, which contains a data source specific value.

The type of SBOM.

**`created_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The time when the SBOM was created.

**`type`**

* **Type**: `string_t`
* **Requirement**: optional

The type of SBOM, normalized to the caption of the `type_id` value. In the case of ‘Other’, it is defined by the source.

**`uid`**

* **Type**: `string_t`
* **Requirement**: optional

A unique identifier for the SBOM or the SBOM generation by a source tool, such as the SPDX `metadata.component.bom-ref`.

**`version`**

* **Type**: `string_t`
* **Requirement**: optional

The specification (spec) version of the particular SBOM, e.g., `1.6`.

## Used By

* [`software_info`](../classes/software_info.md)