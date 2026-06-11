# Elevation

Shadows and overlay dims. Values live in
[data/tokens.yml](../data/tokens.yml) (`tenzir.shadow`, `tenzir.opacity`);
this file explains how surfaces stack.

## Shadow Scale

Every shadow is **two layers** of `neutral-800` at varying opacity — both
layers are required for the correct depth effect. Match the size to the
surface:

| Token       | Surface                                      |
| ----------- | -------------------------------------------- |
| `shadow-l`  | Modals and sidepanels — highest elevation    |
| `shadow-m`  | Popups: menus, popovers, dropdown listboxes  |
| `shadow-s`  | Tooltips and toasts                          |
| `shadow-xs` | Subtle elevation: interactive cards, segmented-control thumbs |

Guidelines:

- Static surfaces are flat: cards and content regions separate via 1px
  `neutral-200` borders, not shadows. Shadows mark floating or
  interactive surfaces only.
- Don't mix shadow sizes within the same component category.
- Shadows are tuned for `neutral-50` surfaces on light backgrounds; in dark
  mode, rely on `neutral-700` hairline borders rather than shadows —
  surfaces stay on `neutral-800`.
- Interactive elevation moves one step (e.g., a card from `shadow-xs` to
  `shadow-s` on hover), never more.

## Dim and Lighten Overlays

Dims darken with `neutral-800` at the `dim-*` opacities; lightens brighten
with `neutral-50`:

| Token        | Use                                          |
| ------------ | -------------------------------------------- |
| `dim-50`     | Full-page backdrop behind modals/sidepanels  |
| `dim-20`     | Pressed state on filled (primary/error) buttons |
| `dim-8`      | Subtle darkening                             |
| `lighten-20` / `lighten-8` | Shortcut hints on filled buttons |

## Pairing with Z-Index

Elevated surfaces combine three things: a **z-index layer**
([layout.md](layout.md)), a **shadow**, and — for blocking surfaces — a
**backdrop dim**:

- Modal: `z-modal` + `shadow-l` + `dim-50` backdrop at `z-overlay`
- Sidepanel: `z-sidepanel` + `shadow-l` + `dim-50` backdrop
- Menu/popover: `z-popover` + `shadow-m`, no backdrop
- Toast: `z-toast` + `shadow-s`
- Tooltip: `z-tooltip` + `shadow-s`
