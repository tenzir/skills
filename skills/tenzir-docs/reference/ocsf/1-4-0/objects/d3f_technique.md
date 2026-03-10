# MITRE DEFEND™ Technique

> The MITRE D3FEND™ Technique object describes the leaf defensive technique ID and/or name associated to a countermeasure.


The MITRE D3FEND™ Technique object describes the leaf defensive technique ID and/or name associated to a countermeasure.

* **Extends**: `_entity`

## Attributes

**`name`**

* **Type**: `string_t`
* **Requirement**: recommended

The name of the defensive technique. For example: `IO Port Restriction`.

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The unique identifier of the defensive technique. For example: `D3-IOPR`.

**`src_url`**

* **Type**: `url_t`
* **Requirement**: optional

The versioned permalink of the defensive technique. For example: `https://d3fend.mitre.org/technique/d3f:IOPortRestriction/`.

## Constraints

At least one of: `name`, `uid`