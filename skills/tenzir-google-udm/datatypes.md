# Datatypes

Common type labels used in the message field reference.

| Type | Notes | Language mappings |
| --- | --- | --- |
| `double` | - | C++: `double`<br>Java: `double`<br>Python: `float`<br>Go: `float64`<br>C#: `double`<br>PHP: `float`<br>Ruby: `Float` |
| `float` | - | C++: `float`<br>Java: `float`<br>Python: `float`<br>Go: `float32`<br>C#: `float`<br>PHP: `float`<br>Ruby: `Float` |
| `int32` | Uses variable-length encoding. Inefficient for encoding negative numbers - if your field is likely to have negative values, use sint32 instead. | C++: `int32`<br>Java: `int`<br>Python: `int`<br>Go: `int32`<br>C#: `int`<br>PHP: `integer`<br>Ruby: `Bignum or Fixnum (as required)` |
| `int64` | Uses variable-length encoding. Inefficient for encoding negative numbers - if your field is likely to have negative values, use sint64 instead. | C++: `int64`<br>Java: `long`<br>Python: `int/long`<br>Go: `int64`<br>C#: `long`<br>PHP: `integer/string`<br>Ruby: `Bignum` |
| `uint32` | Uses variable-length encoding. | C++: `uint32`<br>Java: `int`<br>Python: `int/long`<br>Go: `uint32`<br>C#: `uint`<br>PHP: `integer`<br>Ruby: `Bignum or Fixnum (as required)` |
| `uint64` | Uses variable-length encoding. | C++: `uint64`<br>Java: `long`<br>Python: `int/long`<br>Go: `uint64`<br>C#: `ulong`<br>PHP: `integer/string`<br>Ruby: `Bignum or Fixnum (as required)` |
| `sint32` | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int32s. | C++: `int32`<br>Java: `int`<br>Python: `int`<br>Go: `int32`<br>C#: `int`<br>PHP: `integer`<br>Ruby: `Bignum or Fixnum (as required)` |
| `sint64` | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int64s. | C++: `int64`<br>Java: `long`<br>Python: `int/long`<br>Go: `int64`<br>C#: `long`<br>PHP: `integer/string`<br>Ruby: `Bignum` |
| `fixed32` | Always four bytes. More efficient than uint32 if values are often greater than 2^28. | C++: `uint32`<br>Java: `int`<br>Python: `int`<br>Go: `uint32`<br>C#: `uint`<br>PHP: `integer`<br>Ruby: `Bignum or Fixnum (as required)` |
| `fixed64` | Always eight bytes. More efficient than uint64 if values are often greater than 2^56. | C++: `uint64`<br>Java: `long`<br>Python: `int/long`<br>Go: `uint64`<br>C#: `ulong`<br>PHP: `integer/string`<br>Ruby: `Bignum` |
| `sfixed32` | Always four bytes. | C++: `int32`<br>Java: `int`<br>Python: `int`<br>Go: `int32`<br>C#: `int`<br>PHP: `integer`<br>Ruby: `Bignum or Fixnum (as required)` |
| `sfixed64` | Always eight bytes. | C++: `int64`<br>Java: `long`<br>Python: `int/long`<br>Go: `int64`<br>C#: `long`<br>PHP: `integer/string`<br>Ruby: `Bignum` |
| `bool` | - | C++: `bool`<br>Java: `boolean`<br>Python: `boolean`<br>Go: `bool`<br>C#: `bool`<br>PHP: `boolean`<br>Ruby: `TrueClass/FalseClass` |
| `string` | A string must always contain UTF-8 encoded or 7-bit ASCII text. | C++: `string`<br>Java: `String`<br>Python: `str/unicode`<br>Go: `string`<br>C#: `string`<br>PHP: `string`<br>Ruby: `String (UTF-8)` |
| `bytes` | May contain any arbitrary sequence of bytes. | C++: `string`<br>Java: `ByteString`<br>Python: `str`<br>Go: `[]byte`<br>C#: `ByteString`<br>PHP: `string`<br>Ruby: `String (ASCII-8BIT)` |
