---
title: "Get data from the network"
canonical: https://tenzir.com/docs/guides/collecting/get-data-from-the-network
source: https://tenzir.com/docs/guides/collecting/get-data-from-the-network.md
section: "Docs"
---

# Get data from the network

> This guide shows you how to receive data directly from network sources using TQL. You’ll learn to listen on TCP and UDP sockets for incoming data and capture raw packets from network interfaces.

This guide shows you how to receive data directly from network sources using TQL. You’ll learn to listen on TCP and UDP sockets for incoming data and capture raw packets from network interfaces.

## TCP sockets

[TCP](../../integrations/tcp.md) provides reliable, ordered byte streams. Use TCP when you need guaranteed delivery and message ordering.

### Listen for connections

Use [`accept_tcp`](https://tenzir.com/docs/reference/operators/accept_tcp.md) to start a TCP server that accepts incoming connections:

```tql
accept_tcp "0.0.0.0:9000" {
  read_json
}
```

This listens on all interfaces (`0.0.0.0`) on port 9000. Specify a parsing pipeline to convert incoming bytes to events. Inside the nested pipeline, `$peer.ip` and `$peer.port` identify the connecting client. Set `resolve_hostnames=true` to also expose `$peer.hostname` from reverse DNS.

### Accept multiple input formats

Use [`read_auto`](https://tenzir.com/docs/reference/operators/read_auto.md) when a TCP endpoint receives data from producers that don’t all use the same format:

```tql
accept_tcp "0.0.0.0:9000" {
  read_auto fallback="lines", max_probe_bytes=16Ki
}
```

The detector runs once per connection, so one client can send NDJSON while another sends CSV, Syslog, or another supported format. This pattern is useful for rapid prototyping, shared intake endpoints, and package pipelines where you want to normalize different producer formats after parsing. If most clients send long-lived plain-text streams, use [`read_lines`](https://tenzir.com/docs/reference/operators/read_lines.md) directly instead of waiting for [`read_auto`](https://tenzir.com/docs/reference/operators/read_auto.md) to finish probing.

### Connect to a remote server

Use [`from_tcp`](https://tenzir.com/docs/reference/operators/from_tcp.md) to connect to an existing server:

```tql
from_tcp "192.168.1.100:9000" {
  read_json
}
```

### Enable TLS

Secure your TCP connections with TLS by passing a `tls` record:

```tql
accept_tcp "0.0.0.0:9443", tls={certfile: "cert.pem", keyfile: "key.pem"} {
  read_json
}
```

For testing, generate certificates with trustme:

```bash
uv run --with trustme python -m trustme
```

For production TLS configuration, including mutual TLS and cipher settings, see [Configure TLS](../node-setup/configure-tls.md).

### Accept plaintext and TLS on one port

Use TLS auto-detection when you need to migrate clients from plaintext TCP to TLS without changing the listening port:

```tql
accept_tcp "0.0.0.0:514",
           tls={certfile: "cert.pem", keyfile: "key.pem"},
           auto_detect_tls=true {
  read_syslog
}
```

With `auto_detect_tls=true`, [`accept_tcp`](https://tenzir.com/docs/reference/operators/accept_tcp.md) accepts both plaintext clients and clients that start with a TLS ClientHello on the same endpoint.

## UDP sockets

[UDP](../../integrations/udp.md) is a connectionless protocol ideal for high-volume, loss-tolerant data like syslog messages or metrics.

### Receive UDP datagrams

Use [`accept_udp`](https://tenzir.com/docs/reference/operators/accept_udp.md) to receive UDP messages as structured events:

```tql
accept_udp "0.0.0.0:514"
```

Each datagram becomes an event with `data` (the message content) and `peer` (the sender’s address) fields.

### Parse syslog messages

A common pattern is receiving syslog over UDP:

```tql
accept_udp "0.0.0.0:514"
this = data.parse_syslog()
```

### Enrich with sender metadata

Include the sender’s IP address and collection timestamp in your events:

```tql
accept_udp "0.0.0.0:514"
syslog = data.parse_syslog()
this = {
  ...syslog,
  collector: {
    source_ip: peer.ip,
    received_at: now(),
  },
}
```

## Packet capture

Capture raw network packets with [Network Interface Card](../../integrations/nic.md) for deep packet inspection or network forensics.

### List available interfaces

Find which network interfaces are available:

```tql
nics
select name, addresses, up
where up
```

```tql
{name: "eth0", addresses: ["192.168.1.100", "fe80::1"], up: true}
{name: "lo", addresses: ["127.0.0.1", "::1"], up: true}
```

### Capture packets

Use `from_nic` to capture and parse packets:

```tql
from_nic "eth0" {
  read_pcap
}
```

Each packet becomes an event with metadata and the raw packet data:

```tql
{
  linktype: 1,
  timestamp: 2024-01-15T10:30:45.123456Z,
  captured_packet_length: 74,
  original_packet_length: 74,
  data: "ABY88f1tZJ7zvttmCABFAAA8...",
}
```

### Decapsulate packets

Extract protocol headers from captured packets using the [`decapsulate`](https://tenzir.com/docs/reference/functions/decapsulate.md) function:

```tql
from_nic "eth0" {
  read_pcap
}
packet = decapsulate(this)
select packet
```

```tql
{
  packet: {
    ether: {src: "64-9E-F3-BE-DB-66", dst: "00-16-3C-F1-FD-6D", type: 2048},
    ip: {src: "192.168.1.100", dst: "10.0.0.1", type: 6},
    tcp: {src_port: 54321, dst_port: 443},
    community_id: "1:YXWfTYEyYLKVv5Ge4WqijUnKTrM=",
  },
}
```

The `community_id` field provides a [Community ID](https://github.com/corelight/community-id-spec) hash for correlating network flows across different tools.

### Filter by BPF expression

Use a Berkeley Packet Filter (BPF) expression to drop unwanted traffic before Tenzir parses packets:

```tql
from_nic "eth0", filter="tcp port 443"
```

### Read PCAP files

The same parsing works for PCAP files:

```tql
from_file "capture.pcap" {
  read_pcap
}
packet = decapsulate(this)
```

### Extract flow summaries

Capture packets and extract flow-level summaries:

```tql
from_nic "eth0" {
  read_pcap
}
packet = decapsulate(this)
select
  timestamp,
  src_ip=packet.ip.src,
  dst_ip=packet.ip.dst,
  src_port=packet.tcp.src_port? else packet.udp.src_port?,
  dst_port=packet.tcp.dst_port? else packet.udp.dst_port?,
  community_id=packet.community_id
```

## See also

* [`accept_tcp`](https://tenzir.com/docs/reference/operators/accept_tcp.md)
* [`accept_udp`](https://tenzir.com/docs/reference/operators/accept_udp.md)
* [`from_nic`](https://tenzir.com/docs/reference/operators/from_nic.md)
* [`read_auto`](https://tenzir.com/docs/reference/operators/read_auto.md)
* [TCP](../../integrations/tcp.md)
* [UDP](../../integrations/udp.md)
* [Network Interface Card](../../integrations/nic.md)
* [Syslog](../../integrations/syslog.md)
