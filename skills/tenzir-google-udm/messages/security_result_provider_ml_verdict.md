# SecurityResult.ProviderMLVerdict

Deprecated. MLVerdict result provided from threat providers, like Mandiant. These fields are used to model Mandiant sources.

- **Full name**: `google.backstory.SecurityResult.ProviderMLVerdict`
- **Fields**: `6`

## Fields

### `source_provider`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `sourceProvider`

Source provider giving the ML verdict.

### `benign_count`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `benignCount`

Count of responses where this IoC was marked benign.

### `malicious_count`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `maliciousCount`

Count of responses where this IoC was marked malicious.

### `confidence_score`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `confidenceScore`

Confidence score of the verdict.

### `mandiant_sources`

- **Number**: `5`
- **Cardinality**: `repeated`
- **Type**: [`SecurityResult.Source`](security_result_source.md)
- **JSON name**: `mandiantSources`

List of mandiant sources from which the verdict was generated.

### `third_party_sources`

- **Number**: `6`
- **Cardinality**: `repeated`
- **Type**: [`SecurityResult.Source`](security_result_source.md)
- **JSON name**: `thirdPartySources`

List of third-party sources from which the verdict was generated.
