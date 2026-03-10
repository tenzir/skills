# HTTP Cookie

> The HTTP Cookie object, also known as a web cookie or browser cookie, contains details and values pertaining to a small piece of data that a server sends to a user's web browser.


The HTTP Cookie object, also known as a web cookie or browser cookie, contains details and values pertaining to a small piece of data that a server sends to a user’s web browser. This data is then stored by the browser and sent back to the server with subsequent requests, allowing the server to remember and track certain information about the user’s browsing session or preferences.

## Attributes

**`name`**

* **Type**: `string_t`
* **Requirement**: required

The HTTP cookie name.

**`value`**

* **Type**: `string_t`
* **Requirement**: required

The HTTP cookie value.

**`domain`**

* **Type**: `string_t`
* **Requirement**: optional

The domain name for the server from which the http\_cookie is served.

**`expiration_time`**

* **Type**: `timestamp_t`
* **Requirement**: optional

The expiration time of the HTTP cookie.

**`expiration_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The expiration time of the HTTP cookie.

**`http_only`**

* **Type**: `boolean_t`
* **Requirement**: optional

A cookie attribute to make it inaccessible via JavaScript

**`is_http_only`**

* **Type**: `boolean_t`
* **Requirement**: optional

This attribute prevents the cookie from being accessed via JavaScript.

**`is_secure`**

* **Type**: `boolean_t`
* **Requirement**: optional

The cookie attribute indicates that cookies are sent to the server only when the request is encrypted using the HTTPS protocol.

**`path`**

* **Type**: `string_t`
* **Requirement**: optional

The path of the HTTP cookie.

**`samesite`**

* **Type**: `string_t`
* **Requirement**: optional

The cookie attribute that lets servers specify whether/when cookies are sent with cross-site requests. Values are: Strict, Lax or None

**`secure`**

* **Type**: `boolean_t`
* **Requirement**: optional

The cookie attribute to only send cookies to the server with an encrypted request over the HTTPS protocol.

## Used By

* [`http_activity`](../classes/http_activity.md)