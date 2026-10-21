# Linux Process (process)

Extends the process object to add Linux specific fields

- **Extends**: [Process (process)](../../../objects/process.md)
- **Profiles**: [Linux Users](../profiles/linux_users.md)

## Constraints

- **At least one of**: `pid`, `uid`

## Inherited attributes

**From Process Entity:**
- `cmd_line` (recommended)
- `created_time` (recommended)
- `name` (recommended)
- `pid` (recommended)
- `uid` (recommended)

**From Process:**
- `file` (recommended)
- `parent_process` (recommended)
- `user` (recommended)
