# Technique

> The Technique object describes the technique ID and/or name associated to an attack, as defined by ATT&CK MatrixTM.


The Technique object describes the technique ID and/or name associated to an attack, as defined by ATT\&CK MatrixTM.

* **Extends**: `_entity`

## Attributes

**`name`**

* **Type**: `string_t`
* **Requirement**: recommended

The name of the attack technique, as defined by ATT\&CK MatrixTM. For example: `Active Scanning`.

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The unique identifier of the attack technique, as defined by ATT\&CK MatrixTM. For example: `T1595`.

**`src_url`**

* **Type**: `url_t`
* **Requirement**: optional

The versioned permalink of the attack technique, as defined by ATT\&CK MatrixTM. For example: `https://attack.mitre.org/versions/v14/techniques/T1595/`.

## Constraints

At least one of: `name`, `uid`