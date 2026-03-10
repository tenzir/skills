# MITRE D3FEND™ Tactic

> The MITRE D3FEND™ Tactic object describes the tactic ID and/or name that is associated to an attack, as defined by D3FENDTM Matrix.


The MITRE D3FEND™ Tactic object describes the tactic ID and/or name that is associated to an attack, as defined by D3FENDTM Matrix.

* **Extends**: `_entity`

## Attributes

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The unique identifier of the entity.

**`name`**

* **Type**: `string_t`
* **Requirement**: optional

The tactic name that is associated with the defensive technique, as defined by D3FENDTM Matrix. For example: `Isolate`.

**`src_url`**

* **Type**: `url_t`
* **Requirement**: optional

The versioned permalink of the defensive tactic, as defined by D3FENDTM Matrix. For example: `https://d3fend.mitre.org/tactic/d3f:Isolate/`.

## Constraints

At least one of: `name`, `uid`