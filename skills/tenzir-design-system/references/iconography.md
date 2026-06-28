# Iconography

**Material Symbols Rounded, light (200), outlined**: soft rounded strokes
matching Inter. One family everywhere; don't mix icon sets.

```css
.tnz-icon {
  font-variation-settings: "FILL" 0, "wght" 200, "GRAD" 0, "opsz" 48;
}
```

The high optical size (`opsz` 48, pinned regardless of render size) is what
produces the thin strokes; at `opsz` 24 the same weight renders visibly
chunkier. If too faint below ~16px, step up to weight 300, never lower
the optical size.

Sizes: 16px inline/dense, 20px default UI, 22–24px feature tiles. Icons
inherit their context's text color; status icons use the 600-level hue.

Feature/use-case cards lead with an **icon tile**: a 44px square at the
default radius with a centered glyph, tinted per hue rather than filled
solid: the hue at 10% fill, a 20% border of the same hue, and a 600-level
glyph. In dark mode, lift the border to 40% and the glyph to the 400 level.
Blue is the default; vary the hue to distinguish items across a grid.

Source: [Google Fonts](https://fonts.google.com/icons) (npm
`material-symbols`); export SVGs at weight 200/Rounded for non-web use.
The logo is a brand asset ([assets/logos/](../assets/logos/)), never an
icon substitute.
