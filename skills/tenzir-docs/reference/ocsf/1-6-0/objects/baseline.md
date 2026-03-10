# Baseline

> Describes the baseline or expected behavior of a system, service, or component based on historical observations and measurements.


Describes the baseline or expected behavior of a system, service, or component based on historical observations and measurements. It establishes reference points for comparison to detect anomalies, trends, and deviations from typical patterns.

## Attributes

**`observation_parameter`**

* **Type**: `string_t`
* **Requirement**: required

The specific parameter or property being monitored. Examples include: CPU usage percentage, API response time in milliseconds, HTTP error rate, memory utilization, network latency, transaction volume, etc.

**`observations`**

* **Type**: [`observation`](observation.md)
* **Requirement**: required

Collection of actual measured values, data points and observations recorded for this baseline.

**`observation_type`**

* **Type**: `string_t`
* **Requirement**: recommended

The type of analysis being performed to establish baseline behavior. Common types include: Frequency Analysis, Time Pattern Analysis, Volume Analysis, Sequence Analysis, Distribution Analysis, etc.

**`observed_pattern`**

* **Type**: `string_t`
* **Requirement**: recommended

The specific pattern identified within the observation type. For Frequency Analysis, this could be ‘FREQUENT’, ‘INFREQUENT’, ‘RARE’, or ‘UNSEEN’. For Time Pattern Analysis, this could be ‘BUSINESS\_HOURS’, ‘OFF\_HOURS’, or ‘UNUSUAL\_TIME’. For Volume Analysis, this could be ‘NORMAL\_VOLUME’, ‘HIGH\_VOLUME’, or ‘SURGE’. The pattern values are specific to each observation type and indicate the baseline behavior.