# Elevation

Shadow values live in [data/tokens.yml](../data/tokens.yml)
(`tenzir.shadow`, `tenzir.opacity`).

## Shadows Are the Last Resort

Avoid drop shadows whenever possible. Surfaces separate by **border, backdrop,
or color, not shadows**:

- Static surfaces (cards, panels, regions): flat, 1px `neutral-200`
  borders.
- Modals and sidepanels: the `dim-50` backdrop separates. No shadow.
- Tooltips: the inverted `neutral-800` surface separates. No shadow.
- **Popups floating over same-colored content** are the exception:
  menus, popovers, listboxes use `shadow-m`; toasts `shadow-s`.
- Interactive nuance (active thumbs, hovering cards) may use
  `shadow-xs` → `shadow-s`, one step max.
- **Controls carry no resting shadow.** Buttons, inputs, and form fields sit
  flat on the surface; a resting drop shadow on a control reads as
  inconsistent against its flat siblings. Keep focus rings. Some component
  libraries bake a subtle control shadow by default; zero it.

Component libraries like shadcn/ui already behave this way; keep their
default shadows, add none. In dark mode, skip shadows entirely: surfaces
stay `neutral-800` with `neutral-700` hairline borders.

When used, every shadow is **two layers** of `neutral-800` (see
tokens.yml); both layers required.

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
