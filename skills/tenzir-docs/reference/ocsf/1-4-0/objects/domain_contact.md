# Domain Contact

> The contact information related to a domain registration, e.g., registrant, administrator, abuse, billing, or technical contact.


The contact information related to a domain registration, e.g., registrant, administrator, abuse, billing, or technical contact.

## Attributes

**`type_id`**

* **Type**: `integer_t`

* **Requirement**: required

* **Values**:

  * `0` - `Unknown`: The type is unknown.
  * `1` - `Registrant`: The contact information provided is for the domain registrant.
  * `2` - `Administrative`: The contact information provided is for the domain administrator.
  * `3` - `Technical`: The contact information provided is for the domain technical lead.
  * `4` - `Billing`: The contact information provided is for the domain billing lead.
  * `5` - `Abuse`: The contact information provided is for the domain abuse contact.
  * `99` - `Other`: The type is not mapped. See the `type` attribute, which contains a data source specific value.

The normalized domain contact type ID.

**`email_addr`**

* **Type**: `email_t`
* **Requirement**: recommended

The user’s primary email address.

**`location`**

* **Type**: [`location`](location.md)
* **Requirement**: recommended

Location details for the contract such as the city, state/province, country, etc.

**`name`**

* **Type**: `string_t`
* **Requirement**: optional

The individual or organization name for the contact.

**`phone_number`**

* **Type**: `string_t`
* **Requirement**: optional

The number associated with the phone.

**`type`**

* **Type**: `string_t`
* **Requirement**: optional

The Domain Contact type, normalized to the caption of the `type_id` value. In the case of ‘Other’, it is defined by the source

**`uid`**

* **Type**: `string_t`
* **Requirement**: optional

The unique identifier of the contact information, typically provided in WHOIS information.