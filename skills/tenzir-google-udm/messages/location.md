# Location

Information about a location.

## Fields

### `city`

- Type: `string` (singular)

The city.

### `state`

- Type: `string` (singular)

The state.

### `countryOrRegion`

- Type: `string` (singular)

The country or region.

### `name`

- Type: `string` (singular)

Custom location name (e.g. building or site name like "London Office"). For cloud environments, this is the region (e.g. "us-west2").

### `deskName`

- Type: `string` (singular)

Desk name or individual location, typically for an employee in an office. (e.g. "IN-BLR-BCPC-11-1121D").

### `floorName`

- Type: `string` (singular)

Floor name, number or a combination of the two for a building. (e.g. "1-A").

### `regionLatitude`

- Type: `float` (singular)
- Deprecated: `true`

Deprecated: use regionCoordinates.

### `regionLongitude`

- Type: `float` (singular)
- Deprecated: `true`

Deprecated: use regionCoordinates.

### `regionCoordinates`

- Type: `google.type.LatLng` (singular)

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

### `Location.countryOrRegion`

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
