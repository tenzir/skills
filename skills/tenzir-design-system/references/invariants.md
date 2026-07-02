# Invariants

The non-negotiable rules of the system. Hold these wherever the design is
realized.

- **Only Tenzir hues exist.** Replace, don't extend, any default palette so
  stray colors can't leak in.
- **Surfaces are flat.** Separate by 1px border, backdrop dim, or color, not by
  shadow.
- **Shadows are rare.** The system carries no shadows by default; the one
  sanctioned use is a light-mode surface floating over same-colored content
  (menus, popovers, toasts), never a resting or hover style on controls,
  cards, or static surfaces ([elevation.md](elevation.md)). When a shadow is
  used, it is two layers ([data/tokens.yml](../data/tokens.yml)); dark mode
  uses none at all.
- **Strict light and dark.** Both modes are first-class and clean; keep
  background noise minimal, with no large washes or glows behind content.
- **Gradient is an accent, not a fill.** The blue→green ramp appears as a
  border (to emphasize beyond the primary color) or as display text, never on
  body copy, controls, or fills ([branded-effects.md](branded-effects.md)).
- **Status has two roles.** A 600-level accent for icons and small text, and a
  300-level soft fill (with `neutral-800` text) for badges and callouts
  ([colors.md](colors.md)).
- **Reference tokens, not raw values.** Wire each token once; don't scatter hex
  codes or pixel values.
