# Browser

Information about an entry in the web browser's local history database.

## Fields

### `browser_type` / `browserType`

- Type: [`BrowserType`](../enums/browser_browser_type.md) (singular)

The browser that recorded the history entry (e.g. "Chrome", "Firefox", "Safari", etc.).

### `browser_version` / `browserVersion`

- Type: `string` (singular)

The browser version.

### `first_visit_time` / `firstVisitTime`

- Type: `timestamp` (singular)

The timestamp indicating the initial visit to the URL.

### `last_visit_time` / `lastVisitTime`

- Type: `timestamp` (singular)

The timestamp indicating the most recent visit to the URL.

### `profile`

- Type: `string` (singular)

The browser profile associated with the history entry.

### `typed`

- Type: `bool` (singular)

A boolean value indicating if the URL was typed by the user.

### `visit_type` / `visitType`

- Type: [`UrlVisitType`](../enums/browser_url_visit_type.md) (singular)

Describes the type of navigation or visit (e.g., direct, redirect, etc.).

### `hidden`

- Type: `bool` (singular)

A boolean value indicating if the history entry is hidden.

### `request_origin_uri` / `requestOriginUri`

- Type: `string` (singular)

Indicates the URI from which the current visit originated.

### `visit_count` / `visitCount`

- Type: `int64` (singular)

The total number of times the Url has been visited.

### `visit_count_criteria` / `visitCountCriteria`

- Type: `string` (singular)

Describes the criteria used to calculate the visit_count.

### `indexed_content` / `indexedContent`

- Type: `string` (singular)

Represents the textual content of a web page. This field should be kept short. Large strings may affect latency and payload sizes.

### `first_bookmarked_time` / `firstBookmarkedTime`

- Type: `timestamp` (singular)

The timestamp indicating the first time the URL was bookmarked.

### `cookies`

- Type: [`Cookie`](browser_cookie.md) (repeated)

Information about the cookies.

### `typed_count` / `typedCount`

- Type: `int64` (singular)

The number of times the URL was visited with this specific visit type and visit source.

### `visit_source` / `visitSource`

- Type: [`VisitSource`](../enums/browser_visit_source.md) (singular)

The source of the visit.
