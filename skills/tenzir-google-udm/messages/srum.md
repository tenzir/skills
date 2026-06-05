# Srum

The Srum extension captures details specific to Windows System Resource Usage Monitor (SRUM) events.

## Fields

### `id`

- Type: `string` (singular)

A unique identifier for the SRUM record or the application/user being monitored.

### `background_bytes_read` / `backgroundBytesRead`

- Type: `int64` (singular)

The number of bytes read by the application while running in the background.

### `background_bytes_written` / `backgroundBytesWritten`

- Type: `int64` (singular)

The number of bytes written by the application while running in the background.

### `background_context_switches` / `backgroundContextSwitches`

- Type: `int64` (singular)

The number of context switches performed by the application's threads while in the background.

### `background_cycle_count` / `backgroundCycleCount`

- Type: `int64` (singular)

The amount of CPU cycle time consumed by the application in the background, measured in clock cycles.

### `background_flushes_count` / `backgroundFlushesCount`

- Type: `int64` (singular)

The number of flush operations performed by the application in the background.

### `background_read_operations` / `backgroundReadOperations`

- Type: `int64` (singular)

The number of read operations performed by the application in the background.

### `background_write_operations` / `backgroundWriteOperations`

- Type: `int64` (singular)

The number of write operations performed by the application in the background.

### `interface_luid` / `interfaceLuid`

- Type: `string` (singular)

The Locally Unique Identifier (LUID) for the network interface used for data transfer.
