# Parameter

> The Parameter object provides details regarding a parameter of a a function.


The Parameter object provides details regarding a parameter of a a function.

## Attributes

**`name`**

* **Type**: `string_t`
* **Requirement**: optional

The parameter name.

**`post_value`**

* **Type**: `string_t`
* **Requirement**: optional

The parameter value after function execution.

**`pre_value`**

* **Type**: `string_t`
* **Requirement**: optional

The parameter value before function execution.

## Constraints

At least one of: `name`, `pre_value`, `post_value`