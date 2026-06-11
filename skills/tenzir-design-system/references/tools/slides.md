# Slides

Brand-styled decks (Quarto reveal.js, Google Slides, Canva, PowerPoint).
Values derive from [data/](../../data/); the YAML wins.

- Default slides: `neutral-50` background, `neutral-800` text. Secondary
  text and captions: `neutral-500`.
- Section/title slides may invert to `neutral-800` with `neutral-50` text
  and the light logo variant. Dark panels stay near-background with
  hairline borders; hero/CTA slides get the ambient glow
  ([colors.md](../colors.md#ambient-brand-glow)).
- Kicker pattern: sentence-case gradient-text kicker (`text-lg`, medium) →
  large semibold heading → `neutral-500` subtitle.
- Gradient: display text only (titles, kickers, stat figures).
- Content cards: flat `neutral-50`, 1px `neutral-200` border, optionally
  led by an icon tile ([iconography.md](../iconography.md)).
- Charts: `graph-1..6` in order; axis lines `neutral-300`, labels
  `neutral-500`.

Type scale for 16:9 decks: deck title `text-5xl`, section header
`text-4xl`, slide title `text-3xl` (all semibold, with their built-in
negative tracking); body/bullets `text-lg`–`text-xl`; code `text-base`
mono; captions `text-sm`.

Logos: light backgrounds → `logo-dark.svg`/`logomark-dark.svg`; dark →
the `-light` variants. Logomark alone once the full logo has appeared.
Never recolor, stretch, or add effects.

Quarto reveal.js picks all of this up from the brand file:

```yaml
format: revealjs
brand: path/to/tenzir-design-system/data/brand.yml
```
