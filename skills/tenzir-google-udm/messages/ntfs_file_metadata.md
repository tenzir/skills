# NtfsFileMetadata

NTFS-specific file metadata.

## Fields

### `change_time` / `changeTime`

- Type: `timestamp` (singular)

NTFS MFT entry changed timestamp.

### `filename_create_time` / `filenameCreateTime`

- Type: `timestamp` (singular)

NTFS $FILE_NAME attribute created timestamp.

### `filename_modify_time` / `filenameModifyTime`

- Type: `timestamp` (singular)

NTFS $FILE_NAME attribute modified timestamp.

### `filename_access_time` / `filenameAccessTime`

- Type: `timestamp` (singular)

NTFS $FILE_NAME attribute accessed timestamp.

### `filename_change_time` / `filenameChangeTime`

- Type: `timestamp` (singular)

NTFS $FILE_NAME attribute changed timestamp.

### `usn_journal` / `usnJournal`

- Type: [`UsnJournal`](usn_journal.md) (repeated)

NTFS USN journal.
