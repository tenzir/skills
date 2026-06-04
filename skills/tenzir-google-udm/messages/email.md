# Email

Email info.

- **Full name**: `google.backstory.Email`
- **Fields**: `8`

## Fields

### `from`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `from`

The 'from' address.

### `reply_to`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `replyTo`

The 'reply to' address.

### `to`

- **Number**: `3`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `to`

A list of 'to' addresses.

### `cc`

- **Number**: `4`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `cc`

A list of 'cc' addresses.

### `bcc`

- **Number**: `5`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `bcc`

A list of 'bcc' addresses.

### `mail_id`

- **Number**: `6`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `mailId`

The mail (or message) ID.

### `subject`

- **Number**: `7`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `subject`

The subject line(s) of the email.

### `bounce_address`

- **Number**: `8`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `bounceAddress`

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
