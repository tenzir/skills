# FileMetadataPE

Metadata about the Portable Executable (PE) file.

## Fields

### `imphash`

- Type: `string` (singular)

Imphash of the file.

### `entry_point` / `entryPoint`

- Type: `int64` (singular)

info.pe-entry-point.

### `entry_point_exiftool` / `entryPointExiftool`

- Type: `int64` (singular)

info.exiftool.EntryPoint.

### `compilation_time` / `compilationTime`

- Type: `timestamp` (singular)

info.pe-timestamp.

### `compilation_exiftool_time` / `compilationExiftoolTime`

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

### `resources_type_count` / `resourcesTypeCount`

- Type: [`StringToInt64MapEntry`](string_to_int64_map_entry.md) (repeated)
- Deprecated: `true`

Deprecated: use resources_type_count_str.

### `resources_language_count` / `resourcesLanguageCount`

- Type: [`StringToInt64MapEntry`](string_to_int64_map_entry.md) (repeated)
- Deprecated: `true`

Deprecated: use resources_language_count_str.

### `resources_type_count_str` / `resourcesTypeCountStr`

- Type: [`Label`](label.md) (repeated)

Number of resources by resource type. Example: RT_ICON: 10, RT_DIALOG: 5

### `resources_language_count_str` / `resourcesLanguageCountStr`

- Type: [`Label`](label.md) (repeated)

Number of resources by language. Example: NEUTRAL: 20, ENGLISH US: 10

### `signature_info` / `signatureInfo`

- Type: [`FileMetadataSignatureInfo`](file_metadata_signature_info.md) (singular)
- Deprecated: `true`

FilemetadataSignatureInfo field. deprecated, user File.signature_info instead.
