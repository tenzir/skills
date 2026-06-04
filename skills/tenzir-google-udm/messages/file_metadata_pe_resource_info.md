# FileMetadataPeResourceInfo

File metadata for PE resource.

## Fields

### `sha256Hex`

- Type: `string` (singular)

SHA256_hex field..

### `filetypeMagic`

- Type: `string` (singular)

Type of resource content, as identified by the magic Python module.

### `languageCode`

- Type: `string` (singular)

Human-readable version of the language and sublanguage identifiers, as defined in the Microsoft Windows PE specification.

### `entropy`

- Type: `double` (singular)

Entropy of the resource.

### `fileType`

- Type: `string` (singular)

File type. Note that this value may not match any of the well-known type identifiers defined in the ResourceType enum.
