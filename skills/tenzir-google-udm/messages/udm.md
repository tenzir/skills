# UDM

A Unified Data Model event.

- **Full name**: `google.backstory.UDM`
- **Fields**: `13`

## Fields

### `metadata`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: [`Metadata`](metadata.md)
- **JSON name**: `metadata`

Event metadata such as timestamp, source product, etc.

### `additional`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Struct`
- **JSON name**: `additional`

Any important vendor-specific event data that cannot be adequately represented within the formal sections of the UDM model.

### `principal`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: [`Noun`](noun.md)
- **JSON name**: `principal`

Represents the acting entity that originates the activity described in the event. The principal must include at least one machine detail (hostname, MACs, IPs, port, product-specific identifiers like an EDR asset ID) or user detail (for example, username), and optionally include process details. It must NOT include any of the following fields: email, files, registry keys or values.

### `src`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: [`Noun`](noun.md)
- **JSON name**: `src`

Represents a source entity being acted upon by the participant along with the device or process context for the source object (the machine where the source object resides). For example, if user U copies file A on machine X to file B on machine Y, both file A and machine X would be specified in the src portion of the UDM event.

### `target`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: [`Noun`](noun.md)
- **JSON name**: `target`

Represents a target entity being referenced by the event or an object on the target entity. For example, in a firewall connection from device A to device B, A is described as the principal and B is described as the target. For a process injection by process C into target process D, process C is described as the principal and process D is described as the target.

### `intermediary`

- **Number**: `6`
- **Cardinality**: `repeated`
- **Type**: [`Noun`](noun.md)
- **JSON name**: `intermediary`

Represents details on one or more intermediate entities processing activity described in the event. This includes device details about a proxy server or SMTP relay server. If an active event (that has a principal and possibly target) passes through any intermediaries, they're added here. Intermediaries can impact the overall action, for example blocking or modifying an ongoing request. A rule of thumb here is that 'principal', 'target', and description of the initial action should be the same regardless of the intermediary or its action. A successful network connection from A->B should look the same in principal/target/intermediary as one blocked by firewall C: principal: A, target: B (intermediary: C).

### `observer`

- **Number**: `7`
- **Cardinality**: `singular`
- **Type**: [`Noun`](noun.md)
- **JSON name**: `observer`

Represents an observer entity (for example, a packet sniffer or network-based vulnerability scanner), which is not a direct intermediary, but which observes and reports on the event in question.

### `about`

- **Number**: `8`
- **Cardinality**: `repeated`
- **Type**: [`Noun`](noun.md)
- **JSON name**: `about`

Represents entities referenced by the event that are not otherwise described in principal, src, target, intermediary or observer. For example, it could be used to track email file attachments, domains/URLs/IPs embedded within an email body, and DLLs that are loaded during a PROCESS_LAUNCH event.

### `security_result`

- **Number**: `9`
- **Cardinality**: `repeated`
- **Type**: [`SecurityResult`](security_result.md)
- **JSON name**: `securityResult`

A list of security results.

### `network`

- **Number**: `10`
- **Cardinality**: `singular`
- **Type**: [`Network`](network.md)
- **JSON name**: `network`

All network details go here, including sub-messages with details on each protocol (for example, DHCP, DNS, or HTTP).

### `extensions`

- **Number**: `11`
- **Cardinality**: `singular`
- **Type**: [`Extensions`](extensions.md)
- **JSON name**: `extensions`

All other first-class, event-specific metadata goes in this message. Do not place protocol metadata in Extensions; put it in Network.

### `extracted`

- **Number**: `12`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Struct`
- **JSON name**: `extracted`

Flattened fields extracted from the log.

### `grouped`

- **Number**: `13`
- **Cardinality**: `optional`
- **Type**: [`GroupedFields`](grouped_fields.md)
- **JSON name**: `grouped`

Related UDM fields that are grouped together.
