# Software Package

> The Software Package object describes details about a software package.


The Software Package object describes details about a software package. Defined by D3FEND [d3f:SoftwarePackage](https://d3fend.mitre.org/dao/artifact/d3f:SoftwarePackage/).

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

**`license`**

* **Type**: `string_t`
* **Requirement**: optional

The software license applied to this package.

**`release`**

* **Type**: `string_t`
* **Requirement**: optional

Release is the number of times a version of the software has been packaged.