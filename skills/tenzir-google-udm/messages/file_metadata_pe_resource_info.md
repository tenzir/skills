# FileMetadataPeResourceInfo

File metadata for PE resource.

- **Full name**: `google.backstory.FileMetadataPeResourceInfo`
- **Fields**: `5`

## Fields

### `sha256_hex`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `sha256Hex`

SHA256_hex field..

### `filetype_magic`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `filetypeMagic`

Type of resource content, as identified by the magic Python module.

### `language_code`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `languageCode`

Human-readable version of the language and sublanguage identifiers, as defined in the Microsoft Windows PE specification.

### `entropy`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: `double`
- **JSON name**: `entropy`

Entropy of the resource.

### `file_type`

- **Number**: `6`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `fileType`

File type. Note that this value may not match any of the well-known type identifiers defined in the ResourceType enum.
