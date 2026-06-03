# Volume

Information about a storage volume.

- **Full name**: `google.backstory.Volume`
- **Fields**: `6`

## Fields

### `file_system`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `fileSystem`

The name of the file system on the volume (e.g., "NTFS", "FAT32").

### `mount_point`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `mountPoint`

The path where the volume is mounted (e.g., "C:", "/mnt/data").

### `device_path`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `devicePath`

The system path to the device (e.g., "\\.\HarddiskVolume1", "/dev/sda1").

### `is_mounted`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: `bool`
- **JSON name**: `isMounted`

Indicates whether the volume is currently mounted.

### `is_read_only`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: `bool`
- **JSON name**: `isReadOnly`

Indicates whether the volume is mounted as read-only.

### `name`

- **Number**: `6`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `name`

The user-assigned label or name for the volume.
