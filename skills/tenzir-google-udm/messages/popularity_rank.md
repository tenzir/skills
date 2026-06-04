# PopularityRank

Domain's position in popularity ranks for sources such as Alexa, Quantcast, or Statvoo.

- **Full name**: `google.backstory.PopularityRank`
- **Fields**: `3`

## Fields

### `giver`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `giver`

Name of the rank serial number hexdump.

### `rank`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `rank`

Rank position.

### `ingestion_time`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp`
- **JSON name**: `ingestionTime`

Timestamp when the rank was ingested.
