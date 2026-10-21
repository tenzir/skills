# OSINT Inventory Info (osint_inventory_info)

OSINT Inventory Info events report open source intelligence or threat intelligence inventory data that is either logged or proactively collected. For example, when collecting OSINT information from Threat Intelligence Platforms (TIPs) or Extended Detection and Response (XDR) platforms, or collecting data from OSINT or other generic threat intelligence and enrichment feeds such as APIs and datastores.

- **Class UID**: `5021`
- **Category**: Discovery
- **Extends**: [Discovery (discovery)](discovery.md)
- **Profiles**: [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md), [Host](../profiles/host.md), [OSINT](../profiles/osint.md), [Security Control](../profiles/security_control.md)

## Inherited attributes

**From Discovery:**
- `activity_id` (required)

**From Base Event:**
- `category_uid` (required)
- `metadata` (required)
- `severity_id` (required)
- `time` (required)
- `message` (recommended)
- `observables` (recommended)
- `status` (recommended)
- `status_code` (recommended)
- `status_detail` (recommended)
- `status_id` (recommended)
- `timezone_offset` (recommended)

## Attributes

### `actor`

- **Type**: [`actor`](../objects/actor.md)
- **Requirement**: optional
- **Group**: context

The actor describes the process that was the source of the inventory activity. In the case of OSINT inventory data, that could be a particular process or script that is run to scrape the OSINT or threat intelligence data. For example, it could be a Python process that runs to pull data from a MISP or Shodan API.

### `osint`

- **Type**: [`osint`](../objects/osint.md)
- **Requirement**: required
- **Group**: primary

The OSINT that is being discovered by an inventory process.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `5021`: `OSINT Inventory Info` - OSINT Inventory Info events report open source intelligence or threat intelligence inventory data that is either logged or proactively collected. For example, when collecting OSINT information from Threat Intelligence Platforms (TIPs) or Extended Detection and Response (XDR) platforms, or collecting data from OSINT or other generic threat intelligence and enrichment feeds such as APIs and datastores.

The unique identifier of a class. A class describes the attributes available in an event.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `502100`: `OSINT Inventory Info: Unknown`
- `502101`: `OSINT Inventory Info: Log` - The discovered information is via a log.
- `502102`: `OSINT Inventory Info: Collect` - The discovered information is via a collection process.
- `502199`: `OSINT Inventory Info: Other`

The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
