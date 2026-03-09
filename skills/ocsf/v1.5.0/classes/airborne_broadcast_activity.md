# Airborne Broadcast Activity (airborne_broadcast_activity)

Airborne Broadcast Activity events report the activity of any aircraft or unmanned system as reported and tracked by Automatic Dependent Surveillance - Broadcast (ADS-B) receivers. Based on the ADS-B standards described in [Code of Federal Regulations (CFR) Title 14 Chapter I Subchapter F Part 91](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-F/part-91#91.225) and in other general Federal Aviation Administration (FAA) supplemental orders and guidance described [here](https://www.faa.gov/about/office_org/headquarters_offices/avs/offices/afx/afs/afs400/afs410/ads-b).

- **UID**: `2`
- **Category**: Unmanned Systems
- **Extends**: `unmanned_systems`

## Attributes

### `activity_id`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: primary
- **Sibling**: `activity_name`

#### Enum values

- `0`: `Unknown` - The event activity is unknown.
- `1`: `Capture` - ADS-B information is being captured (collected).
- `2`: `Record` - ADS-B information is being recorded, for example by a standalone transceiver.
- `99`: `Other` - The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

The normalized identifier of the activity that triggered the event.

### `aircraft`

- **Type**: `aircraft`
- **Requirement**: recommended
- **Group**: primary

The Aircraft object represents any aircraft or otherwise airborne asset such as an unmanned system, airplane, balloon, spacecraft, or otherwise. The Aircraft object is intended to normalized data captured or otherwise logged from active radar, passive radar, multi-spectral systems, or the Automatic Dependant Broadcast - Surveillance (ADS-B), and/or Mode S systems.

### `dst_endpoint`

- **Type**: `network_endpoint`
- **Requirement**: optional
- **Group**: context

The destination network endpoint for the ADS-B system, if telemetry is being remotely broadcasted.

### `protocol_name`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: primary

The specific protocol associated with the ADS-B system. E.g. `ADS-B UAT` or `ADS-B ES`.

### `rssi`

- **Type**: `integer_t`
- **Requirement**: optional
- **Group**: context

Recent average RSSI (signal power) measured in dbFS. This value will always be negative, e.g., `-87.13`.

### `src_endpoint`

- **Type**: `network_endpoint`
- **Requirement**: optional
- **Group**: context

The source network endpoint for the ADS-B system.

### `traffic`

- **Type**: `network_traffic`
- **Requirement**: optional
- **Group**: context

Traffic refers to the amount of data transmitted from a ADS-B remote monitoring system at a given point of time. Ex: `bytes_in` and `bytes_out`.

### `unmanned_aerial_system`

- **Type**: `unmanned_aerial_system`
- **Requirement**: required
- **Group**: primary

The Unmanned Aerial System object describes the characteristics, Position Location Information (PLI), and other metadata of Unmanned Aerial Systems (UAS) and other unmanned and drone systems used in Remote ID. Remote ID is defined in the Standard Specification for Remote ID and Tracking (ASTM Designation: F3411-22a) [ASTM F3411-22a](https://cdn.standards.iteh.ai/samples/112830/71297057ac42432880a203654f213709/ASTM-F3411-22a.pdf).

### `unmanned_system_operating_area`

- **Type**: `unmanned_system_operating_area`
- **Requirement**: recommended
- **Group**: primary

The UAS Operating Area object describes details about a precise area of operations for a UAS flight or mission.

### `unmanned_system_operator`

- **Type**: `user`
- **Requirement**: required
- **Group**: primary

The human or machine operator of an Unmanned System.
