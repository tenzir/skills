# FileMetadataPE

Metadata about the Portable Executable (PE) file.

- **Full name**: `google.backstory.FileMetadataPE`
- **Fields**: `13`

## Fields

### `imphash`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `imphash`

Imphash of the file.

### `entry_point`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `entryPoint`

info.pe-entry-point.

### `entry_point_exiftool`

- **Number**: `9`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `entryPointExiftool`

info.exiftool.EntryPoint.

### `compilation_time`

- **Number**: `10`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp`
- **JSON name**: `compilationTime`

info.pe-timestamp.

### `compilation_exiftool_time`

- **Number**: `11`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp`
- **JSON name**: `compilationExiftoolTime`

info.exiftool.TimeStamp.

### `section`

- **Number**: `3`
- **Cardinality**: `repeated`
- **Type**: [`FileMetadataSection`](file_metadata_section.md)
- **JSON name**: `section`

FilemetadataSection fields.

### `imports`

- **Number**: `4`
- **Cardinality**: `repeated`
- **Type**: [`FileMetadataImports`](file_metadata_imports.md)
- **JSON name**: `imports`

FilemetadataImports fields.

### `resource`

- **Number**: `5`
- **Cardinality**: `repeated`
- **Type**: [`FileMetadataPeResourceInfo`](file_metadata_pe_resource_info.md)
- **JSON name**: `resource`

FilemetadataPeResourceInfo fields.

### `resources_type_count`

- **Number**: `6`
- **Cardinality**: `repeated`
- **Type**: [`StringToInt64MapEntry`](string_to_int64_map_entry.md)
- **JSON name**: `resourcesTypeCount`
- **Deprecated**: `true`

Deprecated: use resources_type_count_str.

### `resources_language_count`

- **Number**: `7`
- **Cardinality**: `repeated`
- **Type**: [`StringToInt64MapEntry`](string_to_int64_map_entry.md)
- **JSON name**: `resourcesLanguageCount`
- **Deprecated**: `true`

Deprecated: use resources_language_count_str.

### `resources_type_count_str`

- **Number**: `12`
- **Cardinality**: `repeated`
- **Type**: [`Label`](label.md)
- **JSON name**: `resourcesTypeCountStr`

Number of resources by resource type. Example: RT_ICON: 10, RT_DIALOG: 5

### `resources_language_count_str`

- **Number**: `13`
- **Cardinality**: `repeated`
- **Type**: [`Label`](label.md)
- **JSON name**: `resourcesLanguageCountStr`

Number of resources by language. Example: NEUTRAL: 20, ENGLISH US: 10

### `signature_info`

- **Number**: `8`
- **Cardinality**: `singular`
- **Type**: [`FileMetadataSignatureInfo`](file_metadata_signature_info.md)
- **JSON name**: `signatureInfo`
- **Deprecated**: `true`

FilemetadataSignatureInfo field. deprecated, user File.signature_info instead.
