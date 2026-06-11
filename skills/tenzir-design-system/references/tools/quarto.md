# Quarto

Branding Quarto documents, reports, and presentations with the Tenzir design
system. [data/brand.yml](../../data/brand.yml) follows Quarto's
[brand.yml](https://posit-dev.github.io/brand-yml/) schema and can be
consumed directly.

## Setup

Point the project or document at the brand file:

```yaml
# _quarto.yml or document frontmatter
brand: path/to/tenzir-design-system/data/brand.yml
```

For a project-local copy, vendor `data/brand.yml` and `assets/logos/` next
to your `_quarto.yml` and adjust the logo paths (they are relative to the
brand file).

## What brand.yml Drives Automatically

- **Colors**: page foreground/background, links (`primary`), Bootstrap-style
  roles (`success`, `info`, `warning`, `danger`) in HTML output, and the
  full palette as SCSS variables (`$brand-blue-500`, …) for custom themes.
- **Typography**: Inter for body and headings, JetBrains Mono for code,
  including Google Fonts loading, sizes, and the inline/block code styling
  (neutral-700 on neutral-100).
- **Logos**: light/dark-aware logo selection in formats that support it
  (websites, dashboards, reveal.js).

## Beyond brand.yml

Values outside the brand.yml schema (spacing, radius, shadows, motion —
[data/tokens.yml](../../data/tokens.yml)) need manual wiring:

- **SCSS**: copy the needed values into a theme file, e.g.
  `$tnz-radius: 5px;` or shadow definitions from
  [tools/css.md](css.md).
- **Typst/PDF**: map tokens into template variables. The `tenzir/content`
  repository demonstrates this pattern with its Typst templates.

## Charts in Quarto Documents

Use the graph color order from brand.yml (`graph-1`…`graph-6`): `#0A54FF`,
`#0AADFF`, `#CF0AFF`, `#FF0AA5`, `#FF5C0A`, `#EDAE1D`. See
[diagrams.md](diagrams.md) for Mermaid/Graphviz styling.

## Relationship to tenzir/content

The `tenzir/content` repository (blog posts, solution briefs) currently
carries its own copy of the brand definition (`brand/_brand.yml` with
file-based fonts for offline Typst rendering). This skill's
[data/brand.yml](../../data/brand.yml) is the canonical source; `content`
will be repointed to consume it. Until then, keep the two in sync when
values change.
