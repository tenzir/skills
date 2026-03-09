# User Inventory Info (user_inventory)

User Inventory Info events report user inventory data that is either logged or proactively collected. For example, when collecting user information from Active Directory entries.

- **UID**: `3`
- **Category**: Discovery
- **Extends**: `discovery`

## Attributes

### `actor`

- **Type**: `actor`
- **Requirement**: optional
- **Group**: context

The actor describes the process that was the source of the inventory activity. In the case of user inventory data, that could be a particular process or script that is run to scrape the user data. For example, it could be a powershell process that runs to pull data from the Azure AD graph API.

### `user`

- **Type**: `user`
- **Requirement**: required
- **Group**: primary

The user that is being discovered by an inventory process.
