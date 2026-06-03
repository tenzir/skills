# Srum

The Srum extension captures details specific to Windows System Resource Usage Monitor (SRUM) events.

- **Full name**: `google.backstory.Srum`
- **Fields**: `9`

## Fields

### `id`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `id`

A unique identifier for the SRUM record or the application/user being monitored.

### `background_bytes_read`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `backgroundBytesRead`

The number of bytes read by the application while running in the background.

### `background_bytes_written`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `backgroundBytesWritten`

The number of bytes written by the application while running in the background.

### `background_context_switches`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `backgroundContextSwitches`

The number of context switches performed by the application's threads while in the background.

### `background_cycle_count`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `backgroundCycleCount`

The amount of CPU cycle time consumed by the application in the background, measured in clock cycles.

### `background_flushes_count`

- **Number**: `6`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `backgroundFlushesCount`

The number of flush operations performed by the application in the background.

### `background_read_operations`

- **Number**: `7`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `backgroundReadOperations`

The number of read operations performed by the application in the background.

### `background_write_operations`

- **Number**: `8`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `backgroundWriteOperations`

The number of write operations performed by the application in the background.

### `interface_luid`

- **Number**: `9`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `interfaceLuid`

The Locally Unique Identifier (LUID) for the network interface used for data transfer.
