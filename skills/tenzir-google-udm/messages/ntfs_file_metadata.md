# NtfsFileMetadata

NTFS-specific file metadata.

- **Full name**: `google.backstory.NtfsFileMetadata`
- **Fields**: `6`

## Fields

### `change_time`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp` (imported)
- **JSON name**: `changeTime`

NTFS MFT entry changed timestamp.

### `filename_create_time`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp` (imported)
- **JSON name**: `filenameCreateTime`

NTFS $FILE_NAME attribute created timestamp.

### `filename_modify_time`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp` (imported)
- **JSON name**: `filenameModifyTime`

NTFS $FILE_NAME attribute modified timestamp.

### `filename_access_time`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp` (imported)
- **JSON name**: `filenameAccessTime`

NTFS $FILE_NAME attribute accessed timestamp.

### `filename_change_time`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp` (imported)
- **JSON name**: `filenameChangeTime`

NTFS $FILE_NAME attribute changed timestamp.

### `usn_journal`

- **Number**: `6`
- **Cardinality**: `repeated`
- **Type**: [`UsnJournal`](usn_journal.md)
- **JSON name**: `usnJournal`

NTFS USN journal.
