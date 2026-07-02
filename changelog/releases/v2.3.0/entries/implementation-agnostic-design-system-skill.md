---
title: Implementation-agnostic design system skill
type: change
authors:
  - mavam
  - claude
prs:
  - 24
created: 2026-06-28T14:08:43.330844Z
---

The `tenzir-design-system` skill now focuses on the design system itself: machine-readable tokens plus the principles and invariants that define the style.

The skill owns two things: machine-readable tokens (`data/brand.yml`, `data/tokens.yml`) and the design decisions that explain how to apply them (color usage, typography, elevation, motion, iconography, layout, branded effects, and a short set of non-negotiable invariants). The per-tool integration guides that wired tokens into specific frameworks (Tailwind, shadcn, plain CSS, Quarto, slides, diagrams) and the bundled shadcn theme are gone; how the system gets realized in any given tool is out of scope. The result is a simpler, smaller system: strict light and dark modes, flat surfaces with shadows avoided, and the brand gradient used as a border or display accent.
