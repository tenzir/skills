---
title: Symmetric light and dark text hierarchy in the design system
type: change
authors:
  - mavam
  - claude
prs:
  - 25
created: 2026-07-02T05:50:09.6385Z
---

The `tenzir-design-system` skill now defines one neutral text hierarchy that is symmetric across light and dark mode: emphasis text (headings, active text, icons) takes the mode's strongest neutral (`neutral-800` light, `neutral-50` dark), body text pulls one step in on both ends (`neutral-700` light at 13.4:1, `neutral-300` dark at 12.7:1), and the muted tiers step down from there (`neutral-600`/`neutral-500` light; `neutral-400` dark, the minimum text grey on dark surfaces).

Previously the default text role was the harsh pure-black `neutral-800` (18.7:1), which is uncomfortable for long-form reading such as blog posts and docs. The canonical tokens now agree with the guidance: `foreground` means body text in both modes, headings pin to the emphasis shade, and the dark mapping gains a `text_emphasis` token so tooling can remap headings without consulting prose. The colors guide states the hierarchy once as a light/dark table with WCAG contrast validated per mode.

A coherence pass across the whole system also unified the brand gradient on the canonical `blue-500` → `green-500` ramp everywhere, aligned the shadow guidance so modals separate with the dim backdrop rather than large shadows, clarified that component-library control shadows are zeroed while floating-surface shadows stay, keyed article-prose links to the `primary` role so they follow the dark remap, and reconciled the kicker's size between the typography and branded-effects guidance.
