# Discovery (discovery)

Abstract base class for Discovery event classes. Concrete classes in this category extend this class and inherit its attributes.

- **Category**: Discovery
- **Extends**: [Base Event (base_event)](base_event.md)
- **Profiles**: `cloud`, `datetime`, `host`, `osint`, `security_control`

## Inherited attributes

**From Base Event:**
- `category_uid` (required)
- `class_uid` (required)
- `metadata` (required)
- `severity_id` (required)
- `time` (required)
- `type_uid` (required)
- `message` (recommended)
- `observables` (recommended)
- `status` (recommended)
- `status_code` (recommended)
- `status_detail` (recommended)
- `status_id` (recommended)
- `timezone_offset` (recommended)

## Attributes

### `activity_id`

- **Type**: `integer_t`
- **Sibling**: `activity_name`

#### Enum values

- `1`: `Log` - The discovered information is via a log.
- `2`: `Collect` - The discovered information is via a collection process.

The normalized identifier of the activity that triggered the event.
