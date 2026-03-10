# Identity Provider

> The Identity Provider object contains detailed information about a provider responsible for creating, maintaining, and managing identity information while offering authentication services to applications.


The Identity Provider object contains detailed information about a provider responsible for creating, maintaining, and managing identity information while offering authentication services to applications. An Identity Provider (IdP) serves as a trusted authority that verifies the identity of users and issues authentication tokens or assertions to enable secure access to applications or services.

* **Extends**: `_entity`

## Attributes

**`name`**

* **Type**: `string_t`
* **Requirement**: recommended

The name of the identity provider.

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The unique identifier of the identity provider.

## Constraints

At least one of: `name`, `uid`