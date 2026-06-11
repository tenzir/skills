# Colors

How to choose Tenzir colors. All values live in
[data/brand.yml](../data/brand.yml) (palette and semantic roles) and
[data/tokens.yml](../data/tokens.yml) (alpha tints, overlays, dark mode);
this file explains how to pick among them.

## Design Philosophy

Tenzir UIs are neutral-first: shades of grey carry the layout, and brighter
colors appear sparingly for emphasis, status, and data. Blue and green are
the brand pair — they convey trustworthiness, freshness, safety, and balance
for the security domain.

When in doubt: build the screen entirely from neutrals, then add color only
where it encodes meaning (a primary action, a status, a data series).

## Neutrals

The `neutral-50`…`neutral-800` ramp is the workhorse:

- `neutral-800` — black, default text, icons
- `neutral-700` / `neutral-600` — secondary text, inactive navigation
- `neutral-500` — tertiary text, placeholders; the **lightest grey allowed
  for text** on light backgrounds
- `neutral-400` / `neutral-300` — disabled states, subtle icons
- `neutral-250` / `neutral-200` — borders, dividers, control outlines
- `neutral-100` — app background, hover fills, input fills
- `neutral-50` — white, elevated surfaces, text on filled controls

Surfaces stack as: `neutral-100` page → `neutral-50` surface → 1px
`neutral-200` borders between them.

## Brand and Semantic Roles

Use semantic role names rather than raw hues where possible (roles are
defined in brand.yml):

| Role        | Token (icon/text)  | Subtle background |
| ----------- | ------------------ | ----------------- |
| `primary`   | `blue-500`         | `blue-200`        |
| `success`   | `green-600`        | `green-200`       |
| `info`      | `lightblue-600`    | `lightblue-200`   |
| `warning`   | `yellow-600`       | `yellow-200`      |
| `danger`    | `red-500`          | `red-200`         |

The pattern generalizes: **600 for icons and small text, 500 for fills and
large elements, 200 for tinted backgrounds, 100 for the faintest wash.**

### Brand Gradient

Reserve the blue→green gradient for brand moments (hero elements, accents),
not for everyday UI:

```css
background: linear-gradient(to right, var(--tnz-blue-500), var(--tnz-green-500));
```

## Contrast

- On white/light backgrounds, 500-level hues only pass WCAG AA for large
  text and icons; use the **600 level for small text** (links, labels).
- `neutral-500` is the minimum text grey on `neutral-50`/`neutral-100`;
  anything lighter is decorative only.
- On color-500 fills (e.g., primary buttons), use `neutral-50` text.
- Never encode meaning by color alone — pair status colors with icons or
  text.

## Alpha Tints and Overlays

- Any palette color at 12% alpha (`tint-12`) makes an outline-style fill —
  used for outline tags, badges, and shortcut hints where a solid tint
  would be too heavy.
- Dim overlays darken with `neutral-800` at `dim-50` (full-page behind
  modals), `dim-20` (pressed fills), or `dim-8` (subtle darkening).
- Lighten overlays brighten with `neutral-50` at `lighten-20`/`lighten-8`,
  e.g. for shortcut hints on filled buttons.

## Graph Colors

For multi-series charts, use the `graph-1`…`graph-6` sequence in order:
blue, lightblue, purple, pink, orange, yellow (all 500-level). Single-series
charts use `blue-500` alone. Use the 300-level of the same hue for hover or
area fills.

## Dark Mode

Dark mode remaps semantic roles onto the same palette instead of
introducing new colors: background
`neutral-800`, surfaces `neutral-700`, text `neutral-50`, and status hues
one step lighter (400-level) to keep contrast. The mapping lives in
`tenzir.dark` in [data/tokens.yml](../data/tokens.yml); see
[tools/css.md](tools/css.md) for the implementation pattern.
