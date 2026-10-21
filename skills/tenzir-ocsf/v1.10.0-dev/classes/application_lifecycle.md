# Application Lifecycle (application_lifecycle)

Application Lifecycle events report installation, removal, start, stop of an application or service.

- **Class UID**: `6002`
- **Category**: Application Activity
- **Extends**: [Application Activity (application)](application.md)
- **Profiles**: [AI Operation](../profiles/ai_operation.md), [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md), [Host](../profiles/host.md), [OSINT](../profiles/osint.md), [Record Integrity](../profiles/record_integrity.md), [Security Control](../profiles/security_control.md)

## Constraints

- **At least one of**: `app`, `application`

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

### `ai_agent`

- **Type**: [`ai_agent`](../objects/ai_agent.md)
- **Requirement**: optional
- **Group**: context

The affected application, when it is itself an AI agent.

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

The normalized identifier of the activity that triggered the event. Each event class defines its own set of activity values. Use `0` (Unknown) when the activity cannot be determined. Use `99` (Other) when the activity does not match any defined value, in which case `activity_name` must be populated with the source-specific label.

### `app`

- **Type**: [`product`](../objects/product.md)
- **Requirement**: recommended
- **Group**: context

> **Deprecated since v1.9.0.** Use the `application` attribute instead.

The application that was affected by the lifecycle event.  This also applies to self-updating application systems.

### `application`

- **Type**: [`application`](../objects/application.md)
- **Requirement**: recommended
- **Group**: primary

The application that was affected by the lifecycle event. This also applies to self-updating application systems. Product identity, such as vendor and version, can be conveyed via the nested `product` attribute.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `6002`: `Application Lifecycle` - Application Lifecycle events report installation, removal, start, stop of an application or service.

The unique identifier of a class. A class describes the attributes available in an event. Producers and mappers must set this to the `uid` defined in the event class definition. For example, `Detection Finding` is `2004`.

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

The event/finding type ID. It identifies the event's semantics and structure. Producers and mappers must compute this as `class_uid * 100 + activity_id`. It uniquely identifies the combination of event class and activity across the entire schema. For example, `Detection Finding: Create` is `200401`.
