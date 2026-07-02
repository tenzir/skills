This release tightens the Tenzir design system into a simpler, implementation-agnostic source of truth. It clarifies the light and dark text hierarchy, unifies brand-gradient usage, and removes default shadows so downstream implementations can apply the system consistently.

## 🔧 Changes

### Implementation-agnostic design system skill

The `tenzir-design-system` skill now focuses on the design system itself: machine-readable tokens plus the principles and invariants that define the style.

The skill owns two things: machine-readable tokens (`data/brand.yml`, `data/tokens.yml`) and the design decisions that explain how to apply them (color usage, typography, elevation, motion, iconography, layout, branded effects, and a short set of non-negotiable invariants). The per-tool integration guides that wired tokens into specific frameworks (Tailwind, shadcn, plain CSS, Quarto, slides, diagrams) and the bundled shadcn theme are gone; how the system gets realized in any given tool is out of scope. The result is a simpler, smaller system: strict light and dark modes, flat surfaces with shadows avoided, and the brand gradient used as a border or display accent.

*By @mavam and @claude in #24.*

### Symmetric light and dark text hierarchy in the design system

The `tenzir-design-system` skill now defines one neutral text hierarchy that is symmetric across light and dark mode: emphasis text (headings, active text, icons) takes the mode's strongest neutral (`neutral-800` light, `neutral-50` dark), body text pulls one step in on both ends (`neutral-700` light at 13.4:1, `neutral-300` dark at 12.7:1), and the muted tiers step down from there (`neutral-600`/`neutral-500` light; `neutral-400` dark, the minimum text grey on dark surfaces).

Previously the default text role was the harsh pure-black `neutral-800` (18.7:1), which is uncomfortable for long-form reading such as blog posts and docs. The canonical tokens now agree with the guidance: `foreground` means body text in both modes, headings pin to the emphasis shade, and the dark mapping gains a `text_emphasis` token so tooling can remap headings without consulting prose. The colors guide states the hierarchy once as a light/dark table with WCAG contrast validated per mode.

A coherence pass across the whole system also unified the brand gradient on the canonical `blue-500` → `green-500` ramp everywhere, keyed article-prose links to the `primary` role so they follow the dark remap, and reconciled the kicker's size between the typography and branded-effects guidance.

The shadow policy is now strict: the system carries no shadows by default, and the one sanctioned use is a light-mode surface floating over same-colored content — menus, popovers, and listboxes take `shadow-m` and toasts `shadow-s`. Hover and resting shadows on controls and cards are gone, dark mode uses no shadows at all, and the shadow scale slims to those two sizes, dropping the unused `shadow-xs` and `shadow-l` tokens.

*By @mavam and @claude in #25.*
