# Card

Contained surface grouping related content.

## Specifications

| Property      | Value                                            |
| ------------- | ------------------------------------------------ |
| Background    | `neutral-50`, same as the page — the border separates |
| Border        | 1px `neutral-200`                                |
| Border radius | `radius` (5px)                                   |
| Shadow        | none; interactive cards: `shadow-xs`, `shadow-s` on hover |
| Padding       | `space-4` (16px); compact: `space-3` (12px)      |

Title: `text-base` semibold `neutral-800`; description: `text-sm`
`neutral-600`. Use `neutral-100` for recessed wells inside a card, 1px
`neutral-200` dividers between sections. Don't nest cards. An interactive
card is one link or button semantically.

## Icon Tile

Feature/use-case cards lead with a tinted icon square — a Material
Symbols Rounded glyph ([iconography.md](../iconography.md)):

```css
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
