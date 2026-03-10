# Process

> The Process object describes a running instance of a launched program.


The Process object describes a running instance of a launched program. Defined by D3FEND [d3f:Process](https://d3fend.mitre.org/dao/artifact/d3f:Process/).

* **Extends**: `_entity`

## Attributes

**`cmd_line`**

* **Type**: `string_t`
* **Requirement**: recommended

The full command line used to launch an application, service, process, or job. For example: `ssh user@10.0.0.10`. If the command line is unavailable or missing, the empty string `''` is to be used

**`container`**

* **Type**: [`container`](container.md)
* **Requirement**: recommended

The information describing an instance of a container. A container is a prepackaged, portable system image that runs isolated on an existing system using a container runtime like containerd.

**`created_time`**

* **Type**: `timestamp_t`
* **Requirement**: recommended

The time when the process was created/started.

**`file`**

* **Type**: [`file`](file.md)
* **Requirement**: recommended

The process file object.

**`name`**

* **Type**: `process_name_t`
* **Requirement**: recommended

The friendly name of the process, for example: `Notepad++`.

**`namespace_pid`**

* **Type**: `integer_t`
* **Requirement**: recommended

If running under a process namespace (such as in a container), the process identifier within that process namespace.

**`parent_process`**

* **Type**: [`process`](process.md)
* **Requirement**: recommended

The parent process of this process object. It is recommended to only populate this field for the first process object, to prevent deep nesting.

**`pid`**

* **Type**: `integer_t`
* **Requirement**: recommended

The process identifier, as reported by the operating system. Process ID (PID) is a number used by the operating system to uniquely identify an active process.

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

A unique identifier for this process assigned by the producer (tool). Facilitates correlation of a process event with other events for that process.

**`user`**

* **Type**: [`user`](user.md)
* **Requirement**: recommended

The user under which this process is running.

**`created_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The time when the process was created/started.

**`integrity`**

* **Type**: `string_t`
* **Requirement**: optional

The process integrity level, normalized to the caption of the direction\_id value. In the case of ‘Other’, it is defined by the event source (Windows only).

**`integrity_id`**

* **Type**: `integer_t`

* **Requirement**: optional

* **Values**:

  * `0` - `Unknown`
  * `1` - `Untrusted`
  * `2` - `Low`
  * `3` - `Medium`
  * `4` - `High`
  * `5` - `System`
  * `6` - `Protected`
  * `99` - `Other`

The normalized identifier of the process integrity level (Windows only).

**`lineage`**

* **Type**: `string_t`
* **Requirement**: optional

The lineage of the process, represented by a list of paths for each ancestor process. For example: `['/usr/sbin/sshd', '/usr/bin/bash', '/usr/bin/whoami']`.

**`loaded_modules`**

* **Type**: `string_t`
* **Requirement**: optional

The list of loaded module names.

**`sandbox`**

* **Type**: `string_t`
* **Requirement**: optional

The name of the containment jail (i.e., sandbox). For example, hardened\_ps, high\_security\_ps, oracle\_ps, netsvcs\_ps, or default\_ps.

**`session`**

* **Type**: [`session`](session.md)
* **Requirement**: optional

The user session under which this process is running.

**`terminated_time`**

* **Type**: `timestamp_t`
* **Requirement**: optional

The time when the process was terminated.

**`terminated_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The time when the process was terminated.

**`tid`**

* **Type**: `integer_t`
* **Requirement**: optional

The Identifier of the thread associated with the event, as returned by the operating system.

**`xattributes`**

* **Type**: [`object`](object.md)
* **Requirement**: optional

An unordered collection of zero or more name/value pairs that represent a process extended attribute.

## Constraints

At least one of: `pid`, `uid`

## Used By

* [`authentication`](../classes/authentication.md)
* [`memory_activity`](../classes/memory_activity.md)
* [`process_activity`](../classes/process_activity.md)
* [`security_finding`](../classes/security_finding.md)