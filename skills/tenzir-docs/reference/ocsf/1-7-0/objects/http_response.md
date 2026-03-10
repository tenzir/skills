# HTTP Response

> The HTTP Response object contains detailed information about the response sent from a web server to the requester.


The HTTP Response object contains detailed information about the response sent from a web server to the requester. It encompasses attributes and metadata that describe the response status, headers, body content, and other relevant information.

## Attributes

**`code`**

* **Type**: `integer_t`
* **Requirement**: required

The Hypertext Transfer Protocol (HTTP) status code returned from the web server to the client. For example, 200.

**`http_headers`**

* **Type**: [`http_header`](http_header.md)
* **Requirement**: recommended

Additional HTTP headers of an HTTP request or response.

**`body_length`**

* **Type**: `integer_t`
* **Requirement**: optional

The actual length of the HTTP response body, in number of bytes, independent of a potentially existing Content-Length header.

**`content_type`**

* **Type**: `string_t`
* **Requirement**: optional

The request header that identifies the original [media type](https://www.iana.org/assignments/media-types/media-types.xhtml) of the resource (prior to any content encoding applied for sending).

**`latency`**

* **Type**: `integer_t`
* **Requirement**: optional

The HTTP response latency measured in milliseconds.

**`length`**

* **Type**: `integer_t`
* **Requirement**: optional

The length of the entire HTTP response, in number of bytes.

**`message`**

* **Type**: `string_t`
* **Requirement**: optional

The description of the event/finding, as defined by the source.

**`status`**

* **Type**: `string_t`
* **Requirement**: optional

The response status. For example: A successful HTTP status of ‘OK’ which corresponds to a code of 200.

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