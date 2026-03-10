# save_email


Saves bytes through an SMTP server.

```tql
save_email recipient:str, [endpoint=str, from=str, subject=str, username=str,
      password=str, authzid=str, authorization=str, tls=record, mime=bool]
```

## Description

The `save_email` operator establishes a SMTP(S) connection to a mail server and sends bytes as email body.

### `recipient: str`

The recipient of the mail.

The expected format is either `Name <user@example.org>` with the email in angle brackets, or a plain email adress, such as `user@example.org`.

### `endpoint = str (optional)`

The endpoint of the mail server.

To choose between SMTP and SMTPS, provide a URL with with the corresponding scheme. For example, `smtp://127.0.0.1:25` will establish an unencrypted connection, whereas `smtps://127.0.0.1:25` an encrypted one. If you specify a server without a schema, the protocol defaults to SMTPS.

Defaults to `smtp://localhost:25`.

### `from = str (optional)`

The `From` header.

If you do not specify this parameter, an empty address is sent to the SMTP server which might cause the email to be rejected.

### `subject = str (optional)`

The `Subject` header.

### `username = str (optional)`

The username in an authenticated SMTP connection.

### `password = str (optional)`

The password in an authenticated SMTP connection.

### `authzid = str (optional)`

The authorization identity in an authenticated SMTP connection.

This option is only applicable to the PLAIN SASL authentication mechanism where it is optional. When not specified only the authentication identity (`authcid`) as specified by the username is sent to the server, along with the password. The server derives an `authzid` from the `authcid` when not provided, which it then uses internally. When the `authzid` is specified it can be used to access another user’s inbox, that the user has been granted access to, or a shared mailbox.

### `authorization = str (optional)`

The authorization options for an authenticated SMTP connection.

This login option defines the preferred authentication mechanism, e.g., `AUTH=PLAIN`, `AUTH=LOGIN`, or `AUTH=*`.

### `tls = record (optional)`

TLS configuration. Provide an empty record (`tls={}`) to enable TLS with defaults or set fields to customize it.

```tql
{
  skip_peer_verification: bool, // skip certificate verification.
  cacert: string,               // CA bundle to verify peers.
  certfile: string,             // client certificate to present.
  keyfile: string,              // private key for the client certificate.
  min_version: string,          // minimum TLS version (`"1.0"`, `"1.1"`, `"1.2"`, "1.3"`).
  ciphers: string,              // OpenSSL cipher list string.
  client_ca: string,            // CA to validate client certificates.
  require_client_cert,          // require clients to present a certificate.
}
```

The `client_ca` and `require_client_cert` options are only applied for operators that accept incoming client connections, and otherwise ignored.

Any value not specified in the record will either be picked up from the configuration or if not configured will not be used by the operator.

See the [Node TLS Setup guide](../../guides/node-setup/configure-tls.md) for more details.

### `mime = bool (optional)`

Whether to wrap the chunk into a MIME part.

The operator uses the metadata of the byte chunk for the `Content-Type` MIME header.

Defaults to `false`.

## Examples

Send the Tenzir version string as CSV to `user@example.org`:

```tql
version
write_csv
save_email "user@example.org"
```

Send the email body as MIME part:

```tql
version
write_json
save_email "user@example.org", mime=true
```

This may result in the following email body:

```plaintext
--------------------------s89ecto6c12ILX7893YOEf
Content-Type: application/json
Content-Transfer-Encoding: quoted-printable


{
  "version": "4.10.4+ge0a060567b-dirty",
  "build": "ge0a060567b-dirty",
  "major": 4,
  "minor": 10,
  "patch": 4
}


--------------------------s89ecto6c12ILX7893YOEf--
```

## See Also

* [Email](../../integrations/email.md)