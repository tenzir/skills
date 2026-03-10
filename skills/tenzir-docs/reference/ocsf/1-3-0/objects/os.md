# Operating System (OS)

> The Operating System (OS) object describes characteristics of an OS, such as Linux or Windows.


The Operating System (OS) object describes characteristics of an OS, such as Linux or Windows. Defined by D3FEND [d3f:OperatingSystem](https://d3fend.mitre.org/dao/artifact/d3f:OperatingSystem/).

## Attributes

**`name`**

* **Type**: `string_t`
* **Requirement**: required

The operating system name.

**`type_id`**

* **Type**: `integer_t`

* **Requirement**: required

* **Values**:

  * `0` - `Unknown`: The type is unknown.
  * `99` - `Other`: The type is not mapped. See the `type` attribute, which contains a data source specific value.
  * `100` - `Windows`
  * `101` - `Windows Mobile`
  * `200` - `Linux`
  * `201` - `Android`
  * `300` - `macOS`
  * `301` - `iOS`
  * `302` - `iPadOS`
  * `400` - `Solaris`
  * `401` - `AIX`
  * `402` - `HP-UX`

The type identifier of the operating system.

**`build`**

* **Type**: `string_t`
* **Requirement**: optional

The operating system build number.

**`country`**

* **Type**: `string_t`
* **Requirement**: optional

The operating system country code, as defined by the ISO 3166-1 standard (Alpha-2 code). For the complete list of country codes, see [ISO 3166-1 alpha-2 codes](https://www.iso.org/obp/ui/#iso:pub:PUB500001:en).

**`cpe_name`**

* **Type**: `string_t`
* **Requirement**: optional

The Common Platform Enumeration (CPE) name as described by ([NIST](https://nvd.nist.gov/products/cpe)) For example: `cpe:/a:apple:safari:16.2`.

**`cpu_bits`**

* **Type**: `integer_t`
* **Requirement**: optional

The cpu architecture, the number of bits used for addressing in memory. For example: `32` or `64`.

**`edition`**

* **Type**: `string_t`
* **Requirement**: optional

The operating system edition. For example: `Professional`.

**`lang`**

* **Type**: `string_t`
* **Requirement**: optional

The two letter lower case language codes, as defined by [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1). For example: `en` (English), `de` (German), or `fr` (French).

**`sp_name`**

* **Type**: `string_t`
* **Requirement**: optional

The name of the latest Service Pack.

**`sp_ver`**

* **Type**: `integer_t`
* **Requirement**: optional

The version number of the latest Service Pack.

**`type`**

* **Type**: `string_t`
* **Requirement**: optional

The type of the operating system.

**`version`**

* **Type**: `string_t`
* **Requirement**: optional

The version of the OS running on the device that originated the event. For example: “Windows 10”, “OS X 10.7”, or “iOS 9”.