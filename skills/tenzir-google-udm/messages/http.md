# Http

Specify the full URL of the HTTP request within "target". Also specify any uploaded or downloaded file information within "source" or "target".

- **Full name**: `google.backstory.Http`
- **Fields**: `4`

## Fields

### `method`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `method`

The HTTP request method (e.g. "GET", "POST", "PATCH", "DELETE").

### `referral_url`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `referralUrl`

The URL for the HTTP referer.

### `user_agent`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `userAgent`

The User-Agent request header which includes the application type, operating system, software vendor or software version of the requesting software user agent.

### `response_code`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `responseCode`

The response status code, for example 200, 302, 404, or 500.
