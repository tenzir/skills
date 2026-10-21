# Process (process)

Extends the process object to add Windows specific fields.

- **Extends**: [Process (process)](../../../objects/process.md)

## Constraints

- **At least one of**: `pid`, `uid`, `cpid`

## Inherited attributes

**From Process Entity:**
- `cmd_line` (recommended)
- `cpid` (recommended)
- `created_time` (recommended)
- `name` (recommended)
- `pid` (recommended)
- `uid` (recommended)

**From Process:**
- `file` (recommended)
- `parent_process` (recommended)
- `user` (recommended)

## Attributes

### `hosted_services`

- **Type**: `win/win_service`
- **Requirement**: optional

The Windows services that this process is hosting.
