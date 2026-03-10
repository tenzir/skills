# Endpoint Connection

> The Endpoint Connection object contains information detailing a connection attempt to an endpoint.


The Endpoint Connection object contains information detailing a connection attempt to an endpoint.

## Attributes

**`code`**

* **Type**: `integer_t`
* **Requirement**: recommended

A numerical response status code providing details about the connection.

**`network_endpoint`**

* **Type**: [`network_endpoint`](network_endpoint.md)
* **Requirement**: recommended

Provides characteristics of the network endpoint.

## Constraints

At least one of: `network_endpoint`, `code`