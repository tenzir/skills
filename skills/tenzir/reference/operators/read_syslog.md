---
title: "read_syslog"
canonical: https://tenzir.com/docs/v7.0.0/reference/operators/read_syslog
source: https://tenzir.com/docs/v7.0.0/reference/operators/read_syslog.md
section: "Docs"
---

# read_syslog

> Parses an incoming Syslog stream into events.

Parses an incoming Syslog stream into events.

```tql
read_syslog [accept_pri_only=bool, raw_message=field, merge=bool, raw=bool, schema=string, selector=string, schema_only=bool, unflatten_separator=string]
```

## Description

[Syslog](https://en.wikipedia.org/wiki/Syslog) is a standard format for message logging.

Tenzir supports reading syslog messages in both the standardized “Syslog Protocol” format ([RFC 5424](https://tools.ietf.org/html/rfc5424)), and the older “BSD syslog Protocol” format ([RFC 3164](https://tools.ietf.org/html/rfc3164)).

It also accepts common Check Point structured-data variants, including `key:"value"` parameters, semicolon separators, and messages with no SD-ID.

Depending on the syslog format, the result can be different. Here’s an example of a syslog message in RFC 5424 format:

```plaintext
<165>8 2023-10-11T22:14:15.003Z mymachineexamplecom evntslog 1370 ID47 [exampleSDID@32473 eventSource="Application" eventID="1011"] Event log entry
```

With this input, the parser will produce the following output, with the schema name `syslog.rfc5424`:

```tql
{
  input: "<165>8 2023-10-11T22:14:15.003Z mymachineexamplecom evntslog 1370 ID47 [exampleSDID@32473 eventSource=\"Application\" eventID=\"1011\"] Event log entry",
  output: {
    facility: 20,
    severity: 5,
    version: 8,
    timestamp: 2023-10-11T22:14:15.003Z,
    hostname: "mymachineexamplecom",
    app_name: "evntslog",
    process_id: "1370",
    message_id: "ID47",
    structured_data: {
      "exampleSDID@32473": {
        eventSource: "Application",
        eventID: 1011,
      },
    },
    message: "Event log entry",
  },
}
```

Here’s an example of a syslog message in RFC 3164 format:

```plaintext
<34>Nov 16 14:55:56 mymachine PROGRAM: Freeform message
```

With this input, the parser will produce the following output, with the schema name `syslog.rfc3164`:

```json
{
  "facility": 4,
  "severity": 2,
  "timestamp": "Nov 16 14:55:56",
  "hostname": "mymachine",
  "app_name": "PROGRAM",
  "process_id": null,
  "content": "Freeform message"
}
```

RFC 3164 timestamps don’t include a year or time zone, so `read_syslog` keeps the timestamp as a string. Use [`parse_time`](https://tenzir.com/docs/v7.0.0/reference/functions/parse_time.md) with `reference` to convert it to a timestamp, and with `timezone` to interpret it in the sender’s time zone. See [`parse_time`](https://tenzir.com/docs/v7.0.0/reference/functions/parse_time.md) for examples with fixed references and per-event time zones.

Pipeline

```tql
from_file "syslog.txt" {
  read_syslog
}
timestamp = timestamp.parse_time("%b %e %H:%M:%S", reference=now())
```

If you know the time zone of each sender, look it up per event, for example from a record that maps hostnames to time zones. Daylight saving time is taken into account. The lookup yields null and a warning for an unknown hostname, in which case `parse_time` interprets the timestamp as UTC:

Pipeline

```tql
let $zones = {
  mymachine: "Europe/Berlin",
  othermachine: "America/New_York",
}
from_file "syslog.txt" {
  read_syslog
}
timestamp = timestamp.parse_time(
  "%b %e %H:%M:%S",
  reference=now(),
  timezone=$zones[hostname],
)
```

Some RFC 3164 emitters prepend structured-data blocks to the message content using syntax similar to RFC 5424. When the parser detects valid structured data at the start of the content field, it extracts the key-value pairs into a `structured_data` field and stores the remaining text in `content`. These events use the schema name `syslog.rfc3164.structured`:

```plaintext
<166>2026-02-11T18:01:45.587Z myhost Hostd[2099494]: [Originator@6876 sub=Vimsvc.TaskManager opID=23d59ade] Task Completed
```

```tql
{
  facility: 20,
  severity: 6,
  timestamp: "2026-02-11T18:01:45.587Z",
  hostname: "myhost",
  app_name: "Hostd",
  process_id: "2099494",
  structured_data: {
    "Originator@6876": {
      sub: "Vimsvc.TaskManager",
      opID: "23d59ade",
    },
  },
  content: "Task Completed",
}
```

If the leading brackets don’t contain valid structured data, the parser leaves the content intact and uses the regular `syslog.rfc3164` schema.

### Cisco headers

For supported Cisco legacy dialects, the parser stores the Cisco message identifier in `app_name`, without the leading `%` or trailing colon. The remaining description goes into `content`. For example:

```text
<189>: 2026 Apr 4 08:45:52 PDT: %SYS-5-CONFIG_I: Configured from console by console
```

```json
{
  "facility": 23,
  "severity": 5,
  "timestamp": "2026 Apr 4 08:45:52 PDT",
  "hostname": null,
  "app_name": "SYS-5-CONFIG_I",
  "process_id": null,
  "content": "Configured from console by console"
}
```

The `facility` and `severity` fields come from the syslog PRI value. The embedded Cisco severity stays in `app_name` as part of the message identifier.

The parser also accepts ASA timestamps with an optional year and fractional seconds, followed by a colon:

```text
<166>Sep 01 2026 16:46:57: %ASA-6-302014: Teardown TCP connection
```

```json
{
  "facility": 20,
  "severity": 6,
  "timestamp": "Sep 01 2026 16:46:57",
  "hostname": null,
  "app_name": "ASA-6-302014",
  "process_id": null,
  "content": "Teardown TCP connection"
}
```

For Cisco headers with a hostname before the timestamp, the parser extracts `hostname`. These additional header forms require a Cisco message identifier such as `%ASA-6-302014:` or `%FW-6-SESS_AUDIT_TRAIL:`:

```text
<45>: HOSTNAME-123: Jan 14 05:25:06.737: %FW-6-SESS_AUDIT_TRAIL: tcp session
```

```json
{
  "facility": 5,
  "severity": 5,
  "timestamp": "Jan 14 05:25:06.737",
  "hostname": "HOSTNAME-123",
  "app_name": "FW-6-SESS_AUDIT_TRAIL",
  "process_id": null,
  "content": "tcp session"
}
```

### `accept_pri_only = bool (optional)`

Defaults to `false`. Enable this option to accept text prefixed with a syslog priority after RFC 5424, RFC 3164, and Cisco header parsing fail:

```tql
read_syslog accept_pri_only=true
```

Use this option for sources that intentionally send `<PRI>` followed by plain text instead of a complete syslog header. A valid PRI alone does not prove that the rest of a message is valid syslog, so this fallback is disabled by default.

For input such as `<45>Some message`, the priority must be between 0 and 191, without a sign or leading zeros. The result uses the `syslog.rfc3164` schema:

```json
{
  "facility": 5,
  "severity": 5,
  "timestamp": null,
  "hostname": null,
  "app_name": null,
  "process_id": null,
  "content": "Some message"
}
```

When enabled, this fallback preserves everything after `>`, including leading whitespace and unrecognized or malformed headers. It also accepts an empty body. Each line with a valid PRI prefix starts a new event instead of continuing the previous event. Lines without a recognized header can still continue a previous event.

Automatic format detection with [`read_auto`](https://tenzir.com/docs/v7.0.0/reference/operators/read_auto.md) requires a recognizable syslog header; a PRI prefix alone is insufficient. Select `read_syslog` explicitly for streams containing only PRI-prefixed text. Set `accept_pri_only=true` for those streams. Automatic detection leaves this option disabled, including after it selects `read_syslog`.

**Enabling this option can hide malformed syslog headers.** For example, an RFC 5424 message missing the space between structured data and its message body can be returned successfully as PRI-prefixed text. Only `facility` and `severity` are extracted; the malformed header and body remain in `content`, and the other header fields are null. No warning identifies this fallback.

With the option disabled, unrecognized input keeps the existing behavior: an unmatched line can continue the preceding message, or becomes an unknown record if there is no preceding recognized message.

### Framing

The reader automatically detects [RFC 6587 non-transparent framing](https://datatracker.ietf.org/doc/html/rfc6587#section-3.4.2) or [octet counting](https://datatracker.ietf.org/doc/html/rfc6587#section-3.4.1) from the initial bytes of each input stream.

For non-transparent framing, the supported delimiters are LF (`\n`), CRLF (`\r\n`), and CR (`\r`). NUL (`\0`) and other custom trailers are not supported as delimiters. At end of input, the reader processes any trailing bytes as a final line.

The reader selects octet counting when a positive decimal length is followed by one ASCII space and a complete syslog priority header, such as `<165>`. For example, the message after the length prefix contains 50 bytes:

```text
50 <165>1 2026-11-09T12:00:00Z host app 123 - - hello
```

The length `50` has no brackets. The angle brackets around the priority value `165` are literal characters and belong to the counted message.

The length prefix can contain up to 10 digits and must not start with zero. The priority must contain 1–3 digits with a value from 0 through 191 and no leading zeros except for `<0>`. Detection waits for more input while this signature is incomplete. If the signature does not match, or input ends before it is complete, the reader uses non-transparent framing and preserves all buffered bytes. Legacy timestamps such as `2 18:` and `2026 Apr` therefore continue to use non-transparent framing.

Counted messages can contain embedded newlines and do not require a trailing newline. Use `octet_counting=true` for counted streams whose first message has no PRI header. This explicit setting preserves the existing permissive parsing behavior and emits a deprecation warning.

The selected framing stays fixed for the lifetime of the stream. When used inside [`accept_tcp`](https://tenzir.com/docs/v7.0.0/reference/operators/accept_tcp.md), detection runs independently for each connection. After selecting octet counting, malformed lengths remain errors; the reader does not switch to non-transparent framing.

### `octet_counting = bool (deprecated)`

Explicit values remain supported for compatibility. The reader emits a deprecation warning when it starts:

* `octet_counting=false`: Split the stream at LF, CRLF, or CR delimiters and don’t interpret a leading length prefix.
* `octet_counting=true`: Frame the stream using the declared message lengths. A missing or invalid length prefix stops the parser with an error.

Omit the parameter to enable automatic detection without a deprecation warning.

This deprecation applies only to `read_syslog`. The [`parse_syslog`](https://tenzir.com/docs/v7.0.0/reference/functions/parse_syslog.md) function retains its `octet_counting` options for parsing individual strings.

### `raw_message = field (optional)`

Stores the original, unparsed syslog message in the specified field.

For multi-line messages, the raw message includes all lines joined with newlines.

### `merge = bool (optional)`

This option has no effect and only exists for backward compatibility. Tenzir keeps events with different schemas in the same batch, so heterogeneous input needs no merging.

### `raw = bool (optional)`

Use only the raw types that are native to the parsed format. Fields that have a type specified in the chosen `schema` will still be parsed according to the schema.

### `schema = string (optional)`

Provide the name of a schema to be used by the parser.

If a schema with a matching name is installed, the result will always have all fields from that schema.

* Fields that are specified in the schema, but did not appear in the input will be null.
* Fields that appear in the input, but not in the schema will also be kept. Use `schema_only=true` to reject fields that are not in the schema.

If the given schema does not exist, this option instead assigns the output schema name only.

The `schema` option is incompatible with the `selector` option.

### `selector = string (optional)`

Designates a field value as schema name with an optional dot-separated prefix.

The string is parsed as `<fieldname>[:<prefix>]`. The `prefix` is optional and will be prepended to the field value to generate the schema name.

For example, the Suricata EVE JSON format includes a field `event_type` that contains the event type. Setting the selector to `event_type:suricata` causes an event with the value `flow` for the field `event_type` to map onto the schema `suricata.flow`.

The `selector` option is incompatible with the `schema` option.

### `schema_only = bool (optional)`

When working with an existing schema, this option will ensure that the output schema has *only* the fields from that schema.

If the schema name is obtained via a `selector` and it does not exist, this has no effect.

This option requires either `schema` or `selector` to be set.

### `unflatten_separator = string (optional)`

A delimiter that, if present in keys, causes values to be treated as values of nested records.

A popular example of this is the [Zeek JSON](read_zeek_json.md) format. It includes the fields `id.orig_h`, `id.orig_p`, `id.resp_h`, and `id.resp_p` at the top-level. The data is best modeled as an `id` record with four nested fields `orig_h`, `orig_p`, `resp_h`, and `resp_p`.

Without an unflatten separator, the data looks like this:

Without unflattening

```json
{
  "id.orig_h": "1.1.1.1",
  "id.orig_p": 10,
  "id.resp_h": "1.1.1.2",
  "id.resp_p": 5
}
```

With the unflatten separator set to `.`, Tenzir reads the events like this:

With 'unflatten'

```json
{
  "id": {
    "orig_h": "1.1.1.1",
    "orig_p": 10,
    "resp_h": "1.1.1.2",
    "resp_p": 5
  }
}
```

### Duplicate Keys

If the parser encounters a duplicate key in an event, it will transparently upgrade the field to be a list of values instead.

For a simple example, consider this JSON file:

Duplicate Keys

```json
{"key": 7}
{"key": 0.0, "key": 1}
{"key": 42}
```

```tql
{key: 7}
{key: [0.0, 1]}
{key: 42}
```

The values keep their individual types, so the list can mix values of different types:

Mixed Types

```json
{"key": 0.0, "key": "1.1.1.1", "key": "example.com"}
```

```tql
{key: [0.0, 1.1.1.1, "example.com"]}
```

When you provide a `schema` or `selector`, the last value of a repeated key wins instead.

## Examples

### Read in the `auth.log`

Pipeline

```tql
from_file "/var/log/auth.log" {
  read_syslog
}
```

```tql
{
  facility: null,
  severity: null,
  timestamp: 2024-10-14T07:15:01.348027,
  hostname: "tenzirs-magic-machine",
  app_name: "CRON",
  process_id: "895756",
  content: "pam_unix(cron:session): session opened for user root(uid=0) by root(uid=0)",
}
{
  facility: null,
  severity: null,
  timestamp: 2024-10-14T07:15:01.349838,
  hostname: "tenzirs-magic-machine",
  app_name: "CRON",
  process_id: "895756",
  content: "pam_unix(cron:session): session closed for user root"
}
```

### Receive mixed syslog framing over TCP

Use one listener for clients that send octet-counted messages and clients that use non-transparent framing with LF, CRLF, or CR delimiters:

Pipeline

```tql
accept_tcp "0.0.0.0:514" {
  read_syslog
}
```

Each connection detects its own framing, so both types of client can send messages concurrently.

### Parse Check Point structured data variants

Some Check Point exports use a structured-data dialect that differs from RFC 5424. `read_syslog` supports common variants such as `key:"value"` parameters, semicolon separators, and records that omit the SD-ID.

When an SD-ID is missing, Tenzir stores the parameters under `structured_data.checkpoint_2620`:

checkpoint.txt

```txt
<134>1 2026-02-25T08:14:51Z fwmgt CheckPoint 10024 - [action:"Accept"; conn_direction:"Incoming"; flags:"8667398"]
```

Pipeline

```tql
from_file "checkpoint.txt" {
  read_syslog
}
```

```tql
{
  facility: 16,
  severity: 6,
  version: 1,
  timestamp: 2026-02-25T08:14:51Z,
  hostname: "fwmgt",
  app_name: "CheckPoint",
  process_id: "10024",
  message_id: null,
  structured_data: {
    checkpoint_2620: {
      action: "Accept",
      conn_direction: "Incoming",
      flags: 8667398,
    },
  },
  message: null,
}
```

### Parse RFC 3164 messages with structured data

Some legacy syslog emitters, such as VMware ESXi, prepend structured-data blocks to the message content. The parser extracts them automatically:

Pipeline

```tql
from {
  line: r#"<166>2026-02-11T18:01:45.587Z myhost Hostd[2099494]: [Originator@6876 sub=Vimsvc.TaskManager opID=23d59ade] Task Completed"#,
}
write_lines
read_syslog
```

```tql
{
  facility: 20,
  severity: 6,
  timestamp: "2026-02-11T18:01:45.587Z",
  hostname: "myhost",
  app_name: "Hostd",
  process_id: "2099494",
  structured_data: {
    "Originator@6876": {
      sub: "Vimsvc.TaskManager",
      opID: "23d59ade",
    },
  },
  content: "Task Completed",
}
```

### Preserve the original message

Use `raw_message` to keep the unparsed syslog line alongside the parsed fields:

Pipeline

```tql
from_file "/var/log/auth.log" {
  read_syslog raw_message=raw
}
```

```tql
{
  facility: null,
  severity: null,
  timestamp: 2024-10-14T07:15:01.348027,
  hostname: "tenzirs-magic-machine",
  app_name: "CRON",
  process_id: "895756",
  content: "pam_unix(cron:session): session opened for user root(uid=0) by root(uid=0)",
  raw: "Oct 14 07:15:01 tenzirs-magic-machine CRON[895756]: pam_unix(cron:session): session opened for user root(uid=0) by root(uid=0)",
}
```

## See Also

* [`write_syslog`](https://tenzir.com/docs/v7.0.0/reference/operators/write_syslog.md)
* [`parse_syslog`](https://tenzir.com/docs/v7.0.0/reference/functions/parse_syslog.md)
* [Syslog](https://docs.tenzir.com/integrations/syslog)
