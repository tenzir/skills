# http


The `http` operator is deprecated. Use the dedicated HTTP operators instead.

## Migration guide

Choose the replacement that matches how you used `http`:

* [`from_http`](/reference/operators/from_http.md): make outbound requests and parse the response into events.
* [`to_http`](/reference/operators/to_http.md): send events as a single outbound request to a webhook or API.
* [`accept_http`](/reference/operators/accept_http.md): start a server that listen for inbound requests and process their bodies.
* [`serve_http`](/reference/operators/serve_http.md): start a server that streams pipeline output to clients.