# Trait

> Describes a characteristic or feature of an entity that was observed.


Describes a characteristic or feature of an entity that was observed. For example, this object can be used to represent specific characteristics derived from events or findings that can be surfaced as distinguishing traits of the entity in question.

* **Extends**: `_entity`

## Attributes

**`name`**

* **Type**: `string_t`
* **Requirement**: recommended

The name of the trait.

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The unique identifier of the trait.

**`category`**

* **Type**: `string_t`
* **Requirement**: optional

The high-level grouping or classification this trait belongs to.

**`type`**

* **Type**: `string_t`
* **Requirement**: optional

The type of the trait. For example, this can be used to indicate if the trait acts as a contributing factor (increases risk/severity) or a mitigating factor (decreases risk/severity), in the context of the related finding.

**`values`**

* **Type**: `string_t`
* **Requirement**: optional

The values of the trait.

## Constraints

At least one of: `name`, `uid`