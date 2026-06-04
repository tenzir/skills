# LinuxUtmp.RecordType

The type of activity record from the Utmp file.

## Values

0. `RECORD_TYPE_UNSPECIFIED`: The default record type.
1. `RUN_LVL`: Run-level change.
2. `BOOT_TIME`: System boot time.
3. `NEW_TIME`: New time after system clock change.
4. `OLD_TIME`: Old time before system clock change.
5. `INIT_PROCESS`: Process spawned by init.
6. `LOGIN_PROCESS`: Login process.
7. `USER_PROCESS`: Normal user process (logged-in session).
8. `DEAD_PROCESS`: Terminated process (session ended).
9. `ACCOUNTING`: Accounting message.
