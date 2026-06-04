# File Field Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`
- **License**: Content licensed under Creative Commons Attribution 4.0; code samples licensed under Apache 2.0, as stated in the Google Developers Site Policies.

## Schema

- [File](../messages/file.md)

## Fields

### `File.file_metadata`

- **Purpose**: Metadata associated with the file.
- **Encoding**: String.
- **Examples**: Author Revision number Version number Date last saved

#### Examples

- Author
- Revision number
- Version number
- Date last saved

### `File.full_path`

- **Purpose**: Full path identifying the location of the file on the system.
- **Encoding**: String.
- **Example**: \Program Files\Custom Utilities\Test.exe

#### Examples

- \Program Files\Custom Utilities\Test.exe

### `File.md5`

- **Purpose**: MD5 hash value for the file.
- **Encoding**: String, lower-case hexadecimal.
- **Example**: 35bf623e7db9bf0d68d0dda764fd9e8c

#### Examples

- 35bf623e7db9bf0d68d0dda764fd9e8c

### `File.mime_type`

- **Purpose**: Multipurpose Internet Mail Extensions (MIME) type for the file.
- **Encoding**: String.
- **Examples**: PE PDF powershell script

#### Examples

- PE
- PDF
- powershell script

### `File.sha1`

- **Purpose**: SHA-1 hash value for the file.
- **Encoding**: String, lower-case hexadecimal.
- **Example**: eb3520d53b45815912f2391b713011453ed8abcf

#### Examples

- eb3520d53b45815912f2391b713011453ed8abcf

### `File.sha256`

- **Purpose**: SHA-256 hash value for the file.
- **Encoding**: String, lower-case hexadecimal.
- **Example**: d7173c568b8985e61b4050f81b3fd8e75bc922d2a0843d7079c81ca4b6e36417

#### Examples

- d7173c568b8985e61b4050f81b3fd8e75bc922d2a0843d7079c81ca4b6e36417

### `File.size`

- **Purpose**: Size of the file.
- **Encoding**: 64-bit unsigned integer.
- **Example**: 342135

#### Examples

- 342135
