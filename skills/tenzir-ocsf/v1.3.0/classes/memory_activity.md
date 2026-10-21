# Memory Activity (memory_activity)

Memory Activity events report when a process has memory allocated, read/modified, or other manipulation activities - such as a buffer overflow or turning off data execution protection (DEP).

- **Class UID**: `1004`
- **Category**: System Activity
- **Extends**: [System Activity (system)](system.md)
- **Profiles**: [Host](../profiles/host.md), [Security Control](../profiles/security_control.md), [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md), [OSINT](../profiles/osint.md)

## Associations

- `device` ↔ `actor.user`
- `actor.user` ↔ `device`

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
- `1`: `Allocate Page`
- `2`: `Modify Page`
- `3`: `Delete Page`
- `4`: `Buffer Overflow`
- `5`: `Disable DEP` - Data Execution Permission
- `6`: `Enable DEP` - Data Execution Permission
- `7`: `Read` - Read (Example: `ReadProcessMemory`)
- `8`: `Write` - Write (Example: `WriteProcessMemory`)
- `9`: `Map View` - Map View (Example: `MapViewOfFile2`)
- `99`: `Other` - The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

The normalized identifier of the activity that triggered the event.

### `actual_permissions`

- **Type**: `integer_t`
- **Requirement**: recommended
- **Group**: primary

The permissions that were granted to the in a platform-native format.

### `base_address`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: primary

The memory address that was access or requested.

### `requested_permissions`

- **Type**: `integer_t`
- **Requirement**: recommended
- **Group**: primary

The permissions mask that were requested by the process.

### `size`

- **Type**: `long_t`
- **Requirement**: recommended
- **Group**: primary

The memory size that was access or requested.

### `process`

- **Type**: [`process`](../objects/process.md)
- **Requirement**: required
- **Group**: primary

The process that had memory allocated, read/written, or had other manipulation activities performed on it.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `1004`: `Memory Activity` - Memory Activity events report when a process has memory allocated, read/modified, or other manipulation activities - such as a buffer overflow or turning off data execution protection (DEP).

The unique identifier of a class. A class describes the attributes available in an event.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `100400`: `Memory Activity: Unknown`
- `100401`: `Memory Activity: Allocate Page`
- `100402`: `Memory Activity: Modify Page`
- `100403`: `Memory Activity: Delete Page`
- `100404`: `Memory Activity: Buffer Overflow`
- `100405`: `Memory Activity: Disable DEP` - Data Execution Permission
- `100406`: `Memory Activity: Enable DEP` - Data Execution Permission
- `100407`: `Memory Activity: Read` - Read (Example: `ReadProcessMemory`)
- `100408`: `Memory Activity: Write` - Write (Example: `WriteProcessMemory`)
- `100409`: `Memory Activity: Map View` - Map View (Example: `MapViewOfFile2`)
- `100499`: `Memory Activity: Other`

The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
