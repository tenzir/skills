# Encryption Details

> Details about the encryption methodology utilized.


Details about the encryption methodology utilized.

## Attributes

**`algorithm_id`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`: The algorithm is unknown.
  * `1` - `DES`: Data Encryption Standard Algorithm
  * `2` - `TripleDES`: Triple Data Encryption Standard Algorithm
  * `3` - `AES`: Advanced Encryption Standard Algorithm.
  * `4` - `RSA`: Rivest-Shamir-Adleman Algorithm
  * `5` - `ECC`: Elliptic Curve Cryptography Algorithm
  * `6` - `SM2`: ShangMi Cryptographic Algorithm
  * `99` - `Other`: The algorithm is not mapped. See the `algorithm` attribute, which contains a data source specific value.

The encryption algorithm used.

**`type`**

* **Type**: `string_t`
* **Requirement**: recommended

The type of the encryption used.

**`algorithm`**

* **Type**: `string_t`
* **Requirement**: optional

The encryption algorithm used, normalized to the caption of ‘algorithm\_id

**`key_length`**

* **Type**: `integer_t`
* **Requirement**: optional

The length of the encryption key used.

**`key_uid`**

* **Type**: `string_t`
* **Requirement**: optional

The unique identifier of the key used for encryption. For example, AWS KMS Key ARN.