# UsnJournal.Attribute

File attributes from the USN record (e.g., "READ_ONLY, HIDDEN"). See https://learn.microsoft.com/en-us/windows/win32/fileio/file-attribute-constants for more information about the attributes.

- **Full name**: `google.backstory.UsnJournal.Attribute`
- **Values**: `24`

## Values

### `ATTRIBUTE_UNSPECIFIED`

- **Number**: `0`

Unspecified attribute.

### `READ_ONLY`

- **Number**: `1`

A file that is read-only.

### `HIDDEN`

- **Number**: `2`

The file or directory is hidden.

### `SYSTEM`

- **Number**: `3`

A file or directory that the operating system uses.

### `ARCHIVE`

- **Number**: `4`

Archive file or directory.

### `COMPRESSED`

- **Number**: `5`

A file or directory that is compressed.

### `ENCRYPTED`

- **Number**: `6`

A file or directory that is encrypted.

### `DIRECTORY`

- **Number**: `7`

The handle that identifies the directory.

### `DEVICE`

- **Number**: `8`

Reserved for system use.

### `NORMAL`

- **Number**: `9`

A file that does not have other attributes set.

### `TEMPORARY`

- **Number**: `10`

A file that is being used for temporary storage.

### `SPARSE_FILE`

- **Number**: `11`

A file that is a sparse file.

### `REPARSE_POINT`

- **Number**: `12`

A file or directory that has an associated reparse point.

### `OFFLINE`

- **Number**: `13`

The data of a file is not available immediately.

### `NOT_CONTENT_INDEXED`

- **Number**: `14`

The file or directory is not to be indexed.

### `NON_CONTENT_INDEXED`

- **Number**: `14`
- **Deprecated**: `true`

Deprecated: Use NOT_CONTENT_INDEXED instead.

### `INTEGRITY_STREAM`

- **Number**: `15`

The directory or user data stream is configured with integrity.

### `VIRTUAL`

- **Number**: `16`

Reserved for system use.

### `NO_SCRUB_DATA`

- **Number**: `17`

The user data stream not to be read by the background data integrity scanner.

### `EA`

- **Number**: `18`

A file or directory with extended attributes.

### `PINNED`

- **Number**: `19`

The file or directory should be kept fully present locally.

### `UNPINNED`

- **Number**: `20`

The file or directory should not be kept fully present locally.

### `RECALL_ON_OPEN`

- **Number**: `21`

The file or directory has no physical representation on the local system.

### `RECALL_ON_DATA_ACCESS`

- **Number**: `22`

The file or directory is not fully present locally.
