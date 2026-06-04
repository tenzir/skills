# AtiPrioritization

AtiPrioritization contains various fields used to calculate a priority score for an entity identified as a threat.

## Fields

### `gti_verdict` / `gtiVerdict`

- Type: `int32` (singular)

The confidence score from "GTI verdict" source.

### `gti_severity` / `gtiSeverity`

- Type: `int32` (singular)

The confidence score from "GTI severity" source.

### `gti_threat_score` / `gtiThreatScore`

- Type: `int32` (singular)

The confidence score from "GTI threat score" source.

### `mandiant_analyst_confidence` / `mandiantAnalystConfidence`

- Type: `int32` (singular)

The confidence score from "Mandiant Analyst Intel" source.

### `gti_update_time` / `gtiUpdateTime`

- Type: `timestamp` (singular)

Timestamp of the latest update for GTI verdict, severity, or threat score.

### `active_ir` / `activeIr`

- Type: `bool` (singular)

Whether one or more Mandiant incident response customers had this indicator in their environment.

### `active_ir_first_tagged_time` / `activeIrFirstTaggedTime`

- Type: `timestamp` (singular)

The timestamp of the first time an active IR was applied to this entity.

### `global_customer_count` / `globalCustomerCount`

- Type: `int64` (singular)

Global customer count over the last 30 days

### `global_hit_count` / `globalHitCount`

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

### `attributed_malware` / `attributedMalware`

- Type: [`Association`](security_result_association.md) (repeated)

Malware families associated with this indicator.

### `attributed_threat_actors` / `attributedThreatActors`

- Type: [`Association`](security_result_association.md) (repeated)

Threat actors associated with this indicator.
