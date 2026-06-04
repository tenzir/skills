# FindingVariable

A structure that holds the value and associated metadata for values extracted while producing a Finding.

## Oneofs

- `typed_value`: `boolVal`, `bytesVal`, `doubleVal`, `int64Val`, `uint64Val`, `stringVal`, `timestampTime`, `nullVal`, `boolSeq`, `bytesSeq`, `doubleSeq`, `int64Seq`, `uint64Seq`, `stringSeq`

## Fields

### `type`

- Type: [`FindingVariable.Type`](../enums/finding_variable_type.md) (singular)

The type of the variable.

### `value`

- Type: `string` (singular)

The value in string form.

### `sourcePath`

- Type: `string` (singular)

The UDM field path for the field which this value was derived from. Example: `principal.user.username`

### `boolVal`

- Type: `bool` (singular)
- Oneof: `typed_value`

The value in boolean format.

### `bytesVal`

- Type: `bytes` (singular)
- Oneof: `typed_value`

The value in bytes format.

### `doubleVal`

- Type: `double` (singular)
- Oneof: `typed_value`

The value in double format.

### `int64Val`

- Type: `int64` (singular)
- Oneof: `typed_value`

The value in int64 format.

### `uint64Val`

- Type: `uint64` (singular)
- Oneof: `typed_value`

The value in uint64 format.

### `stringVal`

- Type: `string` (singular)
- Oneof: `typed_value`

The value in string format. Enum values are returned as strings.

### `timestampTime`

- Type: `timestamp` (singular)
- Oneof: `typed_value`

The value in timestamp format.

### `nullVal`

- Type: `bool` (singular)
- Oneof: `typed_value`

Whether the value is null.

### `boolSeq`

- Type: [`BoolSequence`](bool_sequence.md) (singular)
- Oneof: `typed_value`

The value in boolsequence format.

### `bytesSeq`

- Type: [`BytesSequence`](bytes_sequence.md) (singular)
- Oneof: `typed_value`

The value in bytessequence format.

### `doubleSeq`

- Type: [`DoubleSequence`](double_sequence.md) (singular)
- Oneof: `typed_value`

The value in doublesequence format.

### `int64Seq`

- Type: [`Int64Sequence`](int64_sequence.md) (singular)
- Oneof: `typed_value`

The value in int64sequence format.

### `uint64Seq`

- Type: [`Uint64Sequence`](uint64_sequence.md) (singular)
- Oneof: `typed_value`

The value in uint64sequence format.

### `stringSeq`

- Type: [`StringSequence`](string_sequence.md) (singular)
- Oneof: `typed_value`

The value in stringsequence format.
