# Tactic

> The Tactic object describes the tactic ID and/or name that is associated to an attack, as defined by ATT&CK MatrixTM.


The Tactic object describes the tactic ID and/or name that is associated to an attack, as defined by ATT\&CK MatrixTM.

* **Extends**: `_entity`

## Attributes

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The tactic ID that is associated with the attack technique, as defined by ATT\&CK MatrixTM. For example: `TA0043`.

**`name`**

* **Type**: `string_t`
* **Requirement**: optional

The tactic name that is associated with the attack technique, as defined by ATT\&CK MatrixTM. For example: `Reconnaissance`.

**`src_url`**

* **Type**: `url_t`
* **Requirement**: optional

The versioned permalink of the attack tactic, as defined by ATT\&CK MatrixTM. For example: `https://attack.mitre.org/versions/v14/tactics/TA0043/`.

## Constraints

At least one of: `name`, `uid`