# WindowsScheduledTask.TaskTrigger.TriggerType

Enum representing the trigger type of the task. For more details, see https://learn.microsoft.com/en-us/windows/win32/api/taskschd/ne-taskschd-task_trigger_type2.

## Values

0. `TRIGGER_TYPE_UNSPECIFIED`: The trigger frequency is not specified.
1. `EVENT`: Triggers the task when a specific event occurs.
2. `TIME`: Triggers the task at a specific time of day.
3. `DAILY`: Triggers the task on a daily schedule. For example, the task starts at a specific time every day, every other day, or every third day.
4. `WEEKLY`: Triggers the task on a weekly schedule. For example, the task starts at 8:00 AM on a specific day every week or other week.
5. `MONTHLY`: Triggers the task on a monthly schedule. For example, the task starts on specific days of specific months.
6. `MONTHLYDOW`: Triggers the task on a monthly day-of-week schedule. For example, the task starts on a specific days of the week, weeks of the month, and months of the year.
7. `IDLE`: Triggers the task when the computer goes into an idle state.
8. `REGISTRATION`: Triggers the task when the task is registered.
9. `BOOT`: Triggers the task when the computer boots.
10. `LOGON`: Triggers the task when a specific user logs on.
11. `SESSION_STATE_CHANGE`: Triggers the task when a specific user session state changes.
12. `CUSTOM_TRIGGER01`: Custom trigger 01.
