<!-- Source: https://docs.fortinet.com/document/fortisiem/7.5.0/fortisiem-event-data-model/368849/certificate-monitoring-data-model -->

# Certificate Monitoring Data Model

This data model describes certificate added/removed/expired activity.

Example events via Windows Agent:

- AO-WUA-Certificate-Added: A Windows certificate was added
- AO-WUA-Certificate-Removed: A Windows certificate was removed
- AO-WUA-Certificate-Expired: A Windows certificate was expired
- AO-WUA-Certificate-Expiring: A Windows certificate is expiring

In addition to the base event attributes, the following attributes are relevant and may be populated in this data model.

| Event Attribute | Type | Display Name | Description |
| --- | --- | --- | --- |
| hostIpAddr | IP | Host IP | IP address of hostName |
| hostName | string | Host Name | Host where event occurs |
| certInfo | string | Certificate | Certificate Common Name |
| fingerprintId | string | Fingerprint | Certificate fingerprint |
| folder | string | Folder | Folder where the specific Windows store that the cert is in |
| issuer | string | Issuer | Certificate Issuer |
| issuedTo | string | Issued To | Certificate Issued to |
| isSelfSigned | uchar | Is Self Signed | 0 means not self-signed, 1 means self-signed |
| isCertAuthority | uchar | Is Certificate Authority | 0 means not certificate authority, 1 means certificate authority |
| validFrom | DATE | Valid From | Time since when certificate is valid |
| validTo | DATE | Valid To | Time upto which certificate is valid |
| daysToExpiry | uint32 | Days To Expiry | Days to certiciate expirt (derived from Valid To field) |
| serialNumber | string | Serial Number | Ceritificate Serial Number |
| hostKeyAlgo | string | Key Algorithm | Algorithm used to create the certificates |
| hostKeyStrength | Uint32 | Key Strength | size of the hostKey in bits |
| hashCode | string | Hash Code | Certificate fingerprint |
| hashAlgo | string | Hash Algorithm | Algorithm used to create the certificates fingerprint |
