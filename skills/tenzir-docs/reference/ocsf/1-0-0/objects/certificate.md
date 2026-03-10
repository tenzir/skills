# Digital Certificate

> The Digital Certificate, also known as a Public Key Certificate, object contains information about the ownership and usage of a public key.


The Digital Certificate, also known as a Public Key Certificate, object contains information about the ownership and usage of a public key. It serves as a means to establish trust in the authenticity and integrity of the public key and the associated entity. Defined by D3FEND [d3f:Certificate](https://d3fend.mitre.org/dao/artifact/d3f:Certificate/).

## Attributes

**`fingerprints`**

* **Type**: [`fingerprint`](fingerprint.md)
* **Requirement**: required

The fingerprint list of the certificate.

**`issuer`**

* **Type**: `string_t`
* **Requirement**: required

The certificate issuer distinguished name.

**`serial_number`**

* **Type**: `string_t`
* **Requirement**: required

The serial number of the certificate used to create the digital signature.

**`created_time`**

* **Type**: `timestamp_t`
* **Requirement**: recommended

The time when the certificate was created.

**`expiration_time`**

* **Type**: `timestamp_t`
* **Requirement**: recommended

The expiration time of the certificate.

**`subject`**

* **Type**: `string_t`
* **Requirement**: recommended

The certificate subject distinguished name.

**`version`**

* **Type**: `string_t`
* **Requirement**: recommended

The certificate version.

**`created_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The time when the certificate was created.

**`expiration_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The expiration time of the certificate.

## Used By

* [`authentication`](../classes/authentication.md)