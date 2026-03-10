# Software Bill of Materials

> The Software Bill of Materials object describes characteristics of a generated SBOM.


The Software Bill of Materials object describes characteristics of a generated SBOM.

## Attributes

**`package`**

* **Type**: [`package`](package.md)
* **Requirement**: required

The device software that is being discovered by an inventory process.

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

The product that generated the SBOM e.g. cdxgen or Syft.

**`created_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The time when the SBOM was created.

## Used By

* [`software_info`](../classes/software_info.md)