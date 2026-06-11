# shadcn/ui

Tenzir theme for shadcn/ui projects. The ready-to-use theme lives in
[assets/shadcn-theme.css](../../assets/shadcn-theme.css); its values derive
from [data/brand.yml](../../data/brand.yml) and
[data/tokens.yml](../../data/tokens.yml) — if anything disagrees, the YAML
wins.

## Applying the Theme

shadcn/ui components reference semantic CSS variables (`--primary`,
`--muted-foreground`, …) defined in `:root` (light) and `.dark`. Replace
the variable values in the project's global CSS file (the `tailwindCssFile`
from `npx shadcn@latest info`) with the blocks from
[assets/shadcn-theme.css](../../assets/shadcn-theme.css), and keep the
generated `@theme inline` registration as is. Values are the canonical
Tenzir hexes rather than oklch conversions, so they stay byte-identical to
the YAML.

## Previewing with tweakcn

To inspect the theme visually, open the [tweakcn
editor](https://tweakcn.com/editor/theme), choose **Import** (Paste CSS),
and paste the contents of
[assets/shadcn-theme.css](../../assets/shadcn-theme.css). The file carries
the full variable set tweakcn renders — colors, fonts, and radius — for
both light and dark mode. Going the other way, theme tweaks
made in tweakcn export as the same CSS format; fold accepted changes back
into the YAML first, then regenerate the asset.

## Mapping Rationale

| shadcn variable | Tenzir token | Why |
| --- | --- | --- |
| `--background` / `--foreground` | `neutral-100` / `neutral-800` | App background; default text |
| `--card`, `--popover` | `neutral-50` | Elevated surfaces on the neutral-100 page |
| `--primary` | `blue-500` (dark: `blue-400`) | Brand primary; dark mode steps one level lighter |
| `--secondary`, `--muted` | `neutral-200` (dark: `neutral-600`/`neutral-700`) | Subtle fills |
| `--muted-foreground` | `neutral-500` (dark: `neutral-400`) | Tertiary text |
| `--accent` | `neutral-100` (dark: `neutral-600`) | Hover fill on cards/menus |
| `--destructive` | `red-500` (dark: `red-400`) | Danger role |
| `--border` / `--input` | `neutral-200` / `neutral-250` | Dividers; control outlines |
| `--ring` | `blue-500` (dark: `blue-400`) | Active borders are primary |
| `--chart-1..5` | `graph-1..5` | Chart sequence; `yellow-500` is the sixth series |
| `--radius` | `radius` (5px) | shadcn derives `rounded-md` = 3px = `radius-tight` |

Shadows are deliberately not overridden — shadcn's defaults are subtle and
fit the system; mapping the four Tenzir shadow tokens onto shadcn's
eight-level scale reads as too heavy. The Tenzir shadow tokens remain the
reference for hand-built components ([elevation.md](../elevation.md)).

Dark mode follows `tenzir.dark` in tokens.yml: shared palette, surfaces on
`neutral-700`/`neutral-800`, status hues one step lighter (400-level) with
dark foregrounds.

## Fonts

The theme sets `--font-sans` and `--font-mono` to Inter and JetBrains Mono
(see [typography.md](../typography.md) for sourcing). In Next.js, prefer
`next/font` and wire the resulting variables into `--font-sans`/
`--font-mono`.

## Usage Rules

- Style through the semantic utilities (`bg-primary`,
  `text-muted-foreground`, `border-border`) — never raw palette values in
  `className`. The theme then carries light and dark automatically; no
  `dark:` overrides.
- Component variants map cleanly: shadcn `default` button = Tenzir primary
  button, `destructive` = delete button, `secondary`/`ghost` = the subtle
  fills, `outline` = the neutral-250-bordered secondary button.
- For additional status colors (success, warning, info), add custom
  variables following the shadcn `name`/`name-foreground` convention with
  the values from [colors.md](../colors.md): e.g. `--success: #1ab252`
  (green-600) with `--success-foreground: #fdfdfe`, dark
  `--success: #5ee891` (green-400) with `--success-foreground: #0e1017`.
