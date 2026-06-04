# SecurityResult.Verdict

Deprecated. Encapsulates the threat verdict provided by human analysts and ML models. These fields are used to model Mandiant sources.

## Fields

### `sourceCount`

- Type: `int32` (singular)

Number of sources from which intelligence was extracted.

### `responseCount`

- Type: `int32` (singular)

Total response count across all sources.

### `neighbourInfluence`

- Type: `string` (singular)

Describes the neighbour influence of the verdict.

### `verdict`

- Type: [`ProviderMLVerdict`](security_result_provider_ml_verdict.md) (singular)

ML Verdict provided by sources like Mandiant.

### `analystVerdict`

- Type: [`AnalystVerdict`](security_result_analyst_verdict.md) (singular)

Human analyst verdict provided by sources like Mandiant.
