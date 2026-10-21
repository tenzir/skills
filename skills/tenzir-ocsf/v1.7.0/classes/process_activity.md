# Process Activity (process_activity)

Process Activity events report when a process launches, injects, opens or terminates another process, successful or otherwise.

- **Class UID**: `1007`
- **Category**: System Activity
- **Extends**: [System Activity (system)](system.md)
- **Profiles**: [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md), [Host](../profiles/host.md), [OSINT](../profiles/osint.md), [Security Control](../profiles/security_control.md)

## Associations

- `actor.user` ↔ `device`
- `device` ↔ `actor.user`

## Inherited attributes

**From System Activity:**
- `device` (required)

**From Base Event:**
- `category_uid` (required)
- `metadata` (required)
- `severity_id` (required)
- `time` (required)
- `message` (recommended)
- `observables` (recommended)
- `status` (recommended)
- `status_code` (recommended)
- `status_detail` (recommended)
- `status_id` (recommended)
- `timezone_offset` (recommended)

## Attributes

### `activity_id`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `activity_name`

#### Enum values

- `0`: `Unknown` - The event activity is unknown.
- `1`: `Launch` - A request by the actor to launch another process. Refer to the `launch_type_id` attribute for details of the specific launch type.
- `2`: `Terminate` - A request by the actor to terminate a process. This activity is most commonly reflexive, this being the case when a process exits at its own initiation. Note too that Windows security products cannot always identify the actor in the case of inter-process termination. In this case, `actor.process` and `process` refer to the exiting process, i.e. indistinguishable from the reflexive case.
- `3`: `Open` - A request by the actor to obtain a handle or descriptor to a process with the aim of performing further actions upon that process. The target is usually a different process but this activity can also be reflexive.
- `4`: `Inject` - A request by the actor to execute code within the context of a process. The target is usually a different process but this activity can also be reflexive. Refer to the `injection_type_id` attribute for details of the specific injection type.
- `5`: `Set User ID` - A request by the actor to change its user identity by invoking the `setuid()` system call. Common programs like `su` and `sudo` use this mechanism. Note that the impersonation mechanism on Windows is not directly equivalent because it acts at the thread level.
- `99`: `Other` - The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

The normalized identifier of the activity that triggered the event.

### `actor`

- **Type**: [`actor`](../objects/actor.md)
- **Requirement**: required
- **Group**: primary

The actor that performed the activity on the target `process`. For example, the process that started a new process or injected code into another process.

### `actual_permissions`

- **Type**: `integer_t`
- **Requirement**: recommended
- **Group**: primary

The permissions that were granted to the process in a platform-native format.

### `exit_code`

- **Type**: `integer_t`
- **Requirement**: recommended
- **Group**: primary

The exit code reported by a process when it terminates. The convention is that zero indicates success and any non-zero exit code indicates that some error occurred.

### `injection_type`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: primary

The process injection method, normalized to the caption of the injection_type_id value. In the case of 'Other', it is defined by the event source.

### `injection_type_id`

- **Type**: `integer_t`
- **Requirement**: recommended
- **Group**: primary
- **Sibling**: `injection_type`

#### Enum values

- `0`: `Unknown` - The injection type is unknown.
- `1`: `Remote Thread`
- `2`: `Load Library`
- `3`: `Queue APC`
- `99`: `Other` - The injection type is not mapped. See the `injection_type` attribute, which contains a data source specific value.

The normalized identifier of the process injection method.

### `launch_type`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: primary

The specific type of `Launch` activity, normalized to the caption of the `launch_type_id` value. In the case of `Other` it is defined by the event source.

### `launch_type_id`

- **Type**: `integer_t`
- **Requirement**: recommended
- **Group**: primary
- **Sibling**: `launch_type`

#### Enum values

- `0`: `Unknown` - The launch type is unknown or not specified.
- `1`: `Spawn` - Denotes that the `Launch` event represents atomic creation of a new process on Windows. This launch type ID may also be used to represent both steps of Unix process creation in a single `Launch` event.
- `2`: `Fork` - Denotes that the `Launch` event represents the "fork" step of Unix process creation, where a process creates a clone of itself in a parent-child relationship. WSL1 pico processes on Windows also use the 2-step Unix model.
- `3`: `Exec` - Denotes that the `Launch` event represents the "exec" step of Unix process creation, where a process replaces its executable image, command line, and environment. WSL1 pico processes on Windows also use the 2-step Unix model.
- `99`: `Other` - The launch type is not mapped. See the `launch_type` attribute, which contains a data source specific value.

The normalized identifier for the specific type of `Launch` activity.

### `module`

- **Type**: [`module`](../objects/module.md)
- **Requirement**: recommended
- **Group**: primary

The module that was injected by the actor process.

### `process`

- **Type**: [`process`](../objects/process.md)
- **Requirement**: required
- **Group**: primary

The process that was launched, injected into, opened, or terminated.

### `requested_permissions`

- **Type**: `integer_t`
- **Requirement**: recommended
- **Group**: primary

The permissions mask that was requested by the process.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `1007`: `Process Activity` - Process Activity events report when a process launches, injects, opens or terminates another process, successful or otherwise.

The unique identifier of a class. A class describes the attributes available in an event.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `100700`: `Process Activity: Unknown`
- `100701`: `Process Activity: Launch` - A request by the actor to launch another process. Refer to the `launch_type_id` attribute for details of the specific launch type.
- `100702`: `Process Activity: Terminate` - A request by the actor to terminate a process. This activity is most commonly reflexive, this being the case when a process exits at its own initiation. Note too that Windows security products cannot always identify the actor in the case of inter-process termination. In this case, `actor.process` and `process` refer to the exiting process, i.e. indistinguishable from the reflexive case.
- `100703`: `Process Activity: Open` - A request by the actor to obtain a handle or descriptor to a process with the aim of performing further actions upon that process. The target is usually a different process but this activity can also be reflexive.
- `100704`: `Process Activity: Inject` - A request by the actor to execute code within the context of a process. The target is usually a different process but this activity can also be reflexive. Refer to the `injection_type_id` attribute for details of the specific injection type.
- `100705`: `Process Activity: Set User ID` - A request by the actor to change its user identity by invoking the `setuid()` system call. Common programs like `su` and `sudo` use this mechanism. Note that the impersonation mechanism on Windows is not directly equivalent because it acts at the thread level.
- `100799`: `Process Activity: Other`

The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
