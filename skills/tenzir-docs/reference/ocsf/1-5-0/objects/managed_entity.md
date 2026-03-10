# Managed Entity

> The Managed Entity object describes the type and version of an entity, such as a user, device, or policy.


The Managed Entity object describes the type and version of an entity, such as a user, device, or policy. For types in the `type_id` enum list, an associated attribute should be populated. If the type of entity is not in the `type_id` list, information can be put into the `data` attribute, `type_id` should be ‘Other’ and the `type` attribute should label the entity type.

* **Extends**: `_entity`

## Attributes

**`device`**

* **Type**: [`device`](device.md)
* **Requirement**: recommended

An addressable device, computer system or host.

**`email`**

* **Type**: [`email`](email.md)
* **Requirement**: recommended

The email object.

**`group`**

* **Type**: [`group`](group.md)
* **Requirement**: recommended

The group object associated with an entity such as user, policy, or rule.

**`name`**

* **Type**: `string_t`
* **Requirement**: recommended

The name of the managed entity. It should match the name of the specific entity object’s name if populated, or the name of the managed entity if the `type_id` is ‘Other’.

**`org`**

* **Type**: [`organization`](organization.md)
* **Requirement**: recommended

Organization and org unit relevant to the event or object.

**`policy`**

* **Type**: [`policy`](policy.md)
* **Requirement**: recommended

Describes details of a managed policy.

**`type`**

* **Type**: `string_t`
* **Requirement**: recommended

The managed entity type. For example: `Policy`, `User`, `Organization`, `Device`.

**`type_id`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`: The type is unknown.
  * `1` - `Device`: A managed Device entity. This item corresponds to population of the `device` attribute.
  * `2` - `User`: A managed User entity. This item corresponds to population of the `user` attribute.
  * `3` - `Group`: A managed Group entity. This item corresponds to population of the `group` attribute.
  * `4` - `Organization`: A managed Organization entity. This item corresponds to population of the `org` attribute.
  * `5` - `Policy`: A managed Policy entity. This item corresponds to population of the `policy` attribute.
  * `6` - `Email`: A managed Email entity. This item corresponds to population of the `email` attribute.
  * `7` - `Network Zone`: A managed Network Zone entity. Populate the `name` attribute with the zone name and/or the `uid` attribute with the zone ID. Additional zone information can be added to the `data` attribute.
  * `99` - `Other`: The type is not mapped. See the `type` attribute, which contains a data source specific value.

The type of the Managed Entity. It is recommended to also populate the `type` attribute with the associated label, or the source specific name if `Other`.

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The identifier of the managed entity. It should match the `uid` of the specific entity’s object UID if populated, or the source specific ID if the `type_id` is ‘Other’.

**`user`**

* **Type**: [`user`](user.md)
* **Requirement**: recommended

The user that pertains to the event or object.

**`version`**

* **Type**: `string_t`
* **Requirement**: recommended

The version of the managed entity. For example: `1.2.3`.

**`data`**

* **Type**: `json_t`
* **Requirement**: optional

The managed entity content as a JSON object.

**`location`**

* **Type**: [`location`](location.md)
* **Requirement**: optional

The detailed geographical location usually associated with an IP address.

## Constraints

At least one of: `name`, `uid`, `device`, `group`, `org`, `policy`, `user`

## Used By

* [`entity_management`](../classes/entity_management.md)