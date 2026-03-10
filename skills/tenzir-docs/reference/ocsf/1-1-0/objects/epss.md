# EPSS

> The Exploit Prediction Scoring System (EPSS) object describes the estimated probability a vulnerability will be exploited.


The Exploit Prediction Scoring System (EPSS) object describes the estimated probability a vulnerability will be exploited. EPSS is a community-driven effort to combine descriptive information about vulnerabilities (CVEs) with evidence of actual exploitation in-the-wild. ([EPSS](https://www.first.org/epss/)).

## Attributes

**`score`**

* **Type**: `string_t`
* **Requirement**: required

The EPSS score representing the probability \[0-1] of exploitation in the wild in the next 30 days (following score publication).

**`created_time`**

* **Type**: `timestamp_t`
* **Requirement**: recommended

The timestamp indicating when the EPSS score was calculated.

**`version`**

* **Type**: `string_t`
* **Requirement**: recommended

The version of the EPSS model used to calculate the score.

**`created_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The timestamp indicating when the EPSS score was calculated.

**`percentile`**

* **Type**: `float_t`
* **Requirement**: optional

The EPSS score’s percentile representing relative importance and ranking of the score in the larger EPSS dataset.