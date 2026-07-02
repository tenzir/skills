# Motion

Durations and easing curves. Values live in
[data/tokens.yml](../data/tokens.yml) (`tenzir.motion`); this file explains
when and how to animate.

## When to Animate

Animate state changes that benefit from continuity: appearing overlays,
toggles, expanding panels. Don't animate initial page render, large layout
shifts, or anything on the data path (tables, charts updating with live
data).

## Durations

| Token             | Value | Use for                                  |
| ----------------- | ----- | ---------------------------------------- |
| `duration-instant`| 0ms   | Opt-out; state changes that must feel immediate |
| `duration-fast`   | 150ms | Hover/focus color and border transitions |
| `duration-base`   | 200ms | Default UI transitions: toggles, chevrons, fades |
| `duration-slow`   | 300ms | Larger surfaces: panels, modals, accordions |
| `duration-slower` | 500ms | Page-level or deliberate emphasis (rare) |

## Easing

| Token             | Curve                          | Use for            |
| ----------------- | ------------------------------ | ------------------ |
| `ease-standard`   | `cubic-bezier(0.4, 0, 0.2, 1)` | Most transitions; anything that changes in place |
| `ease-decelerate` | `cubic-bezier(0, 0, 0.2, 1)`   | Entering elements (tooltips, modals appearing) |
| `ease-accelerate` | `cubic-bezier(0.4, 0, 1, 1)`   | Exiting elements   |
| `ease-linear`     | `linear`                       | Progress bars and spinners only |

Standard pairings: hover = fast/standard, enter = base/decelerate, exit =
fast/accelerate, large surfaces = slow/decelerate.

## Reduced Motion

Always honor `prefers-reduced-motion: reduce` by disabling non-essential
transitions and animations.
