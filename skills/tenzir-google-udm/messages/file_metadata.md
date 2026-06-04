# FileMetadata

Metadata about a file. Place metadata about different file types here, for example data from the Microsoft Windows VersionInfo block or digital signer details. Use a different sub-message per file type.

- **Full name**: `google.backstory.FileMetadata`
- **Fields**: `1`

## Fields

### `pe`

- Type: [`PeFileMetadata`](pe_file_metadata.md) (singular)
- Deprecated: `true`

Metadata for Microsoft Windows PE files. Deprecate PeFileMetadata in favor of single File proto.
