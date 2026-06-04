# Srum

The Srum extension captures details specific to Windows System Resource Usage Monitor (SRUM) events.

- **Full name**: `google.backstory.Srum`
- **Fields**: `9`

## Fields

### `id`

- Type: `string` (singular)

A unique identifier for the SRUM record or the application/user being monitored.

### `backgroundBytesRead`

- Type: `int64` (singular)

The number of bytes read by the application while running in the background.

### `backgroundBytesWritten`

- Type: `int64` (singular)

The number of bytes written by the application while running in the background.

### `backgroundContextSwitches`

- Type: `int64` (singular)

The number of context switches performed by the application's threads while in the background.

### `backgroundCycleCount`

- Type: `int64` (singular)

The amount of CPU cycle time consumed by the application in the background, measured in clock cycles.

### `backgroundFlushesCount`

- Type: `int64` (singular)

The number of flush operations performed by the application in the background.

### `backgroundReadOperations`

- Type: `int64` (singular)

The number of read operations performed by the application in the background.

### `backgroundWriteOperations`

- Type: `int64` (singular)

The number of write operations performed by the application in the background.

### `interfaceLuid`

- Type: `string` (singular)

The Locally Unique Identifier (LUID) for the network interface used for data transfer.
