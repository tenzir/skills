# Network.ConnectionState

The state of a network connection.

- **Full name**: `google.backstory.Network.ConnectionState`
- **Values**: `11`

## Values

### `CONNECTION_STATE_UNSPECIFIED`

- **Number**: `0`

The default connection state.

### `LISTENING`

- **Number**: `1`

The port is listening for incoming connections.

### `ESTABLISHED`

- **Number**: `2`

A connection has been established.

### `TIME_WAIT`

- **Number**: `3`

The connection is waiting for a timeout.

### `CLOSE_WAIT`

- **Number**: `4`

The connection is waiting for a connection termination request from the local application.

### `CLOSED`

- **Number**: `5`

The connection is closed.

### `SYN_SENT`

- **Number**: `6`

A connection request has been sent.

### `SYN_RECEIVED`

- **Number**: `7`

A connection request has been received.

### `FIN_WAIT1`

- **Number**: `8`

The connection is waiting for a connection termination request from the remote host.

### `FIN_WAIT2`

- **Number**: `9`

The connection is waiting for a connection termination request from the local application.

### `LAST_ACK`

- **Number**: `10`

The connection is waiting for an acknowledgment of the final connection termination request.
