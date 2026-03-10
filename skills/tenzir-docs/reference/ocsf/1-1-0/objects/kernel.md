# Kernel Resource

> The Kernel Resource object provides information about a specific kernel resource, including its name and type.


The Kernel Resource object provides information about a specific kernel resource, including its name and type. It describes essential attributes associated with a resource managed by the kernel of an operating system. Defined by D3FEND [d3f:Kernel](https://d3fend.mitre.org/dao/artifact/d3f:Kernel/).

## Attributes

**`name`**

* **Type**: `string_t`
* **Requirement**: required

The name of the kernel resource.

**`type_id`**

* **Type**: `integer_t`

* **Requirement**: required

* **Values**:

  * `0` - `Unknown`: The type is unknown.
  * `1` - `Shared Mutex`
  * `2` - `System Call`
  * `99` - `Other`: The type is not mapped. See the `type` attribute, which contains a data source specific value.

The type of the kernel resource.

**`is_system`**

* **Type**: `boolean_t`
* **Requirement**: optional

The indication of whether the object is part of the operating system.

**`path`**

* **Type**: `string_t`
* **Requirement**: optional

The full path of the kernel resource.

**`system_call`**

* **Type**: `string_t`
* **Requirement**: optional

The system call that was invoked.

**`type`**

* **Type**: `string_t`
* **Requirement**: optional

The type of the kernel resource.

## Used By

* [`kernel_activity`](../classes/kernel_activity.md)