# File

> The File object represents the metadata associated with a file stored in a computer system.


The File object represents the metadata associated with a file stored in a computer system. It encompasses information about the file itself, including its attributes, properties, and organizational details. Defined by D3FEND [d3f:File](https://next.d3fend.mitre.org/dao/artifact/d3f:File/).

* **Extends**: `_entity`

## Attributes

**`name`**

* **Type**: `file_name_t`
* **Requirement**: required

The name of the file. For example: `svchost.exe`

**`type_id`**

* **Type**: `integer_t`

* **Requirement**: required

* **Values**:

  * `0` - `Unknown`: The type is unknown.
  * `1` - `Regular File`
  * `2` - `Folder`
  * `3` - `Character Device`
  * `4` - `Block Device`
  * `5` - `Local Socket`
  * `6` - `Named Pipe`
  * `7` - `Symbolic Link`
  * `99` - `Other`: The type is not mapped. See the `type` attribute, which may contain a data source specific value.

The file type ID.

**`hashes`**

* **Type**: [`fingerprint`](fingerprint.md)
* **Requirement**: recommended

An array of hash attributes.

**`path`**

* **Type**: `string_t`
* **Requirement**: recommended

The full path to the file. For example: `c:\windows\system32\svchost.exe`.

**`accessed_time`**

* **Type**: `timestamp_t`
* **Requirement**: optional

The time when the file was last accessed.

**`accessed_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The time when the file was last accessed.

**`accessor`**

* **Type**: [`user`](user.md)
* **Requirement**: optional

The name of the user who last accessed the object.

**`attributes`**

* **Type**: `integer_t`
* **Requirement**: optional

The bitmask value that represents the file attributes.

**`company_name`**

* **Type**: `string_t`
* **Requirement**: optional

The name of the company that published the file. For example: `Microsoft Corporation`.

**`confidentiality`**

* **Type**: `string_t`
* **Requirement**: optional

The file content confidentiality, normalized to the confidentiality\_id value. In the case of ‘Other’, it is defined by the event source.

**`confidentiality_id`**

* **Type**: `integer_t`

* **Requirement**: optional

* **Values**:

  * `0` - `Unknown`
  * `1` - `Not Confidential`
  * `2` - `Confidential`
  * `3` - `Secret`
  * `4` - `Top Secret`
  * `99` - `Other`

The normalized identifier of the file content confidentiality indicator.

**`created_time`**

* **Type**: `timestamp_t`
* **Requirement**: optional

The time when the file was created.

**`created_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The time when the file was created.

**`creator`**

* **Type**: [`user`](user.md)
* **Requirement**: optional

The user that created the file.

**`desc`**

* **Type**: `string_t`
* **Requirement**: optional

The description of the file, as returned by file system. For example: the description as returned by the Unix file command or the Windows file type.

**`is_system`**

* **Type**: `boolean_t`
* **Requirement**: optional

The indication of whether the object is part of the operating system.

**`mime_type`**

* **Type**: `string_t`
* **Requirement**: optional

The Multipurpose Internet Mail Extensions (MIME) type of the file, if applicable.

**`modified_time`**

* **Type**: `timestamp_t`
* **Requirement**: optional

The time when the file was last modified.

**`modified_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The time when the file was last modified.

**`modifier`**

* **Type**: [`user`](user.md)
* **Requirement**: optional

The user that last modified the file.

**`owner`**

* **Type**: [`user`](user.md)
* **Requirement**: optional

The user that owns the file/object.

**`parent_folder`**

* **Type**: `string_t`
* **Requirement**: optional

The parent folder in which the file resides. For example: `c:\windows\system32`

**`product`**

* **Type**: [`product`](product.md)
* **Requirement**: optional

The product that created or installed the file.

**`security_descriptor`**

* **Type**: `string_t`
* **Requirement**: optional

The object security descriptor.

**`signature`**

* **Type**: [`digital_signature`](digital_signature.md)
* **Requirement**: optional

The digital signature of the file.

**`size`**

* **Type**: `long_t`
* **Requirement**: optional

The size of data, in bytes.

**`type`**

* **Type**: `string_t`
* **Requirement**: optional

The file type.

**`uid`**

* **Type**: `string_t`
* **Requirement**: optional

The unique identifier of the file as defined by the storage system, such the file system file ID.

**`version`**

* **Type**: `string_t`
* **Requirement**: optional

The file version. For example: `8.0.7601.17514`.

**`xattributes`**

* **Type**: [`object`](object.md)
* **Requirement**: optional

An unordered collection of zero or more name/value pairs where each pair represents a file or folder extended attribute.For example: Windows alternate data stream attributes (ADS stream name, ADS size, etc.), user-defined or application-defined attributes, ACL, owner, primary group, etc. Examples from DCS:

* ads\_name
* ads\_size
* dacl
* owner
* primary\_group
* link\_name - name of the link associated to the file.
* hard\_link\_count - the number of links that are associated to the file.

## Used By

* [`email_file_activity`](../classes/email_file_activity.md)
* [`file_activity`](../classes/file_activity.md)
* [`network_file_activity`](../classes/network_file_activity.md)
* [`smb_activity`](../classes/smb_activity.md)