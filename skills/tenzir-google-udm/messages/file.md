# File

Information about a file.

- **Full name**: `google.backstory.File`
- **Fields**: `42`
- **Nested enums**: `1`

## Nested enums

- [File.FileType](../enums/file_file_type.md)

## Fields

### `sha256`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `sha256`

The SHA256 hash of the file, as a hex-encoded string. This field can be used as an entity indicator for file entities.

### `md5`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `md5`

The MD5 hash of the file, as a hex-encoded string. This field can be used as an entity indicator for file entities.

### `sha1`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `sha1`

The SHA1 hash of the file, as a hex-encoded string. This field can be used as an entity indicator for file entities.

### `size`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: `uint64`
- **JSON name**: `size`

The size of the file in bytes.

### `full_path`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `fullPath`

The full path identifying the location of the file on the system. This field can be used as an entity indicator for file entities.

### `mime_type`

- **Number**: `6`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `mimeType`

The MIME (Multipurpose Internet Mail Extensions) type of the file, for example "PE", "PDF", or "powershell script".

### `file_metadata`

- **Number**: `7`
- **Cardinality**: `singular`
- **Type**: [`FileMetadata`](file_metadata.md)
- **JSON name**: `fileMetadata`
- **Deprecated**: `true`

Metadata associated with the file. Deprecate FileMetadata in favor of using fields in File.

### `security_result`

- **Number**: `36`
- **Cardinality**: `singular`
- **Type**: [`SecurityResult`](security_result.md)
- **JSON name**: `securityResult`

Google Cloud Threat Intelligence (GCTI) security result for the file including threat context and detection metadata.

### `pe_file`

- **Number**: `8`
- **Cardinality**: `singular`
- **Type**: [`FileMetadataPE`](file_metadata_pe.md)
- **JSON name**: `peFile`

Metadata about the Portable Executable (PE) file.

### `ssdeep`

- **Number**: `9`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `ssdeep`

Ssdeep of the file

### `vhash`

- **Number**: `10`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `vhash`

Vhash of the file.

### `ahash`

- **Number**: `11`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `ahash`
- **Deprecated**: `true`

Deprecated. Use authentihash instead.

### `authentihash`

- **Number**: `20`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `authentihash`

Authentihash of the file.

### `symhash`

- **Number**: `41`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `symhash`

SymHash of the file. Used for Mach-O (e.g. MacOS) binaries, to identify similar files based on their symbol table.

### `prefetch_file_metadata`

- **Number**: `43`
- **Cardinality**: `singular`
- **Type**: [`PrefetchFileMetadata`](prefetch_file_metadata.md)
- **JSON name**: `prefetchFileMetadata`

Metadata about the prefetch file.

### `file_type`

- **Number**: `12`
- **Cardinality**: `singular`
- **Type**: [`File.FileType`](../enums/file_file_type.md)
- **JSON name**: `fileType`

FileType field.

### `capabilities_tags`

- **Number**: `13`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `capabilitiesTags`

Capabilities tags.

### `names`

- **Number**: `14`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `names`

Names fields.

### `tags`

- **Number**: `27`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `tags`

Tags for the file.

### `last_modification_time`

- **Number**: `15`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp` (imported)
- **JSON name**: `lastModificationTime`

Timestamp when the file was last updated.

### `create_time`

- **Number**: `39`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp` (imported)
- **JSON name**: `createTime`

Timestamp when the file was created.

### `last_access_time`

- **Number**: `40`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp` (imported)
- **JSON name**: `lastAccessTime`

Timestamp when the file was accessed.

### `prevalence`

- **Number**: `16`
- **Cardinality**: `singular`
- **Type**: [`Prevalence`](prevalence.md)
- **JSON name**: `prevalence`

Prevalence of the file hash in the customer's environment.

### `first_seen_time`

- **Number**: `17`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp` (imported)
- **JSON name**: `firstSeenTime`

Timestamp the file was first seen in the customer's environment.

### `last_seen_time`

- **Number**: `18`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp` (imported)
- **JSON name**: `lastSeenTime`

Timestamp the file was last seen in the customer's environment.

### `stat_mode`

- **Number**: `21`
- **Cardinality**: `singular`
- **Type**: `uint64`
- **JSON name**: `statMode`

The mode of the file. A bit string indicating the permissions and privileges of the file.

### `stat_inode`

- **Number**: `22`
- **Cardinality**: `singular`
- **Type**: `uint64`
- **JSON name**: `statInode`

The file identifier. Unique identifier of object within a file system.

### `stat_dev`

- **Number**: `23`
- **Cardinality**: `singular`
- **Type**: `uint64`
- **JSON name**: `statDev`

The file system identifier to which the object belongs.

### `stat_nlink`

- **Number**: `24`
- **Cardinality**: `singular`
- **Type**: `uint64`
- **JSON name**: `statNlink`

Number of links to file.

### `stat_flags`

- **Number**: `25`
- **Cardinality**: `singular`
- **Type**: `uint32`
- **JSON name**: `statFlags`

User defined flags for file.

### `last_analysis_time`

- **Number**: `26`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp` (imported)
- **JSON name**: `lastAnalysisTime`

Timestamp the file was last analysed.

### `embedded_urls`

- **Number**: `28`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `embeddedUrls`

Embedded urls found in the file.

### `embedded_domains`

- **Number**: `29`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `embeddedDomains`

Embedded domains found in the file.

### `embedded_ips`

- **Number**: `30`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `embeddedIps`

Embedded IP addresses found in the file.

### `exif_info`

- **Number**: `31`
- **Cardinality**: `singular`
- **Type**: [`ExifInfo`](exif_info.md)
- **JSON name**: `exifInfo`

Exif metadata from different file formats extracted by exiftool.

### `signature_info`

- **Number**: `32`
- **Cardinality**: `singular`
- **Type**: [`SignatureInfo`](signature_info.md)
- **JSON name**: `signatureInfo`

File signature information extracted from different tools.

### `pdf_info`

- **Number**: `33`
- **Cardinality**: `singular`
- **Type**: [`PDFInfo`](pdf_info.md)
- **JSON name**: `pdfInfo`

Information about the PDF file structure.

### `first_submission_time`

- **Number**: `34`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp` (imported)
- **JSON name**: `firstSubmissionTime`

First submission time of the file.

### `last_submission_time`

- **Number**: `35`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp` (imported)
- **JSON name**: `lastSubmissionTime`

Last submission time of the file.

### `main_icon`

- **Number**: `37`
- **Cardinality**: `singular`
- **Type**: [`Favicon`](favicon.md)
- **JSON name**: `mainIcon`

Icon's relevant hashes.

### `ntfs`

- **Number**: `38`
- **Cardinality**: `singular`
- **Type**: [`NtfsFileMetadata`](ntfs_file_metadata.md)
- **JSON name**: `ntfs`

NTFS metadata.

### `app_compat_cache`

- **Number**: `42`
- **Cardinality**: `singular`
- **Type**: [`AppCompatMetadata`](app_compat_metadata.md)
- **JSON name**: `appCompatCache`

Windows AppCompatCache (Application Compatibility) metadata.
