# Dns.ResourceRecord

DNS Resource Records. See RFC1035, section 4.1.3.

- **Full name**: `google.backstory.Dns.ResourceRecord`
- **Fields**: `6`

## Fields

### `name`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `name`

The name of the owner of the resource record.

### `type`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `uint32`
- **JSON name**: `type`

The code specifying the type of the resource record.

### `class`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `uint32`
- **JSON name**: `class`

The code specifying the class of the resource record.

### `ttl`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: `uint32`
- **JSON name**: `ttl`

The time interval for which the resource record can be cached before the source of the information should again be queried.

### `data`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `data`

The payload or response to the DNS question for all responses encoded in UTF-8 format

### `binary_data`

- **Number**: `6`
- **Cardinality**: `singular`
- **Type**: `bytes`
- **JSON name**: `binaryData`

The raw bytes of any non-UTF8 strings that might be included as part of a DNS response.
