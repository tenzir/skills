# Url

Url.

- **Full name**: `google.backstory.Url`
- **Fields**: `13`

## Fields

### `url`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `url`

URL.

### `categories`

- **Number**: `2`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `categories`

Categorisation done by VirusTotal partners.

### `favicon`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: [`Favicon`](favicon.md)
- **JSON name**: `favicon`

Difference hash and MD5 hash of the URL's.

### `html_meta`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Struct`
- **JSON name**: `htmlMeta`

Meta tags (only for URLs downloading HTML).

### `last_final_url`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `lastFinalUrl`

If the original URL redirects, where does it end.

### `last_http_response_code`

- **Number**: `6`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `lastHttpResponseCode`

HTTP response code of the last response.

### `last_http_response_content_length`

- **Number**: `7`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `lastHttpResponseContentLength`

Length in bytes of the content received.

### `last_http_response_content_sha256`

- **Number**: `8`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `lastHttpResponseContentSha256`

URL response body's SHA256 hash.

### `last_http_response_cookies`

- **Number**: `9`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Struct`
- **JSON name**: `lastHttpResponseCookies`

Website's cookies.

### `last_http_response_headers`

- **Number**: `10`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Struct`
- **JSON name**: `lastHttpResponseHeaders`

Headers and values of the last HTTP response.

### `tags`

- **Number**: `11`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `tags`

Tags.

### `title`

- **Number**: `12`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `title`

Webpage title.

### `trackers`

- **Number**: `13`
- **Cardinality**: `repeated`
- **Type**: [`Tracker`](tracker.md)
- **JSON name**: `trackers`

Trackers found in the URL in a historical manner.
