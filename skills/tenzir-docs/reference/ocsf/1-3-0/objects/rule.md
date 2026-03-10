# Rule

> The Rule object describes characteristics of a rule associated with a policy or an event.


The Rule object describes characteristics of a rule associated with a policy or an event.

* **Extends**: `_entity`

## Attributes

**`name`**

* **Type**: `string_t`
* **Requirement**: recommended

The name of the rule that generated the event.

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The unique identifier of the rule that generated the event.

**`category`**

* **Type**: `string_t`
* **Requirement**: optional

The rule category.

**`desc`**

* **Type**: `string_t`
* **Requirement**: optional

The description of the rule that generated the event.

**`type`**

* **Type**: `string_t`
* **Requirement**: optional

The rule type.

**`version`**

* **Type**: `string_t`
* **Requirement**: optional

The rule version. For example: `1.1`.

## Constraints

At least one of: `name`, `uid`