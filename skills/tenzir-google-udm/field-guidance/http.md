# Http Field Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`

## Schema

- [Http](../messages/http.md)

## Fields

### `Http.method`

- **Purpose**: Stores the HTTP request method.
- **Encoding**: String.
- **Examples**: GET HEAD POST

#### Examples

- GET
- HEAD
- POST

### `Http.referral_url`

- **Purpose**: Stores the URL for the HTTP referer.
- **Encoding**: Valid RFC 3986 URL.
- **Example**: https://www.altostrat.com

#### Examples

- https://www.altostrat.com

### `Http.response_code`

- **Purpose**: Stores the HTTP response status code, which indicates whether a specific HTTP request has been successfully completed.
- **Encoding**: 32-bit integer.
- **Examples**: 400 404

#### Examples

- 400
- 404

### `Http.user_agent`

- **Purpose**: Stores the User-Agent request header that includes the application type, operating system, software vendor or software version of the requesting software user agent.
- **Encoding**: String.
- **Examples**: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.26 (KHTML, like Gecko) Chrome/41.0.2217.0 Safari/527.33

#### Examples

- Mozilla/5.0 (X11; Linux x86_64)
- AppleWebKit/534.26 (KHTML, like Gecko)
- Chrome/41.0.2217.0
- Safari/527.33
