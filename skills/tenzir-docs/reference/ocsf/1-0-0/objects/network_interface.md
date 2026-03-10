# Network Interface

> The Network Interface object describes the type and associated attributes of a network interface.


The Network Interface object describes the type and associated attributes of a network interface.

* **Extends**: `_entity`

## Attributes

**`type_id`**

* **Type**: `integer_t`

* **Requirement**: required

* **Values**:

  * `0` - `Unknown`: The type is unknown.
  * `1` - `Wired`
  * `2` - `Wireless`
  * `3` - `Mobile`
  * `4` - `Tunnel`
  * `99` - `Other`: The type is not mapped. See the `type` attribute, which may contain a data source specific value.

The network interface type identifier.

**`hostname`**

* **Type**: `hostname_t`
* **Requirement**: recommended

The hostname associated with the network interface.

**`ip`**

* **Type**: `ip_t`
* **Requirement**: recommended

The IP address associated with the network interface.

**`mac`**

* **Type**: `mac_t`
* **Requirement**: recommended

The MAC address of the network interface.

**`name`**

* **Type**: `string_t`
* **Requirement**: recommended

The name of the network interface.

**`namespace`**

* **Type**: `string_t`
* **Requirement**: optional

The namespace is useful in merger or acquisition situations. For example, when similar entities exists that you need to keep separate.

**`subnet_prefix`**

* **Type**: `integer_t`
* **Requirement**: optional

The subnet prefix length determines the number of bits used to represent the network part of the IP address. The remaining bits are reserved for identifying individual hosts within that subnet.

**`type`**

* **Type**: `string_t`
* **Requirement**: optional

The type of network interface.

**`uid`**

* **Type**: `string_t`
* **Requirement**: optional

The unique identifier for the network interface.

## Constraints

At least one of: `ip`, `mac`, `name`, `hostname`

## Used By

* [`dhcp_activity`](../classes/dhcp_activity.md)