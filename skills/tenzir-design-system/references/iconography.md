# Iconography

Tenzir uses **Material Symbols Rounded** at **light weight (200)**, outlined
(no fill) — soft, rounded strokes that match Inter's geometry. This is the
icon family across product and website; don't mix in other icon sets.

## Configuration

Material Symbols is a variable font ([Google
Fonts](https://fonts.google.com/icons), npm package `material-symbols`).
The Tenzir axis settings:

```css
.tnz-icon {
  font-variation-settings: "FILL" 0, "wght" 200, "GRAD" 0, "opsz" 48;
}
```

The **optical size axis is the key to the look**: strokes thin as `opsz`
grows. Pinning `opsz` at 48 — deliberately higher than the render size —
is what produces the soft hairline strokes; at `opsz` 24 the same weight
renders visibly chunkier. If 200/48 gets too faint below ~16px, step up
to weight 300 rather than lowering the optical size.

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
