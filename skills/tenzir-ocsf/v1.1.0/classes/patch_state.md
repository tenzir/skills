# Operating System Patch State (patch_state)

Operating System Patch State reports the installation of an OS patch to a device and any associated knowledgebase articles.

- **Class UID**: `5004`
- **Category**: Discovery
- **Extends**: [Discovery (discovery)](discovery.md)
- **Profiles**: [Host](../profiles/host.md), [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md)

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
- `status_id` (recommended)
- `timezone_offset` (recommended)

## Attributes

### `device`

- **Type**: [`device`](../objects/device.md)
- **Requirement**: required
- **Group**: primary

An addressable device, computer system or host.

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

The unique identifier of a class. A Class describes the attributes available in an event.

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

The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
