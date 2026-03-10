# MITRE Tactic

> The MITRE Tactic object describes the ATT&CK® or ATLAS™ Tactic ID and/or name that is associated to an attack.


The MITRE Tactic object describes the ATT\&CK® or ATLAS™ Tactic ID and/or name that is associated to an attack.

* **Extends**: `_entity`

## Attributes

**`name`**

* **Type**: `string_t`
* **Requirement**: recommended

The Tactic name that is associated with the attack technique. For example: `Reconnaissance` or `ML Model Access`.

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The Tactic ID that is associated with the attack technique. For example: `TA0043`, or `AML.TA0000`.

**`src_url`**

* **Type**: `url_t`
* **Requirement**: optional

The versioned permalink of the Tactic. For example: `https://attack.mitre.org/versions/v14/tactics/TA0043/`.

## Constraints

At least one of: `name`, `uid`