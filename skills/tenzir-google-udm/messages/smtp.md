# Smtp

SMTP info. See RFC 2821.

## Fields

### `helo`

- Type: `string` (singular)

The client's 'HELO'/'EHLO' string.

### `mail_from` / `mailFrom`

- Type: `string` (singular)

The client's 'MAIL FROM' string.

### `rcpt_to` / `rcptTo`

- Type: `string` (repeated)

The client's 'RCPT TO' string(s).

### `server_response` / `serverResponse`

- Type: `string` (repeated)

The server's response(s) to the client.

### `message_path` / `messagePath`

- Type: `string` (singular)

The message's path (extracted from the headers).

### `is_webmail` / `isWebmail`

- Type: `bool` (singular)

If the message was sent via a webmail client.

### `is_tls` / `isTls`

- Type: `bool` (singular)

If the connection switched to TLS.
