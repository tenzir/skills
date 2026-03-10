# HASSH

> The HASSH object contains SSH network fingerprinting values for specific client/server implementations.


The HASSH object contains SSH network fingerprinting values for specific client/server implementations. It provides a standardized way of identifying and categorizing SSH connections based on their unique characteristics and behavior.

## Attributes

**`fingerprint`**

* **Type**: [`fingerprint`](fingerprint.md)
* **Requirement**: required

The hash of the key exchange, encryption, authentication and compression algorithms.

**`algorithm`**

* **Type**: `string_t`
* **Requirement**: recommended

The concatenation of key exchange, encryption, authentication and compression algorithms (separated by ’;’). NOTE: This is not the underlying algorithm for the hash implementation.

## Used By

* [`ssh_activity`](../classes/ssh_activity.md)