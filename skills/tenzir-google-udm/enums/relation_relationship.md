# Relation.Relationship

Type of relationship between the primary entity (a) and related entity (b).

- **Full name**: `google.backstory.Relation.Relationship`
- **Values**: `7`

## Values

### `RELATIONSHIP_UNSPECIFIED`

- **Number**: `0`

Default value

### `OWNS`

- **Number**: `1`

Related entity is owned by the primary entity (e.g. user owns device asset).

### `ADMINISTERS`

- **Number**: `2`

Related entity is administered by the primary entity (e.g. user administers a group).

### `MEMBER`

- **Number**: `3`

Primary entity is a member of the related entity (e.g. user is a member of a group).

### `EXECUTES`

- **Number**: `4`

Primary entity may have executed the related entity.

### `DOWNLOADED_FROM`

- **Number**: `5`

Primary entity may have been downloaded from the related entity.

### `CONTACTS`

- **Number**: `6`

Primary entity contacts the related entity.
