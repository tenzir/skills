# Application Error (application_error)

Application Error events describe issues with an applications. The error message should be put in the event's `message` attribute. The `metadata.product` attribute can be used to capture the originating application information. The `host` profile can used to include the generating device information. This class is helpful (and originally intended for) applications that generate and/or handle OCSF events. This class can also be used for errors in upstream products and services.

- **UID**: `8`
- **Category**: Application Activity
- **Extends**: `application`

## Attributes

### `activity_id`

- **Type**: `integer_t`
- **Sibling**: `activity_name`

#### Enum values

- `1`: `General Error` - The application has experienced an error.
- `2`: `Translation Error` - The application has experienced an error translating (mapping) a raw event to OCSF. Including the original raw event in the raw_data field is highly recommended.

The normalized identifier of the activity that triggered the event.

### `message`

- **Type**: `string_t`

The error message as reported by the application.
