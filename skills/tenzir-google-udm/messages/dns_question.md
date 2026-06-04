# Dns.Question

DNS Questions. See RFC1035, section 4.1.2.

- **Full name**: `google.backstory.Dns.Question`
- **Fields**: `4`

## Fields

### `name`

- Type: `string` (singular)

The domain name.

### `type`

- Type: `uint32` (singular)

The code specifying the type of the query.

### `class`

- Type: `uint32` (singular)

The code specifying the class of the query.

### `prevalence`

- Type: [`Prevalence`](prevalence.md) (singular)

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
