---
name: tenzir-design-system
description: >-
  Tenzir design system: brand tokens (colors, typography, spacing, shadows,
  motion), component specifications, official logos, and per-tool integration
  guides. Use when styling anything Tenzir-branded: web UIs (plain CSS, CSS
  variables, Tailwind, or any frontend framework), Quarto documents and
  reports, slide decks, or diagrams (Mermaid, Graphviz). Also use when the
  user asks about Tenzir brand colors, fonts, logos, dark mode, or how to
  make output look like a Tenzir product.
---

# Tenzir Design System

Canonical home of the Tenzir design system: machine-readable tokens,
component specifications, brand assets, and integration guides for the tools
that consume them.

**The YAML data files are authoritative for all values.** Markdown
references explain how to choose and apply tokens; when a markdown snippet
and the YAML disagree, the YAML wins.

## Data Files

- [data/brand.yml](data/brand.yml) — color palette, semantic roles
  (primary/success/warning/…), graph colors, typography, and logos.
  Follows Quarto's [brand.yml](https://posit-dev.github.io/brand-yml/)
  schema, so Quarto/Shiny can consume it directly.
- [data/tokens.yml](data/tokens.yml) — everything beyond that schema, under
  the `tenzir:` key: spacing, radius, type scale, shadows, opacity and
  tints, motion, z-index, breakpoints, and the dark-mode mapping.
- [source.md](source.md) — how this skill relates to downstream consumers
  and what is out of scope.

## Question Routing

| Question | Load |
| --- | --- |
| What's the hex/value of a token? | [data/brand.yml](data/brand.yml), [data/tokens.yml](data/tokens.yml) |
| Which color/font/size should I use? | [references/colors.md](references/colors.md), [references/typography.md](references/typography.md) |
| Spacing, radius, breakpoints, z-index? | [references/layout.md](references/layout.md) |
| Shadows, overlays, surface stacking? | [references/elevation.md](references/elevation.md) |
| Animation durations and easing? | [references/motion.md](references/motion.md) |
| Implement a button, input, modal, …? | [references/components/](references/components/) — one file per component |
| Write the CSS variables / theme plain CSS? | [references/tools/css.md](references/tools/css.md) |
| Configure Tailwind? | [references/tools/tailwind.md](references/tools/tailwind.md) |
| Brand a Quarto doc or report? | [references/tools/quarto.md](references/tools/quarto.md) |
| Style a Mermaid/Graphviz diagram? | [references/tools/diagrams.md](references/tools/diagrams.md) |
| Build a branded slide deck? | [references/tools/slides.md](references/tools/slides.md) |
| How does this relate to other repos? | [source.md](source.md) |

Load only the files the current task needs. Prefer design tokens and
existing component patterns over bespoke styling.

## Components

Specs in [references/components/](references/components/): buttons,
input-field, search-input, dropdown, checkbox, radio-button, toggle-switch,
segmented-control, tag, badge, tab-bar, toast, hyperlinks, tooltip, modal,
card, menu. Each covers sizes, states, and a CSS implementation using
`--tnz-` custom properties.

## Conventions

- CSS custom properties use the `--tnz-` prefix
  ([references/tools/css.md](references/tools/css.md) has the full block).
- Dark mode remaps semantic roles only; the palette is shared between light
  and dark.

## Assets

Official logos live in `assets/logos/`. Variant names describe the artwork
color — **dark artwork goes on light backgrounds**:

- `logo-dark.svg`, `logomark-dark.svg` — for light backgrounds
- `logo-light.svg`, `logomark-light.svg` — for dark backgrounds

The logomark is the icon-only mark; use it where the full logo has already
appeared or space is tight.
