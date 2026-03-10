# MITRE ATT&CK® Sub Technique

> The MITRE ATT&CK® Sub Technique object describes the sub technique ID and/or name associated to an attack, as defined by [ATT&CK® Matrix](https://attack.mitre.org/wiki/ATT&CK_Matrix).


The MITRE ATT\&CK® Sub Technique object describes the sub technique ID and/or name associated to an attack, as defined by [ATT\&CK® Matrix](https://attack.mitre.org/wiki/ATT\&CK_Matrix).

* **Extends**: `_entity`

## Attributes

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The unique identifier of the attack sub technique, as defined by [ATT\&CK® Matrix](https://attack.mitre.org/wiki/ATT\&CK_Matrix). For example: `T1595.001`.

**`name`**

* **Type**: `string_t`
* **Requirement**: optional

The name of the attack sub technique, as defined by [ATT\&CK® Matrix](https://attack.mitre.org/wiki/ATT\&CK_Matrix). For example: `Scanning IP Blocks`.

**`src_url`**

* **Type**: `url_t`
* **Requirement**: optional

The versioned permalink of the attack sub technique, as defined by [ATT\&CK® Matrix](https://attack.mitre.org/wiki/ATT\&CK_Matrix). For example: `https://attack.mitre.org/versions/v14/techniques/T1595/001/`.

## Constraints

At least one of: `name`, `uid`