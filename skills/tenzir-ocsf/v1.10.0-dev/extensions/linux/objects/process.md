# Linux Process (process)

Extends the process object to add Linux specific fields

- **Extends**: [Process (process)](../../../objects/process.md)
- **Profiles**: [Linux Users](../profiles/linux_users.md)

## Constraints

- **At least one of**: `pid`, `uid`, `cpid`

## Inherited attributes

**From Process Entity:**
- `cmd_line` (recommended)
- `cpid` (recommended)
- `created_time` (recommended)
- `name` (recommended)
- `path` (recommended)
- `pid` (recommended)
- `uid` (recommended)

**From Process:**
- `file` (recommended)
- `parent_process` (recommended)
- `user` (recommended)
