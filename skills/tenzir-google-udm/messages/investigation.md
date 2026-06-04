# Investigation

Represents the aggregated state of an investigation such as categorization, severity, and status. Can be expanded to include analyst assignment details and more.

## Fields

### `verdict`

- Type: [`Verdict`](../enums/verdict.md) (optional)

Describes reason a finding investigation was resolved.

### `reputation`

- Type: [`Reputation`](../enums/reputation.md) (optional)

Describes whether a finding was useful or not-useful.

### `severityScore`

- Type: `uint32` (optional)

Severity score for a finding set by an analyst.

### `status`

- Type: [`Status`](../enums/status.md) (optional)

Describes the workflow status of a finding.

### `comments`

- Type: `string` (repeated)

Comment added by the Analyst.

### `priority`

- Type: [`Priority`](../enums/priority.md) (optional)

Priority of the Alert or Finding set by analyst.

### `rootCause`

- Type: `string` (optional)

Root cause of the Alert or Finding set by analyst.

### `reason`

- Type: [`Reason`](../enums/reason.md) (optional)

Reason for closing the Case or Alert.

### `riskScore`

- Type: `uint32` (optional)

Risk score for a finding set by an analyst.

### `id`

- Type: `string` (optional)

Identifier for the investigation
