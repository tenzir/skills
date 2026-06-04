# UsnJournal

Information from the NTFS USN Journal.

- **Full name**: `google.backstory.UsnJournal`
- **Fields**: `6`
- **Nested enums**: `2`

## Nested enums

- [UsnJournal.Attribute](../enums/usn_journal_attribute.md)
- [UsnJournal.Reason](../enums/usn_journal_reason.md)

## Fields

### `attributesFlag`

- Type: `string` (singular)

File attributes flags from the USN record (e.g., "0x20").

### `attributes`

- Type: [`UsnJournal.Attribute`](../enums/usn_journal_attribute.md) (singular)
- Deprecated: `true`

Deprecated: Use fileAttributes instead. File attributes from the USN record.

### `fileAttributes`

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
