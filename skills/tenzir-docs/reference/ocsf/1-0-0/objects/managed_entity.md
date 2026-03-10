# Managed Entity

> The Managed Entity object describes the type and version of an entity, such as a policy or configuration.


The Managed Entity object describes the type and version of an entity, such as a policy or configuration.

* **Extends**: `_entity`

## Attributes

**`name`**

* **Type**: `string_t`
* **Requirement**: recommended

The name of the managed entity.

**`type`**

* **Type**: `string_t`
* **Requirement**: recommended

The managed entity type. For example: `policy`, `user`, `organizational unit`, `device`.

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The identifier of the managed entity.

**`version`**

* **Type**: `string_t`
* **Requirement**: recommended

The version of the managed entity. For example: `1.2.3`.

**`data`**

* **Type**: `json_t`
* **Requirement**: optional

The managed entity content as a JSON object.

## Constraints

At least one of: `name`, `uid`

## Used By

* [`entity_management`](../classes/entity_management.md)