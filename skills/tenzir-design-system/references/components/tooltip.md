# Tooltip

Small inverted-color popup that labels or explains the element under the
pointer or keyboard focus.

## Props

| Prop        | Values                           |
| ----------- | -------------------------------- |
| `placement` | `top`, `bottom`, `left`, `right` |

## Specifications

| Property      | Value                            |
| ------------- | -------------------------------- |
| Background    | `neutral-800`                    |
| Text          | `neutral-50`, `text-xs`, regular |
| Padding       | `space-1` / `space-2` (4px 8px)  |
| Border radius | `radius` (5px)                   |
| Shadow        | `shadow-s`                       |
| Max width     | 280px                            |
| Offset        | `space-1` (4px) from the anchor  |
| Layer         | `z-tooltip`                      |

## CSS Implementation

```css
.tooltip {
  background: var(--tnz-neutral-800);
  color: var(--tnz-neutral-50);
  font-size: var(--tnz-text-xs);
  line-height: var(--tnz-leading-xs);
  padding: var(--tnz-space-1) var(--tnz-space-2);
  border-radius: var(--tnz-radius);
  box-shadow: var(--tnz-shadow-s);
  max-width: 280px;
  z-index: var(--tnz-z-tooltip);
}

/* Entry animation */
.tooltip {
  opacity: 0;
  transition: opacity var(--tnz-duration-fast) var(--tnz-ease-decelerate);
}

.tooltip--visible {
  opacity: 1;
}
```

## Usage Guidelines

1. **Content**:
   - One short phrase or sentence; no interactive content
   - For rich or interactive content, use a popover-style menu instead

2. **Timing**:
   - Show after a short hover delay (~500ms); hide immediately on leave
   - Show without delay on keyboard focus

3. **Accessibility**:
   - Connect to the anchor with `aria-describedby`
   - Never put information only in a tooltip that has no keyboard-focusable
     anchor
   - Respect `prefers-reduced-motion` by disabling the fade
