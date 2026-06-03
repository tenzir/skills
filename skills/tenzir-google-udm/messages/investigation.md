# Investigation

Represents the aggregated state of an investigation such as categorization, severity, and status. Can be expanded to include analyst assignment details and more.

- **Full name**: `google.backstory.Investigation`
- **Fields**: `10`

## Fields

### `verdict`

- **Number**: `2`
- **Cardinality**: `optional`
- **Type**: [`Verdict`](../enums/verdict.md)
- **JSON name**: `verdict`

Describes reason a finding investigation was resolved.

### `reputation`

- **Number**: `3`
- **Cardinality**: `optional`
- **Type**: [`Reputation`](../enums/reputation.md)
- **JSON name**: `reputation`

Describes whether a finding was useful or not-useful.

### `severity_score`

- **Number**: `4`
- **Cardinality**: `optional`
- **Type**: `uint32`
- **JSON name**: `severityScore`

Severity score for a finding set by an analyst.

### `status`

- **Number**: `5`
- **Cardinality**: `optional`
- **Type**: [`Status`](../enums/status.md)
- **JSON name**: `status`

Describes the workflow status of a finding.

### `comments`

- **Number**: `6`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `comments`

Comment added by the Analyst.

### `priority`

- **Number**: `7`
- **Cardinality**: `optional`
- **Type**: [`Priority`](../enums/priority.md)
- **JSON name**: `priority`

Priority of the Alert or Finding set by analyst.

### `root_cause`

- **Number**: `8`
- **Cardinality**: `optional`
- **Type**: `string`
- **JSON name**: `rootCause`

Root cause of the Alert or Finding set by analyst.

### `reason`

- **Number**: `9`
- **Cardinality**: `optional`
- **Type**: [`Reason`](../enums/reason.md)
- **JSON name**: `reason`

Reason for closing the Case or Alert.

### `risk_score`

- **Number**: `10`
- **Cardinality**: `optional`
- **Type**: `uint32`
- **JSON name**: `riskScore`

Risk score for a finding set by an analyst.

### `id`

- **Number**: `11`
- **Cardinality**: `optional`
- **Type**: `string`
- **JSON name**: `id`

Identifier for the investigation
