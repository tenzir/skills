# Source

Deprecated. Information about the threat intelligence source. These fields are used to model Mandiant sources.

## Fields

### `name`

- Type: `string` (singular)

Name of the IoC source.

### `benign_count` / `benignCount`

- Type: `int32` (singular)

Count of responses where this IoC was marked benign.

### `malicious_count` / `maliciousCount`

- Type: `int32` (singular)

Count of responses where this IoC was marked malicious.

### `quality`

- Type: [`ProductConfidence`](../enums/security_result_product_confidence.md) (singular)

Quality of the IoC mapping extracted from the source.

### `response_count` / `responseCount`

- Type: `int32` (singular)

Total response count from this source.

### `source_count` / `sourceCount`

- Type: `int32` (singular)

Number of sources from which intelligence was extracted.

### `threat_intelligence_sources` / `threatIntelligenceSources`

- Type: [`Source`](security_result_source.md) (repeated)

Different threat intelligence sources from which IoC info was extracted.
