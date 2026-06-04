# FindingVariable

A structure that holds the value and associated metadata for values extracted while producing a Finding.

## Oneofs

- `typed_value`: `bool_val` / `boolVal`, `bytes_val` / `bytesVal`, `double_val` / `doubleVal`, `int64_val` / `int64Val`, `uint64_val` / `uint64Val`, `string_val` / `stringVal`, `timestamp_time` / `timestampTime`, `null_val` / `nullVal`, `bool_seq` / `boolSeq`, `bytes_seq` / `bytesSeq`, `double_seq` / `doubleSeq`, `int64_seq` / `int64Seq`, `uint64_seq` / `uint64Seq`, `string_seq` / `stringSeq`

## Fields

### `type`

- Type: [`FindingVariable.Type`](../enums/finding_variable_type.md) (singular)

The type of the variable.

### `value`

- Type: `string` (singular)

The value in string form.

### `source_path` / `sourcePath`

- Type: `string` (singular)

The UDM field path for the field which this value was derived from. Example: `principal.user.username`

### `bool_val` / `boolVal`

- Type: `bool` (singular)
- Oneof: `typed_value`

The value in boolean format.

### `bytes_val` / `bytesVal`

- Type: `bytes` (singular)
- Oneof: `typed_value`

The value in bytes format.

### `double_val` / `doubleVal`

- Type: `double` (singular)
- Oneof: `typed_value`

The value in double format.

### `int64_val` / `int64Val`

- Type: `int64` (singular)
- Oneof: `typed_value`

The value in int64 format.

### `uint64_val` / `uint64Val`

- Type: `uint64` (singular)
- Oneof: `typed_value`

The value in uint64 format.

### `string_val` / `stringVal`

- Type: `string` (singular)
- Oneof: `typed_value`

The value in string format. Enum values are returned as strings.

### `timestamp_time` / `timestampTime`

- Type: `timestamp` (singular)
- Oneof: `typed_value`

The value in timestamp format.

### `null_val` / `nullVal`

- Type: `bool` (singular)
- Oneof: `typed_value`

Whether the value is null.

### `bool_seq` / `boolSeq`

- Type: [`BoolSequence`](bool_sequence.md) (singular)
- Oneof: `typed_value`

The value in boolsequence format.

### `bytes_seq` / `bytesSeq`

- Type: [`BytesSequence`](bytes_sequence.md) (singular)
- Oneof: `typed_value`

The value in bytessequence format.

### `double_seq` / `doubleSeq`

- Type: [`DoubleSequence`](double_sequence.md) (singular)
- Oneof: `typed_value`

The value in doublesequence format.

### `int64_seq` / `int64Seq`

- Type: [`Int64Sequence`](int64_sequence.md) (singular)
- Oneof: `typed_value`

The value in int64sequence format.

### `uint64_seq` / `uint64Seq`

- Type: [`Uint64Sequence`](uint64_sequence.md) (singular)
- Oneof: `typed_value`

The value in uint64sequence format.

### `string_seq` / `stringSeq`

- Type: [`StringSequence`](string_sequence.md) (singular)
- Oneof: `typed_value`

The value in stringsequence format.
