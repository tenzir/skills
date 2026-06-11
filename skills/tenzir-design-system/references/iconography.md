# Iconography

Tenzir uses **Material Symbols Rounded** at **light weight (300)**, outlined
(no fill) — soft, rounded strokes that match Inter's geometry. This is the
icon family across product and website; don't mix in other icon sets.

## Configuration

Material Symbols is a variable font ([Google
Fonts](https://fonts.google.com/icons), npm package `material-symbols`).
The Tenzir axis settings:

```css
.tnz-icon {
  font-variation-settings: "FILL" 0, "wght" 300, "GRAD" 0, "opsz" 24;
}
```

```html
<span class="material-symbols-rounded tnz-icon">filter_alt</span>
```

For non-web contexts (slides, diagrams, documents), export the same glyphs
as SVG from Google Fonts with weight 300 and the Rounded style.

## Sizes

| Context                         | Size  |
| ------------------------------- | ----- |
| Inline with text, dense UI      | 16px  |
| Default UI (buttons, menus)     | 20px  |
| Feature/icon tiles              | 22–24px |

## Color

Icons inherit the text color of their context:

- Default UI icons: `neutral-800`; secondary: `neutral-500`
- Status icons: the 600-level hue of the status (success `green-600`, …)
- Icon tiles: `blue-500` glyph on a `blue-100` tile with a 1px `blue-200`
  border (see [components/card.md](components/card.md))

## Scope

The Tenzir logo and logomark are brand assets, not icons — use the files in
[assets/logos/](../assets/logos/), never an icon-font substitute.
