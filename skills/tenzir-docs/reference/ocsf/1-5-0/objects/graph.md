# Graph

> A graph data structure representation with nodes and edges.


A graph data structure representation with nodes and edges.

* **Extends**: `_entity`

## Attributes

**`nodes`**

* **Type**: [`node`](node.md)
* **Requirement**: required

The nodes/vertices of the graph - contains the collection of `node` objects that make up the graph.

**`name`**

* **Type**: `string_t`
* **Requirement**: recommended

The graph name - a human readable identifier for the graph.

**`query_language_id`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`: The Query Language is unknown.
  * `1` - `Cypher`: A declarative graph query language developed by Neo4j that allows for expressive and efficient querying of graph databases.
  * `2` - `GraphQL`: A query language for APIs that enables declarative data fetching and provides a complete description of the data in the API.
  * `3` - `Gremlin`: A graph traversal language and virtual machine developed by Apache TinkerPop that enables graph computing across different graph databases.
  * `4` - `GQL`: An ISO standard graph query language designed to provide a unified way to query graph databases.
  * `5` - `G-CORE`: A graph query language that combines features from existing languages while adding support for paths as first-class citizens.
  * `6` - `PGQL`: Property Graph Query Language developed by Oracle that provides SQL-like syntax for querying property graphs.
  * `7` - `SPARQL`: A semantic query language for databases that enables querying and manipulating data stored in RDF format.
  * `99` - `Other`: The Query Language is not mapped. See the `query_language` attribute, which contains a data source specific value.

The normalized identifier of a graph query language that can be used to interact with the graph.

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

Unique identifier of the graph - a unique ID to reference this specific graph.

**`desc`**

* **Type**: `string_t`
* **Requirement**: optional

The graph description - provides additional details about the graph’s purpose and contents.

**`edges`**

* **Type**: [`edge`](edge.md)
* **Requirement**: optional

The edges/connections between nodes in the graph - contains the collection of `edge` objects defining relationships between nodes.

**`is_directed`**

* **Type**: `boolean_t`
* **Requirement**: optional

Indicates if the graph is directed (`true`) or undirected (`false`).

**`query_language`**

* **Type**: `string_t`
* **Requirement**: optional

The graph query language, normalized to the caption of the `query_language_id` value.

**`type`**

* **Type**: `string_t`
* **Requirement**: optional

The graph type. Typically useful to represent the specifc type of graph that is used.

## Constraints

At least one of: `name`, `uid`