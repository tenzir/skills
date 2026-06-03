# Process.State

The state of the process. See https://psutil.readthedocs.io/en/stable/#process-status-constants.

- **Full name**: `google.backstory.Process.State`
- **Values**: `15`

## Values

### `STATE_UNSPECIFIED`

- **Number**: `0`

Undetermined state.

### `RUNNING`

- **Number**: `1`

Process is running or runnable.

### `SLEEPING`

- **Number**: `2`

Process is waiting for an event.

### `DISK_SLEEP`

- **Number**: `3`

Process is in uninterruptible sleep, typically I/O.

### `STOPPED`

- **Number**: `4`

Process is stopped.

### `TRACING_STOP`

- **Number**: `5`

Process is stopped by debugger.

### `ZOMBIE`

- **Number**: `6`

Process is terminated but not reaped by parent.

### `DEAD`

- **Number**: `7`

Process is terminated.

### `WAKE_KILL`

- **Number**: `8`

Process is woken to be killed.

### `WAKING`

- **Number**: `9`

Process is waking from sleep.

### `PARKED`

- **Number**: `10`

Linux specific: process is parked.

### `IDLE`

- **Number**: `11`

Linux, macOS, and FreeBSD specific: process is idle.

### `LOCKED`

- **Number**: `12`

FreeBSD specific: process is locked.

### `WAITING`

- **Number**: `13`

FreeBSD specific: process is waiting.

### `SUSPENDED`

- **Number**: `14`

NetBSD specific: process is suspended.
