# Email

Email info.

## Fields

### `from`

- Type: `string` (singular)

The 'from' address.

### `replyTo`

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

### `mailId`

- Type: `string` (singular)

The mail (or message) ID.

### `subject`

- Type: `string` (repeated)

The subject line(s) of the email.

### `bounceAddress`

- Type: `string` (singular)

The envelope from address. [https://en.wikipedia.org/wiki/Bounce_address](https://en.wikipedia.org/wiki/Bounce_address)

## Guidance

Population guidance from the Google UDM usage guide.

### `Email.bcc`

- **Purpose**: Stores the bcc email addresses.
- **Encoding**: String.

### `Email.cc`

- **Purpose**: Stores the cc email addresses.
- **Encoding**: String.

### `Email.from`

- **Purpose**: Stores the from email address.
- **Encoding**: String.

### `Email.mailId`

- **Purpose**: Stores the mail (or message) id.
- **Encoding**: String.
- **Example**: 192544.132632@email.example.com

#### Examples

- 192544.132632@email.example.com

### `Email.replyTo`

- **Purpose**: Stores the `replyTo` email address.
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
