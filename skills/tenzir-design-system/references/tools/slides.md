# Slides

Brand-styled slide decks (Quarto reveal.js, Google Slides, Canva,
PowerPoint). Values derive from [data/brand.yml](../../data/brand.yml) and
[data/tokens.yml](../../data/tokens.yml); if anything here disagrees with
the YAML, the YAML wins.

## Layout and Color

- Default slides: `neutral-50` (#FDFDFE) background, `neutral-800`
  (#0E1017) text.
- Section dividers / title slides may invert: `neutral-800` background,
  `neutral-50` text — use the light logo variant there. Panels on dark
  slides stay near-background (barely lighter than `neutral-800`) with
  `lighten-8` hairline borders and no shadows. Give dark hero/CTA slides
  the ambient brand glow — soft blue and green radial washes from the
  edges (see the recipe in [colors.md](../colors.md#ambient-brand-glow)).
- Accents: `blue-500` for emphasis, links, and highlights. The blue→green
  brand gradient is the display accent: hero/title text, section
  kickers, and highlighted stat figures — never body content.
- Content slides follow the kicker pattern: a sentence-case gradient-text
  kicker at `text-lg`/medium (the production style), a large semibold
  heading, and a `neutral-500` subtitle. The uppercase `text-capitalized`
  overline is the quieter variant for dense or document-like contexts.
- Secondary text (speaker names, footers, captions): `neutral-500`.
- Content cards on light slides are flat: `neutral-50` with a 1px
  `neutral-200` border, optionally led by an icon tile (`blue-100`
  square, 1px `blue-200` border, `blue-500` Material Symbols Rounded
  glyph — see [iconography.md](../iconography.md)).

## Typography

Inter for all text, JetBrains Mono for code. Mapping the type scale to a
16:9 deck (scale up proportionally for larger canvases):

| Element        | Token       | Weight   |
| -------------- | ----------- | -------- |
| Deck title     | `text-5xl`  | semibold |
| Slide title    | `text-3xl`  | semibold |
| Section header | `text-4xl`  | semibold |
| Body           | `text-lg`/`text-xl` | regular |
| Bullets        | `text-lg`   | regular  |
| Code           | `text-base` mono | regular |
| Captions/footer| `text-sm`   | regular, `neutral-500` |
| Kicker/overline| `text-capitalized`, uppercase | medium |

Apply the negative tracking baked into `text-2xl`+ for titles.

## Logos

From [assets/logos/](../../assets/logos/) — variant names describe the
artwork color:

- Light backgrounds → `logo-dark.svg` / `logomark-dark.svg`
- Dark backgrounds → `logo-light.svg` / `logomark-light.svg`
- Use the logomark alone (e.g., slide footers) once the full logo has
  appeared on the title slide; never recolor, stretch, or add effects.

## Charts

Use the graph order `blue-500`, `lightblue-500`, `purple-500`, `pink-500`,
`orange-500`, `yellow-500` (#0A54FF, #0AADFF, #CF0AFF, #FF0AA5, #FF5C0A,
#EDAE1D). Single-series charts: `blue-500` only. Axis lines and gridlines:
`neutral-300`; axis labels: `neutral-500`.

## Quarto reveal.js

Point the deck at the brand file and Quarto handles colors, fonts, and the
title-slide logo:

```yaml
format: revealjs
brand: path/to/tenzir-design-system/data/brand.yml
```

See [quarto.md](quarto.md) for details.
