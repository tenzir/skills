# Email

Email info.

## Fields

### `from`

- Type: `string` (singular)

The 'from' address.

### `reply_to` / `replyTo`

- Type: `string` (singular)

The 'reply to' address.

### `to`

- Type: `string` (repeated)

A list of 'to' addresses.

### `cc`

- Type: `string` (repeated)

A list of 'cc' addresses.

### `bcc`

- Type: `string` (repeated)

A list of 'bcc' addresses.

### `mail_id` / `mailId`

- Type: `string` (singular)

The mail (or message) ID.

### `subject`

- Type: `string` (repeated)

The subject line(s) of the email.

### `bounce_address` / `bounceAddress`

- Type: `string` (singular)

The envelope from address. [https://en.wikipedia.org/wiki/Bounce_address](https://en.wikipedia.org/wiki/Bounce_address)

## Guidance

Population guidance from the Google UDM usage guide.

### `bcc`

- **Purpose**: Stores the bcc email addresses.
- **Encoding**: String.

### `cc`

- **Purpose**: Stores the cc email addresses.
- **Encoding**: String.

### `from`

- **Purpose**: Stores the from email address.
- **Encoding**: String.

### `mail_id` / `mailId`

- **Purpose**: Stores the mail (or message) id.
- **Encoding**: String.
- **Example**: 192544.132632@email.example.com

#### Examples

- 192544.132632@email.example.com

### `reply_to` / `replyTo`

- **Purpose**: Stores the reply_to email address.
- **Encoding**: String.

### `subject`

- **Purpose**: Stores the email subject line.
- **Encoding**: String.
- **Example**: "Please read this message."

#### Examples

- "Please read this message."

### `to`

- **Purpose**: Stores the to email addresses.
- **Encoding**: String.
