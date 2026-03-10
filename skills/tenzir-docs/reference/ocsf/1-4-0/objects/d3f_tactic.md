# MITRE D3FEND™ Tactic

> The MITRE D3FEND™ Tactic object describes the tactic ID and/or name that is associated to an attack


The MITRE D3FEND™ Tactic object describes the tactic ID and/or name that is associated to an attack

* **Extends**: `_entity`

## Attributes

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The unique identifier of the entity.

**`name`**

* **Type**: `string_t`
* **Requirement**: optional

The tactic name that is associated with the defensive technique. For example: `Isolate`.

**`src_url`**

* **Type**: `url_t`
* **Requirement**: optional

The versioned permalink of the defensive tactic. For example: `https://d3fend.mitre.org/tactic/d3f:Isolate/`.

## Constraints

At least one of: `name`, `uid`