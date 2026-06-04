# AtiPrioritization

AtiPrioritization contains various fields used to calculate a priority score for an entity identified as a threat.

- **Full name**: `google.backstory.AtiPrioritization`
- **Fields**: `15`

## Fields

### `gti_verdict`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `gtiVerdict`

The confidence score from "GTI verdict" source.

### `gti_severity`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `gtiSeverity`

The confidence score from "GTI severity" source.

### `gti_threat_score`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `gtiThreatScore`

The confidence score from "GTI threat score" source.

### `mandiant_analyst_confidence`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `mandiantAnalystConfidence`

The confidence score from "Mandiant Analyst Intel" source.

### `gti_update_time`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp`
- **JSON name**: `gtiUpdateTime`

Timestamp of the latest update for GTI verdict, severity, or threat score.

### `active_ir`

- **Number**: `6`
- **Cardinality**: `singular`
- **Type**: `bool`
- **JSON name**: `activeIr`

Whether one or more Mandiant incident response customers had this indicator in their environment.

### `active_ir_first_tagged_time`

- **Number**: `7`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp`
- **JSON name**: `activeIrFirstTaggedTime`

The timestamp of the first time an active IR was applied to this entity.

### `global_customer_count`

- **Number**: `8`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `globalCustomerCount`

Global customer count over the last 30 days

### `global_hit_count`

- **Number**: `9`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `globalHitCount`

Global hit count over the last 30 days

### `exclusive`

- **Number**: `10`
- **Cardinality**: `singular`
- **Type**: `bool`
- **JSON name**: `exclusive`

Whether the indicator is being used by a maximum of one threat actor.

### `osint`

- **Number**: `11`
- **Cardinality**: `singular`
- **Type**: `bool`
- **JSON name**: `osint`

Whether the indicator details are available in open source.

### `scanner`

- **Number**: `12`
- **Cardinality**: `singular`
- **Type**: `bool`
- **JSON name**: `scanner`

Whether the indicator is a scanner.

### `reviewed`

- **Number**: `13`
- **Cardinality**: `singular`
- **Type**: `bool`
- **JSON name**: `reviewed`

Whether the indicator verdict has passed review.

### `attributed_malware`

- **Number**: `14`
- **Cardinality**: `repeated`
- **Type**: [`SecurityResult.Association`](security_result_association.md)
- **JSON name**: `attributedMalware`

Malware families associated with this indicator.

### `attributed_threat_actors`

- **Number**: `15`
- **Cardinality**: `repeated`
- **Type**: [`SecurityResult.Association`](security_result_association.md)
- **JSON name**: `attributedThreatActors`

Threat actors associated with this indicator.
