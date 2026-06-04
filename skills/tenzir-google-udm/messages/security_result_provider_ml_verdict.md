# ProviderMLVerdict

Deprecated. MLVerdict result provided from threat providers, like Mandiant. These fields are used to model Mandiant sources.

## Fields

### `sourceProvider`

- Type: `string` (singular)

Source provider giving the ML verdict.

### `benignCount`

- Type: `int32` (singular)

Count of responses where this IoC was marked benign.

### `maliciousCount`

- Type: `int32` (singular)

Count of responses where this IoC was marked malicious.

### `confidenceScore`

- Type: `int32` (singular)

Confidence score of the verdict.

### `mandiantSources`

- Type: [`Source`](security_result_source.md) (repeated)

List of mandiant sources from which the verdict was generated.

### `thirdPartySources`

- Type: [`Source`](security_result_source.md) (repeated)

List of third-party sources from which the verdict was generated.
