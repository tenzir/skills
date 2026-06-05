# FileMetadataPeResourceInfo

File metadata for PE resource.

## Fields

### `sha256_hex` / `sha256Hex`

- Type: `string` (singular)

SHA256_hex field..

### `filetype_magic` / `filetypeMagic`

- Type: `string` (singular)

Type of resource content, as identified by the magic Python module.

### `language_code` / `languageCode`

- Type: `string` (singular)

Human-readable version of the language and sublanguage identifiers, as defined in the Microsoft Windows PE specification.

### `entropy`

- Type: `double` (singular)

Entropy of the resource.

### `file_type` / `fileType`

- Type: `string` (singular)

File type. Note that this value may not match any of the well-known type identifiers defined in the ResourceType enum.
