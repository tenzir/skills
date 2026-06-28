---
name: tenzir-design-system
description: >-
  Tenzir design system: brand tokens (colors, typography, spacing, shadows,
  motion), design principles and invariants, and official logos. Use when
  styling anything Tenzir-branded: web UIs (shadcn/ui, Tailwind, plain CSS, or
  any frontend framework), Quarto documents and reports, slide decks, or
  diagrams (Mermaid, Graphviz). Also use when the user asks about Tenzir brand
  colors, fonts, logos, gradients, dark mode, or how to make output look like a
  Tenzir product.
---

# Tenzir Design System

Canonical home of the Tenzir design system: machine-readable tokens, design
principles, and brand assets. The skill defines **values** and **design
decisions**; how those get realized in any given tool is out of scope.

**The YAML data files are authoritative for all values; the markdown captures
the design decisions:** how to choose and apply tokens. When a snippet and the
YAML disagree, the YAML wins.

## Data Files

- [data/brand.yml](data/brand.yml): color palette, semantic roles
  (primary/success/warning/…), graph colors, typography, and logos. Follows
  Quarto's [brand.yml](https://posit-dev.github.io/brand-yml/) schema, so
  Quarto/Shiny can consume it directly.
- [data/tokens.yml](data/tokens.yml): everything beyond that schema, under the
  `tenzir:` key: spacing, radius, type scale, shadows, opacity and tints,
  motion, z-index, breakpoints, and the dark-mode mapping.
- [source.md](source.md): scope and non-goals.

## Question Routing

| Question | Load |
| --- | --- |
| What's the hex/value of a token? | [data/brand.yml](data/brand.yml), [data/tokens.yml](data/tokens.yml) |
| Which color/font/size should I use? | [references/colors.md](references/colors.md), [references/typography.md](references/typography.md) |
| Spacing, radius, breakpoints, z-index? | [references/layout.md](references/layout.md) |
| Shadows, overlays, surface stacking? | [references/elevation.md](references/elevation.md) |
| Animation durations and easing? | [references/motion.md](references/motion.md) |
| Which icon set/style? | [references/iconography.md](references/iconography.md) |
| Branded effect (gradient border, gradient text, kicker, prose)? | [references/branded-effects.md](references/branded-effects.md) |
| The non-negotiable design rules? | [references/invariants.md](references/invariants.md) |
| Scope and non-goals? | [source.md](source.md) |

Load only the files the current task needs. Prefer design tokens and existing
component patterns over bespoke styling.

## Components

There are no Tenzir component specs. The system contributes the invariants
(tokens, flat surfaces, elevation, gradients, iconography), not component
anatomy. Build components with your project's library and honor the
[invariants](references/invariants.md).

## Conventions

- The skill is tool-agnostic: it owns the **values** ([data/](data/)) and the
  **design decisions** (the `references/` principle docs and the
  [invariants](references/invariants.md)). How those get realized in a given
  tool is out of scope.
- Light and dark are both strict, first-class modes that share one palette and
  remap semantic roles; keep background noise minimal.

## Assets

Official logos live in `assets/logos/`. Variant names describe the artwork
color; **dark artwork goes on light backgrounds**:

- `logo-dark.svg`, `logomark-dark.svg`: for light backgrounds
- `logo-light.svg`, `logomark-light.svg`: for dark backgrounds

The logomark is the icon-only mark; use it where the full logo has already
appeared or space is tight.
