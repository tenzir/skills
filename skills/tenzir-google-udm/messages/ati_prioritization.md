# AtiPrioritization

AtiPrioritization contains various fields used to calculate a priority score for an entity identified as a threat.

## Fields

### `gtiVerdict`

- Type: `int32` (singular)

The confidence score from "GTI verdict" source.

### `gtiSeverity`

- Type: `int32` (singular)

The confidence score from "GTI severity" source.

### `gtiThreatScore`

- Type: `int32` (singular)

The confidence score from "GTI threat score" source.

### `mandiantAnalystConfidence`

- Type: `int32` (singular)

The confidence score from "Mandiant Analyst Intel" source.

### `gtiUpdateTime`

- Type: `google.protobuf.Timestamp` (singular)

Timestamp of the latest update for GTI verdict, severity, or threat score.

### `activeIr`

- Type: `bool` (singular)

Whether one or more Mandiant incident response customers had this indicator in their environment.

### `activeIrFirstTaggedTime`

- Type: `google.protobuf.Timestamp` (singular)

The timestamp of the first time an active IR was applied to this entity.

### `globalCustomerCount`

- Type: `int64` (singular)

Global customer count over the last 30 days

### `globalHitCount`

- Type: `int64` (singular)

Global hit count over the last 30 days

### `exclusive`

- Type: `bool` (singular)

Whether the indicator is being used by a maximum of one threat actor.

### `osint`

- Type: `bool` (singular)

Whether the indicator details are available in open source.

### `scanner`

- Type: `bool` (singular)

Whether the indicator is a scanner.

### `reviewed`

- Type: `bool` (singular)

Whether the indicator verdict has passed review.

### `attributedMalware`

- Type: [`Association`](security_result_association.md) (repeated)

Malware families associated with this indicator.

### `attributedThreatActors`

- Type: [`Association`](security_result_association.md) (repeated)

Threat actors associated with this indicator.
