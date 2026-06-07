# Process.State

The state of the process. See https://psutil.readthedocs.io/en/stable/#process-status-constants.

## Values

- `STATE_UNSPECIFIED` (0): Undetermined state.
- `RUNNING` (1): Process is running or runnable.
- `SLEEPING` (2): Process is waiting for an event.
- `DISK_SLEEP` (3): Process is in uninterruptible sleep, typically I/O.
- `STOPPED` (4): Process is stopped.
- `TRACING_STOP` (5): Process is stopped by debugger.
- `ZOMBIE` (6): Process is terminated but not reaped by parent.
- `DEAD` (7): Process is terminated.
- `WAKE_KILL` (8): Process is woken to be killed.
- `WAKING` (9): Process is waking from sleep.
- `PARKED` (10): Linux specific: process is parked.
- `IDLE` (11): Linux, macOS, and FreeBSD specific: process is idle.
- `LOCKED` (12): FreeBSD specific: process is locked.
- `WAITING` (13): FreeBSD specific: process is waiting.
- `SUSPENDED` (14): NetBSD specific: process is suspended.
