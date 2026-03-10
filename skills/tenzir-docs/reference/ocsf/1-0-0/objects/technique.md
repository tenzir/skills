# Technique

> The Technique object describes the technique related to an attack, as defined by ATT&CK MatrixTM.


The Technique object describes the technique related to an attack, as defined by ATT\&CK MatrixTM.

* **Extends**: `_entity`

## Attributes

**`name`**

* **Type**: `string_t`
* **Requirement**: recommended

The name of the attack technique, as defined by ATT\&CK MatrixTM. For example: `Drive-by Compromise`.

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The unique identifier of the attack technique, as defined by ATT\&CK MatrixTM. For example: `T1189`.

## Constraints

At least one of: `name`, `uid`