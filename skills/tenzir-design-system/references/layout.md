# Layout

Spacing, border radius, breakpoints, and z-index layering. Values live in
[data/tokens.yml](../data/tokens.yml) (`tenzir.spacing`, `tenzir.radius`,
`tenzir.breakpoint`, `tenzir.z_index`); this file explains how to choose.

## Spacing

Tenzir follows a compact 4px scale with half steps (`space-0` = 0 through
`space-20` = 80px). Pick by tier:

| Tier                  | Tokens               | Use for                                  |
| --------------------- | -------------------- | ---------------------------------------- |
| Tight (0–8px)         | `space-0`…`space-2`  | Icon gaps, badge padding, inline metadata |
| Component (12–16px)   | `space-3`, `space-4` | Ordinary component padding, form-field gaps |
| Group (20–32px)       | `space-5`…`space-8`  | Content groups, section gaps             |
| Page (40–80px)        | `space-10`, `space-16`, `space-20` | Page-level separation, major sections |

Guidelines:

- Express spacing in rem in CSS (16px root) so it scales with user font
  preferences; the px values in tokens.yml are the design reference.
- Use the same token for related elements to keep vertical rhythm; note the
  deliberate jumps 32→40→64px for major layout breaks.

## Border Radius

- `radius` (5px) — the default for all rectangular components: buttons,
  inputs, dropdowns, tags, toasts, cards, modals, tooltips.
- `radius-tight` (3px) — small inline components: badges, shortcut badges,
  buttons nested inside a 5px container (segmented controls, menu items).
- `radius-pill` (35px) — intentionally capsule-shaped controls only (toggle
  switches).
- Radio buttons are circular: `border-radius: 50%`.

Always reference the token instead of hardcoding the pixel value.

## Breakpoints

> Proposed tokens — see [source.md](../source.md).

`sm` 640 / `md` 768 / `lg` 1024 / `xl` 1280 / `xxl` 1536 (px, min-width).
These match Tailwind's defaults, so Tailwind consumers need no
configuration. Design desktop-first toward `lg`; the product UIs are
data-dense and not optimized below `md`.

## Z-Index Layering

> Proposed tokens — see [source.md](../source.md).

Layers step by 100 so applications can slot custom layers in between:

| Token         | Value | Surface                                  |
| ------------- | ----- | ---------------------------------------- |
| `z-base`      | 0     | Normal flow                              |
| `z-sticky`    | 100   | Sticky headers, pinned table columns     |
| `z-dropdown`  | 200   | Dropdown listboxes attached to controls  |
| `z-overlay`   | 300   | Full-page dim (pairs with `dim-50`)      |
| `z-sidepanel` | 400   | Sidepanels above the overlay             |
| `z-modal`     | 500   | Modal dialogs                            |
| `z-popover`   | 600   | Menus/popovers (may open above modals)   |
| `z-toast`     | 700   | Toasts                                   |
| `z-tooltip`   | 800   | Tooltips — always on top                 |

See [elevation.md](elevation.md) for pairing layers with shadows and dims.
