# UsnJournal

Information from the NTFS USN Journal.

## Fields

### `attributes_flag` / `attributesFlag`

- Type: `string` (singular)

File attributes flags from the USN record (e.g., "0x20").

### `attributes`

- Type: [`UsnJournal.Attribute`](../enums/usn_journal_attribute.md) (singular)
- Deprecated: `true`

Deprecated: Use file_attributes instead. File attributes from the USN record.

### `file_attributes` / `fileAttributes`

- Type: [`UsnJournal.Attribute`](../enums/usn_journal_attribute.md) (repeated)

File attributes from the USN record.

### `allocated`

- Type: `bool` (singular)

Indicates whether the file is allocated in the Master File Table (MFT).

### `reason`

- Type: [`UsnJournal.Reason`](../enums/usn_journal_reason.md) (singular)
- Deprecated: `true`

Deprecated: Use reasons instead. Human-readable string describing the reason for the USN journal entry. (e.g., "USN_REASON_FILE_CREATE").

### `reasons`

- Type: [`UsnJournal.Reason`](../enums/usn_journal_reason.md) (repeated)

Human-readable string describing the reasons for the USN journal entry (e.g., "USN_REASON_FILE_CREATE").
