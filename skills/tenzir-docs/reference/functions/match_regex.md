# match_regex


Checks if a string partially matches a regular expression.

```tql
match_regex(input:string, regex:string) -> bool
```

## Description

The `match_regex` function returns `true` if `regex` matches a substring of `input`.

To check whether the full string matches, you can use `^` and `$` to signify start and end of the string.

### `input: string`

The string to partially match.

### `regex: string`

The regular expression try and match.

The supported regular expression syntax is [RE2](https://github.com/google/re2/wiki/Syntax). In particular, this means that lookahead `(?=...)` and lookbehind `(?<=...)` are not supported by `match_regex` at the moment.

## Examples

### Check contains a matching substring

```tql
from {input: "Hello There World"},
  {input: "hi there!"},
  {input: "Good Morning" }
output = input.match_regex("[T|t]here")
```

```tql
{input: "Hello There World", output: true}
{input: "hi there!", output: true}
{input: "Good Morning", output: false}
```

### Check if a string matches fully

```tql
from {input: "example"},
  {input: "Example!"},
  {input: "example?" }
output = input.match_regex("^[E|e]xample[!]?$")
```

```tql
{input: "example", output: true}
{input: "example!", output: true}
{input: "example?", output: false}
```

## See Also

* fn[`replace_regex`](replace_regex.md)
* fn[`split_regex`](split_regex.md)
* fn[`starts_with`](starts_with.md)
* fn[`ends_with`](ends_with.md)
* [Manipulate strings](../../guides/transformation/manipulate-strings.md)