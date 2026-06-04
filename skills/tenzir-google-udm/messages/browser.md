# Browser

Information about an entry in the web browser's local history database.

## Fields

### `browserType`

- Type: [`BrowserType`](../enums/browser_browser_type.md) (singular)

The browser that recorded the history entry (e.g. "Chrome", "Firefox", "Safari", etc.).

### `browserVersion`

- Type: `string` (singular)

The browser version.

### `firstVisitTime`

- Type: `timestamp` (singular)

The timestamp indicating the initial visit to the URL.

### `lastVisitTime`

- Type: `timestamp` (singular)

The timestamp indicating the most recent visit to the URL.

### `profile`

- Type: `string` (singular)

The browser profile associated with the history entry.

### `typed`

- Type: `bool` (singular)

A boolean value indicating if the URL was typed by the user.

### `visitType`

- Type: [`UrlVisitType`](../enums/browser_url_visit_type.md) (singular)

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

- Type: `timestamp` (singular)

The timestamp indicating the first time the URL was bookmarked.

### `cookies`

- Type: [`Cookie`](browser_cookie.md) (repeated)

Information about the cookies.

### `typedCount`

- Type: `int64` (singular)

The number of times the URL was visited with this specific visit type and visit source.

### `visitSource`

- Type: [`VisitSource`](../enums/browser_visit_source.md) (singular)

The source of the visit.
