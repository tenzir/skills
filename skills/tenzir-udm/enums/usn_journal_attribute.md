# UsnJournal.Attribute

File attributes from the USN record (e.g., "READ_ONLY, HIDDEN"). See https://learn.microsoft.com/en-us/windows/win32/fileio/file-attribute-constants for more information about the attributes.

## Values

- `ATTRIBUTE_UNSPECIFIED` (0): Unspecified attribute.
- `READ_ONLY` (1): A file that is read-only.
- `HIDDEN` (2): The file or directory is hidden.
- `SYSTEM` (3): A file or directory that the operating system uses.
- `ARCHIVE` (4): Archive file or directory.
- `COMPRESSED` (5): A file or directory that is compressed.
- `ENCRYPTED` (6): A file or directory that is encrypted.
- `DIRECTORY` (7): The handle that identifies the directory.
- `DEVICE` (8): Reserved for system use.
- `NORMAL` (9): A file that does not have other attributes set.
- `TEMPORARY` (10): A file that is being used for temporary storage.
- `SPARSE_FILE` (11): A file that is a sparse file.
- `REPARSE_POINT` (12): A file or directory that has an associated reparse point.
- `OFFLINE` (13): The data of a file is not available immediately.
- `NOT_CONTENT_INDEXED` (14): The file or directory is not to be indexed.
- `NON_CONTENT_INDEXED` (14, deprecated): Deprecated: Use NOT_CONTENT_INDEXED instead.
- `INTEGRITY_STREAM` (15): The directory or user data stream is configured with integrity.
- `VIRTUAL` (16): Reserved for system use.
- `NO_SCRUB_DATA` (17): The user data stream not to be read by the background data integrity scanner.
- `EA` (18): A file or directory with extended attributes.
- `PINNED` (19): The file or directory should be kept fully present locally.
- `UNPINNED` (20): The file or directory should not be kept fully present locally.
- `RECALL_ON_OPEN` (21): The file or directory has no physical representation on the local system.
- `RECALL_ON_DATA_ACCESS` (22): The file or directory is not fully present locally.
