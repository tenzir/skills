# Networks Query (networks_query)

Networks Query events report information about network adapters.

- **UID**: `13`
- **Category**: Discovery
- **Extends**: `discovery_result`

## Attributes

### `network_interfaces`

- **Type**: `network_interface`
- **Requirement**: required
- **Group**: primary

The physical or virtual network interfaces that are associated with the device, one for each unique MAC address/IP address/hostname/name combination.

Note: The first element of the array is the network information that pertains to the event.
