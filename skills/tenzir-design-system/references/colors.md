# Colors

Values live in [data/brand.yml](../data/brand.yml) (palette, semantic
roles) and [data/tokens.yml](../data/tokens.yml) (tints, overlays, dark
mode); this file explains how to choose.

## Neutral-First

Shades of grey carry the layout; color appears only where it encodes
meaning: a primary action, a status, a data series. Blue and green are the
brand pair.

Text follows one hierarchy, symmetric across modes: emphasis takes the
mode's strongest neutral, body text pulls one step in on both ends, and the
muted tiers step down from there.

| Text role                                     | Light         | Dark          |
| --------------------------------------------- | ------------- | ------------- |
| Emphasis: headings, active text, icons        | `neutral-800` | `neutral-50`  |
| Body: paragraphs, prose, default text         | `neutral-700` | `neutral-300` |
| Secondary: supporting text, inactive nav      | `neutral-600` | `neutral-400` |
| Tertiary: placeholders, captions              | `neutral-500` | `neutral-400` |

The remaining neutrals carry the light-mode layout:

- `neutral-400`/`neutral-300`: disabled states, subtle icons
- `neutral-250`/`neutral-200`: borders, dividers, control outlines
- `neutral-100` (wells): filled inputs, hover fills, nav strips
- `neutral-50` (white): page, surfaces, text on filled controls

Surfaces are flat: page, regions, and cards all sit on `neutral-50`,
separated by 1px `neutral-200` borders; `neutral-100` marks recessed wells,
never the page. Shadows are reserved for floating surfaces
([elevation.md](elevation.md)).

## Roles

| Role      | Icon/text       | Subtle background |
| --------- | --------------- | ----------------- |
| `primary` | `blue-500`      | `blue-200`        |
| `success` | `green-600`     | `green-200`       |
| `info`    | `lightblue-600` | `lightblue-200`   |
| `warning` | `yellow-600`    | `yellow-200`      |
| `danger`  | `red-500`       | `red-200`         |

The pattern generalizes: **600 for icons and small text, 500 for fills,
200 for tinted backgrounds, 100 for the faintest wash.** Status and trend
chips apply it directly: 100/200-level tint background, 600-level text of
the same hue.

**Two status forms.** The table above is the **600-level accent** for icons
and small text. Filled status chips (badges, callouts) instead use a softer
**300-level soft fill** with `neutral-800` text. Both are valid; pick by
context: accent for marks, soft fill for chips. `danger`/`error` stays at 500
(light) / 400 (dark) rather than softening.

## Contrast

- The minimum text grey is `neutral-500` on light and `neutral-400` on dark
  (`neutral-500` fails small-text contrast on `neutral-800`), which is why
  the dark secondary and tertiary tiers share `neutral-400`.
- 500-level hues on light backgrounds pass only for large text/icons; use
  600-level for small text.
- On color-500 fills, use `neutral-50` text.
- On `neutral-800`, lead-ins are semibold `neutral-50`.
- Never encode meaning by color alone.

## Brand Gradient

A left-to-right `blue-500` → `green-500` linear gradient, used two ways: as a
**border** to accentuate an element beyond what the primary color can carry,
and as **display text** (hero headlines, section kickers, stat figures). It
reads the same on light and dark (the ramp never changes). Never body text,
controls, or fills. Size gradient text to its content so each element runs the
full ramp; a short label on a container-wide gradient samples only blue. See
[branded-effects.md](branded-effects.md).

## Tints and Overlays

- Any palette color at 12% alpha (`tint-12`) makes an outline-style fill
  (outline tags, badges, shortcut hints).
- Dims darken with `neutral-800` (`dim-50` page backdrop, `dim-20`
  pressed fills, `dim-8` subtle); lightens brighten with `neutral-50`.

## Graph Colors

Multi-series charts use `graph-1`…`graph-6` in order: blue, lightblue,
purple, pink, orange, yellow (500-level). Single series: `blue-500`.
Paired series (ingress/egress) use one hue at two shades (`blue-500` +
`blue-300`) instead of two hues. 300-level for hover/area fills.

## Diagrams

Diagram nodes stay neutral-first: `neutral-50`/`neutral-100` fills,
`neutral-300` borders, `neutral-800` text; lines and arrows `neutral-400`.
Emphasis nodes take a `blue-500` border or `blue-200` fill. Color multiple
categories with the graph order above. Labels use Inter; code-like node
content uses JetBrains Mono.

## Dark Mode

Light and dark are both first-class, strict modes; keep background noise
minimal, with no large washes or glows behind content. Dark mode remaps roles
onto the same palette (`tenzir.dark` in tokens.yml): background and surfaces
`neutral-800`, wells and borders `neutral-700`, and text per the hierarchy in
[Neutral-First](#neutral-first). Status hues move one step lighter
(400-level). Surfaces stay flat; lifting them to `neutral-700` reads as heavy
navy slabs.
