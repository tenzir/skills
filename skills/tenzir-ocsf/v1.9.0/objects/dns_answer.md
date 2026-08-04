# DNS Answer (dns_answer)

The DNS Answer object represents a specific response provided by the Domain Name System (DNS) when querying for information about a domain or performing a DNS operation. It encapsulates the relevant details and data returned by the DNS server in response to a query.

- **Extends**: [DNS Resource Record (dns_resource_record)](dns_resource_record.md)

## Attributes

### `flag_ids`

- **Type**: `integer_t`
- **Requirement**: recommended
- **Sibling**: `flags`

#### Enum values

- `1`: `Authoritative Answer`
- `2`: `Truncated Response`
- `3`: `Recursion Desired`
- `4`: `Recursion Available`
- `5`: `Authentic Data`
- `6`: `Checking Disabled`

The list of DNS answer header flag IDs.

### `flags`

- **Type**: `string_t`
- **Requirement**: optional

The list of DNS answer header flags.

### `packet_uid`

- **Type**: `integer_t`
- **Requirement**: recommended

The DNS packet identifier assigned by the program that generated the query. The identifier is copied to the response.
