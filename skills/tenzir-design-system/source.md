# Source and Scope

This skill is the canonical home of the Tenzir design system. The YAML files
under [data/](data/) are authoritative for all values; the markdown
references explain how to choose and apply them. Evolve the system here —
change the YAML first, then update any markdown or downstream consumer that
depends on the changed values.

## Relationship to other repositories

`tenzir/content` (`brand/_brand.yml`, `brand/_tenzir.yml`) currently carries
its own copy of these definitions for Quarto/Typst rendering. Follow-up:
repoint that repository to consume this skill's [data/](data/) files so the
values exist in exactly one place. Until then, treat this skill as the source
of truth and propagate changes downstream.

Unlike the content repository, this skill references fonts via Google Fonts
(`source: google` in [data/brand.yml](data/brand.yml)) instead of vendoring
TTF files. Consumers that need file-based fonts (offline rendering, Typst)
should override the font source locally.

## Non-goals

- **Component specs** for tables, avatars, pagination, progress indicators,
  and skeletons: the system does not cover them yet; add specs here when a
  real need appears rather than inventing them speculatively.
- **Icon library**: the content repository's `brand/assets/icons/` are
  website content, not design-system assets. This skill ships only the
  official logos.
