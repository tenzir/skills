# TCP


The [Transmission Control Protocol (TCP)](https://en.wikipedia.org/wiki/Transmission_Control_Protocol) provides a bidirectional byte stream over IP. Tenzir provides operators for both sides of a TCP conversation: connecting to remote endpoints, accepting incoming connections, and serving data to connected clients.

Use the IP address `0.0.0.0` to listen on all available network interfaces.

## Connecting to remote endpoints

Use [`from_tcp`](/reference/operators/from_tcp.md) to connect to a remote TCP endpoint as a client and read data from it, or [`to_tcp`](/reference/operators/to_tcp.md) to send data to a remote endpoint. Both operators reconnect automatically with exponential backoff on connection failure.

## Accepting incoming connections

Use [`accept_tcp`](/reference/operators/accept_tcp.md) to listen on a local endpoint and accept incoming TCP connections. Each connection spawns a nested pipeline that processes the incoming byte stream independently. Inside that pipeline, `$peer.ip` and `$peer.port` describe the connected client. Set `resolve_hostnames=true` to also expose `$peer.hostname` from reverse DNS.

## Serving data to clients

Use [`serve_tcp`](/reference/operators/serve_tcp.md) to start a TCP server that broadcasts pipeline output to all connected clients. A nested pipeline serializes events into bytes before sending.

See [Get data from the network](../guides/collecting/get-data-from-the-network.md) for practical examples.

## SSL/TLS

All TCP operators support TLS via the `tls` option. Pass an empty record (`tls={}`) for defaults, or provide specific options like `certfile` and `keyfile`.