# Geo Location

> The Geo Location object describes a geographical location, usually associated with an IP address.


The Geo Location object describes a geographical location, usually associated with an IP address. Defined by D3FEND [d3f:PhysicalLocation](https://d3fend.mitre.org/dao/artifact/d3f:PhysicalLocation/).

## Attributes

**`city`**

* **Type**: `string_t`
* **Requirement**: recommended

The name of the city.

**`continent`**

* **Type**: `string_t`
* **Requirement**: recommended

The name of the continent.

**`country`**

* **Type**: `string_t`
* **Requirement**: recommended

The ISO 3166-1 Alpha-2 country code. For the complete list of country codes see [ISO 3166-1 alpha-2 codes](https://www.iso.org/obp/ui/#iso:pub:PUB500001:en).

Note: The two letter country code should be capitalized. For example: `US` or `CA`.

**`coordinates`**

* **Type**: `float_t`
* **Requirement**: optional

A two-element array, containing a longitude/latitude pair. The format conforms with [GeoJSON](https://geojson.org). For example: `[-73.983, 40.719]`.

**`desc`**

* **Type**: `string_t`
* **Requirement**: optional

The description of the geographical location.

**`geohash`**

* **Type**: `string_t`
* **Requirement**: optional

Geohash of the geo-coordinates (latitude and longitude).[Geohashing](https://en.wikipedia.org/wiki/Geohash) is a geocoding system used to encode geographic coordinates in decimal degrees, to a single string.

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

**`provider`**

* **Type**: `string_t`
* **Requirement**: optional

The provider of the geographical location data.

**`region`**

* **Type**: `string_t`
* **Requirement**: optional

The alphanumeric code that identifies the principal subdivision (e.g. province or state) of the country. Region codes are defined at [ISO 3166-2](https://www.iso.org/iso-3166-country-codes.html) and have a limit of three characters. For example, see [the region codes for the US](https://www.iso.org/obp/ui/#iso:code:3166:US).

## Constraints

At least one of: `city`, `country`, `postal_code`, `region`