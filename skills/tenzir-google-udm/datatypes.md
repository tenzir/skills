# Datatypes

Common type labels used in the message field reference.

| Type | Meaning |
| --- | --- |
| `string` | Text value. |
| `bool` | Boolean value. |
| `bytes` | Binary value. |
| `int32`, `int64`, `uint32`, `uint64` | Integer value. |
| `float`, `double` | Floating-point numeric value. |
| `timestamp` | Timestamp value. Check field guidance for the expected format. |
| `duration` | Duration value. Check field guidance for the expected format. |
| `object` | Structured object for values that do not fit a specific UDM message. |
| `interval` | Time interval value. |
| `latLng` | Geographic latitude and longitude value. |
| `map<K, V>` | Keyed collection whose keys and values use the listed types. |
