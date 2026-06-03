# SignatureInfo

File signature information extracted from different tools.

- **Full name**: `google.backstory.SignatureInfo`
- **Fields**: `2`

## Fields

### `sigcheck`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: [`FileMetadataSignatureInfo`](file_metadata_signature_info.md)
- **JSON name**: `sigcheck`

Signature information extracted from the sigcheck tool.

### `codesign`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: [`FileMetadataCodesign`](file_metadata_codesign.md)
- **JSON name**: `codesign`

Signature information extracted from the codesign utility.
