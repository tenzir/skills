# shadcn/ui

The ready-to-use theme lives in
[assets/shadcn-theme.css](../../assets/shadcn-theme.css); values derive
from [data/](../../data/) — the YAML wins on any disagreement.

Replace the `:root` and `.dark` variable values in the project's global
CSS (the `tailwindCssFile` from `npx shadcn@latest info`) with the blocks
from that file, keeping the generated `@theme inline` registration. To
preview visually, paste the file into the [tweakcn
editor](https://tweakcn.com/editor/theme) (Import → Paste CSS); tweakcn
exports the same format back — fold accepted changes into the YAML first.

## Mapping

| shadcn variable | Tenzir token (light / dark) |
| --- | --- |
| `--background`, `--card`, `--popover` | `neutral-50` / `neutral-800` — flat surfaces, borders separate |
| `--foreground` | `neutral-800` / `neutral-50` |
| `--primary` | `blue-500` / `blue-400` |
| `--secondary`, `--muted`, `--accent` | `neutral-100` / `neutral-700` |
| `--muted-foreground` | `neutral-500` / `neutral-400` |
| `--destructive` | `red-500` / `red-400` |
| `--border` / `--input` | `neutral-200`, `neutral-250` / `neutral-700` |
| `--ring` | `blue-300` / `blue-400` |
| `--chart-1..5` | `graph-1..5` (`yellow-500` for a sixth) |
| `--radius` | 5px — shadcn derives `rounded-md` = 3px = `radius-tight` |

Notes:

- The ring stays soft (`blue-300`) because shadcn also draws it on
  buttons, where a primary ring reads as a double border. For the
  product's focused-input look, add
  `<Input className="focus-visible:border-primary" />`.
- Shadows are not overridden — shadcn's defaults match the elevation
  rules ([elevation.md](../elevation.md)).
- Fonts: set `--font-sans`/`--font-mono` to Inter and JetBrains Mono in
  `@theme` (or via `next/font`).
- Extra status colors follow the `name`/`name-foreground` convention with
  values from [colors.md](../colors.md), e.g. `--success: #1ab252` /
  dark `#5ee891`.
