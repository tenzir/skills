---
title: Multi-tool design system skill with machine-readable tokens
type: change
authors:
  - mavam
  - claude
prs:
  - 22
created: 2026-06-10T16:47:40.292337Z
---

The `tenzir-design-system` skill is now the canonical home of the Tenzir design system and supports many consumers beyond Platform CSS: plain CSS, Tailwind, Quarto documents, slide decks, and Mermaid/Graphviz diagrams.

Token values now live in machine-readable YAML: `data/brand.yml` follows Quarto's brand.yml schema and can be consumed directly via `brand: data/brand.yml`, while `data/tokens.yml` carries the extended tokens (spacing, radius, type scale, shadows, motion, z-index, breakpoints, and a dark-mode mapping). Markdown references explain how to choose tokens; per-tool guides under `references/tools/` provide ready-to-use CSS custom properties, Tailwind v4/v3 configuration, and diagram/slide styling. New component specs cover tooltip, modal, card, and menu, and `source.md` documents which tokens are Figma-sourced versus proposed defaults.
