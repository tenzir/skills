# MITRE D3FEND™

> The [MITRE D3FEND™](https://d3fend.mitre.org) object describes the tactic, technique & sub-technique associated with a countermeasure as defined in DEFEND MatrixTM.


The [MITRE D3FEND™](https://d3fend.mitre.org) object describes the tactic, technique & sub-technique associated with a countermeasure as defined in DEFEND MatrixTM.

## Attributes

**`d3f_tactic`**

* **Type**: [`d3f_tactic`](d3f_tactic.md)
* **Requirement**: recommended

The Tactic object describes the tactic ID and/or name that is associated with a countermeasure, as defined by D3FEND MatrixTM.

**`d3f_technique`**

* **Type**: [`d3f_technique`](d3f_technique.md)
* **Requirement**: recommended

The Defend Technique object describes the technique ID and/or name associated with a countermeasure, as defined by D3FEND MatrixTM.

**`version`**

* **Type**: `string_t`
* **Requirement**: recommended

The D3FEND MatrixTM version.

## Constraints

At least one of: `d3f_tactic`, `d3f_technique`

## Used By

* [`file_remediation_activity`](../classes/file_remediation_activity.md)
* [`network_remediation_activity`](../classes/network_remediation_activity.md)
* [`process_remediation_activity`](../classes/process_remediation_activity.md)
* [`remediation_activity`](../classes/remediation_activity.md)