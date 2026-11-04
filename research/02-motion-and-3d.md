# Motion, transitions, scrolling and 3D catalogue

All timings and budgets below are proposed starting values, not measurements of reference websites.

## Motion language

Use a feeling of settling, pouring and gentle warmth. Animate transform and opacity where practical. Let text finish quickly enough to read; do not animate every letter throughout the page. One library should own each animated property. Avoid competing scroll handlers and independent render loops.

| Interaction | Proposed effect | Starting timing | Reduced-motion / mobile treatment |
|---|---|---|---|
| Initial hero | Heading rises 12–20px with opacity; cup settles | 500–800ms; short stagger | Immediate content or short opacity fade |
| Button | Color, border or underline; press scale approximately .98 | 120–180ms | Keep feedback, remove scaling if needed |
| Product card | Image rises 4–6px; shadow deepens slightly | 180–250ms | Static image; focus outline; no hover dependency |
| Section reveal | 12–24px rise and fade once | 350–550ms | Static content |
| Menu category | Brief crossfade or height-aware layout transition | 150–250ms | Instant swap; maintain focus |
| Mobile navigation | Panel fades with a small vertical offset | 180–250ms | Immediate or fade-only; correct focus behavior |
| Gallery lightbox | Image fades or gently scales into its frame | 180–250ms | Fade-only; Escape and close button |
| Page transition | Short crossfade, optionally shared image | 150–300ms | Normal navigation when unsupported |
| Cup pointer response | Approximately 3–5 degrees of tilt | Damped response | Disabled for touch and reduced motion |
| Photo parallax | Limited displacement, roughly 20–40px | Scroll-linked | Disabled on small screens and reduced motion |
| Steam | Faint slow decorative drift | 4–6s loop | Static or omitted; pause when offscreen; apply required motion controls |

Suggested easing: quick ease-out for controls, smooth deceleration for reveals, lightly damped spring for cup orientation. Avoid rubbery springs for prices, menu text and navigation. Stop decorative animation when the page is hidden.

## Scroll behavior

Default to native document scrolling. Anchor links may use browser smooth scrolling when motion preference allows it. Maintain keyboard Page Up/Down, Home/End, touch scrolling, browser Back and normal scroll restoration. Do not make reaching the menu dependent on completing an animation.

[GSAP ScrollTrigger](https://gsap.com/docs/v3/Plugins/ScrollTrigger/) is a candidate for a coordinated storytelling sequence with scrub and pin behavior. Prototype only one short desktop scene: beans → cup → finished drink. Keep text outside canvas and offer all three stages in normal flow for narrow screens and reduced motion. A suggested initial pin budget is around one additional viewport of scroll; actual usability determines whether pinning stays.

[Lenis](https://github.com/darkroomengineering/lenis) is optional, not the default. Its role is scroll interpolation, not making heavy scenes intrinsically faster. Add it only if a measured prototype benefits; review anchors, nested scrolling, touch behavior, focus and ScrollTrigger synchronization. Disable interpolation for reduced motion. Never combine multiple smooth-scroll engines.

Avoid mandatory horizontal scrolling, scroll snapping for the entire page, repeated long pins, reverse-direction surprises, cursor replacement, scroll-jacking, sound autoplay and loading screens that block access to content.

## What “3D images” can mean

| Format | What it provides | Good café use | Main tradeoff |
|---|---|---|---|
| Static 3D render | A normal image rendered from a model | Premium hero or product composition | No true interactive rotation; excellent fallback |
| Transparent raster cutout | Isolated cup or pastry with stylized depth | Overlapping editorial cards | Must look correct on the chosen background |
| 2.5D layered composition | Images at different depths with limited movement | Cup, shadow and beans moving subtly | Perspective illusion rather than full 3D |
| Rendered animation video | Predictable cinematic lighting and motion | Short pour or steam sequence | Media weight; poster and motion controls needed |
| Image sequence | Scrubbable pre-rendered frames | A controlled short pouring narrative | Many frames can create excessive downloads and memory use |
| Real-time GLB model | Actual interactive geometry | One rotatable ceramic cup | GPU, model optimization and fallbacks |
| Full real-time scene | Camera, lighting, particles and interaction | A highly expressive coffee ritual | Highest engineering and device-testing cost |

An AI-generated 3D-looking raster is still an image. It does not automatically contain geometry, editable materials or consistent unseen angles. Production-ready interactive models need a separate modeling and optimization process.

## Ten 3D concept candidates

| Concept | Proposed placement and behavior | Effort / performance risk | Recommendation |
|---|---|---|---|
| Ceramic latte cup and saucer | Hero; subtle settling or optional rotation | Medium / medium | Best initial candidate |
| Iced latte with ice and layers | Seasonal product; static render or turntable | Medium-high / high if refractive | Prefer baked render first |
| Floating roasted beans | Small accents around hero | Low-medium / low if instanced | Use sparingly; not across all sections |
| Croissant still life | Food card or pairing section | Medium / low as image | Strong supporting asset |
| Coffee bag turntable | Beans shop, if applicable | Medium / medium | Only if packaged products are sold |
| Pour-over setup | Craft story with three stages | High / medium-high | Optional showcase prototype |
| Exploded drink layers | Explain espresso, milk and foam | Medium-high / medium | Useful only with an equivalent text explanation |
| Miniature café diorama | About or location illustration | High / high | Later exploration; real venue photos still needed |
| Espresso-machine close-up | Short branded film or still | High / high | Prefer rendered video or photography |
| Coffee-ring typography | Decorative heading motif | Low / low as SVG or CSS | Use code-native artwork, no WebGL required |

## Recommended scene treatment

Warm off-white ceramic with a handmade rim, espresso crema or believable latte art, soft window light from upper left and a grounded contact shadow. Position the cup on the right for desktop with negative space for live HTML copy on the left. Produce a separate mobile crop. Avoid tiny floating objects over body text. Camera rotation must not reveal unfinished geometry or unreadable branding.

Build one optimized model and reuse it for hero poster, detail stills and optional live interaction. Bake lighting where appropriate. Use instancing for repeated beans; keep draw calls, transparent layers, texture size and shadows under review. [React Three Fiber's performance guide](https://r3f.docs.pmnd.rs/advanced/scaling-performance) describes on-demand rendering and adaptive performance techniques.

## Initial engineering budgets to test

- Hero poster: aim for 150–300KB in an appropriate modern image format, with responsive variants.
- Compressed hero GLB: aim for 1–2MB; fallback to poster if the scene cannot remain responsive.
- Texture dimensions: start at 1K; justify each 2K texture through visual comparison.
- One active canvas; stop or suspend work offscreen and on hidden tabs.
- Cap device pixel ratio initially around 1–1.5 on constrained devices and tune from measurements.
- Aim for smooth animation on target devices; reduce quality or use the poster when frame time is consistently poor. Do not promise 60fps on all hardware.

These are project heuristics, not universal limits or library guarantees. Include runtime and decoder transfers when measuring the complete 3D download.

## Fallback ladder

1. Show HTML headline, actions and optimized poster immediately.
2. Load an optional scene after critical content, based on capability and preference.
3. Use a static scene or poster for reduced motion, constrained conditions or failed loading.
4. On WebGL loss or initialization error, restore the poster without layout shift.
5. Keep the menu, address and controls outside canvas and usable without 3D.

## Unusual effects worth prototyping

Choose at most one initially: a circular coffee-surface image reveal, beans assembling around a stationary cup, or a short scroll-controlled cup turn. A shader ripple or milk-pour simulation should earn its cost through a small prototype. Full fluid simulation, constant bloom, film grain overlays and multi-canvas backgrounds are poor default choices for a practical café site.
