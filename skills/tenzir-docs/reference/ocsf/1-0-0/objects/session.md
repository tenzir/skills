# Session

> The Session object describes details about an authenticated session. e.g.


The Session object describes details about an authenticated session. e.g. Session Creation Time, Session Issuer. Defined by D3FEND [d3f:Session](https://d3fend.mitre.org/dao/artifact/d3f:Session/).

## Attributes

**`created_time`**

* **Type**: `timestamp_t`
* **Requirement**: recommended

The time when the session was created.

**`is_remote`**

* **Type**: `boolean_t`
* **Requirement**: recommended

The indication of whether the session is remote.

**`issuer`**

* **Type**: `string_t`
* **Requirement**: recommended

The identifier of the session issuer.

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The unique identifier of the session.

**`created_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The time when the session was created.

**`credential_uid`**

* **Type**: `string_t`
* **Requirement**: optional

The unique identifier of the user’s credential. For example, AWS Access Key ID.

**`expiration_time`**

* **Type**: `timestamp_t`
* **Requirement**: optional

The session expiration time.

**`expiration_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The session expiration time.

**`uuid`**

* **Type**: `uuid_t`
* **Requirement**: optional

The universally unique identifier of the session.

## Used By

* [`authentication`](../classes/authentication.md)
* [`authorize_session`](../classes/authorize_session.md)