# FileMetadataPE

Metadata about the Portable Executable (PE) file.

## Fields

### `imphash`

- Type: `string` (singular)

Imphash of the file.

### `entryPoint`

- Type: `int64` (singular)

info.pe-entry-point.

### `entryPointExiftool`

- Type: `int64` (singular)

info.exiftool.EntryPoint.

### `compilationTime`

- Type: `timestamp` (singular)

info.pe-timestamp.

### `compilationExiftoolTime`

- Type: `timestamp` (singular)

info.exiftool.TimeStamp.

### `section`

- Type: [`FileMetadataSection`](file_metadata_section.md) (repeated)

FilemetadataSection fields.

### `imports`

- Type: [`FileMetadataImports`](file_metadata_imports.md) (repeated)

FilemetadataImports fields.

### `resource`

- Type: [`FileMetadataPeResourceInfo`](file_metadata_pe_resource_info.md) (repeated)

FilemetadataPeResourceInfo fields.

### `resourcesTypeCount`

- Type: [`StringToInt64MapEntry`](string_to_int64_map_entry.md) (repeated)
- Deprecated: `true`

Deprecated: use resourcesTypeCountStr.

### `resourcesLanguageCount`

- Type: [`StringToInt64MapEntry`](string_to_int64_map_entry.md) (repeated)
- Deprecated: `true`

Deprecated: use resourcesLanguageCountStr.

### `resourcesTypeCountStr`

- Type: [`Label`](label.md) (repeated)

Number of resources by resource type. Example: RT_ICON: 10, RT_DIALOG: 5

### `resourcesLanguageCountStr`

- Type: [`Label`](label.md) (repeated)

Number of resources by language. Example: NEUTRAL: 20, ENGLISH US: 10

### `signatureInfo`

- Type: [`FileMetadataSignatureInfo`](file_metadata_signature_info.md) (singular)
- Deprecated: `true`

FilemetadataSignatureInfo field. deprecated, user File.signatureInfo instead.
