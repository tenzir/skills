# FindingVariable

A structure that holds the value and associated metadata for values extracted while producing a Finding.

- **Full name**: `google.backstory.FindingVariable`
- **Fields**: `17`
- **Nested enums**: `1`

## Nested enums

- [FindingVariable.Type](../enums/finding_variable_type.md)

## Oneofs

- `typed_value`: `bool_val`, `bytes_val`, `double_val`, `int64_val`, `uint64_val`, `string_val`, `timestamp_time`, `null_val`, `bool_seq`, `bytes_seq`, `double_seq`, `int64_seq`, `uint64_seq`, `string_seq`

## Fields

### `type`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: [`FindingVariable.Type`](../enums/finding_variable_type.md)
- **JSON name**: `type`

The type of the variable.

### `value`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `value`

The value in string form.

### `source_path`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `sourcePath`

The UDM field path for the field which this value was derived from. Example: `principal.user.username`

### `bool_val`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: `bool`
- **JSON name**: `boolVal`
- **Oneof**: `typed_value`

The value in boolean format.

### `bytes_val`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: `bytes`
- **JSON name**: `bytesVal`
- **Oneof**: `typed_value`

The value in bytes format.

### `double_val`

- **Number**: `6`
- **Cardinality**: `singular`
- **Type**: `double`
- **JSON name**: `doubleVal`
- **Oneof**: `typed_value`

The value in double format.

### `int64_val`

- **Number**: `7`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `int64Val`
- **Oneof**: `typed_value`

The value in int64 format.

### `uint64_val`

- **Number**: `8`
- **Cardinality**: `singular`
- **Type**: `uint64`
- **JSON name**: `uint64Val`
- **Oneof**: `typed_value`

The value in uint64 format.

### `string_val`

- **Number**: `9`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `stringVal`
- **Oneof**: `typed_value`

The value in string format. Enum values are returned as strings.

### `timestamp_time`

- **Number**: `17`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp`
- **JSON name**: `timestampTime`
- **Oneof**: `typed_value`

The value in timestamp format.

### `null_val`

- **Number**: `10`
- **Cardinality**: `singular`
- **Type**: `bool`
- **JSON name**: `nullVal`
- **Oneof**: `typed_value`

Whether the value is null.

### `bool_seq`

- **Number**: `11`
- **Cardinality**: `singular`
- **Type**: [`BoolSequence`](bool_sequence.md)
- **JSON name**: `boolSeq`
- **Oneof**: `typed_value`

The value in boolsequence format.

### `bytes_seq`

- **Number**: `12`
- **Cardinality**: `singular`
- **Type**: [`BytesSequence`](bytes_sequence.md)
- **JSON name**: `bytesSeq`
- **Oneof**: `typed_value`

The value in bytessequence format.

### `double_seq`

- **Number**: `13`
- **Cardinality**: `singular`
- **Type**: [`DoubleSequence`](double_sequence.md)
- **JSON name**: `doubleSeq`
- **Oneof**: `typed_value`

The value in doublesequence format.

### `int64_seq`

- **Number**: `14`
- **Cardinality**: `singular`
- **Type**: [`Int64Sequence`](int64_sequence.md)
- **JSON name**: `int64Seq`
- **Oneof**: `typed_value`

The value in int64sequence format.

### `uint64_seq`

- **Number**: `15`
- **Cardinality**: `singular`
- **Type**: [`Uint64Sequence`](uint64_sequence.md)
- **JSON name**: `uint64Seq`
- **Oneof**: `typed_value`

The value in uint64sequence format.

### `string_seq`

- **Number**: `16`
- **Cardinality**: `singular`
- **Type**: [`StringSequence`](string_sequence.md)
- **JSON name**: `stringSeq`
- **Oneof**: `typed_value`

The value in stringsequence format.
