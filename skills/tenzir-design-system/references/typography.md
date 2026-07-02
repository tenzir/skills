# Typography

How to use Tenzir type. Families, base settings, and the full size scale
live in [data/brand.yml](../data/brand.yml) and
[data/tokens.yml](../data/tokens.yml) (`tenzir.typography`); this file
explains how to choose.

## Families

- **Inter**: everything except code. The corporate font for UI, documents,
  and slides.
- **JetBrains Mono**: code and anywhere a monospace font is required
  (pipelines, identifiers, log excerpts).

Both are open source and available from Google Fonts; for self-hosting use
[rsms.me/inter](https://rsms.me/inter/) and
[jetbrains.com/mono](https://www.jetbrains.com/lp/mono/), or the variable
fonts from Fontsource. In CSS, prefer variable fonts with static fallbacks:

```css
font-family: "Inter Variable", "Inter", system-ui, sans-serif;
font-family: "JetBrains Mono Variable", "JetBrains Mono", monospace;
```

## Choosing a Size

The scale runs `text-xxs` (10px) through `text-5xl` (48px), each with a
paired line height (see `tenzir.typography.text` in tokens.yml):

- `text-base` (16px): default body size in roomy layouts
- `text-sm` (14px): compact body copy, dense UI, and the **default code
  size**
- `text-xxs` / `text-xs`: captions, metadata, footers, dense sidebars
- `text-lg` / `text-xl`: subheads
- `text-2xl` and above: titles; these sizes carry built-in negative
  tracking, so apply the paired letter-spacing
- `text-capitalized` (12px, +5% tracking): uppercase labels and category
  markers; always uppercase. The brand **kicker** applies the same
  uppercase, +5% tracking treatment in JetBrains Mono at `text-sm`/`text-xs`
  ([branded-effects.md](branded-effects.md))

JetBrains Mono uses the same scale but only `text-xxs` through `text-xl`.

## Weights

| Weight   | Value | Use for                                   |
| -------- | ----- | ----------------------------------------- |
| regular  | 400   | Body text, general content, code          |
| medium   | 500   | UI labels, emphasis, links, error messages in code |
| semibold | 600   | Headings, important elements, code headlines |

Bolder weights than 600 are not part of the system.

## Monospace Emphasis

For emphasis inside code, use the italic `-em` variants (`text-xs-em`,
`text-sm-em`, −0.04em tracking) instead of bolding; see
`tenzir.typography.mono_emphasis` in tokens.yml.
