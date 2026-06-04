# IoCStats

Information about the threat intelligence source. These fields are used to model Mandiant sources.

## Fields

### `ioc_stats_type` / `iocStatsType`

- Type: [`IoCStatsType`](../enums/security_result_io_c_stats_type.md) (singular)

Describes the source of the IoCStat.

### `first_level_source` / `firstLevelSource`

- Type: `string` (singular)

Name of first level IoC source, for example Mandiant or a third-party.

### `second_level_source` / `secondLevelSource`

- Type: `string` (singular)

Name of the second-level IoC source, for example Crowdsourced Threat Analysis or Knowledge Graph.

### `benign_count` / `benignCount`

- Type: `int32` (singular)

Count of responses where the IoC was identified as benign.

### `quality`

- Type: [`ProductConfidence`](../enums/security_result_product_confidence.md) (singular)

Level of confidence in the IoC mapping extracted from the source.

### `malicious_count` / `maliciousCount`

- Type: `int32` (singular)

Count of responses where the IoC was identified as malicious.

### `response_count` / `responseCount`

- Type: `int32` (singular)

Total number of response from the source.

### `source_count` / `sourceCount`

- Type: `int32` (singular)

Number of sources from which information was extracted.
