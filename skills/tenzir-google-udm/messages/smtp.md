# Smtp

SMTP info. See RFC 2821.

## Fields

### `helo`

- Type: `string` (singular)

The client's 'HELO'/'EHLO' string.

### `mailFrom`

- Type: `string` (singular)

The client's 'MAIL FROM' string.

### `rcptTo`

- Type: `string` (repeated)

The client's 'RCPT TO' string(s).

### `serverResponse`

- Type: `string` (repeated)

The server's response(s) to the client.

### `messagePath`

- Type: `string` (singular)

The message's path (extracted from the headers).

### `isWebmail`

- Type: `bool` (singular)

If the message was sent via a webmail client.

### `isTls`

- Type: `bool` (singular)

If the connection switched to TLS.
