# Time Span

> The Time Span object represents different time period durations.


The Time Span object represents different time period durations. If a timespan is fractional, i.e. crosses one period, e.g. a week and 3 days, more than one may be populated since each member is of integral type. In that case `type_id` if present should be set to `Other.`A timespan may also be defined by its time interval boundaries, `start_time` and `end_time`.

## Attributes

**`duration`**

* **Type**: `long_t`
* **Requirement**: recommended

The duration of the time span in milliseconds.

**`duration_days`**

* **Type**: `integer_t`
* **Requirement**: recommended

The duration of the time span in days.

**`duration_hours`**

* **Type**: `integer_t`
* **Requirement**: recommended

The duration of the time span in hours.

**`duration_mins`**

* **Type**: `integer_t`
* **Requirement**: recommended

The duration of the time span in minutes.

**`duration_months`**

* **Type**: `integer_t`
* **Requirement**: recommended

The duration of the time span in months.

**`duration_secs`**

* **Type**: `integer_t`
* **Requirement**: recommended

The duration of the time span in seconds.

**`duration_weeks`**

* **Type**: `integer_t`
* **Requirement**: recommended

The duration of the time span in weeks.

**`duration_years`**

* **Type**: `integer_t`
* **Requirement**: recommended

The duration of the time span in years.

**`end_time`**

* **Type**: `timestamp_t`
* **Requirement**: recommended

The end time or conclusion of the timespan’s interval.

**`start_time`**

* **Type**: `timestamp_t`
* **Requirement**: recommended

The start time or beginning of the timespan’s interval.

**`type_id`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`: The type is unknown.
  * `1` - `Milliseconds`
  * `2` - `Seconds`
  * `3` - `Minutes`
  * `4` - `Hours`
  * `5` - `Days`
  * `6` - `Weeks`
  * `7` - `Months`
  * `8` - `Years`
  * `9` - `Time Interval`: The `start_time` and `end_time` should be set.
  * `99` - `Other`: The type is not mapped. See the `type` attribute, which contains a data source specific value.

The normalized identifier for the time span duration type.

**`end_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The end time or conclusion of the timespan’s interval.

**`start_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The start time or beginning of the timespan’s interval.

**`type`**

* **Type**: `string_t`
* **Requirement**: optional

The type of time span duration the object represents.

## Constraints

At least one of: `duration`, `duration_days`, `duration_hours`, `duration_mins`, `duration_months`, `duration_secs`, `duration_weeks`, `duration_years`, `end_time`, `start_time`