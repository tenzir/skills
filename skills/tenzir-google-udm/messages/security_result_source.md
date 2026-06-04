# SecurityResult.Source

Deprecated. Information about the threat intelligence source. These fields are used to model Mandiant sources.

- **Full name**: `google.backstory.SecurityResult.Source`
- **Fields**: `7`

## Fields

### `name`

- Type: `string` (singular)

Name of the IoC source.

### `benignCount`

- Type: `int32` (singular)

Count of responses where this IoC was marked benign.

### `maliciousCount`

- Type: `int32` (singular)

Count of responses where this IoC was marked malicious.

### `quality`

- Type: [`SecurityResult.ProductConfidence`](../enums/security_result_product_confidence.md) (singular)

Quality of the IoC mapping extracted from the source.

### `responseCount`

- Type: `int32` (singular)

Total response count from this source.

### `sourceCount`

- Type: `int32` (singular)

Number of sources from which intelligence was extracted.

### `threatIntelligenceSources`

- Type: [`SecurityResult.Source`](security_result_source.md) (repeated)

Different threat intelligence sources from which IoC info was extracted.
