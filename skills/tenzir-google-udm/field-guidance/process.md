# Process Field Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`
- **License**: Content licensed under Creative Commons Attribution 4.0; code samples licensed under Apache 2.0, as stated in the Google Developers Site Policies.

## Schema

- [Process](../messages/process.md)

## Fields

### `Process.command_line`

- **Purpose**: Stores the command line string for the process.
- **Encoding**: String.
- **Example**: c:\windows\system32\net.exe group.

#### Examples

- c:\windows\system32\net.exe group.

### `Process.file`

- **Purpose**: Stores the filename of the file in use by the process.
- **Encoding**: String.
- **Example**: report.xls

#### Examples

- report.xls

### `Process.parent_process`

- **Purpose**: Stores the details of the parent process.
- **Encoding**: Noun (Process)

### `Process.parent_process.product_specific_process_id`

- **Purpose**: Stores the product specific process ID for the parent process.
- **Encoding**: String.
- **Examples**: MySQL:78778 or CS:90512

#### Examples

- MySQL:78778 or CS:90512

### `Process.pid`

- **Purpose**: Stores the process ID.
- **Encoding**: String.
- **Examples**: 308 2002

#### Examples

- 308
- 2002

### `Process.product_specific_process_id`

- **Purpose**: Stores the product specific process ID.
- **Encoding**: String.
- **Examples**: MySQL:78778 or CS:90512

#### Examples

- MySQL:78778 or CS:90512
