# Analytic

> The Analytic object contains details about the analytic technique used to analyze and derive insights from the data or information that led to the creation of a finding or conclusion.


The Analytic object contains details about the analytic technique used to analyze and derive insights from the data or information that led to the creation of a finding or conclusion.

* **Extends**: `_entity`

## Attributes

**`type_id`**

* **Type**: `integer_t`

* **Requirement**: required

* **Values**:

  * `0` - `Unknown`: The type is unknown.
  * `1` - `Rule`
  * `2` - `Behavioral`
  * `3` - `Statistical`
  * `4` - `Learning (ML/DL)`
  * `99` - `Other`: The type is not mapped. See the `type` attribute, which contains a data source specific value.

The analytic type ID.

**`name`**

* **Type**: `string_t`
* **Requirement**: recommended

The name of the analytic that generated the finding.

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The unique identifier of the analytic that generated the finding.

**`category`**

* **Type**: `string_t`
* **Requirement**: optional

The analytic category.

**`desc`**

* **Type**: `string_t`
* **Requirement**: optional

The description of the analytic that generated the finding.

**`related_analytics`**

* **Type**: [`analytic`](analytic.md)
* **Requirement**: optional

Other analytics related to this analytic.

**`type`**

* **Type**: `string_t`
* **Requirement**: optional

The analytic type.

**`version`**

* **Type**: `string_t`
* **Requirement**: optional

The analytic version. For example: `1.1`.

## Constraints

At least one of: `name`, `uid`

## Used By

* [`security_finding`](../classes/security_finding.md)