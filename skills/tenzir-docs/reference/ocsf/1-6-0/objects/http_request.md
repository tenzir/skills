# HTTP Request

> The HTTP Request object represents the attributes of a request made to a web server.


The HTTP Request object represents the attributes of a request made to a web server. It encapsulates the details and metadata associated with an HTTP request, including the request method, headers, URL, query parameters, body content, and other relevant information.

## Attributes

**`http_headers`**

* **Type**: [`http_header`](http_header.md)
* **Requirement**: recommended

Additional HTTP headers of an HTTP request or response.

**`http_method`**

* **Type**: `string_t`

* **Requirement**: recommended

* **Values**:

  * `OPTIONS` - `Options`: The OPTIONS method describes the communication options for the target resource.
  * `GET` - `Get`: The GET method requests a representation of the specified resource. Requests using GET should only retrieve data.
  * `HEAD` - `Head`: The HEAD method asks for a response identical to a GET request, but without the response body.
  * `POST` - `Post`: The POST method submits an entity to the specified resource, often causing a change in state or side effects on the server.
  * `PUT` - `Put`: The PUT method replaces all current representations of the target resource with the request payload.
  * `DELETE` - `Delete`: The DELETE method deletes the specified resource.
  * `TRACE` - `Trace`: The TRACE method performs a message loop-back test along the path to the target resource.
  * `CONNECT` - `Connect`: The CONNECT method establishes a tunnel to the server identified by the target resource.
  * `PATCH` - `Patch`: The PATCH method applies partial modifications to a resource.

The [HTTP request method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) indicates the desired action to be performed for a given resource.

**`url`**

* **Type**: [`url`](url.md)
* **Requirement**: recommended

The URL object that pertains to the request.

**`user_agent`**

* **Type**: `string_t`
* **Requirement**: recommended

The request header that identifies the operating system and web browser.

**`version`**

* **Type**: `string_t`
* **Requirement**: recommended

The Hypertext Transfer Protocol (HTTP) version.

**`args`**

* **Type**: `string_t`
* **Requirement**: optional

The arguments sent along with the HTTP request.

**`body_length`**

* **Type**: `integer_t`
* **Requirement**: optional

The actual length of the HTTP request body, in number of bytes, independent of a potentially existing Content-Length header.

**`length`**

* **Type**: `integer_t`
* **Requirement**: optional

The length of the entire HTTP request, in number of bytes.

**`referrer`**

* **Type**: `string_t`
* **Requirement**: optional

The request header that identifies the address of the previous web page, which is linked to the current web page or resource being requested.

**`uid`**

* **Type**: `string_t`
* **Requirement**: optional

The unique identifier of the http request.

**`x_forwarded_for`**

* **Type**: `ip_t`
* **Requirement**: optional

The X-Forwarded-For header identifying the originating IP address(es) of a client connecting to a web server through an HTTP proxy or a load balancer.

## Used By

* [`account_change`](../classes/account_change.md)
* [`api_activity`](../classes/api_activity.md)
* [`authentication`](../classes/authentication.md)
* [`authorize_session`](../classes/authorize_session.md)
* [`datastore_activity`](../classes/datastore_activity.md)
* [`dhcp_activity`](../classes/dhcp_activity.md)
* [`dns_activity`](../classes/dns_activity.md)
* [`entity_management`](../classes/entity_management.md)
* [`file_hosting`](../classes/file_hosting.md)
* [`ftp_activity`](../classes/ftp_activity.md)
* [`group_management`](../classes/group_management.md)
* [`http_activity`](../classes/http_activity.md)
* [`network_activity`](../classes/network_activity.md)
* [`network_file_activity`](../classes/network_file_activity.md)
* [`ntp_activity`](../classes/ntp_activity.md)
* [`rdp_activity`](../classes/rdp_activity.md)
* [`smb_activity`](../classes/smb_activity.md)
* [`ssh_activity`](../classes/ssh_activity.md)
* [`tunnel_activity`](../classes/tunnel_activity.md)
* [`user_access`](../classes/user_access.md)
* [`web_resource_access_activity`](../classes/web_resource_access_activity.md)
* [`web_resources_activity`](../classes/web_resources_activity.md)