# Location

Information about a location.

- **Full name**: `google.backstory.Location`
- **Fields**: `9`

## Fields

### `city`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `city`

The city.

### `state`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `state`

The state.

### `country_or_region`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `countryOrRegion`

The country or region.

### `name`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `name`

Custom location name (e.g. building or site name like "London Office"). For cloud environments, this is the region (e.g. "us-west2").

### `desk_name`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `deskName`

Desk name or individual location, typically for an employee in an office. (e.g. "IN-BLR-BCPC-11-1121D").

### `floor_name`

- **Number**: `6`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `floorName`

Floor name, number or a combination of the two for a building. (e.g. "1-A").

### `region_latitude`

- **Number**: `7`
- **Cardinality**: `singular`
- **Type**: `float`
- **JSON name**: `regionLatitude`
- **Deprecated**: `true`

Deprecated: use region_coordinates.

### `region_longitude`

- **Number**: `8`
- **Cardinality**: `singular`
- **Type**: `float`
- **JSON name**: `regionLongitude`
- **Deprecated**: `true`

Deprecated: use region_coordinates.

### `region_coordinates`

- **Number**: `9`
- **Cardinality**: `singular`
- **Type**: `google.type.LatLng`
- **JSON name**: `regionCoordinates`

Coordinates for the associated region. See [https://cloud.google.com/vision/docs/reference/rest/v1/LatLng](https://cloud.google.com/vision/docs/reference/rest/v1/LatLng) for a description of the fields.

## Guidance

Population guidance from the Google UDM usage guide.

### `Location.city`

- **Purpose**: Stores the name of the city.
- **Encoding**: String.

#### Examples

- Sunnyvale
- Chicago
- Malaga

### `Location.country_or_region`

- **Purpose**: Stores the name of the country or region of the world.
- **Encoding**: String.

#### Examples

- United States
- United Kingdom
- Spain

### `Location.name`

- **Purpose**: Stores the name specific to the enterprise, such as a building or campus.
- **Encoding**: String.

#### Examples

- Campus 7B
- Building A2

### `Location.state`

- **Purpose**: Stores the name of the state, province, or territory.
- **Encoding**: String.

#### Examples

- California
- Illinois
- Ontario
