# Warm Editorial — motion specification

Status: proposed, not implemented.

Use CSS for controls and one-time 16px/450ms section reveals. Cup may settle over 650ms; optional tiny pointer tilt only on fine pointers. Avoid scroll pinning.

## Implementation record

For each effect record: element, user purpose, trigger, duration/easing, runtime owner, responsive behavior, reduced-motion behavior, cleanup and failure fallback. Timings are tuned during implementation, not treated as benchmark results.

| Effect | Trigger | Default implementation | Reduced motion | Cleanup |
|---|---|---|---|---|
| Control feedback | Hover/focus/press | Short color/border response; preserve visible focus | Immediate or short color-only feedback | CSS states require no listener cleanup |
| Optional section entrance | First viewport entry | As allowed by this design's plan; reveal once | Static visible content | Disconnect observer on route exit |
| Route entry | Selected gallery card/direct entry | Focus main heading after route settles; optional brief fade | Instant navigation and focus | Cancel pending transition callbacks |
| Design-specific artwork | Only if approved in plan | Follow the design-specific paragraph above | Static poster/art | Stop loops and release scene resources if used |

## Acceptance

- [ ] With animation initialization blocked, all content remains readable.
- [ ] Reduced motion applies before effects start and responds to preference changes.
- [ ] No animation moves a navigation target while the visitor is trying to activate it.
- [ ] Rapid switching leaves no background observers, timelines or canvases owned by this route.
- [ ] No essential information exists only in an animation or canvas.
