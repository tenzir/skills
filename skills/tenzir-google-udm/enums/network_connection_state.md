# Network.ConnectionState

The state of a network connection.

## Values

0. `CONNECTION_STATE_UNSPECIFIED`: The default connection state.
1. `LISTENING`: The port is listening for incoming connections.
2. `ESTABLISHED`: A connection has been established.
3. `TIME_WAIT`: The connection is waiting for a timeout.
4. `CLOSE_WAIT`: The connection is waiting for a connection termination request from the local application.
5. `CLOSED`: The connection is closed.
6. `SYN_SENT`: A connection request has been sent.
7. `SYN_RECEIVED`: A connection request has been received.
8. `FIN_WAIT1`: The connection is waiting for a connection termination request from the remote host.
9. `FIN_WAIT2`: The connection is waiting for a connection termination request from the local application.
10. `LAST_ACK`: The connection is waiting for an acknowledgment of the final connection termination request.
