# write_pcap


Serializes packet events as a PCAP byte stream.

```tql
write_pcap
```

## Description

The `write_pcap` operator transforms packet events into a [PCAP](https://datatracker.ietf.org/doc/id/draft-gharris-opsawg-pcap-00.html) byte stream.

The operator accepts `pcap.packet` events. When present, it also uses `pcap.file_header` events emitted by [`read_pcap`](/reference/operators/read_pcap.md) to preserve the original timestamp precision and byte order.

If no `pcap.file_header` event is present, `write_pcap` generates a file header from the first packet’s `linktype` and writes timestamps with nanosecond precision.

The structured representation of packets has the `pcap.packet` schema:

```yaml
pcap.packet:
  record:
    - linktype: uint64
    - timestamp: time
    - captured_packet_length: uint64
    - original_packet_length: uint64
    - data: blob
```

PCAPNG

The current implementation does *not* support [PCAPNG](https://www.ietf.org/archive/id/draft-tuexen-opsawg-pcapng-05.html).

## Examples

### Write a live capture to a PCAP file

```tql
from_nic "en1"
to_file "/logs/packets.pcap" {
  write_pcap
}
```

### Round-trip a PCAP file while preserving its file header

```tql
from_file "/tmp/trace.pcap" {
  read_pcap emit_file_headers=true
}
to_file "/tmp/trace-copy.pcap" {
  write_pcap
}
```

## See Also

* [`from_nic`](/reference/operators/from_nic.md)
* [`read_pcap`](/reference/operators/read_pcap.md)