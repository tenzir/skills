# Ticket

> The Ticket object represents ticket in the customer's IT Service Management (ITSM) systems like ServiceNow, Jira, etc.


The Ticket object represents ticket in the customer’s IT Service Management (ITSM) systems like ServiceNow, Jira, etc.

## Attributes

**`src_url`**

* **Type**: `url_t`
* **Requirement**: recommended

The url of a ticket in the ticket system.

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

Unique identifier of the ticket.

**`status`**

* **Type**: `string_t`
* **Requirement**: optional

The status of the ticket normalized to the caption of the `status_id` value. In the case of `99`, this value should as defined by the source.

**`status_details`**

* **Type**: `string_t`
* **Requirement**: optional

A list of contextual descriptions of the `status, status_id` values.

**`status_id`**

* **Type**: `integer_t`

* **Requirement**: optional

* **Values**:

  * `0` - `Unknown`: The status is unknown.
  * `1` - `New`: The ticket is new and yet to be reviewed.
  * `2` - `In Progress`: The ticket is actively being worked on.
  * `3` - `Notified`: Relevant parties have been notified about the ticket.
  * `4` - `On Hold`: Work on the ticket is temporarily suspended.
  * `5` - `Resolved`: The ticket is resolved and a solution is implemented, pending confirmation or verification from the requestor.
  * `6` - `Closed`: The ticket has been completed and closed.
  * `7` - `Canceled`: The ticket has been canceled and will not be processed.
  * `8` - `Reopened`: The ticket was previously closed, but has been reopened.
  * `99` - `Other`: The status is not mapped. See the `status` attribute, which contains a data source specific value.

The normalized identifier for the ticket status.

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

* [`application_security_posture_finding`](../classes/application_security_posture_finding.md)
* [`compliance_finding`](../classes/compliance_finding.md)
* [`data_security_finding`](../classes/data_security_finding.md)
* [`detection_finding`](../classes/detection_finding.md)
* [`iam_analysis_finding`](../classes/iam_analysis_finding.md)
* [`incident_finding`](../classes/incident_finding.md)
* [`vulnerability_finding`](../classes/vulnerability_finding.md)