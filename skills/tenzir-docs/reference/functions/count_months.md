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

[`count_years`](/reference/functions/count_years.md), [`count_months`](/reference/functions/count_months.md), [`count_weeks`](/reference/functions/count_weeks.md), [`count_days`](/reference/functions/count_days.md), [`count_hours`](/reference/functions/count_hours.md), [`count_minutes`](/reference/functions/count_minutes.md), [`count_seconds`](/reference/functions/count_seconds.md), [`count_milliseconds`](/reference/functions/count_milliseconds.md), [`count_microseconds`](/reference/functions/count_microseconds.md), [`count_nanoseconds`](/reference/functions/count_nanoseconds.md)