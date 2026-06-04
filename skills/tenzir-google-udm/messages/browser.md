# Browser

Information about an entry in the web browser's local history database.

- **Full name**: `google.backstory.Browser`
- **Fields**: `16`
- **Nested messages**: `1`
- **Nested enums**: `3`

## Nested messages

- [Browser.Cookie](browser_cookie.md)

## Nested enums

- [Browser.BrowserType](../enums/browser_browser_type.md)
- [Browser.UrlVisitType](../enums/browser_url_visit_type.md)
- [Browser.VisitSource](../enums/browser_visit_source.md)

## Fields

### `browserType`

- Type: [`Browser.BrowserType`](../enums/browser_browser_type.md) (singular)

The browser that recorded the history entry (e.g. "Chrome", "Firefox", "Safari", etc.).

### `browserVersion`

- Type: `string` (singular)

The browser version.

### `firstVisitTime`

- Type: `google.protobuf.Timestamp` (singular)

The timestamp indicating the initial visit to the URL.

### `lastVisitTime`

- Type: `google.protobuf.Timestamp` (singular)

The timestamp indicating the most recent visit to the URL.

### `profile`

- Type: `string` (singular)

The browser profile associated with the history entry.

### `typed`

- Type: `bool` (singular)

A boolean value indicating if the URL was typed by the user.

### `visitType`

- Type: [`Browser.UrlVisitType`](../enums/browser_url_visit_type.md) (singular)

Describes the type of navigation or visit (e.g., direct, redirect, etc.).

### `hidden`

- Type: `bool` (singular)

A boolean value indicating if the history entry is hidden.

### `requestOriginUri`

- Type: `string` (singular)

Indicates the URI from which the current visit originated.

### `visitCount`

- Type: `int64` (singular)

The total number of times the Url has been visited.

### `visitCountCriteria`

- Type: `string` (singular)

Describes the criteria used to calculate the visitCount.

### `indexedContent`

- Type: `string` (singular)

Represents the textual content of a web page. This field should be kept short. Large strings may affect latency and payload sizes.

### `firstBookmarkedTime`

- Type: `google.protobuf.Timestamp` (singular)

The timestamp indicating the first time the URL was bookmarked.

### `cookies`

- Type: [`Browser.Cookie`](browser_cookie.md) (repeated)

Information about the cookies.

### `typedCount`

- Type: `int64` (singular)

The number of times the URL was visited with this specific visit type and visit source.

### `visitSource`

- Type: [`Browser.VisitSource`](../enums/browser_visit_source.md) (singular)

The source of the visit.
