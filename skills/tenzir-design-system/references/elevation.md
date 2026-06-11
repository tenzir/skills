# Elevation

Shadows and overlay dims. Values live in
[data/tokens.yml](../data/tokens.yml) (`tenzir.shadow`, `tenzir.opacity`);
this file explains how surfaces stack.

## Shadows Are the Last Resort

Tenzir surfaces separate by **border, backdrop, or color — shadows come
last**, and only where nothing else does the job:

- Static surfaces (cards, panels, content regions): flat, separated by
  1px `neutral-200` borders. No shadow.
- Modals and sidepanels: the `dim-50` backdrop is the separator. No
  shadow needed.
- Tooltips: the inverted `neutral-800` surface separates itself. No
  shadow needed.
- **Popups that float over same-colored content** — menus, popovers,
  dropdown listboxes, toasts — are the one place a shadow earns its
  keep: use `shadow-m` (toasts: `shadow-s`).
- Interactive nuance (an active segmented-control thumb, a hovering
  interactive card) may carry `shadow-xs`/`shadow-s`.

## Shadow Scale

When a shadow is warranted, every shadow is **two layers** of
`neutral-800` at varying opacity — both layers are required for the
correct depth effect:

| Token       | Use                                          |
| ----------- | -------------------------------------------- |
| `shadow-m`  | Popups: menus, popovers, dropdown listboxes  |
| `shadow-s`  | Toasts; hover state of interactive cards     |
| `shadow-xs` | Subtle interactive nuance (thumbs, cards)    |
| `shadow-l`  | Reserved: page-level emphasis where a backdrop is unavailable |

Guidelines:

- Don't mix shadow sizes within the same component category.
- Shadows are tuned for `neutral-50` surfaces on light backgrounds; in dark
  mode, rely on `neutral-700` hairline borders rather than shadows —
  surfaces stay on `neutral-800`.
- Interactive elevation moves one step (e.g., a card from `shadow-xs` to
  `shadow-s` on hover), never more.
- This matches component libraries like shadcn/ui out of the box: their
  default shadows on overlay components are fine; don't add more.

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

Elevated surfaces combine a **z-index layer** ([layout.md](layout.md))
with whichever separator fits:

- Modal: `z-modal` + `dim-50` backdrop at `z-overlay`
- Sidepanel: `z-sidepanel` + `dim-50` backdrop
- Menu/popover: `z-popover` + `shadow-m`, no backdrop
- Toast: `z-toast` + `shadow-s`
- Tooltip: `z-tooltip`, inverted surface, no shadow
