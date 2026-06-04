# File

Information about a file.

## Fields

### `sha256`

- Type: `string` (singular)

The SHA256 hash of the file, as a hex-encoded string. This field can be used as an entity indicator for file entities.

### `md5`

- Type: `string` (singular)

The MD5 hash of the file, as a hex-encoded string. This field can be used as an entity indicator for file entities.

### `sha1`

- Type: `string` (singular)

The SHA1 hash of the file, as a hex-encoded string. This field can be used as an entity indicator for file entities.

### `size`

- Type: `uint64` (singular)

The size of the file in bytes.

### `fullPath`

- Type: `string` (singular)

The full path identifying the location of the file on the system. This field can be used as an entity indicator for file entities.

### `mimeType`

- Type: `string` (singular)

The MIME (Multipurpose Internet Mail Extensions) type of the file, for example "PE", "PDF", or "powershell script".

### `fileMetadata`

- Type: [`FileMetadata`](file_metadata.md) (singular)
- Deprecated: `true`

Metadata associated with the file. Deprecate FileMetadata in favor of using fields in File.

### `securityResult`

- Type: [`SecurityResult`](security_result.md) (singular)

Google Cloud Threat Intelligence (GCTI) security result for the file including threat context and detection metadata.

### `peFile`

- Type: [`FileMetadataPE`](file_metadata_pe.md) (singular)

Metadata about the Portable Executable (PE) file.

### `ssdeep`

- Type: `string` (singular)

Ssdeep of the file

### `vhash`

- Type: `string` (singular)

Vhash of the file.

### `ahash`

- Type: `string` (singular)
- Deprecated: `true`

Deprecated. Use authentihash instead.

### `authentihash`

- Type: `string` (singular)

Authentihash of the file.

### `symhash`

- Type: `string` (singular)

SymHash of the file. Used for Mach-O (e.g. MacOS) binaries, to identify similar files based on their symbol table.

### `prefetchFileMetadata`

- Type: [`PrefetchFileMetadata`](prefetch_file_metadata.md) (singular)

Metadata about the prefetch file.

### `fileType`

- Type: [`FileType`](../enums/file_file_type.md) (singular)

FileType field.

### `capabilitiesTags`

- Type: `string` (repeated)

Capabilities tags.

### `names`

- Type: `string` (repeated)

Names fields.

### `tags`

- Type: `string` (repeated)

Tags for the file.

### `lastModificationTime`

- Type: `timestamp` (singular)

Timestamp when the file was last updated.

### `createTime`

- Type: `timestamp` (singular)

Timestamp when the file was created.

### `lastAccessTime`

- Type: `timestamp` (singular)

Timestamp when the file was accessed.

### `prevalence`

- Type: [`Prevalence`](prevalence.md) (singular)

Prevalence of the file hash in the customer's environment.

### `firstSeenTime`

- Type: `timestamp` (singular)

Timestamp the file was first seen in the customer's environment.

### `lastSeenTime`

- Type: `timestamp` (singular)

Timestamp the file was last seen in the customer's environment.

### `statMode`

- Type: `uint64` (singular)

The mode of the file. A bit string indicating the permissions and privileges of the file.

### `statInode`

- Type: `uint64` (singular)

The file identifier. Unique identifier of object within a file system.

### `statDev`

- Type: `uint64` (singular)

The file system identifier to which the object belongs.

### `statNlink`

- Type: `uint64` (singular)

Number of links to file.

### `statFlags`

- Type: `uint32` (singular)

User defined flags for file.

### `lastAnalysisTime`

- Type: `timestamp` (singular)

Timestamp the file was last analysed.

### `embeddedUrls`

- Type: `string` (repeated)

Embedded urls found in the file.

### `embeddedDomains`

- Type: `string` (repeated)

Embedded domains found in the file.

### `embeddedIps`

- Type: `string` (repeated)

Embedded IP addresses found in the file.

### `exifInfo`

- Type: [`ExifInfo`](exif_info.md) (singular)

Exif metadata from different file formats extracted by exiftool.

### `signatureInfo`

- Type: [`SignatureInfo`](signature_info.md) (singular)

File signature information extracted from different tools.

### `pdfInfo`

- Type: [`PDFInfo`](pdf_info.md) (singular)

Information about the PDF file structure.

### `firstSubmissionTime`

- Type: `timestamp` (singular)

First submission time of the file.

### `lastSubmissionTime`

- Type: `timestamp` (singular)

Last submission time of the file.

### `mainIcon`

- Type: [`Favicon`](favicon.md) (singular)

Icon's relevant hashes.

### `ntfs`

- Type: [`NtfsFileMetadata`](ntfs_file_metadata.md) (singular)

NTFS metadata.

### `appCompatCache`

- Type: [`AppCompatMetadata`](app_compat_metadata.md) (singular)

Windows AppCompatCache (Application Compatibility) metadata.

## Guidance

Population guidance from the Google UDM usage guide.

### `File.fileMetadata`

- **Purpose**: Metadata associated with the file.
- **Encoding**: String.

#### Examples

- Author
- Revision number
- Version number
- Date last saved

### `File.fullPath`

- **Purpose**: Full path identifying the location of the file on the system.
- **Encoding**: String.
- **Example**: \Program Files\Custom Utilities\`Test.exe`

#### Examples

- \Program Files\Custom Utilities\Test.exe

### `File.md5`

- **Purpose**: MD5 hash value for the file.
- **Encoding**: String, lower-case hexadecimal.
- **Example**: 35bf623e7db9bf0d68d0dda764fd9e8c

#### Examples

- 35bf623e7db9bf0d68d0dda764fd9e8c

### `File.mimeType`

- **Purpose**: Multipurpose Internet Mail Extensions (MIME) type for the file.
- **Encoding**: String.

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
