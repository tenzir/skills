# Network Activity (network_activity)

Network Activity events report network connection and traffic activity.

- **Class UID**: `4001`
- **Category**: Network Activity
- **Extends**: [Network (network)](network.md)
- **Profiles**: `host`, `network_proxy`, `security_control`, `load_balancer`, `cloud`, `datetime`, `osint`

## Inherited attributes

**From Network:**
- `dst_endpoint` (required)
- `connection_info` (recommended)
- `proxy` (recommended)
- `src_endpoint` (recommended)
- `traffic` (recommended)

**From Base Event:**
- `metadata` (required)
- `severity_id` (required)
- `message` (recommended)
- `observables` (recommended)
- `status` (recommended)
- `status_code` (recommended)
- `status_detail` (recommended)
- `status_id` (recommended)

## Attributes

### `url`

- **Type**: [`url`](../objects/url.md)
- **Requirement**: recommended
- **Group**: primary

The URL details relevant to the network traffic.
