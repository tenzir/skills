# Card

Contained surface that groups related content on the app background.

## Props

| Prop          | Values                     |
| ------------- | -------------------------- |
| `interactive` | `true`, `false`            |
| `padding`     | `compact`, `default`       |

## Specifications

| Property        | Value                                       |
| --------------- | ------------------------------------------- |
| Background      | `neutral-50`, same as the page — the border does the separation |
| Border          | 1px `neutral-200`                           |
| Border radius   | `radius` (5px)                              |
| Shadow          | none (flat); `shadow-xs` → `shadow-s` on hover if interactive |
| Padding default | `space-4` (16px)                            |
| Padding compact | `space-3` (12px)                            |
| Content gap     | `space-2` (8px)                             |

## CSS Implementation

```css
.card {
  background: var(--tnz-neutral-50);
  border: 1px solid var(--tnz-neutral-200);
  border-radius: var(--tnz-radius);
  padding: var(--tnz-space-4);
}

.card--compact {
  padding: var(--tnz-space-3);
}

/* Interactive card */
.card--interactive {
  cursor: pointer;
  transition: box-shadow var(--tnz-duration-fast) var(--tnz-ease-standard);
}

.card--interactive {
  box-shadow: var(--tnz-shadow-xs);
}

.card--interactive:hover {
  box-shadow: var(--tnz-shadow-s);
}

.card--interactive:focus-visible {
  outline: none;
  box-shadow:
    0 0 0 2px var(--tnz-primary-200),
    var(--tnz-shadow-xs);
}

/* Card header */
.card__title {
  font-size: var(--tnz-text-base);
  line-height: var(--tnz-leading-base);
  font-weight: var(--tnz-font-semibold);
  color: var(--tnz-neutral-800);
}

.card__description {
  font-size: var(--tnz-text-sm);
  line-height: var(--tnz-leading-sm);
  color: var(--tnz-neutral-600);
}

/* Icon tile: feature/use-case cards lead with a tinted, hairline-bordered
   icon square. The glyph is a Material Symbols Rounded icon at light
   weight — see ../iconography.md. */
.card__icon-tile {
  display: grid;
  place-items: center;
  width: 44px;
  height: 44px;
  background: var(--tnz-blue-100);
  border: 1px solid var(--tnz-blue-200);
  color: var(--tnz-blue-500);
  border-radius: var(--tnz-radius);
}
```

## Usage Guidelines

1. **Surfaces**:
   - Cards share the `neutral-50` page background; the 1px `neutral-200`
     border alone separates them — do not nest cards
   - For sections inside a card, separate with 1px `neutral-200` dividers
   - Use `neutral-100` for recessed wells inside a card, not for the card
     itself

2. **Elevation**:
   - Static cards are flat; only interactive cards carry `shadow-xs` and
     elevate to `shadow-s` on hover

3. **Accessibility**:
   - An interactive card is a single link or button semantically; avoid
     multiple competing click targets inside it
