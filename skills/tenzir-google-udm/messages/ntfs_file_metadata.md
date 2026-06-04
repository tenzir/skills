# NtfsFileMetadata

NTFS-specific file metadata.

## Fields

### `changeTime`

- Type: `timestamp` (singular)

NTFS MFT entry changed timestamp.

### `filenameCreateTime`

- Type: `timestamp` (singular)

NTFS $FILE_NAME attribute created timestamp.

### `filenameModifyTime`

- Type: `timestamp` (singular)

NTFS $FILE_NAME attribute modified timestamp.

### `filenameAccessTime`

- Type: `timestamp` (singular)

NTFS $FILE_NAME attribute accessed timestamp.

### `filenameChangeTime`

- Type: `timestamp` (singular)

NTFS $FILE_NAME attribute changed timestamp.

### `usnJournal`

- Type: [`UsnJournal`](usn_journal.md) (repeated)

NTFS USN journal.
