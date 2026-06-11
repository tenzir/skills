# Source and Scope

The YAML files under [data/](data/) are authoritative for all values; the
markdown explains how to choose and apply them. Change the YAML first, then
update dependent markdown and downstream consumers.

## Downstream

`tenzir/content` (`brand/_brand.yml`, `brand/_tenzir.yml`) carries its own
copy of these definitions for Quarto/Typst rendering. Follow-up: repoint it
to this skill's [data/](data/) files. Until then, propagate changes there.

This skill references fonts via Google Fonts (`source: google`); consumers
needing file-based fonts (offline/Typst) override locally.

## Non-goals

- Component specs: shadcn/ui on the theme is the component layer; the
  system contributes tokens and invariants, not component anatomy.
- Page-level marketing composition (section rhythms, footers, logo
  walls, illustrations): exchangeable by design — only the core brand
  lives here.
- Icon assets: the system specifies the icon style
  ([references/iconography.md](references/iconography.md)), not a bundled
  set. Only the official logos ship here.
