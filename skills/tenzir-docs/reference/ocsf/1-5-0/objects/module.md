# Module

> The Module object describes the load attributes of a module.


The Module object describes the load attributes of a module.

## Attributes

**`load_type_id`**

* **Type**: `integer_t`

* **Requirement**: required

* **Values**:

  * `0` - `Unknown`: The load type is unknown.
  * `1` - `Standard`: A normal module loaded by the normal windows loading mechanism i.e. LoadLibrary.
  * `2` - `Non Standard`: A module loaded in a way avoidant of normal windows procedures. i.e. Bootstrapped Loading/Manual Dll Loading.
  * `3` - `ShellCode`: A raw module in process memory that is READWRITE\_EXECUTE and had a thread started in its range.
  * `4` - `Mapped`: A memory mapped file, typically created with CreatefileMapping/MapViewOfFile.
  * `5` - `NonStandard Backed`: A module loaded in a non standard way. However, GetModuleFileName succeeds on this allocation.
  * `99` - `Other`: The load type is not mapped. See the `load_type` attribute, which contains a data source specific value.

The normalized identifier for how the module was loaded in memory.

**`base_address`**

* **Type**: `string_t`
* **Requirement**: recommended

The memory address where the module was loaded.

**`file`**

* **Type**: [`file`](file.md)
* **Requirement**: recommended

The module file object.

**`start_address`**

* **Type**: `string_t`
* **Requirement**: recommended

The start address of the execution.

**`type`**

* **Type**: `string_t`
* **Requirement**: recommended

The module type.

**`function_name`**

* **Type**: `string_t`
* **Requirement**: optional

The entry-point function of the module. The system calls the entry-point function whenever a process or thread loads or unloads the module.

**`load_type`**

* **Type**: `string_t`
* **Requirement**: optional

The load type, normalized to the caption of the load\_type\_id value. In the case of ‘Other’, it is defined by the event source.

## Used By

* [`module_activity`](../classes/module_activity.md)
* [`module_query`](../classes/module_query.md)
* [`process_activity`](../classes/process_activity.md)