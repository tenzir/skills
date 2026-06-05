# Artifact

Information about an artifact. The artifact can only be an IP.

## Fields

### `ip`

- Type: `string` (singular)

IP address of the artifact. This field can be used as an entity indicator for an external destination IP entity.

### `prevalence`

- Type: [`Prevalence`](prevalence.md) (singular)

The prevalence of the artifact within the customer's environment.

### `first_seen_time` / `firstSeenTime`

- Type: `timestamp` (singular)

First seen timestamp of the IP in the customer's environment.

### `last_seen_time` / `lastSeenTime`

- Type: `timestamp` (singular)

Last seen timestamp of the IP address in the customer's environment.

### `location`

- Type: [`Location`](location.md) (singular)

Location of the Artifact's IP address.

### `network`

- Type: [`Network`](network.md) (singular)

Network information related to the Artifact's IP address.

### `as_owner` / `asOwner`

- Type: `string` (singular)

Owner of the Autonomous System to which the IP address belongs.

### `asn`

- Type: `int64` (singular)

Autonomous System Number to which the IP address belongs.

### `jarm`

- Type: `string` (singular)

The JARM hash for the IP address. (https://engineering.salesforce.com/easily-identify-malicious-servers-on-the-internet-with-jarm-e095edac525a).

### `last_https_certificate` / `lastHttpsCertificate`

- Type: [`SSLCertificate`](ssl_certificate.md) (singular)

SSL certificate information about the IP address.

### `last_https_certificate_date` / `lastHttpsCertificateDate`

- Type: `timestamp` (singular)

Most recent date for the certificate in VirusTotal.

### `regional_internet_registry` / `regionalInternetRegistry`

- Type: `string` (singular)

RIR (one of the current RIRs: AFRINIC, ARIN, APNIC, LACNIC or RIPE NCC).

### `tags`

- Type: `string` (repeated)

Identification attributes

### `whois`

- Type: `string` (singular)

WHOIS information as returned from the pertinent WHOIS server.

### `whois_date` / `whoisDate`

- Type: `timestamp` (singular)

Date of the last update of the WHOIS record in VirusTotal.

### `tunnels`

- Type: [`Tunnels`](tunnels.md) (repeated)

VPN tunnels.

### `anonymous`

- Type: `bool` (singular)

Whether the VPN tunnels are configured for anonymous browsing or not.

### `artifact_client` / `artifactClient`

- Type: [`ArtifactClient`](artifact_client.md) (singular)

Entity or software accessing or utilizing network resources.

### `risks`

- Type: `string` (repeated)

This field lists potential risks associated with the network activity.
