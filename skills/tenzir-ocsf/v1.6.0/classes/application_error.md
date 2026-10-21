# Application Error (application_error)

Application Error events describe issues with an applications. The error message should be put in the event's `message` attribute. The `metadata.product` attribute can be used to capture the originating application information. The `host` profile can used to include the generating device information. This class is helpful for applications that generate or handle OCSF events and can also be used for errors in upstream products and services.

- **Class UID**: `6008`
- **Category**: Application Activity
- **Extends**: [Application Activity (application)](application.md)
- **Profiles**: [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md), [Host](../profiles/host.md), [OSINT](../profiles/osint.md), [Security Control](../profiles/security_control.md)

## Inherited attributes

**From Base Event:**
- `category_uid` (required)
- `metadata` (required)
- `severity_id` (required)
- `time` (required)
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
- `1`: `General Error` - The application has experienced an error.
- `2`: `Translation Error` - The application has experienced an error translating (mapping) a raw event to OCSF. Including the original raw event in the raw_data field is highly recommended.
- `99`: `Other` - The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

The normalized identifier of the activity that triggered the event.

### `message`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: primary

The error message as reported by the application.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `6008`: `Application Error` - Application Error events describe issues with an applications. The error message should be put in the event's `message` attribute. The `metadata.product` attribute can be used to capture the originating application information. The `host` profile can used to include the generating device information. This class is helpful for applications that generate or handle OCSF events and can also be used for errors in upstream products and services.

The unique identifier of a class. A class describes the attributes available in an event.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `600800`: `Application Error: Unknown`
- `600801`: `Application Error: General Error` - The application has experienced an error.
- `600802`: `Application Error: Translation Error` - The application has experienced an error translating (mapping) a raw event to OCSF. Including the original raw event in the raw_data field is highly recommended.
- `600899`: `Application Error: Other`

The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
