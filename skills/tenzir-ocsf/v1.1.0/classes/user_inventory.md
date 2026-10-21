# User Inventory Info (user_inventory)

User Inventory Info events report user inventory data that is either logged or proactively collected. For example, when collecting user information from Active Directory entries.

- **Class UID**: `5003`
- **Category**: Discovery
- **Extends**: [Discovery (discovery)](discovery.md)
- **Profiles**: [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md)

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

### `actor`

- **Type**: [`actor`](../objects/actor.md)
- **Requirement**: optional
- **Group**: context

The actor describes the process that was the source of the inventory activity. In the case of user inventory data, that could be a particular process or script that is run to scrape the user data. For example, it could be a powershell process that runs to pull data from the Azure AD graph API.

### `user`

- **Type**: [`user`](../objects/user.md)
- **Requirement**: required
- **Group**: primary

The user that is being discovered by an inventory process.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `5003`: `User Inventory Info` - User Inventory Info events report user inventory data that is either logged or proactively collected. For example, when collecting user information from Active Directory entries.

The unique identifier of a class. A Class describes the attributes available in an event.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `500300`: `User Inventory Info: Unknown`
- `500301`: `User Inventory Info: Log` - The discovered information is via a log.
- `500302`: `User Inventory Info: Collect` - The discovered information is via a collection process.
- `500399`: `User Inventory Info: Other`

The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
