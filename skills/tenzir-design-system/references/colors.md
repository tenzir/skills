# Colors

Values live in [data/brand.yml](../data/brand.yml) (palette, semantic
roles) and [data/tokens.yml](../data/tokens.yml) (tints, overlays, dark
mode); this file explains how to choose.

## Neutral-First

Shades of grey carry the layout; color appears only where it encodes
meaning — a primary action, a status, a data series. Blue and green are
the brand pair.

- `neutral-800` — black: default text, icons
- `neutral-700`/`neutral-600` — secondary text, inactive navigation
- `neutral-500` — tertiary text, placeholders; the lightest text grey
- `neutral-400`/`neutral-300` — disabled states, subtle icons
- `neutral-250`/`neutral-200` — borders, dividers, control outlines
- `neutral-100` — wells: filled inputs, hover fills, nav strips
- `neutral-50` — white: page, surfaces, text on filled controls

Surfaces are flat: page, regions, and cards all sit on `neutral-50`,
separated by 1px `neutral-200` borders — `neutral-100` marks recessed
wells, never the page. Shadows are reserved for floating surfaces
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

## Contrast

- 500-level hues on light backgrounds pass only for large text/icons; use
  600-level for small text. `neutral-500` is the minimum text grey.
- On color-500 fills, use `neutral-50` text.
- On `neutral-800`, body text is `neutral-300` or lighter (`neutral-400`
  for captions only); lead-ins are semibold `neutral-50`.
- Never encode meaning by color alone.

## Brand Gradient

```css
background: linear-gradient(to right, var(--tnz-blue-500), var(--tnz-green-500));
```

The display accent — hero headlines, section kickers, stat figures — as
text, on light and dark alike (the ramp never changes). Never body text,
controls, or fills. Size gradient text to its content
(`width: fit-content`) so each element runs the full ramp; a short label
on a container-wide gradient samples only blue.

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

## Dark Mode

Dark mode remaps roles onto the same palette (`tenzir.dark` in
tokens.yml): background and surfaces `neutral-800`, wells and borders
`neutral-700`, text `neutral-50`, status hues one step lighter
(400-level). Surfaces stay flat — lifting them to `neutral-700` reads as
heavy navy slabs.

### Ambient Brand Glow

Dark hero/CTA sections come alive through glow, not lighter panels: large
soft radial gradients of brand blue and green bleeding in from the edges
of `neutral-800`.

```css
background:
  radial-gradient(45% 55% at 12% 75%,
    rgb(from var(--tnz-blue-500) r g b / 30%), transparent 70%),
  radial-gradient(45% 55% at 88% 75%,
    rgb(from var(--tnz-green-500) r g b / 25%), transparent 70%),
  var(--tnz-neutral-800);
```

Anchor the radial centers inside the section so the glow dissolves before
the edges (a clipped glow seams against dark pages); bleed off the edge
only when the section ends the page. These sections are pinned dark in
both themes — the glow, not a luminance flip, sets them apart. Keep glows
away from dense UI and data displays.
