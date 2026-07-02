# Elevation

Shadow values live in [data/tokens.yml](../data/tokens.yml)
(`tenzir.shadow`, `tenzir.opacity`).

## No Shadows by Default

The system is flat: shadows are not part of the resting visual language and
appear only in rare circumstances. Surfaces separate by **border, backdrop,
or color, not shadows**:

- Static surfaces (cards, panels, regions): flat, 1px `neutral-200`
  borders.
- Controls (buttons, inputs, form fields): flat, with no resting or hover
  shadow; hover and active states change color or border instead. Keep focus
  rings. Zero any control shadow a component library bakes in by default.
- Modals and sidepanels: the `dim-50` backdrop separates. No shadow.
- Tooltips: the inverted `neutral-800` surface separates. No shadow.

The one sanctioned exception is a **light-mode surface floating over
same-colored content**, where neither a border nor a backdrop can separate:
menus, popovers, and listboxes use `shadow-m`; toasts use `shadow-s`. Every
shadow is **two layers** of `neutral-800` (see tokens.yml); both layers
required. Component libraries often ship broader shadow defaults; keep only
the menu, popover, and toast shadows and zero the rest.

In dark mode, skip shadows entirely: a `neutral-800` shadow has nothing to
darken on the near-black `neutral-800` background, and the common
workarounds are off the table — lightening surfaces to fake elevation
violates the flat-surface invariant, and a light "shadow" reads as glow,
signaling emission rather than depth. Floating surfaces stay `neutral-800`
and separate with `neutral-700` hairline borders instead.

The principle behind the asymmetry: **each mode uses the cheapest
sufficient separator.** Borders are always the first choice; light mode
falls back to a shadow only where a border cannot separate white from
white, while on dark the `neutral-700` hairline covers every case.

## Overlay Dims

| Token        | Use                                          |
| ------------ | -------------------------------------------- |
| `dim-50`     | Full-page backdrop behind modals/sidepanels  |
| `dim-20`     | Pressed state on filled buttons              |
| `dim-8`      | Subtle darkening                             |
| `lighten-20` / `lighten-8` | Shortcut hints on filled buttons |

Layering: modal `z-modal` + backdrop at `z-overlay`; sidepanel
`z-sidepanel` + backdrop; menu/popover `z-popover`; toast `z-toast`;
tooltip `z-tooltip` (see [layout.md](layout.md)).
