# Relation.Relationship

Type of relationship between the primary entity (a) and related entity (b).

## Values

0. `RELATIONSHIP_UNSPECIFIED`: Default value
1. `OWNS`: Related entity is owned by the primary entity (e.g. user owns device asset).
2. `ADMINISTERS`: Related entity is administered by the primary entity (e.g. user administers a group).
3. `MEMBER`: Primary entity is a member of the related entity (e.g. user is a member of a group).
4. `EXECUTES`: Primary entity may have executed the related entity.
5. `DOWNLOADED_FROM`: Primary entity may have been downloaded from the related entity.
6. `CONTACTS`: Primary entity contacts the related entity.
