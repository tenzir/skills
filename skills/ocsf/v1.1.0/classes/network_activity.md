# Network Activity (network_activity)

Network Activity events report network connection and traffic activity.

- **Class UID**: `4001`
- **Category**: Network Activity
- **Extends**: [Network (network)](network.md)
- **Profiles**: `host`, `network_proxy`, `security_control`, `load_balancer`, `cloud`, `datetime`

## Inherited attributes

**From Network:**
- `dst_endpoint` (required)
- `src_endpoint` (required)
- `connection_info` (recommended)

**From Base Event:**
- `metadata` (required)
- `severity_id` (required)
- `message` (recommended)
- `status_id` (recommended)

## Attributes

### `url`

- **Type**: [`url`](../objects/url.md)
- **Requirement**: optional
- **Group**: primary

The URL details relevant to the network traffic.
