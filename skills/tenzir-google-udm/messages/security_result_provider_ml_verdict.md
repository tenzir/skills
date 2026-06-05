# ProviderMLVerdict

Deprecated. MLVerdict result provided from threat providers, like Mandiant. These fields are used to model Mandiant sources.

## Fields

### `source_provider` / `sourceProvider`

- Type: `string` (singular)

Source provider giving the ML verdict.

### `benign_count` / `benignCount`

- Type: `int32` (singular)

Count of responses where this IoC was marked benign.

### `malicious_count` / `maliciousCount`

- Type: `int32` (singular)

Count of responses where this IoC was marked malicious.

### `confidence_score` / `confidenceScore`

- Type: `int32` (singular)

Confidence score of the verdict.

### `mandiant_sources` / `mandiantSources`

- Type: [`Source`](security_result_source.md) (repeated)

List of mandiant sources from which the verdict was generated.

### `third_party_sources` / `thirdPartySources`

- Type: [`Source`](security_result_source.md) (repeated)

List of third-party sources from which the verdict was generated.
