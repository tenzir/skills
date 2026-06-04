# UDM

A Unified Data Model event.

- **Full name**: `google.backstory.UDM`
- **Fields**: `13`

## Fields

### `metadata`

- Type: [`Metadata`](metadata.md) (singular)

Event metadata such as timestamp, source product, etc.

### `additional`

- Type: `google.protobuf.Struct` (singular)

Any important vendor-specific event data that cannot be adequately represented within the formal sections of the UDM model.

### `principal`

- Type: [`Noun`](noun.md) (singular)

Represents the acting entity that originates the activity described in the event. The principal must include at least one machine detail (hostname, MACs, IPs, port, product-specific identifiers like an EDR asset ID) or user detail (for example, username), and optionally include process details. It must NOT include any of the following fields: email, files, registry keys or values.

### `src`

- Type: [`Noun`](noun.md) (singular)

Represents a source entity being acted upon by the participant along with the device or process context for the source object (the machine where the source object resides). For example, if user U copies file A on machine X to file B on machine Y, both file A and machine X would be specified in the src portion of the UDM event.

### `target`

- Type: [`Noun`](noun.md) (singular)

Represents a target entity being referenced by the event or an object on the target entity. For example, in a firewall connection from device A to device B, A is described as the principal and B is described as the target. For a process injection by process C into target process D, process C is described as the principal and process D is described as the target.

### `intermediary`

- Type: [`Noun`](noun.md) (repeated)

Represents details on one or more intermediate entities processing activity described in the event. This includes device details about a proxy server or SMTP relay server. If an active event (that has a principal and possibly target) passes through any intermediaries, they're added here. Intermediaries can impact the overall action, for example blocking or modifying an ongoing request. A rule of thumb here is that 'principal', 'target', and description of the initial action should be the same regardless of the intermediary or its action. A successful network connection from A->B should look the same in principal/target/intermediary as one blocked by firewall C: principal: A, target: B (intermediary: C).

### `observer`

- Type: [`Noun`](noun.md) (singular)

Represents an observer entity (for example, a packet sniffer or network-based vulnerability scanner), which is not a direct intermediary, but which observes and reports on the event in question.

### `about`

- Type: [`Noun`](noun.md) (repeated)

Represents entities referenced by the event that are not otherwise described in principal, src, target, intermediary or observer. For example, it could be used to track email file attachments, domains/URLs/IPs embedded within an email body, and DLLs that are loaded during a PROCESS_LAUNCH event.

### `securityResult`

- Type: [`SecurityResult`](security_result.md) (repeated)

A list of security results.

### `network`

- Type: [`Network`](network.md) (singular)

All network details go here, including sub-messages with details on each protocol (for example, DHCP, DNS, or HTTP).

### `extensions`

- Type: [`Extensions`](extensions.md) (singular)

All other first-class, event-specific metadata goes in this message. Do not place protocol metadata in Extensions; put it in Network.

### `extracted`

- Type: `google.protobuf.Struct` (singular)

Flattened fields extracted from the log.

### `grouped`

- Type: [`GroupedFields`](grouped_fields.md) (optional)

Related UDM fields that are grouped together.
