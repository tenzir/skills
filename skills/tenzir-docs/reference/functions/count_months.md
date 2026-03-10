# count_months


Counts the number of `months` in a duration.

```tql
count_months(x:duration) -> float
```

## Description

This function returns the number of months in a duration, i.e., `duration / 1/12 * 1y`.

### `x: duration`

The duration to count in.

## See Also

[`count_years`](count_years.md), [`count_months`](count_months.md), [`count_weeks`](count_weeks.md), [`count_days`](count_days.md), [`count_hours`](count_hours.md), [`count_minutes`](count_minutes.md), [`count_seconds`](count_seconds.md), [`count_milliseconds`](count_milliseconds.md), [`count_microseconds`](count_microseconds.md), [`count_nanoseconds`](count_nanoseconds.md)