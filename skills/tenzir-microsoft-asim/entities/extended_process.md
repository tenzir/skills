# ASimExtendedProcess

- **Source**: [`ASIM/schemas/entities/ASimExtendedProcess.yaml`](https://github.com/Azure/Azure-Sentinel/blob/0db4cc9a326a610d44000d6af1b7035432db74ba/ASIM/schemas/entities/ASimExtendedProcess.yaml)
- **Fields**: `21`

## Included by

- [ProcessEvent](../schemas/process_event.md) as `Acting`
- [ProcessEvent](../schemas/process_event.md) as `Parent`
- [ProcessEvent](../schemas/process_event.md) as `Target`

## Raw fields

### `<<Role>>ProcessCommandLine`

- **Class**: `Optional`
- **Type**: `string`

The command line used to run the process.

#### Examples

- `choco.exe -v`

### `<<Role>>ProcessCreationTime`

- **Class**: `Optional`
- **Type**: `datetime`

The date and time when the acting process was started.

### `<<Role>>ProcessFileCompany`

- **Class**: `Optional`
- **Type**: `string`

The company that created the acting process image file.

#### Examples

- `Microsoft`

### `<<Role>>ProcessFileDescription`

- **Class**: `Optional`
- **Type**: `string`

The description embedded in the version information of the acting process image file.

#### Examples

- `Notepad++ - a free (GPL) source code editor`

### `<<Role>>ProcessFileInternalName`

- **Class**: `Optional`
- **Type**: `string`

The product internal file name from the version information of the acting process image file.

#### Examples

- `extensions.dll`

### `<<Role>>ProcessFileOriginalName`

- **Class**: `Optional`
- **Type**: `string`

The product original file name from the version information of the acting process image file.

#### Examples

- `Notepad++.exe`

### `<<Role>>ProcessFileProduct`

- **Class**: `Optional`
- **Type**: `string`

The product name from the version information in the acting process image file.

#### Examples

- `Notepad++`

### `<<Role>>ProcessFileSize`

- **Class**: `Optional`
- **Type**: `long`

The size of the file that ran the acting process.

### `<<Role>>ProcessFileVersion`

- **Class**: `Optional`
- **Type**: `string`

The product version from the version information of the acting process image file.

#### Examples

- `7.9.5.0`

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

### `<<Role>>ProcessIMPHASH`

- **Class**: `Optional`
- **Type**: `string`

The Import Hash of all the library DLLs that are used by the acting process.

### `<<Role>>ProcessInjectedAddress`

- **Class**: `Optional`
- **Type**: `string`

The memory address in which the responsible acting process is stored.

### `<<Role>>ProcessIntegrityLevel`

- **Class**: `Optional`
- **Type**: `string`

Integrity levels determine the process level of protection or access.

#### Examples

- `High`

### `<<Role>>ProcessIsHidden`

- **Class**: `Optional`
- **Type**: `bool`

An indication of whether the acting process is in hidden mode.

### `<<Role>>ProcessMD5`

- **Class**: `Optional`
- **Type**: `string`

The MD5 hash of the acting process image file.

#### Examples

- `75a599802f1fa166cdadb360960b1dd0`

### `<<Role>>ProcessName`

- **Class**: `Optional`
- **Type**: `string`

The name of the process. This name is commonly derived from the image or executable file that's used to define the initial code and data that's mapped into the process' virtual address space.

#### Examples

- `C:\Windows\explorer.exe`

### `<<Role>>ProcessSHA1`

- **Class**: `Optional`
- **Type**: `string`

The SHA-1 hash of the acting process image file.

#### Examples

- `d55c5a4df19b46db8c54c801c4665d3338acdab0`

### `<<Role>>ProcessSHA256`

- **Class**: `Optional`
- **Type**: `string`

The SHA-256 hash of the acting process image file.

#### Examples

- `e81bb824c4a09a811af17deae22f22dd2e1ec8cbb00b22629d2899f7c68da274`

### `<<Role>>ProcessSHA512`

- **Class**: `Optional`
- **Type**: `string`

The SHA-512 hash of the acting process image file.

#### Examples

- `3b7fc7cc370707c1df045c35342f3d64ea7076abd84f8a8c046a7cca2b85901689f3cf4bdc1f5fc232a60456cb9d2f48702bf8f8f1064f9bcc7d70edad9f860e`

### `<<Role>>ProcessTokenElevation`

- **Class**: `Optional`
- **Type**: `string`

A token indicating the presence or absence of User Access Control (UAC) privilege elevation applied to the acting process.

#### Examples

- `None`
