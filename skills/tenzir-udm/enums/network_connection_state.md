# ConnectionState

The state of a network connection.

## Values

- `CONNECTION_STATE_UNSPECIFIED` (0): The default connection state.
- `LISTENING` (1): The port is listening for incoming connections.
- `ESTABLISHED` (2): A connection has been established.
- `TIME_WAIT` (3): The connection is waiting for a timeout.
- `CLOSE_WAIT` (4): The connection is waiting for a connection termination request from the local application.
- `CLOSED` (5): The connection is closed.
- `SYN_SENT` (6): A connection request has been sent.
- `SYN_RECEIVED` (7): A connection request has been received.
- `FIN_WAIT1` (8): The connection is waiting for a connection termination request from the remote host.
- `FIN_WAIT2` (9): The connection is waiting for a connection termination request from the local application.
- `LAST_ACK` (10): The connection is waiting for an acknowledgment of the final connection termination request.
