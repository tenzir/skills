# Dns

DNS information.

- **Full name**: `google.backstory.Dns`
- **Fields**: `12`
- **Nested messages**: `2`

## Nested messages

- [Dns.Question](dns_question.md)
- [Dns.ResourceRecord](dns_resource_record.md)

## Fields

### `id`

- **Number**: `6`
- **Cardinality**: `singular`
- **Type**: `uint32`
- **JSON name**: `id`

DNS query id.

### `response`

- **Number**: `7`
- **Cardinality**: `singular`
- **Type**: `bool`
- **JSON name**: `response`

Set to true if the event is a DNS response. See QR field from RFC1035.

### `opcode`

- **Number**: `8`
- **Cardinality**: `singular`
- **Type**: `uint32`
- **JSON name**: `opcode`

The DNS OpCode used to specify the type of DNS query (for example, QUERY, IQUERY, or STATUS).

### `authoritative`

- **Number**: `9`
- **Cardinality**: `singular`
- **Type**: `bool`
- **JSON name**: `authoritative`

Other DNS header flags. See RFC1035, section 4.1.1.

### `truncated`

- **Number**: `10`
- **Cardinality**: `singular`
- **Type**: `bool`
- **JSON name**: `truncated`

Whether the DNS response was truncated.

### `recursion_desired`

- **Number**: `11`
- **Cardinality**: `singular`
- **Type**: `bool`
- **JSON name**: `recursionDesired`

Whether a recursive DNS lookup is desired.

### `recursion_available`

- **Number**: `12`
- **Cardinality**: `singular`
- **Type**: `bool`
- **JSON name**: `recursionAvailable`

Whether a recursive DNS lookup is available.

### `response_code`

- **Number**: `13`
- **Cardinality**: `singular`
- **Type**: `uint32`
- **JSON name**: `responseCode`

Response code. See RCODE from RFC1035.

### `questions`

- **Number**: `1`
- **Cardinality**: `repeated`
- **Type**: [`Dns.Question`](dns_question.md)
- **JSON name**: `questions`

A list of domain protocol message questions.

### `answers`

- **Number**: `2`
- **Cardinality**: `repeated`
- **Type**: [`Dns.ResourceRecord`](dns_resource_record.md)
- **JSON name**: `answers`

A list of answers to the domain name query.

### `authority`

- **Number**: `3`
- **Cardinality**: `repeated`
- **Type**: [`Dns.ResourceRecord`](dns_resource_record.md)
- **JSON name**: `authority`

A list of domain name servers which verified the answers to the domain name queries.

### `additional`

- **Number**: `4`
- **Cardinality**: `repeated`
- **Type**: [`Dns.ResourceRecord`](dns_resource_record.md)
- **JSON name**: `additional`

A list of additional domain name servers that can be used to verify the answer to the domain.
