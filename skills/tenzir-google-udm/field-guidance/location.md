# Location Field Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`
- **License**: Content licensed under Creative Commons Attribution 4.0; code samples licensed under Apache 2.0, as stated in the Google Developers Site Policies.

## Schema

- [Location](../messages/location.md)

## Fields

### `Location.city`

- **Purpose**: Stores the name of the city.
- **Encoding**: String.
- **Examples**: Sunnyvale Chicago Malaga

#### Examples

- Sunnyvale
- Chicago
- Malaga

### `Location.country_or_region`

- **Purpose**: Stores the name of the country or region of the world.
- **Encoding**: String.
- **Examples**: United States United Kingdom Spain

#### Examples

- United States
- United Kingdom
- Spain

### `Location.name`

- **Purpose**: Stores the name specific to the enterprise, such as a building or campus.
- **Encoding**: String.
- **Examples**: Campus 7B Building A2

#### Examples

- Campus 7B
- Building A2

### `Location.state`

- **Purpose**: Stores the name of the state, province, or territory.
- **Encoding**: String.
- **Examples**: California Illinois Ontario

#### Examples

- California
- Illinois
- Ontario
