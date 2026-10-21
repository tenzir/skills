# Clipboard Activity (clipboard_activity)

Clipboard Activity events report when a process performs an action on a clipboard.

- **Class UID**: `1012`
- **Category**: System Activity
- **Extends**: [System Activity (system)](system.md)
- **Profiles**: [AI Operation](../profiles/ai_operation.md), [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md), [Host](../profiles/host.md), [OSINT](../profiles/osint.md), [Record Integrity](../profiles/record_integrity.md), [Security Control](../profiles/security_control.md)

## Associations

- `actor.user` ↔ `device`
- `device` ↔ `actor.user`

## Inherited attributes

**From System Activity:**
- `actor` (required)
- `device` (required)

**From Base Event:**
- `category_uid` (required)
- `metadata` (required)
- `severity_id` (required)
- `time` (required)
- `message` (recommended)
- `observables` (recommended)
- `status` (recommended)
- `status_code` (recommended)
- `status_detail` (recommended)
- `status_id` (recommended)
- `timezone_offset` (recommended)

## Attributes

### `activity_id`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `activity_name`

#### Enum values

- `0`: `Unknown` - The event activity is unknown.
- `1`: `Read` - A clipboard was read from. In user-interface terms, this is a 'paste' operation. If present, `source_process` is the process which performed the `Write` activity or, in other words, the process from which the data was copied.
- `2`: `Write` - A clipboard was written to. In user-interface terms, this is a 'copy' or 'cut' operation.
- `3`: `Clear` - A clipboard was cleared.
- `99`: `Other` - The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

The normalized identifier of the activity that triggered the event. Each event class defines its own set of activity values. Use `0` (Unknown) when the activity cannot be determined. Use `99` (Other) when the activity does not match any defined value, in which case `activity_name` must be populated with the source-specific label.

### `clipboard`

- **Type**: [`clipboard`](../objects/clipboard.md)
- **Requirement**: required
- **Group**: primary

The clipboard that is the target of the activity.

### `source_process`

- **Type**: [`process`](../objects/process.md)
- **Requirement**: optional
- **Group**: context

For a `Read` activity, this is the process which performed the `Write`. In other words, `actor.process` is the process performing the paste and `source_process` is the process that performed the copy.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `1012`: `Clipboard Activity` - Clipboard Activity events report when a process performs an action on a clipboard.

The unique identifier of a class. A class describes the attributes available in an event. Producers and mappers must set this to the `uid` defined in the event class definition. For example, `Detection Finding` is `2004`.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `101200`: `Clipboard Activity: Unknown`
- `101201`: `Clipboard Activity: Read` - A clipboard was read from. In user-interface terms, this is a 'paste' operation. If present, `source_process` is the process which performed the `Write` activity or, in other words, the process from which the data was copied.
- `101202`: `Clipboard Activity: Write` - A clipboard was written to. In user-interface terms, this is a 'copy' or 'cut' operation.
- `101203`: `Clipboard Activity: Clear` - A clipboard was cleared.
- `101299`: `Clipboard Activity: Other`

The event/finding type ID. It identifies the event's semantics and structure. Producers and mappers must compute this as `class_uid * 100 + activity_id`. It uniquely identifies the combination of event class and activity across the entire schema. For example, `Detection Finding: Create` is `200401`.
