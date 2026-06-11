# Modal

Blocking overlay surface for focused tasks. Comes in two variants: a centered
dialog and an edge-anchored sidepanel.

## Props

| Prop      | Values               |
| --------- | -------------------- |
| `variant` | `dialog`, `sidepanel` |
| `size`    | `s` (400px), `m` (560px), `l` (720px) |

## Specifications

### Shared

| Property   | Value                                        |
| ---------- | -------------------------------------------- |
| Surface    | `neutral-50`                                 |
| Shadow     | `shadow-l`                                   |
| Backdrop   | `neutral-800` at `dim-50`, `z-overlay`       |
| Layer      | dialog `z-modal`, sidepanel `z-sidepanel`    |
| Header     | `text-lg` semibold, `neutral-800`            |
| Padding    | `space-6` (24px); `space-4` (16px) for small dialogs |
| Section gap | `space-4` (16px) between header, body, footer |

### Dialog

| Property      | Value                            |
| ------------- | -------------------------------- |
| Border radius | `radius` (5px)                   |
| Position      | centered, top-aligned at ~20vh for tall content |
| Max height    | 80vh, body scrolls               |

### Sidepanel

| Property      | Value                              |
| ------------- | ---------------------------------- |
| Border radius | 0 (flush with the viewport edge)   |
| Position      | right edge, full height            |
| Width         | size token; resizable panels keep a 320px minimum |

## CSS Implementation

```css
/* Backdrop */
.modal-backdrop {
  position: fixed;
  inset: 0;
  background: rgb(from var(--tnz-neutral-800) r g b / var(--tnz-dim-50));
  z-index: var(--tnz-z-overlay);
}

/* Dialog */
.modal {
  position: fixed;
  background: var(--tnz-neutral-50);
  border-radius: var(--tnz-radius);
  box-shadow: var(--tnz-shadow-l);
  z-index: var(--tnz-z-modal);
  display: flex;
  flex-direction: column;
  gap: var(--tnz-space-4);
  padding: var(--tnz-space-6);
  max-height: 80vh;
}

/* Sidepanel variant */
.modal--sidepanel {
  top: 0;
  right: 0;
  bottom: 0;
  border-radius: 0;
  z-index: var(--tnz-z-sidepanel);
}

/* Entry animation */
.modal {
  transition:
    opacity var(--tnz-duration-slow) var(--tnz-ease-decelerate),
    transform var(--tnz-duration-slow) var(--tnz-ease-decelerate);
}

.modal__title {
  font-size: var(--tnz-text-lg);
  line-height: var(--tnz-leading-lg);
  font-weight: var(--tnz-font-semibold);
  color: var(--tnz-neutral-800);
}

.modal__body {
  overflow-y: auto;
  font-size: var(--tnz-text-sm);
  line-height: var(--tnz-leading-sm);
  color: var(--tnz-neutral-600);
}

.modal__footer {
  display: flex;
  justify-content: flex-end;
  gap: var(--tnz-space-2);
}
```

## Usage Guidelines

1. **When to use which variant**:
   - Dialog: confirmations, short forms, focused decisions
   - Sidepanel: inspect/edit flows that benefit from page context staying
     visible

2. **Footer actions**:
   - Right-align buttons; primary action last
   - Destructive confirmations use the delete button variants from
     [buttons.md](buttons.md)

3. **Accessibility**:
   - Set `role="dialog"` and `aria-modal="true"`; label with the title
   - Trap focus inside while open; return focus to the trigger on close
   - Close on Escape and (for non-destructive flows) backdrop click
   - Respect `prefers-reduced-motion` by disabling the slide/fade
