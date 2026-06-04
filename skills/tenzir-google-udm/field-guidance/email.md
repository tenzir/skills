# Email Field Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`

## Schema

- [Email](../messages/email.md)

## Fields

### `Email.bcc`

- **Purpose**: Stores the bcc email addresses.
- **Encoding**: String.

### `Email.cc`

- **Purpose**: Stores the cc email addresses.
- **Encoding**: String.

### `Email.from`

- **Purpose**: Stores the from email address.
- **Encoding**: String.

### `Email.mail_id`

- **Purpose**: Stores the mail (or message) id.
- **Encoding**: String.
- **Example**: 192544.132632@email.example.com

#### Examples

- 192544.132632@email.example.com

### `Email.reply_to`

- **Purpose**: Stores the reply_to email address.
- **Encoding**: String.

### `Email.subject`

- **Purpose**: Stores the email subject line.
- **Encoding**: String.
- **Example**: "Please read this message."

#### Examples

- "Please read this message."

### `Email.to`

- **Purpose**: Stores the to email addresses.
- **Encoding**: String.
