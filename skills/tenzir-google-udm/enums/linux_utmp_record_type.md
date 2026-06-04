# RecordType

The type of activity record from the Utmp file.

## Values

- `RECORD_TYPE_UNSPECIFIED` (0): The default record type.
- `RUN_LVL` (1): Run-level change.
- `BOOT_TIME` (2): System boot time.
- `NEW_TIME` (3): New time after system clock change.
- `OLD_TIME` (4): Old time before system clock change.
- `INIT_PROCESS` (5): Process spawned by init.
- `LOGIN_PROCESS` (6): Login process.
- `USER_PROCESS` (7): Normal user process (logged-in session).
- `DEAD_PROCESS` (8): Terminated process (session ended).
- `ACCOUNTING` (9): Accounting message.
