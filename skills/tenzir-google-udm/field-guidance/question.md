# Question Field Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`

## Schema

- [Dns.Question](../messages/dns_question.md)

## Fields

### `Question.class`

- **Purpose**: Stores the code specifying the class of the query.
- **Encoding**: 32-bit integer.

### `Question.name`

- **Purpose**: Stores the domain name.
- **Encoding**: String.

### `Question.type`

- **Purpose**: Stores the code specifying the type of the query.
- **Encoding**: 32-bit integer.
