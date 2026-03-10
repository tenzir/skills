# Tactic

> The Tactic object describes the tactic IDs and/or name that are associated with the attack technique, as defined by ATT&CK MatrixTM.


The Tactic object describes the tactic IDs and/or name that are associated with the attack technique, as defined by ATT\&CK MatrixTM.

* **Extends**: `_entity`

## Attributes

**`name`**

* **Type**: `string_t`
* **Requirement**: recommended

The tactic name that is associated with the attack technique, as defined by ATT\&CK MatrixTM.

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The tactic ID that is associated with the attack technique, as defined by ATT\&CK MatrixTM.

## Constraints

At least one of: `name`, `uid`