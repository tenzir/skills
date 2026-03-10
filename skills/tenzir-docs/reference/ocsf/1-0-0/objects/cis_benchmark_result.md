# CIS Benchmark Result

> The CIS Benchmark Result object contains information as defined by the Center for Internet Security ([CIS](https://www.cisecurity.org/cis-benchmarks/)) benchmark result.


The CIS Benchmark Result object contains information as defined by the Center for Internet Security ([CIS](https://www.cisecurity.org/cis-benchmarks/)) benchmark result. CIS Benchmarks are a collection of best practices for securely configuring IT systems, software, networks, and cloud infrastructure.

## Attributes

**`name`**

* **Type**: `string_t`
* **Requirement**: required

The CIS benchmark name.

**`desc`**

* **Type**: `string_t`
* **Requirement**: optional

The CIS benchmark description.

**`remediation`**

* **Type**: [`remediation`](remediation.md)
* **Requirement**: optional

The remediation recommendations on how to fix the identified issue(s).

**`rule`**

* **Type**: [`rule`](rule.md)
* **Requirement**: optional

The CIS benchmark rule.

## Used By

* [`config_state`](../classes/config_state.md)