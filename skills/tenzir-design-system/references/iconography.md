# Iconography

**Material Symbols Rounded, light (200), outlined** — soft rounded strokes
matching Inter. One family everywhere; don't mix icon sets.

```css
.tnz-icon {
  font-variation-settings: "FILL" 0, "wght" 200, "GRAD" 0, "opsz" 48;
}
```

The high optical size (`opsz` 48, pinned regardless of render size) is what
produces the thin strokes; at `opsz` 24 the same weight renders visibly
chunkier. If too faint below ~16px, step up to weight 300 — never lower
the optical size.

Sizes: 16px inline/dense, 20px default UI, 22–24px feature tiles. Icons
inherit their context's text color; status icons use the 600-level hue;
icon tiles are `blue-500` on `blue-100` (see
[components/card.md](components/card.md)).

Source: [Google Fonts](https://fonts.google.com/icons) (npm
`material-symbols`); export SVGs at weight 200/Rounded for non-web use.
The logo is a brand asset ([assets/logos/](../assets/logos/)), never an
icon substitute.
