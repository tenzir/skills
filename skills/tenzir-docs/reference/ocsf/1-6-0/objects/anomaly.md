# Anomaly

> Describes an anomaly or deviation detected in a system.


Describes an anomaly or deviation detected in a system. Anomalies are unexpected activity patterns that could indicate potential issues needing attention.

## Attributes

**`observation_parameter`**

* **Type**: `string_t`
* **Requirement**: required

The specific parameter, metric or property where the anomaly was observed. Examples include: CPU usage percentage, API response time in milliseconds, HTTP error rate, memory utilization, network latency, transaction volume, etc. This helps identify the exact aspect of the system exhibiting anomalous behavior.

**`observations`**

* **Type**: [`observation`](observation.md)
* **Requirement**: required

Details about the observed anomaly or observations that were flagged as anomalous compared to expected baseline behavior.

**`observation_type`**

* **Type**: `string_t`
* **Requirement**: recommended

The type of analysis methodology used to detect the anomaly. This indicates how the anomaly was identified through different analytical approaches. Common types include: Frequency Analysis, Time Pattern Analysis, Volume Analysis, Sequence Analysis, Distribution Analysis, etc.

**`observed_pattern`**

* **Type**: `string_t`
* **Requirement**: recommended

The specific pattern identified within the observation type. For Frequency Analysis, this could be ‘FREQUENT’, ‘INFREQUENT’, ‘RARE’, or ‘UNSEEN’. For Time Pattern Analysis, this could be ‘BUSINESS\_HOURS’, ‘OFF\_HOURS’, or ‘UNUSUAL\_TIME’. For Volume Analysis, this could be ‘NORMAL\_VOLUME’, ‘HIGH\_VOLUME’, or ‘SURGE’. The pattern values are specific to each observation type and indicate how the observed behavior relates to the baseline.