# Ticket

> The Ticket object represents ticket in the customer's systems like Salesforce, jira etc.


The Ticket object represents ticket in the customer’s systems like Salesforce, jira etc.

## Attributes

**`src_url`**

* **Type**: `url_t`
* **Requirement**: recommended

The url of a ticket in the ticket system.

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

Unique ticket identifier like ticket id.

**`title`**

* **Type**: `string_t`
* **Requirement**: optional

The title of the ticket.

**`type`**

* **Type**: `string_t`
* **Requirement**: optional

The linked ticket type determines whether the ticket is internal or in an external ticketing system.

**`type_id`**

* **Type**: `integer_t`

* **Requirement**: optional

* **Values**:

  * `0` - `Unknown`: The type is unknown.
  * `1` - `Internal`
  * `2` - `External`
  * `99` - `Other`: The type is not mapped. See the `type` attribute, which contains a data source specific value.

The normalized identifier for the ticket type.

## Constraints

At least one of: `src_url`, `uid`

## Used By

* [`incident_finding`](../classes/incident_finding.md)