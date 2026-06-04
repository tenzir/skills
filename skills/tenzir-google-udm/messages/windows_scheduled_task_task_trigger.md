# TaskTrigger

The trigger of the scheduled task.

## Fields

### `enabled`

- Type: `bool` (singular)

Indicates whether the task trigger is enabled.

### `duration`

- Type: `duration` (singular)

The duration of the task trigger repetition.

### `interval`

- Type: `string` (singular)

The interval between each repetition of the task. The format for this string is `P<days>DT<hours>H<minutes>M<seconds>S` (for example, "PT5M" is 5 minutes, "PT1H" is 1 hour, and "PT20M" is 20 minutes). The maximum time allowed is 31 days, and the minimum time allowed is 1 minute.

### `triggerType`

- Type: [`TriggerType`](../enums/windows_scheduled_task_task_trigger_trigger_type.md) (singular)

The trigger frequency of the task.
