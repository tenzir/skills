# WindowsScheduledTask.TaskTrigger

The trigger of the scheduled task.

- **Full name**: `google.backstory.WindowsScheduledTask.TaskTrigger`
- **Fields**: `4`
- **Nested enums**: `1`

## Nested enums

- [WindowsScheduledTask.TaskTrigger.TriggerType](../enums/windows_scheduled_task_task_trigger_trigger_type.md)

## Fields

### `enabled`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `bool`
- **JSON name**: `enabled`

Indicates whether the task trigger is enabled.

### `duration`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Duration` (imported)
- **JSON name**: `duration`

The duration of the task trigger repetition.

### `interval`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `interval`

The interval between each repetition of the task. The format for this string is `P<days>DT<hours>H<minutes>M<seconds>S` (for example, "PT5M" is 5 minutes, "PT1H" is 1 hour, and "PT20M" is 20 minutes). The maximum time allowed is 31 days, and the minimum time allowed is 1 minute.

### `trigger_type`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: [`WindowsScheduledTask.TaskTrigger.TriggerType`](../enums/windows_scheduled_task_task_trigger_trigger_type.md)
- **JSON name**: `triggerType`

The trigger frequency of the task.
