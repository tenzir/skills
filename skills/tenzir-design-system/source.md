# Source and Provenance

This skill is the canonical home of the Tenzir design system tokens. The YAML
files under [data/](data/) are authoritative for all values; the markdown
references explain how to choose and apply them.

## Provenance markers

Sections in [data/tokens.yml](data/tokens.yml) carry one of two markers:

- **figma** — sourced from the official Tenzir design system in Figma. These
  values are settled; change them only when the Figma source changes.
- **proposed** — derived defaults added for completeness and consistency with
  the Figma-sourced tokens. They fill gaps the Figma system does not cover
  yet: motion, z-index layering, breakpoints, and dark mode. Treat them as
  the recommended defaults, but expect them to be refined when the design
  team formalizes these areas.

Component references under [references/components/](references/components/)
follow the same convention: specs without a banner are Figma-sourced; specs
opening with a "Derived spec" banner (tooltip, modal, card, menu) are
proposed.

## Notable normalizations

- The Figma `green-transparent` tint uses the off-palette base `#1CC45A`;
  the skill normalizes it to `green-600` (`#1AB252`) at 12% alpha.
- Earlier versions of this skill contained shadow snippets with the typo
  `#0E1217`; the correct shadow base is `neutral-800` (`#0E1017`).

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
  and skeletons: nothing in the Figma system implies them, so the skill does
  not invent them.
- **Icon library**: the content repository's `brand/assets/icons/` are
  website content, not design-system assets. This skill ships only the
  official logos.
