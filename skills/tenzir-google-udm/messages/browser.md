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

### `browser_type`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: [`Browser.BrowserType`](../enums/browser_browser_type.md)
- **JSON name**: `browserType`

The browser that recorded the history entry (e.g. "Chrome", "Firefox", "Safari", etc.).

### `browser_version`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `browserVersion`

The browser version.

### `first_visit_time`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp`
- **JSON name**: `firstVisitTime`

The timestamp indicating the initial visit to the URL.

### `last_visit_time`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp`
- **JSON name**: `lastVisitTime`

The timestamp indicating the most recent visit to the URL.

### `profile`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `profile`

The browser profile associated with the history entry.

### `typed`

- **Number**: `6`
- **Cardinality**: `singular`
- **Type**: `bool`
- **JSON name**: `typed`

A boolean value indicating if the URL was typed by the user.

### `visit_type`

- **Number**: `7`
- **Cardinality**: `singular`
- **Type**: [`Browser.UrlVisitType`](../enums/browser_url_visit_type.md)
- **JSON name**: `visitType`

Describes the type of navigation or visit (e.g., direct, redirect, etc.).

### `hidden`

- **Number**: `8`
- **Cardinality**: `singular`
- **Type**: `bool`
- **JSON name**: `hidden`

A boolean value indicating if the history entry is hidden.

### `request_origin_uri`

- **Number**: `9`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `requestOriginUri`

Indicates the URI from which the current visit originated.

### `visit_count`

- **Number**: `10`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `visitCount`

The total number of times the Url has been visited.

### `visit_count_criteria`

- **Number**: `11`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `visitCountCriteria`

Describes the criteria used to calculate the visit_count.

### `indexed_content`

- **Number**: `12`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `indexedContent`

Represents the textual content of a web page. This field should be kept short. Large strings may affect latency and payload sizes.

### `first_bookmarked_time`

- **Number**: `13`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp`
- **JSON name**: `firstBookmarkedTime`

The timestamp indicating the first time the URL was bookmarked.

### `cookies`

- **Number**: `14`
- **Cardinality**: `repeated`
- **Type**: [`Browser.Cookie`](browser_cookie.md)
- **JSON name**: `cookies`

Information about the cookies.

### `typed_count`

- **Number**: `15`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `typedCount`

The number of times the URL was visited with this specific visit type and visit source.

### `visit_source`

- **Number**: `16`
- **Cardinality**: `singular`
- **Type**: [`Browser.VisitSource`](../enums/browser_visit_source.md)
- **JSON name**: `visitSource`

The source of the visit.
