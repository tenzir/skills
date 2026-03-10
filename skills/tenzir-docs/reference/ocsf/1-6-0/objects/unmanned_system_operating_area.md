# Unmanned System Operating Area

> The Unmanned System Operating Area object describes details about a precise area of operations for a UAS flight or mission.


The Unmanned System Operating Area object describes details about a precise area of operations for a UAS flight or mission.

* **Extends**: `location`

## Attributes

**`city`**

* **Type**: `string_t`
* **Requirement**: recommended

The name of the city.

**`continent`**

* **Type**: `string_t`
* **Requirement**: recommended

The name of the continent.

**`count`**

* **Type**: `integer_t`
* **Requirement**: recommended

Indicates the number of UAS in the operating area.

**`country`**

* **Type**: `string_t`
* **Requirement**: recommended

The ISO 3166-1 Alpha-2 country code.

Note: The two letter country code should be capitalized. For example: `US` or `CA`.

**`locations`**

* **Type**: [`location`](location.md)
* **Requirement**: recommended

A list of Position Location Information (PLI) (latitude/longitude pairs) defining the area where a group or Intent-Based Network Participant operation is taking place. (This field is only applicable to Network Remote ID.)

**`type_id`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown/Undeclared`: The UA type is empty or not declared.
  * `1` - `Takeoff Location`
  * `2` - `Fixed Location`
  * `3` - `Dynamic Location`
  * `99` - `Other`: The type is not mapped. See the `type` attribute, which contains a data source specific value.

The operating area type identifier.

**`aerial_height`**

* **Type**: `string_t`
* **Requirement**: optional

Expressed as either height above takeoff location or height above ground level (AGL) for a UAS current location. This value is provided in meters and must have a minimum resolution of 1 m. Special Values: `Invalid`, `No Value`, or `Unknown: -1000 m`.

**`altitude_ceiling`**

* **Type**: `string_t`
* **Requirement**: optional

Maximum altitude (WGS-84 HAE) for a group or an Intent-Based Network Participant. Measured in meters. Special Values: `Invalid`, `No Value`, or `Unknown: -1000 m`.

**`altitude_floor`**

* **Type**: `string_t`
* **Requirement**: optional

Minimum altitude (WGS-84 HAE) for a group or an Intent-Based Network Participant. Measured in meters. Special Values: `Invalid`, `No Value`, or `Unknown: -1000 m`.

**`coordinates`**

* **Type**: `float_t`
* **Requirement**: optional

A two-element array, containing a longitude/latitude pair. The format conforms with [GeoJSON](https://geojson.org). For example: `[-73.983, 40.719]`.

**`desc`**

* **Type**: `string_t`
* **Requirement**: optional

The description of the geographical location.

**`end_time`**

* **Type**: `timestamp_t`
* **Requirement**: optional

The date and time at which a group or an Intent-Based Network Participant operation ends. (This field is only applicable to Network Remote ID.)

**`end_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The date and time at which a group or an Intent-Based Network Participant operation ends. (This field is only applicable to Network Remote ID.)

**`geodetic_altitude`**

* **Type**: `string_t`
* **Requirement**: optional

The aircraft distance above or below the ellipsoid as measured along a line that passes through the aircraft and is normal to the surface of the WGS-84 ellipsoid. This value is provided in meters and must have a minimum resolution of 1 m. Special Values: `Invalid`, `No Value`, or `Unknown: -1000 m`.

**`geodetic_vertical_accuracy`**

* **Type**: `string_t`
* **Requirement**: optional

Provides quality/containment on geodetic altitude. This is based on ADS-B Geodetic Vertical Accuracy (GVA). Measured in meters.

**`geohash`**

* **Type**: `string_t`
* **Requirement**: optional

Geohash of the geo-coordinates (latitude and longitude).[Geohashing](https://en.wikipedia.org/wiki/Geohash) is a geocoding system used to encode geographic coordinates in decimal degrees, to a single string.

**`horizontal_accuracy`**

* **Type**: `string_t`
* **Requirement**: optional

Provides quality/containment on horizontal position. This is based on ADS-B NACp. Measured in meters.

**`is_on_premises`**

* **Type**: `boolean_t`
* **Requirement**: optional

The indication of whether the location is on premises.

**`isp`**

* **Type**: `string_t`
* **Requirement**: optional

The name of the Internet Service Provider (ISP).

**`lat`**

* **Type**: `float_t`
* **Requirement**: optional

The geographical Latitude coordinate represented in Decimal Degrees (DD). For example: `42.361145`.

**`long`**

* **Type**: `float_t`
* **Requirement**: optional

The geographical Longitude coordinate represented in Decimal Degrees (DD). For example: `-71.057083`.

**`postal_code`**

* **Type**: `string_t`
* **Requirement**: optional

The postal code of the location.

**`pressure_altitude`**

* **Type**: `string_t`
* **Requirement**: optional

The uncorrected barometric pressure altitude (based on reference standard 29.92 inHg, 1013.25 mb) provides a reference for algorithms that utilize ‘altitude deltas’ between aircraft. This value is provided in meters and must have a minimum resolution of 1 m.. Special Values: `Invalid`, `No Value`, or `Unknown: -1000 m`.

**`provider`**

* **Type**: `string_t`
* **Requirement**: optional

The provider of the geographical location data.

**`radius`**

* **Type**: `string_t`
* **Requirement**: optional

Farthest horizontal distance from the reported location at which any UA in a group may be located (meters). Also allows defining the area where an Intent-Based Network Participant operation is taking place. Default: 0 m.

**`region`**

* **Type**: `string_t`
* **Requirement**: optional

The alphanumeric code that identifies the principal subdivision (e.g. province or state) of the country. For example, ‘CH-VD’ for the Canton of Vaud, Switzerland

**`start_time`**

* **Type**: `timestamp_t`
* **Requirement**: optional

The date and time at which a group or an Intent-Based Network Participant operation starts. (This field is only applicable to Network Remote ID.)

**`start_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The date and time at which a group or an Intent-Based Network Participant operation starts. (This field is only applicable to Network Remote ID.)

**`type`**

* **Type**: `string_t`
* **Requirement**: optional

The type of operating area. For example, `Takeoff Location`, `Fixed Location`, `Dynamic Location`.

## Constraints

At least one of: `city`, `country`, `postal_code`, `region`

## Used By

* [`airborne_broadcast_activity`](../classes/airborne_broadcast_activity.md)
* [`drone_flights_activity`](../classes/drone_flights_activity.md)