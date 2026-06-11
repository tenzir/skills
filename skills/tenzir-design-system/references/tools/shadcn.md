# shadcn/ui

Tenzir theme for shadcn/ui projects. All values derive from
[data/brand.yml](../../data/brand.yml) and
[data/tokens.yml](../../data/tokens.yml); if anything here disagrees with
the YAML, the YAML wins.

shadcn/ui components reference semantic CSS variables (`--primary`,
`--muted-foreground`, …) defined in `:root` (light) and `.dark`. To apply
the Tenzir theme, replace the variable values in the project's global CSS
file (the `tailwindCssFile` from `npx shadcn@latest info`) and keep the
generated `@theme inline` registration as is. Values are the canonical
Tenzir hexes rather than oklch conversions, so they stay byte-identical to
the YAML.

## Theme

```css
:root {
  /* Surfaces: neutral-100 page, neutral-50 cards/popovers */
  --background: #f7f8fa;
  --foreground: #0e1017;
  --card: #fdfdfe;
  --card-foreground: #0e1017;
  --popover: #fdfdfe;
  --popover-foreground: #0e1017;

  /* Actions */
  --primary: #0a54ff; /* blue-500 */
  --primary-foreground: #fdfdfe;
  --secondary: #f0f1f5; /* neutral-200 */
  --secondary-foreground: #0e1017;
  --destructive: #ff0a33; /* red-500 */
  --destructive-foreground: #fdfdfe;

  /* States */
  --muted: #f0f1f5; /* neutral-200 */
  --muted-foreground: #68738d; /* neutral-500 */
  --accent: #f7f8fa; /* neutral-100 hover fill on cards */
  --accent-foreground: #0e1017;

  /* Lines and focus */
  --border: #f0f1f5; /* neutral-200 */
  --input: #e3e6ed; /* neutral-250 control outlines */
  --ring: #e0eaff; /* blue-200 focus ring */

  /* Charts: graph-1..5; use yellow-500 #edae1d for a sixth series */
  --chart-1: #0a54ff;
  --chart-2: #0aadff;
  --chart-3: #cf0aff;
  --chart-4: #ff0aa5;
  --chart-5: #ff5c0a;

  /* Sidebar */
  --sidebar: #f7f8fa;
  --sidebar-foreground: #0e1017;
  --sidebar-primary: #0a54ff;
  --sidebar-primary-foreground: #fdfdfe;
  --sidebar-accent: #f0f1f5;
  --sidebar-accent-foreground: #0e1017;
  --sidebar-border: #f0f1f5;
  --sidebar-ring: #e0eaff;

  /* radius (5px) makes rounded-md = 3px = radius-tight */
  --radius: 0.3125rem;
}

/* Dark mode: semantic remapping from tenzir.dark — shared palette,
   status hues one step lighter (400-level) with dark foregrounds. */
.dark {
  --background: #0e1017; /* neutral-800 */
  --foreground: #fdfdfe;
  --card: #262e40; /* neutral-700 */
  --card-foreground: #fdfdfe;
  --popover: #262e40;
  --popover-foreground: #fdfdfe;

  --primary: #477eff; /* blue-400 */
  --primary-foreground: #0e1017;
  --secondary: #414b62; /* neutral-600 */
  --secondary-foreground: #fdfdfe;
  --destructive: #ff4766; /* red-400 */
  --destructive-foreground: #0e1017;

  --muted: #262e40; /* neutral-700 */
  --muted-foreground: #959db1; /* neutral-400 */
  --accent: #414b62; /* neutral-600 */
  --accent-foreground: #fdfdfe;

  --border: #414b62; /* neutral-600 */
  --input: #414b62;
  --ring: #477eff; /* blue-400 */

  /* Chart hues are shared between light and dark */
  --chart-1: #0a54ff;
  --chart-2: #0aadff;
  --chart-3: #cf0aff;
  --chart-4: #ff0aa5;
  --chart-5: #ff5c0a;

  --sidebar: #0e1017;
  --sidebar-foreground: #fdfdfe;
  --sidebar-primary: #477eff;
  --sidebar-primary-foreground: #0e1017;
  --sidebar-accent: #262e40;
  --sidebar-accent-foreground: #fdfdfe;
  --sidebar-border: #414b62;
  --sidebar-ring: #477eff;
}
```

## Fonts

Register the brand families in the `@theme inline` block (Tailwind v4):

```css
@theme inline {
  --font-sans: "Inter Variable", "Inter", system-ui, sans-serif;
  --font-mono: "JetBrains Mono Variable", "JetBrains Mono", monospace;
}
```

In Next.js, prefer `next/font` with Inter and JetBrains Mono and wire the
resulting variables into `--font-sans`/`--font-mono`.

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
- Shadows: shadcn components ship with Tailwind's default shadows; for
  pixel-faithful Tenzir elevation, override `--shadow-*` per
  [tailwind.md](tailwind.md).
