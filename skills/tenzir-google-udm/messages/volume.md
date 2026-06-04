# Volume

Information about a storage volume.

## Fields

### `file_system` / `fileSystem`

- Type: `string` (singular)

The name of the file system on the volume (e.g., "NTFS", "FAT32").

### `mount_point` / `mountPoint`

- Type: `string` (singular)

The path where the volume is mounted (e.g., "C:", "/mnt/data").

### `device_path` / `devicePath`

- Type: `string` (singular)

The system path to the device (e.g., "\\.\HarddiskVolume1", "/dev/sda1").

### `is_mounted` / `isMounted`

- Type: `bool` (singular)

Indicates whether the volume is currently mounted.

### `is_read_only` / `isReadOnly`

- Type: `bool` (singular)

Indicates whether the volume is mounted as read-only.

### `name`

- Type: `string` (singular)

The user-assigned label or name for the volume.
