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
- `neutral-100` — wells and fills: filled inputs, hover fills, nav strips,
  heatmap cells
- `neutral-50` — white: the page background, surfaces, text on filled
  controls

Surfaces are flat: the page is `neutral-50`, and content regions and cards
sit on the same `neutral-50`, separated by 1px `neutral-200` borders or
hairline dividers rather than background shifts. `neutral-100` marks
recessed wells inside a surface, not the page itself. Shadows are reserved
for floating surfaces (menus, modals, toasts).

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

Status count chips and stat-trend chips follow it directly: a 100–200-level
tint background with 600-level text of the same hue (e.g. a running count
on `blue-100` in `blue-600`, a trend delta on `blue-100` in `blue-600`).

### Brand Gradient

The blue→green gradient is the signature display accent, on light and dark
backgrounds alike:

```css
background: linear-gradient(to right, var(--tnz-blue-500), var(--tnz-green-500));
```

Use it for hero headlines, section kickers/overlines, and highlighted stat
figures — applied as a text gradient. Never use it for body text, UI
controls, or large fills.

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

For **paired series** — two facets of the same measure, like
ingress/egress or read/write — use one hue at two shades (`blue-500` +
`blue-300`) instead of two hues. Reserve the multi-hue sequence for
genuinely independent series.

## Dark Mode

Dark sections in production sit on exactly `neutral-800`, and the flat
surface model carries over: cards and panels share the `neutral-800`
background, separated by `neutral-700` hairline borders, with no shadows.
`neutral-700` is also the well and hover layer — the dark counterpart of
`neutral-100`. Avoid lifting whole surfaces to `neutral-700`: its blue
cast reads as heavy navy slabs against the near-black page.

### Ambient Brand Glow

What makes production dark surfaces feel alive is not lighter panels but
**ambient glow**: large, soft radial gradients of the brand colors bleeding
in from the edges of the section, fading into `neutral-800`. Blue (toward
lightblue at the hot core) anchors one side, green the other:

```css
.dark-hero {
  background:
    radial-gradient(50% 70% at 0% 100%,
      rgb(from var(--tnz-blue-500) r g b / 35%), transparent 70%),
    radial-gradient(50% 70% at 100% 100%,
      rgb(from var(--tnz-green-500) r g b / 30%), transparent 70%),
    var(--tnz-neutral-800);
}
```

A quieter variant for section tops is a single deep navy wash —
`blue-500` at ~20% fading downward into the background. Use glows for
hero and CTA moments, not behind dense UI or data displays.

Dark mode remaps semantic roles onto the same palette instead of
introducing new colors: background
and surfaces `neutral-800`, wells and borders `neutral-700`, text
`neutral-50`, and status hues one step lighter (400-level) to keep
contrast. The mapping lives in `tenzir.dark` in
[data/tokens.yml](../data/tokens.yml); see [tools/css.md](tools/css.md)
for the implementation pattern.
