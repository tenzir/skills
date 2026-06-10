# Menu

> **Derived spec** — proposed for consistency with the design system; not
> Figma-sourced. See [source.md](../../source.md).

Floating list of actions, opened from a trigger (context menu, overflow menu,
command menu). Complements [dropdown.md](dropdown.md), which is the form
control for selecting a value.

## Props

| Prop   | Values                       |
| ------ | ---------------------------- |
| `item` | `default`, `destructive`     |

## Specifications

### Container

| Property      | Value                          |
| ------------- | ------------------------------ |
| Background    | `neutral-50`                   |
| Border        | 1px `neutral-200`              |
| Border radius | `radius` (5px)                 |
| Shadow        | `shadow-m`                     |
| Padding       | `space-1` (4px)                |
| Min width     | 160px                          |
| Layer         | `z-popover`                    |
| Offset        | `space-1` (4px) from trigger   |

### Items

| State              | Background    | Text          |
| ------------------ | ------------- | ------------- |
| Default            | transparent   | `neutral-800` |
| Hover/highlighted  | `neutral-100` | `neutral-800` |
| Pressed            | `neutral-200` | `neutral-800` |
| Disabled           | transparent   | `neutral-400` |
| Destructive        | transparent   | `red-500`     |
| Destructive hover  | `red-100`     | `red-600`     |

| Property      | Value                            |
| ------------- | -------------------------------- |
| Height        | 32px                             |
| Padding       | `space-1` / `space-2` (4px 8px)  |
| Text          | `text-sm`, regular               |
| Icon          | 16px, `space-2` (8px) gap        |
| Border radius | `radius-tight` (3px)             |
| Separator     | 1px `neutral-200`, `space-1` vertical margin |

## CSS Implementation

```css
.menu {
  background: var(--tnz-neutral-50);
  border: 1px solid var(--tnz-neutral-200);
  border-radius: var(--tnz-radius);
  box-shadow: var(--tnz-shadow-m);
  padding: var(--tnz-space-1);
  min-width: 160px;
  z-index: var(--tnz-z-popover);
}

.menu__item {
  display: flex;
  align-items: center;
  gap: var(--tnz-space-2);
  height: 32px;
  padding: var(--tnz-space-1) var(--tnz-space-2);
  border-radius: var(--tnz-radius-tight);
  font-size: var(--tnz-text-sm);
  line-height: var(--tnz-leading-sm);
  color: var(--tnz-neutral-800);
  cursor: pointer;
}

.menu__item:hover,
.menu__item--highlighted {
  background: var(--tnz-neutral-100);
}

.menu__item:active {
  background: var(--tnz-neutral-200);
}

.menu__item:disabled {
  color: var(--tnz-neutral-400);
  cursor: not-allowed;
}

.menu__item--destructive {
  color: var(--tnz-red-500);
}

.menu__item--destructive:hover {
  background: var(--tnz-red-100);
  color: var(--tnz-red-600);
}

.menu__separator {
  height: 1px;
  background: var(--tnz-neutral-200);
  margin: var(--tnz-space-1) 0;
}
```

## Usage Guidelines

1. **Ordering**:
   - Most common actions first; destructive actions last, after a separator

2. **Labels**:
   - Verb-first labels ("Rename", "Delete pipeline"); no trailing punctuation
   - Show keyboard shortcuts right-aligned in `neutral-500` when available

3. **Accessibility**:
   - Use `role="menu"`/`role="menuitem"` with roving focus
   - Support Arrow keys, Home/End, Enter, and Escape
   - Return focus to the trigger on close
