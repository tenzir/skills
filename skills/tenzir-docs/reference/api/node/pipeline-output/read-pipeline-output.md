# Read pipeline output

> post/serve

post`/serve`

Reads events from an existing pipeline output stream. By default, the endpoint uses long polling (`timeout: 5s`) and returns as soon as at least one event is available (`min_events: 1`).

Requires authentication`TenzirToken`

## Request body`application/json`

`serve_id``string`required

The output stream identifier returned when the pipeline was launched.

`continuation_token``string`optional

The continuation token from the previous response. Omit this field for the initial request.

`max_events``integer`optional

The maximum number of events to return.

Default`1024`

`min_events``integer`optional

The minimum number of events to wait for before returning.

Default`1`

`timeout``string`optional

The maximum time to spend on the request. Reaching the timeout returns the available events and is not an error. The timeout must not be greater than 10 seconds.

Default`5s`

`schema``enum`optional

The schema representation to include in the response. Use `exact` for a representation that matches Tenzir's type system exactly, and `never` to omit schema definitions.

Allowed values`legacy``exact``never`

Default`legacy`

Example

```json
{
  "serve_id": "query-1",
  "max_events": 1024,
  "min_events": 1,
  "timeout": "5s",
  "schema": "exact"
}
```

## Responses

200Events are available, the timeout was reached, or the pipeline reached a terminal state.

`next_continuation_token``string | null`required

The token to use when reading the next batch. The value is `null` when the pipeline reached a terminal state.

`state``enum`required

The pipeline state at the time of the request.

Allowed values`running``completed``failed`

`schemas``array<object>`optional

The schemas for the returned events. This field is omitted when the request sets `schema` to `never`.

Array items

`schema_id``string`optional

The unique schema identifier.

`definition``unknown`optional

The schema definition in JSON format.

`events``array<object>`required

The returned events.

Array items

`schema_id``string`optional

The unique schema identifier.

`data``object`optional

The event data in JSON format.

Example

```json
{
  "next_continuation_token": "340ce2j",
  "state": "running",
  "schemas": [
    {
      "schema_id": "c631d301e4b18f4",
      "definition": {
        "name": "tenzir.summarize",
        "kind": "record",
        "type": "tenzir.summarize",
        "attributes": {},
        "path": [],
        "fields": []
      }
    }
  ],
  "events": [
    {
      "schema_id": "c631d301e4b18f4",
      "data": {
        "timestamp": "2023-04-26T12:00:00Z",
        "schema": "zeek.conn",
        "events": 50
      }
    }
  ]
}
```

400The request body is invalid.

`error``string`required

The error message.
