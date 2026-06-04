# Url

Url.

## Fields

### `url`

- Type: `string` (singular)

URL.

### `categories`

- Type: `string` (repeated)

Categorisation done by VirusTotal partners.

### `favicon`

- Type: [`Favicon`](favicon.md) (singular)

Difference hash and MD5 hash of the URL's.

### `htmlMeta`

- Type: `object` (singular)

Meta tags (only for URLs downloading HTML).

### `lastFinalUrl`

- Type: `string` (singular)

If the original URL redirects, where does it end.

### `lastHttpResponseCode`

- Type: `int32` (singular)

HTTP response code of the last response.

### `lastHttpResponseContentLength`

- Type: `int64` (singular)

Length in bytes of the content received.

### `lastHttpResponseContentSha256`

- Type: `string` (singular)

URL response body's SHA256 hash.

### `lastHttpResponseCookies`

- Type: `object` (singular)

Website's cookies.

### `lastHttpResponseHeaders`

- Type: `object` (singular)

Headers and values of the last HTTP response.

### `tags`

- Type: `string` (repeated)

Tags.

### `title`

- Type: `string` (singular)

Webpage title.

### `trackers`

- Type: [`Tracker`](tracker.md) (repeated)

Trackers found in the URL in a historical manner.
