# Process.State

The state of the process. See https://psutil.readthedocs.io/en/stable/#process-status-constants.

## Values

0. `STATE_UNSPECIFIED`: Undetermined state.
1. `RUNNING`: Process is running or runnable.
2. `SLEEPING`: Process is waiting for an event.
3. `DISK_SLEEP`: Process is in uninterruptible sleep, typically I/O.
4. `STOPPED`: Process is stopped.
5. `TRACING_STOP`: Process is stopped by debugger.
6. `ZOMBIE`: Process is terminated but not reaped by parent.
7. `DEAD`: Process is terminated.
8. `WAKE_KILL`: Process is woken to be killed.
9. `WAKING`: Process is waking from sleep.
10. `PARKED`: Linux specific: process is parked.
11. `IDLE`: Linux, macOS, and FreeBSD specific: process is idle.
12. `LOCKED`: FreeBSD specific: process is locked.
13. `WAITING`: FreeBSD specific: process is waiting.
14. `SUSPENDED`: NetBSD specific: process is suspended.
