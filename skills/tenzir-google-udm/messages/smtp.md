# Smtp

SMTP info. See RFC 2821.

- **Full name**: `google.backstory.Smtp`
- **Fields**: `7`

## Fields

### `helo`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `helo`

The client's 'HELO'/'EHLO' string.

### `mail_from`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `mailFrom`

The client's 'MAIL FROM' string.

### `rcpt_to`

- **Number**: `3`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `rcptTo`

The client's 'RCPT TO' string(s).

### `server_response`

- **Number**: `4`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `serverResponse`

The server's response(s) to the client.

### `message_path`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `messagePath`

The message's path (extracted from the headers).

### `is_webmail`

- **Number**: `6`
- **Cardinality**: `singular`
- **Type**: `bool`
- **JSON name**: `isWebmail`

If the message was sent via a webmail client.

### `is_tls`

- **Number**: `7`
- **Cardinality**: `singular`
- **Type**: `bool`
- **JSON name**: `isTls`

If the connection switched to TLS.
