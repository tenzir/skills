# Browser.Cookie

Browser cookie.

- **Full name**: `google.backstory.Browser.Cookie`
- **Fields**: `11`
- **Nested enums**: `1`

## Nested enums

- [Browser.Cookie.CookieSameSite](../enums/browser_cookie_cookie_same_site.md)

## Fields

### `name`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `name`

The unique name identifying the cookie.

### `value`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `value`

The data stored within the cookie.

### `domain`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `domain`

The domain for which the cookie is valid.

### `path`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `path`

The URL path for which the cookie is valid.

### `expiration_time`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp`
- **JSON name**: `expirationTime`

The date and time when the cookie will expire.

### `http_only`

- **Number**: `6`
- **Cardinality**: `singular`
- **Type**: `bool`
- **JSON name**: `httpOnly`

Indicates if the cookie is inaccessible via client-side scripts (e.g., JavaScript).

### `secure`

- **Number**: `7`
- **Cardinality**: `singular`
- **Type**: `bool`
- **JSON name**: `secure`

Indicates if the cookie should only be sent over secure HTTPS connections.

### `max_age`

- **Number**: `8`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `maxAge`

The maximum age of the cookie in seconds.

### `same_site`

- **Number**: `9`
- **Cardinality**: `singular`
- **Type**: [`Browser.Cookie.CookieSameSite`](../enums/browser_cookie_cookie_same_site.md)
- **JSON name**: `sameSite`

Affects cross-site request behavior.

### `session`

- **Number**: `10`
- **Cardinality**: `singular`
- **Type**: `bool`
- **JSON name**: `session`

Indicates if the cookie is persistent.

### `partitioned`

- **Number**: `11`
- **Cardinality**: `singular`
- **Type**: `bool`
- **JSON name**: `partitioned`

Shows if the cookies is stored using partitioned storage.
