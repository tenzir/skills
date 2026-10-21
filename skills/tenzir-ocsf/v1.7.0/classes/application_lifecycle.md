# Application Lifecycle (application_lifecycle)

Application Lifecycle events report installation, removal, start, stop of an application or service.

- **Class UID**: `6002`
- **Category**: Application Activity
- **Extends**: [Application Activity (application)](application.md)
- **Profiles**: [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md), [Host](../profiles/host.md), [OSINT](../profiles/osint.md), [Security Control](../profiles/security_control.md)

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
- `1`: `Install` - Install the application.
- `2`: `Remove` - Remove the application.
- `3`: `Start` - Start the application.
- `4`: `Stop` - Stop the application.
- `5`: `Restart` - Restart the application.
- `6`: `Enable` - Enable the application.
- `7`: `Disable` - Disable the application.
- `8`: `Update` - Update the application.
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
- `600201`: `Application Lifecycle: Install` - Install the application.
- `600202`: `Application Lifecycle: Remove` - Remove the application.
- `600203`: `Application Lifecycle: Start` - Start the application.
- `600204`: `Application Lifecycle: Stop` - Stop the application.
- `600205`: `Application Lifecycle: Restart` - Restart the application.
- `600206`: `Application Lifecycle: Enable` - Enable the application.
- `600207`: `Application Lifecycle: Disable` - Disable the application.
- `600208`: `Application Lifecycle: Update` - Update the application.
- `600299`: `Application Lifecycle: Other`

The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
