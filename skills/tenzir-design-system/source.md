# Source and Scope

The YAML files under [data/](data/) are authoritative for all **values**; the
`references/` markdown captures the **design decisions**: how to choose and
apply tokens. Change the YAML first, then update the dependent markdown.

The skill stops at values and decisions. How any tool realizes them is out of
scope; the design system never bends to a particular implementation.

This skill references fonts via Google Fonts (`source: google`); output that
needs file-based fonts (offline, PDF) overrides locally.

## Non-goals

- Component specs: the system contributes tokens and invariants, not component
  anatomy.
- Page-level composition (section rhythms, footers, logo walls, illustrations):
  exchangeable by design; only the core brand lives here.
- Tool-specific implementation: CSS blocks, framework configs, theme files.
- Icon assets: the system specifies the icon style
  ([references/iconography.md](references/iconography.md)), not a bundled set.
  Only the official logos ship here.
