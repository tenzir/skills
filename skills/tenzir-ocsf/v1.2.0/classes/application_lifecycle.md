# Application Lifecycle (application_lifecycle)

Application Lifecycle events report installation, removal, start, stop of an application or service.

- **Class UID**: `6002`
- **Category**: Application Activity
- **Extends**: [Application Activity (application)](application.md)
- **Profiles**: [Host](../profiles/host.md), [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md)

## Inherited attributes

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

### `activity_id`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `activity_name`

#### Enum values

- `0`: `Unknown` - The event activity is unknown.
- `1`: `Install`
- `2`: `Remove`
- `3`: `Start`
- `4`: `Stop`
- `99`: `Other` - The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

The normalized identifier of the activity that triggered the event.

### `app`

- **Type**: [`product`](../objects/product.md)
- **Requirement**: required
- **Group**: primary

The application that was affected by the lifecycle event.  This also applies to self-updating application systems.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `6002`: `Application Lifecycle` - Application Lifecycle events report installation, removal, start, stop of an application or service.

The unique identifier of a class. A class describes the attributes available in an event.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `600200`: `Application Lifecycle: Unknown`
- `600201`: `Application Lifecycle: Install`
- `600202`: `Application Lifecycle: Remove`
- `600203`: `Application Lifecycle: Start`
- `600204`: `Application Lifecycle: Stop`
- `600299`: `Application Lifecycle: Other`

The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
