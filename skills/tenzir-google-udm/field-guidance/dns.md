# Dns Field Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`

## Schema

- [Dns](../messages/dns.md)

## Fields

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

### `Dns.recursion_available`

- **Purpose**: Set to true if a recursive DNS lookup is available.
- **Encoding**: Boolean.

### `Dns.recursion_desired`

- **Purpose**: Set to true if a recursive DNS lookup is requested.
- **Encoding**: Boolean.

### `Dns.response`

- **Purpose**: Set to true if the event is a DNS response.
- **Encoding**: Boolean.

### `Dns.response_code`

- **Purpose**: Stores the DNS response code as defined by RFC 1035, Domain Names - Implementation and Specification.
- **Encoding**: 32-bit integer.

### `Dns.truncated`

- **Purpose**: Set to true if this is a truncated DNS response.
- **Encoding**: Boolean.
