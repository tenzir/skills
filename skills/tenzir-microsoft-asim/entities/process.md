# ASimProcess

- **Source**: [`ASIM/schemas/entities/ASimProcess.yaml`](https://github.com/Azure/Azure-Sentinel/blob/0db4cc9a326a610d44000d6af1b7035432db74ba/ASIM/schemas/entities/ASimProcess.yaml)
- **Fields**: `4`

## Included by

- [Dns](../schemas/dns.md) as `Src`
- [FileEvent](../schemas/file_event.md) as `Acting`
- [RegistryEvent](../schemas/registry_event.md) as `Acting`
- [RegistryEvent](../schemas/registry_event.md) as `Parent`

## Raw fields

### `<<Role>>ProcessCommandLine`

- **Class**: `Optional`
- **Type**: `string`

The command line used to run the process.

#### Examples

- `choco.exe -v`

### `<<Role>>ProcessGuid`

- **Class**: `Optional`
- **Type**: `string`

A generated unique identifier (GUID) of the process. Enables identifying the process across systems.

#### Examples

- `EF3BD0BD-2B74-60C5-AF5C-010000001E00`

### `<<Role>>ProcessId`

- **Class**: `Optional`
- **Type**: `string`

The process ID (PID) of the process. The type is defined as string to support varying systems, but on Windows and Linux this value must be numeric. If you are using a Windows or Linux machine and used a different type, make sure to convert the values. For example, if you used a hexadecimal value, convert it to a decimal value.

#### Examples

- `48610176`

### `<<Role>>ProcessName`

- **Class**: `Optional`
- **Type**: `string`

The name of the process. This name is commonly derived from the image or executable file that's used to define the initial code and data that's mapped into the process' virtual address space.

#### Examples

- `C:\Windows\explorer.exe`
