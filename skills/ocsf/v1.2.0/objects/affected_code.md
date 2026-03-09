# Affected Code (affected_code)

The Affected Code object describes details about a code block identified as vulnerable.

- **Extends**: `object`

## Attributes

### `end_line`

- **Type**: `integer_t`
- **Requirement**: recommended

The line number of the last line of code block identified as vulnerable.

### `file`

- **Type**: `file`
- **Requirement**: required

Details about the file that contains the affected code block.

### `owner`

- **Type**: `user`
- **Requirement**: optional

Details about the user that owns the affected file.

### `remediation`

- **Type**: `remediation`
- **Requirement**: optional

Describes the recommended remediation steps to address identified issue(s).

### `start_line`

- **Type**: `integer_t`
- **Requirement**: recommended

The line number of the first line of code block identified as vulnerable.
