# UsnJournal.Attribute

File attributes from the USN record (e.g., "READ_ONLY, HIDDEN"). See https://learn.microsoft.com/en-us/windows/win32/fileio/file-attribute-constants for more information about the attributes.

## Values

0. `ATTRIBUTE_UNSPECIFIED`: Unspecified attribute.
1. `READ_ONLY`: A file that is read-only.
2. `HIDDEN`: The file or directory is hidden.
3. `SYSTEM`: A file or directory that the operating system uses.
4. `ARCHIVE`: Archive file or directory.
5. `COMPRESSED`: A file or directory that is compressed.
6. `ENCRYPTED`: A file or directory that is encrypted.
7. `DIRECTORY`: The handle that identifies the directory.
8. `DEVICE`: Reserved for system use.
9. `NORMAL`: A file that does not have other attributes set.
10. `TEMPORARY`: A file that is being used for temporary storage.
11. `SPARSE_FILE`: A file that is a sparse file.
12. `REPARSE_POINT`: A file or directory that has an associated reparse point.
13. `OFFLINE`: The data of a file is not available immediately.
14. `NOT_CONTENT_INDEXED`: The file or directory is not to be indexed.
14. `NON_CONTENT_INDEXED` (deprecated): Deprecated: Use NOT_CONTENT_INDEXED instead.
15. `INTEGRITY_STREAM`: The directory or user data stream is configured with integrity.
16. `VIRTUAL`: Reserved for system use.
17. `NO_SCRUB_DATA`: The user data stream not to be read by the background data integrity scanner.
18. `EA`: A file or directory with extended attributes.
19. `PINNED`: The file or directory should be kept fully present locally.
20. `UNPINNED`: The file or directory should not be kept fully present locally.
21. `RECALL_ON_OPEN`: The file or directory has no physical representation on the local system.
22. `RECALL_ON_DATA_ACCESS`: The file or directory is not fully present locally.
