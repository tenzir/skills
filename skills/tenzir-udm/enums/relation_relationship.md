# Relationship

Type of relationship between the primary entity (a) and related entity (b).

## Values

- `RELATIONSHIP_UNSPECIFIED` (0): Default value
- `OWNS` (1): Related entity is owned by the primary entity (e.g. user owns device asset).
- `ADMINISTERS` (2): Related entity is administered by the primary entity (e.g. user administers a group).
- `MEMBER` (3): Primary entity is a member of the related entity (e.g. user is a member of a group).
- `EXECUTES` (4): Primary entity may have executed the related entity.
- `DOWNLOADED_FROM` (5): Primary entity may have been downloaded from the related entity.
- `CONTACTS` (6): Primary entity contacts the related entity.
