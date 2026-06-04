# NtfsFileMetadata

NTFS-specific file metadata.

- **Full name**: `google.backstory.NtfsFileMetadata`
- **Fields**: `6`

## Fields

### `changeTime`

- Type: `google.protobuf.Timestamp` (singular)

NTFS MFT entry changed timestamp.

### `filenameCreateTime`

- Type: `google.protobuf.Timestamp` (singular)

NTFS $FILE_NAME attribute created timestamp.

### `filenameModifyTime`

- Type: `google.protobuf.Timestamp` (singular)

NTFS $FILE_NAME attribute modified timestamp.

### `filenameAccessTime`

- Type: `google.protobuf.Timestamp` (singular)

NTFS $FILE_NAME attribute accessed timestamp.

### `filenameChangeTime`

- Type: `google.protobuf.Timestamp` (singular)

NTFS $FILE_NAME attribute changed timestamp.

### `usnJournal`

- Type: [`UsnJournal`](usn_journal.md) (repeated)

NTFS USN journal.
