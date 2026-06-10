# Card

> **Derived spec** — proposed for consistency with the design system; not
> Figma-sourced. See [source.md](../../source.md).

Contained surface that groups related content on the app background.

## Props

| Prop          | Values                     |
| ------------- | -------------------------- |
| `interactive` | `true`, `false`            |
| `padding`     | `compact`, `default`       |

## Specifications

| Property        | Value                                       |
| --------------- | ------------------------------------------- |
| Background      | `neutral-50` on a `neutral-100` page        |
| Border          | 1px `neutral-200`                           |
| Border radius   | `radius` (5px)                              |
| Shadow          | `shadow-xs`; `shadow-s` on hover if interactive |
| Padding default | `space-4` (16px)                            |
| Padding compact | `space-3` (12px)                            |
| Content gap     | `space-2` (8px)                             |

## CSS Implementation

```css
.card {
  background: var(--tnz-neutral-50);
  border: 1px solid var(--tnz-neutral-200);
  border-radius: var(--tnz-radius);
  box-shadow: var(--tnz-shadow-xs);
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
```

## Usage Guidelines

1. **Surfaces**:
   - Cards sit on the `neutral-100` app background; do not nest cards
   - For sections inside a card, separate with 1px `neutral-200` dividers

2. **Elevation**:
   - Static cards stay at `shadow-xs`; only interactive cards elevate on
     hover

3. **Accessibility**:
   - An interactive card is a single link or button semantically; avoid
     multiple competing click targets inside it
