# Affected Software Package

> The Affected Package object describes details about a software package identified as affected by a vulnerability/vulnerabilities.


The Affected Package object describes details about a software package identified as affected by a vulnerability/vulnerabilities.

* **Extends**: `package`

## Attributes

**`name`**

* **Type**: `string_t`
* **Requirement**: required

The software package name.

**`version`**

* **Type**: `string_t`
* **Requirement**: required

The software package version.

**`architecture`**

* **Type**: `string_t`
* **Requirement**: recommended

Architecture is a shorthand name describing the type of computer hardware the packaged software is meant to run on.

**`epoch`**

* **Type**: `integer_t`
* **Requirement**: optional

The software package epoch. Epoch is a way to define weighted dependencies based on version numbers.

**`fixed_in_version`**

* **Type**: `string_t`
* **Requirement**: optional

The software package version in which a reported vulnerability was patched/fixed.

**`license`**

* **Type**: `string_t`
* **Requirement**: optional

The software license applied to this package.

**`package_manager`**

* **Type**: `string_t`
* **Requirement**: optional

The software packager manager utilized to manage a package on a system, e.g. npm, yum, dpkg etc.

**`path`**

* **Type**: `string_t`
* **Requirement**: optional

The installation path of the affected package.

**`purl`**

* **Type**: `string_t`
* **Requirement**: optional

A purl is a URL string used to identify and locate a software package in a mostly universal and uniform way across programming languages, package managers, packaging conventions, tools, APIs and databases.

**`release`**

* **Type**: `string_t`
* **Requirement**: optional

Release is the number of times a version of the software has been packaged.

**`remediation`**

* **Type**: [`remediation`](remediation.md)
* **Requirement**: optional

Describes the recommended remediation steps to address identified issue(s).