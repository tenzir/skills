# Operating System Patch State (patch_state)

Operating System Patch State reports the installation of an OS patch to a device and any associated knowledgebase articles.

- **Class UID**: `5004`
- **Category**: Discovery
- **Extends**: [Discovery (discovery)](discovery.md)
- **Profiles**: [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md), [Host](../profiles/host.md), [OSINT](../profiles/osint.md), [Record Integrity](../profiles/record_integrity.md), [Security Control](../profiles/security_control.md)

## Constraints

- **At least one of**: `device.os.sp_name`, `device.os.sp_ver`, `device.os.version`

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

### `device`

- **Type**: [`device`](../objects/device.md)
- **Requirement**: required
- **Group**: primary

The host or device where the activity was observed. Populate with details such as hostname, IP address, OS, and hardware identifiers when available from the source.

### `kb_article_list`

- **Type**: [`kb_article`](../objects/kb_article.md)
- **Requirement**: recommended
- **Group**: primary

A list of KB articles or patches related to an endpoint. A KB Article contains metadata that describes the patch or an update.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `5004`: `Operating System Patch State` - Operating System Patch State reports the installation of an OS patch to a device and any associated knowledgebase articles.

The unique identifier of a class. A class describes the attributes available in an event. Producers and mappers must set this to the `uid` defined in the event class definition. For example, `Detection Finding` is `2004`.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `500400`: `Operating System Patch State: Unknown`
- `500401`: `Operating System Patch State: Log` - The discovered information is via a log.
- `500402`: `Operating System Patch State: Collect` - The discovered information is via a collection process.
- `500499`: `Operating System Patch State: Other`

The event/finding type ID. It identifies the event's semantics and structure. Producers and mappers must compute this as `class_uid * 100 + activity_id`. It uniquely identifies the combination of event class and activity across the entire schema. For example, `Detection Finding: Create` is `200401`.
