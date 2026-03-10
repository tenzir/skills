# Discovery Details

> The Discovery Details object describes results of a discovery task/job.


The Discovery Details object describes results of a discovery task/job.

## Attributes

**`count`**

* **Type**: `integer_t`
* **Requirement**: recommended

The number of discovered entities of the specified type.

**`type`**

* **Type**: `string_t`
* **Requirement**: recommended

The specific type of information that was discovered. e.g.` name, phone_number, etc.`

**`occurrence_details`**

* **Type**: [`occurrence_details`](occurrence_details.md)
* **Requirement**: optional

Details about where in the target entity, specified information was discovered. Only the attributes, relevant to the target entity type should be populuated.

**`occurrences`**

* **Type**: [`occurrence_details`](occurrence_details.md)
* **Requirement**: optional

Details about where in the target entity, specified information was discovered. Only the attributes, relevant to the target entity type should be populuated.

**`value`**

* **Type**: `string_t`
* **Requirement**: optional

Optionally, the specific value of discovered information.