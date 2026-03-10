# Functions


Functions appear in [expressions](expressions.md) and take positional and/or named arguments, producing a value as a result of their computation.

Function signatures have the following notation:

```tql
f(arg1:<type>, arg2=<type>, [arg3=type]) -> <type>
```

* `arg:<type>`: positional argument
* `arg=<type>`: named argument
* `[arg=type]`: optional (named) argument
* `-> <type>`: function return type

## Aggregation

### [all](functions/all.md)

Computes the conjunction (AND) of all grouped boolean values.

```tql
all([true,true,false])
```

### [any](functions/any.md)

Computes the disjunction (OR) of all grouped boolean values.

```tql
any([true,false,true])
```

### [collect](functions/collect.md)

Creates a list of all non-null grouped values, preserving duplicates.

```tql
collect([1,2,2,3])
```

### [count](functions/count.md)

Counts the events or non-null grouped values.

```tql
count([1,2,null])
```

### [count\_distinct](functions/count_distinct.md)

Counts all distinct non-null grouped values.

```tql
count_distinct([1,2,2,3])
```

### [count\_if](functions/count_if.md)

Counts the events or non-null grouped values matching a given predicate.

```tql
count_if([1,2,null], x => x > 1)
```

### [distinct](functions/distinct.md)

Creates a sorted list without duplicates of non-null grouped values.

```tql
distinct([1,2,2,3])
```

### [entropy](functions/entropy.md)

Computes the Shannon entropy of all grouped values.

```tql
entropy([1,1,2,3])
```

### [first](functions/first.md)

Takes the first non-null grouped value.

```tql
first([null,2,3])
```

### [last](functions/last.md)

Takes the last non-null grouped value.

```tql
last([1,2,null])
```

### [max](functions/max.md)

Computes the maximum of all grouped values.

```tql
max([1,2,3])
```

### [mean](functions/mean.md)

Computes the mean of all grouped values.

```tql
mean([1,2,3])
```

### [median](functions/median.md)

Computes the approximate median of all grouped values using a t-digest algorithm.

```tql
median([1,2,3,4])
```

### [min](functions/min.md)

Computes the minimum of all grouped values.

```tql
min([1,2,3])
```

### [mode](functions/mode.md)

Takes the most common non-null grouped value.

```tql
mode([1,1,2,3])
```

### [otherwise](functions/otherwise.md)

Returns a `fallback` value if `primary` is `null`.

```tql
x.otherwise(0)
```

### [quantile](functions/quantile.md)

Computes the specified quantile of all grouped values.

```tql
quantile([1,2,3,4], q=0.5)
```

### [stddev](functions/stddev.md)

Computes the standard deviation of all grouped values.

```tql
stddev([1,2,3])
```

### [sum](functions/sum.md)

Computes the sum of all values.

```tql
sum([1,2,3])
```

### [value\_counts](functions/value_counts.md)

Returns a list of all grouped values alongside their frequency.

```tql
value_counts([1,2,2,3])
```

### [variance](functions/variance.md)

Computes the variance of all grouped values.

```tql
variance([1,2,3])
```

## Bit Operations

### [bit\_and](functions/bit_and.md)

Computes the bit-wise AND of its arguments.

```tql
bit_and(lhs, rhs)
```

### [bit\_not](functions/bit_not.md)

Computes the bit-wise NOT of its argument.

```tql
bit_not(x)
```

### [bit\_or](functions/bit_or.md)

Computes the bit-wise OR of its arguments.

```tql
bit_or(lhs, rhs)
```

### [bit\_xor](functions/bit_xor.md)

Computes the bit-wise XOR of its arguments.

```tql
bit_xor(lhs, rhs)
```

### [shift\_left](functions/shift_left.md)

Performs a bit-wise left shift.

```tql
shift_left(lhs, rhs)
```

### [shift\_right](functions/shift_right.md)

Performs a bit-wise right shift.

```tql
shift_right(lhs, rhs)
```

## Decoding

### [decode\_base58](functions/decode_base58.md)

Decodes bytes as Base58.

```tql
decode_base58("JxF12TrwUP45BMd")
```

### [decode\_base64](functions/decode_base64.md)

Decodes bytes as Base64.

```tql
decode_base64("VGVuemly")
```

### [decode\_hex](functions/decode_hex.md)

Decodes bytes from their hexadecimal representation.

```tql
decode_hex("4e6f6E6365")
```

### [decode\_url](functions/decode_url.md)

Decodes URL encoded strings.

```tql
decode_url("Hello%20World")
```

## Encoding

### [encode\_base58](functions/encode_base58.md)

Encodes bytes as Base58.

```tql
encode_base58("Tenzir")
```

### [encode\_base64](functions/encode_base64.md)

Encodes bytes as Base64.

```tql
encode_base64("Tenzir")
```

### [encode\_hex](functions/encode_hex.md)

Encodes bytes into their hexadecimal representation.

```tql
encode_hex("Tenzir")
```

### [encode\_url](functions/encode_url.md)

Encodes strings using URL encoding.

```tql
encode_url("Hello World")
```

## Hashing

### [hash\_md5](functions/hash_md5.md)

Computes an MD5 hash digest.

```tql
hash_md5("foo")
```

### [hash\_sha1](functions/hash_sha1.md)

Computes a SHA-1 hash digest.

```tql
hash_sha1("foo")
```

### [hash\_sha224](functions/hash_sha224.md)

Computes a SHA-224 hash digest.

```tql
hash_sha224("foo")
```

### [hash\_sha256](functions/hash_sha256.md)

Computes a SHA-256 hash digest.

```tql
hash_sha256("foo")
```

### [hash\_sha3\_224](functions/hash_sha3_224.md)

Computes a SHA3-224 hash digest.

```tql
hash_sha3_224("foo")
```

### [hash\_sha3\_256](functions/hash_sha3_256.md)

Computes a SHA3-256 hash digest.

```tql
hash_sha3_256("foo")
```

### [hash\_sha3\_384](functions/hash_sha3_384.md)

Computes a SHA3-384 hash digest.

```tql
hash_sha3_384("foo")
```

### [hash\_sha3\_512](functions/hash_sha3_512.md)

Computes a SHA3-512 hash digest.

```tql
hash_sha3_512("foo")
```

### [hash\_sha384](functions/hash_sha384.md)

Computes a SHA-384 hash digest.

```tql
hash_sha384("foo")
```

### [hash\_sha512](functions/hash_sha512.md)

Computes a SHA-512 hash digest.

```tql
hash_sha512("foo")
```

### [hash\_xxh3](functions/hash_xxh3.md)

Computes an XXH3 hash digest.

```tql
hash_xxh3("foo")
```

## IP

### [ip\_category](functions/ip_category.md)

Returns the type classification of an IP address.

```tql
ip_category(8.8.8.8)
```

### [is\_global](functions/is_global.md)

Checks whether an IP address is a global address.

```tql
is_global(8.8.8.8)
```

### [is\_link\_local](functions/is_link_local.md)

Checks whether an IP address is a link-local address.

```tql
is_link_local(169.254.1.1)
```

### [is\_loopback](functions/is_loopback.md)

Checks whether an IP address is a loopback address.

```tql
is_loopback(127.0.0.1)
```

### [is\_multicast](functions/is_multicast.md)

Checks whether an IP address is a multicast address.

```tql
is_multicast(224.0.0.1)
```

### [is\_private](functions/is_private.md)

Checks whether an IP address is a private address.

```tql
is_private(192.168.1.1)
```

### [is\_v4](functions/is_v4.md)

Checks whether an IP address has version number 4.

```tql
is_v4(1.2.3.4)
```

### [is\_v6](functions/is_v6.md)

Checks whether an IP address has version number 6.

```tql
is_v6(::1)
```

### [network](functions/network.md)

Retrieves the network address of a subnet.

```tql
10.0.0.0/8.network()
```

## List

### [add](functions/add.md)

Adds an element into a list if it doesn't already exist (set-insertion).

```tql
xs.add(y)
```

### [append](functions/append.md)

Inserts an element at the back of a list.

```tql
xs.append(y)
```

### [concatenate](functions/concatenate.md)

Merges two lists.

```tql
concatenate(xs, ys)
```

### [get](functions/get.md)

Gets a field from a record or an element from a list

```tql
xs.get(index, fallback)
```

### [length](functions/length.md)

Retrieves the length of a list.

```tql
[1,2,3].length()
```

### [map](functions/map.md)

Maps each list element to an expression.

```tql
xs.map(x => x + 3)
```

### [prepend](functions/prepend.md)

Inserts an element at the start of a list.

```tql
xs.prepend(y)
```

### [remove](functions/remove.md)

Removes all occurrences of an element from a list.

```tql
xs.remove(y)
```

### [sort](functions/sort.md)

Sorts lists and record fields.

```tql
xs.sort()
```

### [where](functions/where.md)

Filters list elements based on a predicate.

```tql
xs.where(x => x > 5)
```

### [zip](functions/zip.md)

Combines two lists into a list of pairs.

```tql
zip(xs, ys)
```

## Math

### [abs](functions/abs.md)

Returns the absolute value.

```tql
abs(-42)
```

### [ceil](functions/ceil.md)

Computes the ceiling of a number or a time/duration with a specified unit.

```tql
ceil(4.2)
```

### [floor](functions/floor.md)

Computes the floor of a number or a time/duration with a specified unit.

```tql
floor(4.8)
```

### [round](functions/round.md)

Rounds a number or a time/duration with a specified unit.

```tql
round(4.6)
```

### [sqrt](functions/sqrt.md)

Computes the square root of a number.

```tql
sqrt(49)
```

## Networking

### [community\_id](functions/community_id.md)

Computes the Community ID for a network connection/flow.

```tql
community_id(src_ip=1.2.3.4, dst_ip=4.5.6.7, proto="tcp")
```

### [decapsulate](functions/decapsulate.md)

Decapsulates packet data at link, network, and transport layer.

```tql
decapsulate(this)
```

### [encrypt\_cryptopan](functions/encrypt_cryptopan.md)

Encrypts an IP address via Crypto-PAn.

```tql
encrypt_cryptopan(1.2.3.4)
```

## OCSF

### [ocsf::category\_name](functions/ocsf/category_name.md)

Returns the `category_name` for a given `category_uid`.

```tql
ocsf::category_name(2)
```

### [ocsf::category\_uid](functions/ocsf/category_uid.md)

Returns the `category_uid` for a given `category_name`.

```tql
ocsf::category_uid("Findings")
```

### [ocsf::class\_name](functions/ocsf/class_name.md)

Returns the `class_name` for a given `class_uid`.

```tql
ocsf::class_name(4003)
```

### [ocsf::class\_uid](functions/ocsf/class_uid.md)

Returns the `class_uid` for a given `class_name`.

```tql
ocsf::class_uid("DNS Activity")
```

### [ocsf::type\_name](functions/ocsf/type_name.md)

Returns the `type_name` for a given `type_uid`.

```tql
ocsf::type_name(400704)
```

### [ocsf::type\_uid](functions/ocsf/type_uid.md)

Returns the `type_uid` for a given `type_name`.

```tql
ocsf::type_uid("SSH Activity: Fail")
```

## Parsing

### [parse\_cef](functions/parse_cef.md)

Parses a string as a CEF message

```tql
string.parse_cef()
```

### [parse\_csv](functions/parse_csv.md)

Parses a string as CSV (Comma-Separated Values).

```tql
string.parse_csv(header=["a","b"])
```

### [parse\_grok](functions/parse_grok.md)

Parses a string according to a grok pattern.

```tql
string.parse_grok("%{IP:client} …")
```

### [parse\_json](functions/parse_json.md)

Parses a string as a JSON value.

```tql
string.parse_json()
```

### [parse\_kv](functions/parse_kv.md)

Parses a string as key-value pairs.

```tql
string.parse_kv()
```

### [parse\_leef](functions/parse_leef.md)

Parses a string as a LEEF message

```tql
string.parse_leef()
```

### [parse\_ssv](functions/parse_ssv.md)

Parses a string as space separated values.

```tql
string.parse_ssv(header=["a","b"])
```

### [parse\_syslog](functions/parse_syslog.md)

Parses a string as a Syslog message.

```tql
string.parse_syslog()
```

### [parse\_tsv](functions/parse_tsv.md)

Parses a string as tab separated values.

```tql
string.parse_tsv(header=["a","b"])
```

### [parse\_winlog](functions/parse_winlog.md)

Parses a string as a Windows Event Log XML record.

```tql
string.parse_winlog()
```

### [parse\_xml](functions/parse_xml.md)

Parses a string as XML and extracts elements matching an XPath expression.

```tql
string.parse_xml(xpath="//element")
```

### [parse\_xsv](functions/parse_xsv.md)

Parses a string as delimiter separated values.

```tql
string.parse_xsv(",", ";", "", header=["a","b"])
```

### [parse\_yaml](functions/parse_yaml.md)

Parses a string as a YAML value.

```tql
string.parse_yaml()
```

## Printing

### [print\_cef](functions/print_cef.md)

Prints records as Common Event Format (CEF) messages

```tql
extension.print_cef(cef_version="0", device_vendor="Tenzir", device_product="Tenzir Node", device_version="5.5.0", signature_id=id, name="description", severity="7")
```

### [print\_csv](functions/print_csv.md)

Prints a record as a comma-separated string of values.

```tql
record.print_csv()
```

### [print\_json](functions/print_json.md)

Transforms a value into a JSON string.

```tql
record.print_json()
```

### [print\_kv](functions/print_kv.md)

Prints records in a key-value format.

```tql
record.print_kv()
```

### [print\_leef](functions/print_leef.md)

Prints records as LEEF messages

```tql
attributes.print_leef(vendor="Tenzir",product_name="Tenzir Node", product_name="5.5.0",event_class_id=id)
```

### [print\_ndjson](functions/print_ndjson.md)

Transforms a value into a single-line JSON string.

```tql
record.print_ndjson()
```

### [print\_ssv](functions/print_ssv.md)

Prints a record as a space-separated string of values.

```tql
record.print_ssv()
```

### [print\_tsv](functions/print_tsv.md)

Prints a record as a tab-separated string of values.

```tql
record.print_tsv()
```

### [print\_xsv](functions/print_xsv.md)

Prints a record as a delimited sequence of values.

```tql
record.print_tsv()
```

### [print\_yaml](functions/print_yaml.md)

Prints a value as a YAML document.

```tql
record.print_yaml()
```

## Record

### [get](functions/get.md)

Gets a field from a record or an element from a list

```tql
xs.get(index, fallback)
```

### [has](functions/has.md)

Checks whether a record has a specified field.

```tql
record.has("field")
```

### [keys](functions/keys.md)

Retrieves a list of field names from a record.

```tql
record.keys()
```

### [merge](functions/merge.md)

Combines two records into a single record by merging their fields.

```tql
merge(foo, bar)
```

### [sort](functions/sort.md)

Sorts lists and record fields.

```tql
xs.sort()
```

## Runtime

### [config](functions/config.md)

Reads Tenzir's configuration file.

```tql
config()
```

### [env](functions/env.md)

Reads an environment variable.

```tql
env("PATH")
```

### [secret](functions/secret.md)

Use the value of a secret.

```tql
secret("KEY")
```

## Subnet

### [network](functions/network.md)

Retrieves the network address of a subnet.

```tql
10.0.0.0/8.network()
```

## Time & Date

### [count\_days](functions/count_days.md)

Counts the number of `days` in a duration.

```tql
count_days(100d)
```

### [count\_hours](functions/count_hours.md)

Counts the number of `hours` in a duration.

```tql
count_hours(100d)
```

### [count\_microseconds](functions/count_microseconds.md)

Counts the number of `microseconds` in a duration.

```tql
count_microseconds(100d)
```

### [count\_milliseconds](functions/count_milliseconds.md)

Counts the number of `milliseconds` in a duration.

```tql
count_milliseconds(100d)
```

### [count\_minutes](functions/count_minutes.md)

Counts the number of `minutes` in a duration.

```tql
count_minutes(100d)
```

### [count\_months](functions/count_months.md)

Counts the number of `months` in a duration.

```tql
count_months(100d)
```

### [count\_nanoseconds](functions/count_nanoseconds.md)

Counts the number of `nanoseconds` in a duration.

```tql
count_nanoseconds(100d)
```

### [count\_seconds](functions/count_seconds.md)

Counts the number of `seconds` in a duration.

```tql
count_seconds(100d)
```

### [count\_weeks](functions/count_weeks.md)

Counts the number of `weeks` in a duration.

```tql
count_weeks(100d)
```

### [count\_years](functions/count_years.md)

Counts the number of `years` in a duration.

```tql
count_years(100d)
```

### [day](functions/day.md)

Extracts the day component from a timestamp.

```tql
ts.day()
```

### [days](functions/days.md)

Converts a number to equivalent days.

```tql
days(100)
```

### [format\_time](functions/format_time.md)

Formats a time into a string that follows a specific format.

```tql
ts.format_time("%d/ %m/%Y")
```

### [from\_epoch](functions/from_epoch.md)

Interprets a duration as Unix time.

```tql
from_epoch(time_ms * 1ms)
```

### [hour](functions/hour.md)

Extracts the hour component from a timestamp.

```tql
ts.hour()
```

### [hours](functions/hours.md)

Converts a number to equivalent hours.

```tql
hours(100)
```

### [microseconds](functions/microseconds.md)

Converts a number to equivalent microseconds.

```tql
microseconds(100)
```

### [milliseconds](functions/milliseconds.md)

Converts a number to equivalent milliseconds.

```tql
milliseconds(100)
```

### [minute](functions/minute.md)

Extracts the minute component from a timestamp.

```tql
ts.minute()
```

### [minutes](functions/minutes.md)

Converts a number to equivalent minutes.

```tql
minutes(100)
```

### [month](functions/month.md)

Extracts the month component from a timestamp.

```tql
ts.month()
```

### [months](functions/months.md)

Converts a number to equivalent months.

```tql
months(100)
```

### [nanoseconds](functions/nanoseconds.md)

Converts a number to equivalent nanoseconds.

```tql
nanoseconds(100)
```

### [now](functions/now.md)

Gets the current wallclock time.

```tql
now()
```

### [parse\_time](functions/parse_time.md)

Parses a time from a string that follows a specific format.

```tql
"10/11/2012".parse_time("%d/%m/%Y")
```

### [second](functions/second.md)

Extracts the second component from a timestamp with subsecond precision.

```tql
ts.second()
```

### [seconds](functions/seconds.md)

Converts a number to equivalent seconds.

```tql
seconds(100)
```

### [since\_epoch](functions/since_epoch.md)

Interprets a time value as duration since the Unix epoch.

```tql
since_epoch(2021-02-24)
```

### [weeks](functions/weeks.md)

Converts a number to equivalent weeks.

```tql
weeks(100)
```

### [year](functions/year.md)

Extracts the year component from a timestamp.

```tql
ts.year()
```

### [years](functions/years.md)

Converts a number to equivalent years.

```tql
years(100)
```

## Utility

### [contains](functions/contains.md)

Searches for a value within data structures recursively.

```tql
this.contains("value")
```

### [contains\_null](functions/contains_null.md)

Checks whether the input contains any `null` values.

```tql
{x: 1, y: null}.contains_null() == true
```

### [is\_empty](functions/is_empty.md)

Checks whether a value is empty.

```tql
"".is_empty()
```

### [random](functions/random.md)

Generates a random number in *\[0,1]*.

```tql
random()
```

### [uuid](functions/uuid.md)

Generates a Universally Unique Identifier (UUID) string.

```tql
uuid()
```

## String

### Filesystem

### [file\_contents](functions/file_contents.md)

Reads a file's contents.

```tql
file_contents("/path/to/file")
```

### [file\_name](functions/file_name.md)

Extracts the file name from a file path.

```tql
file_name("/path/to/log.json")
```

### [parent\_dir](functions/parent_dir.md)

Extracts the parent directory from a file path.

```tql
parent_dir("/path/to/log.json")
```

### Inspection

### [ends\_with](functions/ends_with.md)

Checks if a string ends with a specified substring.

```tql
"hello".ends_with("lo")
```

### [is\_alnum](functions/is_alnum.md)

Checks if a string is alphanumeric.

```tql
"hello123".is_alnum()
```

### [is\_alpha](functions/is_alpha.md)

Checks if a string contains only alphabetic characters.

```tql
"hello".is_alpha()
```

### [is\_lower](functions/is_lower.md)

Checks if a string is in lowercase.

```tql
"hello".is_lower()
```

### [is\_numeric](functions/is_numeric.md)

Checks if a string contains only numeric characters.

```tql
"1234".is_numeric()
```

### [is\_printable](functions/is_printable.md)

Checks if a string contains only printable characters.

```tql
"hello".is_printable()
```

### [is\_title](functions/is_title.md)

Checks if a string follows title case.

```tql
"Hello World".is_title()
```

### [is\_upper](functions/is_upper.md)

Checks if a string is in uppercase.

```tql
"HELLO".is_upper()
```

### [length\_bytes](functions/length_bytes.md)

Returns the length of a string in bytes.

```tql
"hello".length_bytes()
```

### [length\_chars](functions/length_chars.md)

Returns the length of a string in characters.

```tql
"hello".length_chars()
```

### [match\_regex](functions/match_regex.md)

Checks if a string partially matches a regular expression.

```tql
"Hi".match_regex("[Hh]i")
```

### [slice](functions/slice.md)

Slices a string with offsets and strides.

```tql
"Hi".slice(begin=2, stride=4)
```

### [starts\_with](functions/starts_with.md)

Checks if a string starts with a specified substring.

```tql
"hello".starts_with("he")
```

### Transformation

### [capitalize](functions/capitalize.md)

Capitalizes the first character of a string.

```tql
"hello".capitalize()
```

### [join](functions/join.md)

Joins a list of strings into a single string using a separator.

```tql
join(["a", "b", "c"], ",")
```

### [pad\_end](functions/pad_end.md)

Pads a string at the end to a specified length.

```tql
"hello".pad_end(10)
```

### [pad\_start](functions/pad_start.md)

Pads a string at the start to a specified length.

```tql
"hello".pad_start(10)
```

### [replace](functions/replace.md)

Replaces characters within a string.

```tql
"hello".replace("o", "a")
```

### [replace\_regex](functions/replace_regex.md)

Replaces characters within a string based on a regular expression.

```tql
"hello".replace("l+o", "y")
```

### [reverse](functions/reverse.md)

Reverses the characters of a string.

```tql
"hello".reverse()
```

### [split](functions/split.md)

Splits a string into substrings.

```tql
split("a,b,c", ",")
```

### [split\_regex](functions/split_regex.md)

Splits a string into substrings with a regex.

```tql
split_regex("a1b2c", r"\d")
```

### [to\_lower](functions/to_lower.md)

Converts a string to lowercase.

```tql
"HELLO".to_lower()
```

### [to\_title](functions/to_title.md)

Converts a string to title case.

```tql
"hello world".to_title()
```

### [to\_upper](functions/to_upper.md)

Converts a string to uppercase.

```tql
"hello".to_upper()
```

### [trim](functions/trim.md)

Trims whitespace or specified characters from both ends of a string.

```tql
" hello ".trim()
```

### [trim\_end](functions/trim_end.md)

Trims whitespace or specified characters from the end of a string.

```tql
"hello ".trim_end()
```

### [trim\_start](functions/trim_start.md)

Trims whitespace or specified characters from the start of a string.

```tql
" hello".trim_start()
```

## Type System

### Conversion

### [duration](functions/duration.md)

Casts an expression to a duration value.

```tql
duration("1.34w")
```

### [float](functions/float.md)

Casts an expression to a float.

```tql
float(42)
```

### [int](functions/int.md)

Casts an expression to an integer.

```tql
int(-4.2)
```

### [ip](functions/ip.md)

Casts an expression to an IP address.

```tql
ip("1.2.3.4")
```

### [string](functions/string.md)

Casts an expression to a string.

```tql
string(1.2.3.4)
```

### [subnet](functions/subnet.md)

Casts an expression to a subnet value.

```tql
subnet("1.2.3.4/16")
```

### [time](functions/time.md)

Casts an expression to a time value.

```tql
time("2020-03-15")
```

### [uint](functions/uint.md)

Casts an expression to an unsigned integer.

```tql
uint(4.2)
```

### Introspection

### [type\_id](functions/type_id.md)

Retrieves the type id of an expression.

```tql
type_id(1 + 3.2)
```

### [type\_of](functions/type_of.md)

Retrieves the type definition of an expression.

```tql
type_of(this)
```

### Transposition

### [flatten](functions/flatten.md)

Flattens nested data.

```tql
flatten(this)
```

### [unflatten](functions/unflatten.md)

Unflattens nested data.

```tql
unflatten(this)
```