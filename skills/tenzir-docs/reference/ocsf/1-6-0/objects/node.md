# Node

> Represents a node or a vertex in a graph structure.


Represents a node or a vertex in a graph structure.

## Attributes

**`uid`**

* **Type**: `string_t`
* **Requirement**: required

A unique string or numeric identifier that distinguishes this node from all others in the graph. Must be unique across all nodes.

**`name`**

* **Type**: `string_t`
* **Requirement**: recommended

A human-readable name or label for the node. Should be descriptive and unique within the graph context.

**`data`**

* **Type**: `json_t`
* **Requirement**: optional

Additional data about the node stored as key-value pairs. Can include custom properties specific to the node.

**`desc`**

* **Type**: `string_t`
* **Requirement**: optional

A human-readable description of the node’s purpose or meaning in the graph.

**`type`**

* **Type**: `string_t`
* **Requirement**: optional

Categorizes the node into a specific class or type. Useful for grouping and filtering nodes.