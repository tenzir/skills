# Browser.Cookie

Browser cookie.

- **Full name**: `google.backstory.Browser.Cookie`
- **Fields**: `11`
- **Nested enums**: `1`

## Nested enums

- [Browser.Cookie.CookieSameSite](../enums/browser_cookie_cookie_same_site.md)

## Fields

### `name`

- Type: `string` (singular)

The unique name identifying the cookie.

### `value`

- Type: `string` (singular)

The data stored within the cookie.

### `domain`

- Type: `string` (singular)

The domain for which the cookie is valid.

### `path`

- Type: `string` (singular)

The URL path for which the cookie is valid.

### `expirationTime`

- Type: `google.protobuf.Timestamp` (singular)

The date and time when the cookie will expire.

### `httpOnly`

- Type: `bool` (singular)

Indicates if the cookie is inaccessible via client-side scripts (e.g., JavaScript).

### `secure`

- Type: `bool` (singular)

Indicates if the cookie should only be sent over secure HTTPS connections.

### `maxAge`

- Type: `int64` (singular)

The maximum age of the cookie in seconds.

### `sameSite`

- Type: [`Browser.Cookie.CookieSameSite`](../enums/browser_cookie_cookie_same_site.md) (singular)

Affects cross-site request behavior.

### `session`

- Type: `bool` (singular)

Indicates if the cookie is persistent.

### `partitioned`

- Type: `bool` (singular)

Shows if the cookies is stored using partitioned storage.
