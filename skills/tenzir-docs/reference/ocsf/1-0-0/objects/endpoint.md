# Endpoint

> The Endpoint object describes a physical or virtual device that connects to and exchanges information with a computer network.


The Endpoint object describes a physical or virtual device that connects to and exchanges information with a computer network. Some examples of endpoints are mobile devices, desktop computers, virtual machines, embedded devices, and servers. Internet-of-Things devices—like cameras, lighting, refrigerators, security systems, smart speakers, and thermostats—are also endpoints.

* **Extends**: `_entity`

## Attributes

**`hostname`**

* **Type**: `hostname_t`
* **Requirement**: recommended

The fully qualified name of the endpoint.

**`instance_uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The unique identifier of a VM instance.

**`interface_name`**

* **Type**: `string_t`
* **Requirement**: recommended

The name of the network interface (e.g. eth2).

**`interface_uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The unique identifier of the network interface.

**`ip`**

* **Type**: `ip_t`
* **Requirement**: recommended

The IP address of the endpoint, in either IPv4 or IPv6 format.

**`name`**

* **Type**: `string_t`
* **Requirement**: recommended

The short name of the endpoint.

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The unique identifier of the endpoint.

**`domain`**

* **Type**: `string_t`
* **Requirement**: optional

The name of the domain.

**`location`**

* **Type**: [`location`](location.md)
* **Requirement**: optional

The geographical location of the endpoint.

**`mac`**

* **Type**: `mac_t`
* **Requirement**: optional

The Media Access Control (MAC) address of the endpoint.

**`subnet_uid`**

* **Type**: `string_t`
* **Requirement**: optional

The unique identifier of a virtual subnet.

**`vlan_uid`**

* **Type**: `string_t`
* **Requirement**: optional

The Virtual LAN identifier.

**`vpc_uid`**

* **Type**: `string_t`
* **Requirement**: optional

The unique identifier of the Virtual Private Cloud (VPC).

## Constraints

At least one of: `ip`, `uid`, `name`, `hostname`, `instance_uid`, `interface_uid`, `interface_name`