# Transport Layer Security (TLS)

> The Transport Layer Security (TLS) object describes the negotiated TLS protocol used for secure communications over an establish network connection.


The Transport Layer Security (TLS) object describes the negotiated TLS protocol used for secure communications over an establish network connection.

## Attributes

**`version`**

* **Type**: `string_t`
* **Requirement**: required

The TLS protocol version.

**`certificate`**

* **Type**: [`certificate`](certificate.md)
* **Requirement**: recommended

The certificate object containing information about the digital certificate.

**`certificate_chain`**

* **Type**: `string_t`
* **Requirement**: recommended

The Chain of Certificate Serial Numbers field provides a chain of Certificate Issuer Serial Numbers leading to the Root Certificate Issuer.

**`cipher`**

* **Type**: `string_t`
* **Requirement**: recommended

The negotiated cipher suite.

**`client_ciphers`**

* **Type**: `string_t`
* **Requirement**: recommended

The client cipher suites that were exchanged during the TLS handshake negotiation.

**`ja3_hash`**

* **Type**: [`fingerprint`](fingerprint.md)
* **Requirement**: recommended

The MD5 hash of a JA3 string.

**`ja3s_hash`**

* **Type**: [`fingerprint`](fingerprint.md)
* **Requirement**: recommended

The MD5 hash of a JA3S string.

**`sni`**

* **Type**: `string_t`
* **Requirement**: recommended

The Server Name Indication (SNI) extension sent by the client.

**`alert`**

* **Type**: `integer_t`
* **Requirement**: optional

The integer value of TLS alert if present. The alerts are defined in the TLS specification in [RFC-2246](https://datatracker.ietf.org/doc/html/rfc2246).

**`extension_list`**

* **Type**: [`tls_extension`](tls_extension.md)
* **Requirement**: optional

The list of TLS extensions.

**`handshake_dur`**

* **Type**: `integer_t`
* **Requirement**: optional

The amount of total time for the TLS handshake to complete after the TCP connection is established, including client-side delays, in milliseconds.

**`key_length`**

* **Type**: `integer_t`
* **Requirement**: optional

The length of the encryption key.

**`sans`**

* **Type**: [`san`](san.md)
* **Requirement**: optional

The list of subject alternative names that are secured by a specific certificate.

**`server_ciphers`**

* **Type**: `string_t`
* **Requirement**: optional

The server cipher suites that were exchanged during the TLS handshake negotiation.

**`tls_extension_list`**

* **Type**: [`tls_extension`](tls_extension.md)
* **Requirement**: optional

The list of TLS extensions.

## Used By

* [`airborne_broadcast_activity`](../classes/airborne_broadcast_activity.md)
* [`dhcp_activity`](../classes/dhcp_activity.md)
* [`dns_activity`](../classes/dns_activity.md)
* [`drone_flights_activity`](../classes/drone_flights_activity.md)
* [`ftp_activity`](../classes/ftp_activity.md)
* [`http_activity`](../classes/http_activity.md)
* [`network_activity`](../classes/network_activity.md)
* [`network_file_activity`](../classes/network_file_activity.md)
* [`ntp_activity`](../classes/ntp_activity.md)
* [`rdp_activity`](../classes/rdp_activity.md)
* [`smb_activity`](../classes/smb_activity.md)
* [`ssh_activity`](../classes/ssh_activity.md)
* [`tunnel_activity`](../classes/tunnel_activity.md)
* [`web_resource_access_activity`](../classes/web_resource_access_activity.md)
* [`web_resources_activity`](../classes/web_resources_activity.md)