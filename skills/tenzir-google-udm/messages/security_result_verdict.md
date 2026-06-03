# SecurityResult.Verdict

Deprecated. Encapsulates the threat verdict provided by human analysts and ML models. These fields are used to model Mandiant sources.

- **Full name**: `google.backstory.SecurityResult.Verdict`
- **Fields**: `5`

## Fields

### `source_count`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `sourceCount`

Number of sources from which intelligence was extracted.

### `response_count`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `responseCount`

Total response count across all sources.

### `neighbour_influence`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `neighbourInfluence`

Describes the neighbour influence of the verdict.

### `verdict`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: [`SecurityResult.ProviderMLVerdict`](security_result_provider_ml_verdict.md)
- **JSON name**: `verdict`

ML Verdict provided by sources like Mandiant.

### `analyst_verdict`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: [`SecurityResult.AnalystVerdict`](security_result_analyst_verdict.md)
- **JSON name**: `analystVerdict`

Human analyst verdict provided by sources like Mandiant.
