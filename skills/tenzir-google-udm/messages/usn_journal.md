# UsnJournal

Information from the NTFS USN Journal.

- **Full name**: `google.backstory.UsnJournal`
- **Fields**: `6`
- **Nested enums**: `2`

## Nested enums

- [UsnJournal.Attribute](../enums/usn_journal_attribute.md)
- [UsnJournal.Reason](../enums/usn_journal_reason.md)

## Fields

### `attributes_flag`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `attributesFlag`

File attributes flags from the USN record (e.g., "0x20").

### `attributes`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: [`UsnJournal.Attribute`](../enums/usn_journal_attribute.md)
- **JSON name**: `attributes`
- **Deprecated**: `true`

Deprecated: Use file_attributes instead. File attributes from the USN record.

### `file_attributes`

- **Number**: `5`
- **Cardinality**: `repeated`
- **Type**: [`UsnJournal.Attribute`](../enums/usn_journal_attribute.md)
- **JSON name**: `fileAttributes`

File attributes from the USN record.

### `allocated`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `bool`
- **JSON name**: `allocated`

Indicates whether the file is allocated in the Master File Table (MFT).

### `reason`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: [`UsnJournal.Reason`](../enums/usn_journal_reason.md)
- **JSON name**: `reason`
- **Deprecated**: `true`

Deprecated: Use reasons instead. Human-readable string describing the reason for the USN journal entry. (e.g., "USN_REASON_FILE_CREATE").

### `reasons`

- **Number**: `6`
- **Cardinality**: `repeated`
- **Type**: [`UsnJournal.Reason`](../enums/usn_journal_reason.md)
- **JSON name**: `reasons`

Human-readable string describing the reasons for the USN journal entry (e.g., "USN_REASON_FILE_CREATE").
