# DNSRecord

DNS record.

- **Full name**: `google.backstory.DNSRecord`
- **Fields**: `10`

## Fields

### `type`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `type`

Type.

### `value`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `value`

Value.

### `ttl`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Duration` (imported)
- **JSON name**: `ttl`

Time to live.

### `priority`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `priority`

Priority.

### `retry`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `retry`

Retry.

### `refresh`

- **Number**: `6`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Duration` (imported)
- **JSON name**: `refresh`

Refresh.

### `minimum`

- **Number**: `7`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Duration` (imported)
- **JSON name**: `minimum`

Minimum.

### `expire`

- **Number**: `8`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Duration` (imported)
- **JSON name**: `expire`

Expire.

### `serial`

- **Number**: `9`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `serial`

Serial.

### `rname`

- **Number**: `10`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `rname`

Rname.
