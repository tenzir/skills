# Job

> The Job object provides information about a scheduled job or task, including its name, command line, and state.


The Job object provides information about a scheduled job or task, including its name, command line, and state. It encompasses attributes that describe the properties and status of the scheduled job.

## Attributes

**`file`**

* **Type**: [`file`](file.md)
* **Requirement**: required

The file that pertains to the job.

**`name`**

* **Type**: `string_t`
* **Requirement**: required

The name of the job.

**`cmd_line`**

* **Type**: `string_t`
* **Requirement**: recommended

The job command line.

**`created_time`**

* **Type**: `timestamp_t`
* **Requirement**: recommended

The time when the job was created.

**`desc`**

* **Type**: `string_t`
* **Requirement**: recommended

The description of the job.

**`last_run_time`**

* **Type**: `timestamp_t`
* **Requirement**: recommended

The time when the job was last run.

**`run_state_id`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`
  * `1` - `Ready`
  * `2` - `Queued`
  * `3` - `Running`
  * `4` - `Stopped`
  * `99` - `Other`

The run state ID of the job.

**`created_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The time when the job was created.

**`last_run_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The time when the job was last run.

**`next_run_time`**

* **Type**: `timestamp_t`
* **Requirement**: optional

The time when the job will next be run.

**`next_run_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The time when the job will next be run.

**`run_state`**

* **Type**: `string_t`
* **Requirement**: optional

The run state of the job.

**`user`**

* **Type**: [`user`](user.md)
* **Requirement**: optional

The user that created the job.

## Used By

* [`job_query`](../classes/job_query.md)
* [`scheduled_job_activity`](../classes/scheduled_job_activity.md)