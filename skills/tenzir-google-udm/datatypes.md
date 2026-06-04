# Standard Datatypes

Standard datatype notes from the Google UDM field list.

## Source

- **Unified Data Model field list**: https://docs.cloud.google.com/chronicle/docs/reference/udm-field-list?hl=en
  - Google last updated: `2026-06-03 UTC`
- **License**: Content licensed under Creative Commons Attribution 4.0; code samples licensed under Apache 2.0, as stated in the Google Developers Site Policies.

| Datatype | Notes | C# | C++ | Go | Java | PHP | Python | Ruby |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `double` |  | double | double | float64 | double | float | float | Float |
| `float` |  | float | float | float32 | float | float | float | Float |
| `int32` | Uses variable-length encoding. Inefficient for encoding negative numbers - if your field is likely to have negative values, use sint32 instead. | int | int32 | int32 | int | integer | int | Bignum or Fixnum (as required) |
| `int64` | Uses variable-length encoding. Inefficient for encoding negative numbers - if your field is likely to have negative values, use sint64 instead. | long | int64 | int64 | long | integer/string | int/long | Bignum |
| `uint32` | Uses variable-length encoding. | uint | uint32 | uint32 | int | integer | int/long | Bignum or Fixnum (as required) |
| `uint64` | Uses variable-length encoding. | ulong | uint64 | uint64 | long | integer/string | int/long | Bignum or Fixnum (as required) |
| `sint32` | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int32s. | int | int32 | int32 | int | integer | int | Bignum or Fixnum (as required) |
| `sint64` | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int64s. | long | int64 | int64 | long | integer/string | int/long | Bignum |
| `fixed32` | Always four bytes. More efficient than uint32 if values are often greater than 2^28. | uint | uint32 | uint32 | int | integer | int | Bignum or Fixnum (as required) |
| `fixed64` | Always eight bytes. More efficient than uint64 if values are often greater than 2^56. | ulong | uint64 | uint64 | long | integer/string | int/long | Bignum |
| `sfixed32` | Always four bytes. | int | int32 | int32 | int | integer | int | Bignum or Fixnum (as required) |
| `sfixed64` | Always eight bytes. | long | int64 | int64 | long | integer/string | int/long | Bignum |
| `bool` |  | bool | bool | bool | boolean | boolean | boolean | TrueClass/FalseClass |
| `string` | A string must always contain UTF-8 encoded or 7-bit ASCII text. | string | string | string | String | string | str/unicode | String (UTF-8) |
| `bytes` | May contain any arbitrary sequence of bytes. | ByteString | string | []byte | ByteString | string | str | String (ASCII-8BIT) |
