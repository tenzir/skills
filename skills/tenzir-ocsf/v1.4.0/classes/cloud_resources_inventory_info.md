# Cloud Resources Inventory Info (cloud_resources_inventory_info)

Cloud Resources Inventory Info events report cloud asset inventory data that is either logged or proactively collected. For example, use this event class when creating an inventory of cloud resource information from a Configuration Management Database (CMDB), Cyber Asset Attack Surface Management (CAASM), direct public cloud service provider APIs, Software-as-a-Service (SaaS) APIs, or otherwise.

- **Class UID**: `5023`
- **Category**: Discovery
- **Extends**: [Discovery (discovery)](discovery.md)
- **Profiles**: [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md), [Host](../profiles/host.md), [OSINT](../profiles/osint.md), [Security Control](../profiles/security_control.md)

## Constraints

- **At least one of**: `cloud`, `container`, `database`, `databucket`, `idp`, `resources`, `table`

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

### `cloud`

- **Type**: [`cloud`](../objects/cloud.md)
- **Requirement**: recommended
- **Group**: primary

Cloud service provider or SaaS platform metadata about the cloud resource(s) that are being discovered by an inventory process.

### `container`

- **Type**: [`container`](../objects/container.md)
- **Requirement**: recommended
- **Group**: primary

A cloud-based container image or running container discovered by an inventory process.

### `database`

- **Type**: [`database`](../objects/database.md)
- **Requirement**: recommended
- **Group**: primary

A cloud-based database discovered by an inventory process.

### `databucket`

- **Type**: [`databucket`](../objects/databucket.md)
- **Requirement**: recommended
- **Group**: primary

A cloud-based data bucket or other object storage discovered by an inventory process.

### `idp`

- **Type**: [`idp`](../objects/idp.md)
- **Requirement**: recommended
- **Group**: primary

The Identity Provider that is being discovered by an inventory process, or that is related to the cloud resource(s) being discovered by an inventory process.

### `region`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: context

The cloud region where the resource is located, e.g., `us-isof-south-1`, `eastus2`, `us-central1`, etc.

### `resources`

- **Type**: [`resource_details`](../objects/resource_details.md)
- **Requirement**: recommended
- **Group**: primary

The cloud resource(s) that are being discovered by an inventory process. Use this object if there is not a direct object match in the class.

### `table`

- **Type**: [`table`](../objects/table.md)
- **Requirement**: recommended
- **Group**: primary

A cloud-based database table discovered by an inventory process.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `5023`: `Cloud Resources Inventory Info` - Cloud Resources Inventory Info events report cloud asset inventory data that is either logged or proactively collected. For example, use this event class when creating an inventory of cloud resource information from a Configuration Management Database (CMDB), Cyber Asset Attack Surface Management (CAASM), direct public cloud service provider APIs, Software-as-a-Service (SaaS) APIs, or otherwise.

The unique identifier of a class. A class describes the attributes available in an event.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `502300`: `Cloud Resources Inventory Info: Unknown`
- `502301`: `Cloud Resources Inventory Info: Log` - The discovered information is via a log.
- `502302`: `Cloud Resources Inventory Info: Collect` - The discovered information is via a collection process.
- `502399`: `Cloud Resources Inventory Info: Other`

The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
