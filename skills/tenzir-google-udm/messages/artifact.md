# Artifact

Information about an artifact. The artifact can only be an IP.

- **Full name**: `google.backstory.Artifact`
- **Fields**: `19`

## Fields

### `ip`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `ip`

IP address of the artifact. This field can be used as an entity indicator for an external destination IP entity.

### `prevalence`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: [`Prevalence`](prevalence.md)
- **JSON name**: `prevalence`

The prevalence of the artifact within the customer's environment.

### `first_seen_time`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp` (imported)
- **JSON name**: `firstSeenTime`

First seen timestamp of the IP in the customer's environment.

### `last_seen_time`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp` (imported)
- **JSON name**: `lastSeenTime`

Last seen timestamp of the IP address in the customer's environment.

### `location`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: [`Location`](location.md)
- **JSON name**: `location`

Location of the Artifact's IP address.

### `network`

- **Number**: `6`
- **Cardinality**: `singular`
- **Type**: [`Network`](network.md)
- **JSON name**: `network`

Network information related to the Artifact's IP address.

### `as_owner`

- **Number**: `7`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `asOwner`

Owner of the Autonomous System to which the IP address belongs.

### `asn`

- **Number**: `8`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `asn`

Autonomous System Number to which the IP address belongs.

### `jarm`

- **Number**: `9`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `jarm`

The JARM hash for the IP address. (https://engineering.salesforce.com/easily-identify-malicious-servers-on-the-internet-with-jarm-e095edac525a).

### `last_https_certificate`

- **Number**: `10`
- **Cardinality**: `singular`
- **Type**: [`SSLCertificate`](ssl_certificate.md)
- **JSON name**: `lastHttpsCertificate`

SSL certificate information about the IP address.

### `last_https_certificate_date`

- **Number**: `11`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp` (imported)
- **JSON name**: `lastHttpsCertificateDate`

Most recent date for the certificate in VirusTotal.

### `regional_internet_registry`

- **Number**: `12`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `regionalInternetRegistry`

RIR (one of the current RIRs: AFRINIC, ARIN, APNIC, LACNIC or RIPE NCC).

### `tags`

- **Number**: `13`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `tags`

Identification attributes

### `whois`

- **Number**: `14`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `whois`

WHOIS information as returned from the pertinent WHOIS server.

### `whois_date`

- **Number**: `15`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp` (imported)
- **JSON name**: `whoisDate`

Date of the last update of the WHOIS record in VirusTotal.

### `tunnels`

- **Number**: `16`
- **Cardinality**: `repeated`
- **Type**: [`Tunnels`](tunnels.md)
- **JSON name**: `tunnels`

VPN tunnels.

### `anonymous`

- **Number**: `17`
- **Cardinality**: `singular`
- **Type**: `bool`
- **JSON name**: `anonymous`

Whether the VPN tunnels are configured for anonymous browsing or not.

### `artifact_client`

- **Number**: `18`
- **Cardinality**: `singular`
- **Type**: [`ArtifactClient`](artifact_client.md)
- **JSON name**: `artifactClient`

Entity or software accessing or utilizing network resources.

### `risks`

- **Number**: `19`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `risks`

This field lists potential risks associated with the network activity.
