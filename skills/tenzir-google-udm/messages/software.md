# Software

Information about a software package or application.

- **Full name**: `google.backstory.Software`
- **Fields**: `5`

## Fields

### `name`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `name`

The name of the software.

### `version`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `version`

The version of the software.

### `permissions`

- **Number**: `3`
- **Cardinality**: `repeated`
- **Type**: [`Permission`](permission.md)
- **JSON name**: `permissions`

System permissions granted to the software. For example, "android.permission.WRITE_EXTERNAL_STORAGE"

### `description`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `description`

The description of the software.

### `vendor_name`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `vendorName`

The name of the software vendor.
