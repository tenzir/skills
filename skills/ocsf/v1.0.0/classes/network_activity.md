# Network Activity (network_activity)

Abstract base class for Network Activity event classes. Concrete classes in this category extend this class and inherit its attributes.

- **Category**: Network Activity
- **Extends**: [Base Event (base_event)](base_event.md)
- **Profiles**: `host`, `security_control`, `cloud`, `datetime`

## Inherited attributes

**From Base Event:**
- `metadata` (required)
- `severity_id` (required)
- `message` (recommended)
- `status_id` (recommended)

## Attributes

### `activity_id`

- **Type**: `integer_t`
- **Sibling**: `activity_name`

#### Enum values

- `99`: `Other` - The event activity is not mapped.
- `0`: `Unknown` - The event activity is unknown.

The normalized identifier of the activity that triggered the event.
