# Unmanned Aerial System

> The Unmanned Aerial System object describes the characteristics, Position Location Information (PLI), and other metadata of Unmanned Aerial Systems (UAS) and other unmanned and drone systems used in Remote ID.


The Unmanned Aerial System object describes the characteristics, Position Location Information (PLI), and other metadata of Unmanned Aerial Systems (UAS) and other unmanned and drone systems used in Remote ID. Remote ID is defined in the Standard Specification for Remote ID and Tracking (ASTM Designation: F3411-22a) [ASTM F3411-22a](https://cdn.standards.iteh.ai/samples/112830/71297057ac42432880a203654f213709/ASTM-F3411-22a.pdf).

* **Extends**: `aircraft`

## Attributes

**`location`**

* **Type**: [`location`](location.md)
* **Requirement**: recommended

The detailed geographical location usually associated with an IP address.

**`serial_number`**

* **Type**: `string_t`
* **Requirement**: recommended

The serial number of the unmanned system. This is expressed in `CTA-2063-A` format.

**`type_id`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown/Undeclared`: The UAS type is empty or not declared.
  * `1` - `Airplane`
  * `2` - `Helicopter`: Can also be a Multi-rotor Unmanned Aircraft (e.g., Quad-copter).
  * `3` - `Gyroplane`
  * `4` - `Hybrid Lift`: Fixed wing aircraft that can take off vertically.
  * `5` - `Ornithopter`
  * `6` - `Glider`
  * `7` - `Kite`
  * `8` - `Free Balloon`
  * `9` - `Captive Balloon`
  * `10` - `Airship`: E.g., a blimp.
  * `11` - `Free Fall/Parachute`: Parachutes, or objects without any power or propulsion mechanism.
  * `12` - `Rocket`
  * `13` - `Tethered Powered Aircraft`
  * `14` - `Ground Obstacle`
  * `99` - `Other`: The type is not mapped. See the `type` attribute, which contains a data source specific value.

The UAS type identifier.

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The primary identification identifier for an unmanned system. This can be a Serial Number (in `CTA-2063-A` format, the Registration ID (provided by the `CAA`, a UTM, or a unique Session ID.

**`uid_alt`**

* **Type**: `string_t`
* **Requirement**: recommended

A secondary identification identifier for an unmanned system. This can be a Serial Number (in `CTA-2063-A` format, the Registration ID (provided by the `CAA`, a UTM, or a unique Session ID.

**`uuid`**

* **Type**: `uuid_t`
* **Requirement**: recommended

The Unmanned Aircraft System Traffic Management (UTM) provided universal unique ID (UUID) traceable to a non-obfuscated ID where this UTM UUID acts as a ‘session id’ to protect exposure of operationally sensitive information.

**`hw_info`**

* **Type**: [`device_hw_info`](device_hw_info.md)
* **Requirement**: optional

The endpoint hardware information.

**`model`**

* **Type**: `string_t`
* **Requirement**: optional

The model name of the aircraft or unmanned system.

**`name`**

* **Type**: `string_t`
* **Requirement**: optional

The name of the unmanned system as reported by tracking or sensing hardware.

**`speed`**

* **Type**: `string_t`
* **Requirement**: optional

Ground speed of flight. This value is provided in meters per second with a minimum resolution of 0.25 m/s. Special Values: `Invalid`, `No Value`, or `Unknown: 255 m/s`.

**`speed_accuracy`**

* **Type**: `string_t`
* **Requirement**: optional

Provides quality/containment on horizontal ground speed. Measured in meters/second.

**`track_direction`**

* **Type**: `string_t`
* **Requirement**: optional

Direction of flight expressed as a “True North-based” ground track angle. This value is provided in clockwise degrees with a minimum resolution of 1 degree. If aircraft is not moving horizontally, use the “Unknown” value

**`type`**

* **Type**: `string_t`
* **Requirement**: optional

The type of the UAS. For example, Helicopter, Gyroplane, Rocket, etc.

**`vertical_speed`**

* **Type**: `string_t`
* **Requirement**: optional

Vertical speed upward relative to the WGS-84 datum, measured in meters per second. Special Values: `Invalid`, `No Value`, or `Unknown: 63 m/s`.

## Constraints

At least one of: `name`, `serial_number`, `uid`, `uid_alt`

## Used By

* [`airborne_broadcast_activity`](../classes/airborne_broadcast_activity.md)
* [`drone_flights_activity`](../classes/drone_flights_activity.md)