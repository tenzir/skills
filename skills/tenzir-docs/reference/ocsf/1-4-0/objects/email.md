# Email

> The Email object describes the email metadata such as sender, recipients, and direction, and can include embedded URLs and files.


The Email object describes the email metadata such as sender, recipients, and direction, and can include embedded URLs and files.

## Attributes

**`data_classification`**

* **Type**: [`data_classification`](data_classification.md)
* **Requirement**: recommended

The Data Classification object includes information about data classification levels and data category types.

**`data_classifications`**

* **Type**: [`data_classification`](data_classification.md)
* **Requirement**: recommended

A list of Data Classification objects, that include information about data classification levels and data category types, indentified by a classifier.

**`from`**

* **Type**: `email_t`
* **Requirement**: recommended

The machine-readable email header From values, as defined by RFC 5322. For example `example.user@usersdomain.com`

**`message_uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The email header Message-ID value, as defined by RFC 5322.

**`reply_to`**

* **Type**: `email_t`
* **Requirement**: recommended

The machine-readable email header Reply-To values, as defined by RFC 5322. For example `example.user@usersdomain.com`

**`size`**

* **Type**: `long_t`
* **Requirement**: recommended

The size in bytes of the email, including attachments.

**`smtp_from`**

* **Type**: `email_t`
* **Requirement**: recommended

The value of the SMTP MAIL FROM command.

**`smtp_to`**

* **Type**: `email_t`
* **Requirement**: recommended

The value of the SMTP envelope RCPT TO command.

**`subject`**

* **Type**: `string_t`
* **Requirement**: recommended

The email header Subject value, as defined by RFC 5322.

**`to`**

* **Type**: `email_t`
* **Requirement**: recommended

The machine-readable email header To values, as defined by RFC 5322. For example `example.user@usersdomain.com`

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The unique identifier of the email thread.

**`cc`**

* **Type**: `email_t`
* **Requirement**: optional

The machine-readable email header Cc values, as defined by RFC 5322. For example `example.user@usersdomain.com`.

**`cc_mailboxes`**

* **Type**: `string_t`
* **Requirement**: optional

The human-readable email header Cc Mailbox values. For example `'Example User &lt;example.user@usersdomain.com&gt;'`.

**`delivered_to`**

* **Type**: `email_t`
* **Requirement**: optional

The machine-readable Delivered-To email header field. For example `example.user@usersdomain.com`

**`delivered_to_list`**

* **Type**: `email_t`
* **Requirement**: optional

The machine-readable Delivered-To email header values. For example `example.user@usersdomain.com`

**`files`**

* **Type**: [`file`](file.md)
* **Requirement**: optional

The files embedded or attached to the email.

**`from_mailbox`**

* **Type**: `string_t`
* **Requirement**: optional

The human-readable email header From Mailbox value. For example `'Example User &lt;example.user@usersdomain.com&gt;'`.

**`http_headers`**

* **Type**: [`http_header`](http_header.md)
* **Requirement**: optional

Additional HTTP headers of an HTTP request or response.

**`raw_header`**

* **Type**: `string_t`
* **Requirement**: optional

The email authentication header.

**`reply_to_mailboxes`**

* **Type**: `string_t`
* **Requirement**: optional

The human-readable email header Reply To Mailbox values. For example `'Example User &lt;example.user@usersdomain.com&gt;'`.

**`to_mailboxes`**

* **Type**: `string_t`
* **Requirement**: optional

The human-readable email header To Mailbox values. For example `'Example User &lt;example.user@usersdomain.com&gt;'`.

**`urls`**

* **Type**: [`url`](url.md)
* **Requirement**: optional

The URLs embedded in the email.

**`x_originating_ip`**

* **Type**: `ip_t`
* **Requirement**: optional

The X-Originating-IP header identifying the emails originating IP address(es).

## Constraints

At least one of: `from`, `to`

## Used By

* [`email_activity`](../classes/email_activity.md)