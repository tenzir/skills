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

- Type: `uint32` (singular)

DNS query id.

### `response`

- Type: `bool` (singular)

Set to true if the event is a DNS response. See QR field from RFC1035.

### `opcode`

- Type: `uint32` (singular)

The DNS OpCode used to specify the type of DNS query (for example, QUERY, IQUERY, or STATUS).

### `authoritative`

- Type: `bool` (singular)

Other DNS header flags. See RFC1035, section 4.1.1.

### `truncated`

- Type: `bool` (singular)

Whether the DNS response was truncated.

### `recursionDesired`

- Type: `bool` (singular)

Whether a recursive DNS lookup is desired.

### `recursionAvailable`

- Type: `bool` (singular)

Whether a recursive DNS lookup is available.

### `responseCode`

- Type: `uint32` (singular)

Response code. See RCODE from RFC1035.

### `questions`

- Type: [`Dns.Question`](dns_question.md) (repeated)

A list of domain protocol message questions.

### `answers`

- Type: [`Dns.ResourceRecord`](dns_resource_record.md) (repeated)

A list of answers to the domain name query.

### `authority`

- Type: [`Dns.ResourceRecord`](dns_resource_record.md) (repeated)

A list of domain name servers which verified the answers to the domain name queries.

### `additional`

- Type: [`Dns.ResourceRecord`](dns_resource_record.md) (repeated)

A list of additional domain name servers that can be used to verify the answer to the domain.

## Guidance

Population guidance from the Google UDM usage guide.

### `Dns.additional`

- **Purpose**: Stores the additional domain name servers that can be used to verify the answer to the domain. See Population of DNS Resource Record metadata.

### `Dns.answers`

- **Purpose**: Stores the answer to the domain name query. See Population of DNS Resource Record metadata.

### `Dns.authoritative`

- **Purpose**: Set to true for authoritative DNS servers.
- **Encoding**: Boolean.

### `Dns.authority`

- **Purpose**: Stores the domain name servers that verified the answer to the domain name query. See Population of DNS Resource Record metadata.

### `Dns.id`

- **Purpose**: Stores the DNS query identifier.
- **Encoding**: 32-bit integer.

### `Dns.opcode`

- **Purpose**: Stores the DNS OpCode used to specify the type of DNS query (standard, inverse, server status, etc.).
- **Encoding**: 32-bit integer.

### `Dns.questions`

- **Purpose**: Stores the domain protocol message questions. See Population of DNS Question metadata.

### `Dns.recursionAvailable`

- **Purpose**: Set to true if a recursive DNS lookup is available.
- **Encoding**: Boolean.

### `Dns.recursionDesired`

- **Purpose**: Set to true if a recursive DNS lookup is requested.
- **Encoding**: Boolean.

### `Dns.response`

- **Purpose**: Set to true if the event is a DNS response.
- **Encoding**: Boolean.

### `Dns.responseCode`

- **Purpose**: Stores the DNS response code as defined by RFC 1035, Domain Names - Implementation and Specification.
- **Encoding**: 32-bit integer.

### `Dns.truncated`

- **Purpose**: Set to true if this is a truncated DNS response.
- **Encoding**: Boolean.
