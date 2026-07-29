# Branded Effects

The brand leans on a small, restrained set of effects. The design system is
deliberately simple: strict light and dark modes, minimal background noise,
and flat surfaces. The signature accent is the brand gradient, which appears
as a **border** to emphasize something beyond the reach of the primary color,
and as display text. Values reference the palette in [colors.md](colors.md)
and [data/brand.yml](../data/brand.yml).

## Gradient border

The primary way to push an element past the emphasis the primary color can
give: a thin ring of the brand's blue→green ramp on the element's
edge. Use it to lift a key interactive card or a featured surface above its
neighbors, and keep it rare so it stays special. It may animate (a slow
rotation on hover or focus); honor `prefers-reduced-motion` by dropping the
motion.

## Brand gradient text

The blue→green ramp (`blue-500` → `green-500`, left to right) as a **display
accent only**: hero headlines, section kickers, stat figures. Never body copy,
controls, or fills. Size the gradient to its content so each element runs the
full ramp; a short label over a container-wide gradient samples only blue.
Works unchanged on light and dark.

## Kicker (section eyebrow)

A compact monospaced, uppercase, letter-spaced label that introduces a heading
and reads as technical: JetBrains Mono, `text-sm` (compact variant `text-xs`),
600 weight, +5% tracking, uppercase. Color is applied separately, usually the
brand gradient above, or muted. See [typography.md](typography.md).

## Links

Neutral with the accent on hover: a link inherits the surrounding text color
and carries a 1px underline in a softened decoration color (currentColor at
40% alpha, `--link-underline`) at 0.18em offset; hover and focus-visible turn
text and underline to the accent (`--link-hover`, aliasing `primary-accent`:
`blue-600` light, `blue-300` dark). The underline is the affordance, so it
never relies on color alone. Blue-as-link would spend the brand hue on every
anchor and stop signaling anything on link-dense surfaces; with this
treatment the accent appears only under the pointer. Whole-row and card
anchors skip the underline entirely; their hover fill and layout carry the
affordance, and titles inside them stay bare. Buttons and CTAs keep their
solid `primary` fills.

Email is the exception: hover is unreliable there (Outlook ignores it, touch
has none), so email links render in the paragraph color with a persistent
full-color underline, and the accent returns only as a `:hover` bonus for
webmail clients that honor `<style>`.

## Article prose

Long-form body typography for rendered markdown (blog posts), keyed to tokens:
body `text-lg` at 1.75 line height (a deliberate long-form exception to the
paired line height); generous heading rhythm (h2 `text-2xl` with its paired
tracking, h3 `text-xl`); links per the neutral treatment above; blockquotes
with a `blue-300` inline-start rule, italic and muted; inline code in the
muted well at `radius-tight`. Hand-rolled against tokens rather than a
typography plugin, since the palette carries only Tenzir hues.

## Single-tone logo flatten

When only one logo artwork variant is available for a surface, flatten it to
solid white (for dark surfaces) or solid black (for light surfaces). Prefer the
correct [logo variant](../SKILL.md) over recoloring; flatten only as a fallback.
