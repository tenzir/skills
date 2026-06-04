# Http

Specify the full URL of the HTTP request within "target". Also specify any uploaded or downloaded file information within "source" or "target".

## Fields

### `method`

- Type: `string` (singular)

The HTTP request method (e.g. "GET", "POST", "PATCH", "DELETE").

### `referral_url` / `referralUrl`

- Type: `string` (singular)

The URL for the HTTP referer.

### `user_agent` / `userAgent`

- Type: `string` (singular)

The User-Agent request header which includes the application type, operating system, software vendor or software version of the requesting software user agent.

### `response_code` / `responseCode`

- Type: `int32` (singular)

The response status code, for example 200, 302, 404, or 500.

## Guidance

Population guidance from the Google UDM usage guide.

### `method`

- **Purpose**: Stores the HTTP request method.
- **Encoding**: String.

#### Examples

- GET
- HEAD
- POST

### `referral_url` / `referralUrl`

- **Purpose**: Stores the URL for the HTTP referer.
- **Encoding**: Valid RFC 3986 URL.
- **Example**: https://www.altostrat.com

#### Examples

- https://www.altostrat.com

### `response_code` / `responseCode`

- **Purpose**: Stores the HTTP response status code, which indicates whether a specific HTTP request has been successfully completed.
- **Encoding**: 32-bit integer.

#### Examples

- 400
- 404

### `user_agent` / `userAgent`

- **Purpose**: Stores the User-Agent request header that includes the application type, operating system, software vendor or software version of the requesting software user agent.
- **Encoding**: String.

#### Examples

- Mozilla/5.0 (X11; Linux x86_64)
- AppleWebKit/534.26 (KHTML, like Gecko)
- Chrome/41.0.2217.0
- Safari/527.33
