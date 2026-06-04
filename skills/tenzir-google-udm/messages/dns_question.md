# Dns.Question

DNS Questions. See RFC1035, section 4.1.2.

- **Full name**: `google.backstory.Dns.Question`
- **Fields**: `4`

## Fields

### `name`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `name`

The domain name.

### `type`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `uint32`
- **JSON name**: `type`

The code specifying the type of the query.

### `class`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `uint32`
- **JSON name**: `class`

The code specifying the class of the query.

### `prevalence`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: [`Prevalence`](prevalence.md)
- **JSON name**: `prevalence`

The prevalence of the domain within the customer's environment.

## Guidance

Population guidance from the Google UDM usage guide.

### `Question.class`

- **Purpose**: Stores the code specifying the class of the query.
- **Encoding**: 32-bit integer.

### `Question.name`

- **Purpose**: Stores the domain name.
- **Encoding**: String.

### `Question.type`

- **Purpose**: Stores the code specifying the type of the query.
- **Encoding**: 32-bit integer.
