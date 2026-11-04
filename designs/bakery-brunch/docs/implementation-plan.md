# Bakery & Brunch — detailed implementation plan

Status: planned, not implemented · 5 November 2026

## 1. Shared foundation and design-gallery contract

Use the common application shell, shared café content contract, gallery routing and persistent “Change design” control defined in [the shared implementation plan](../../../docs/shared-implementation-plan.md). Keep this design’s layout, style tokens, sections, assets and motion in its own folder. This first milestone and the final completion gate are identical across all eight plans.

Deliverable: a direct `/designs/bakery-brunch/` entry, a gallery card, a validated registry record and a page that can return to `/designs/` without reloading the application unnecessarily. Essential content and navigation must work before optional motion loads.

## 2. Design objective and scope

Food-first imagery, warm type and large category blocks make breakfast and pastry immediately tangible while emphasizing availability and visit information.

Build a complete responsive homepage containing navigation, meaningful product/menu content, story/space content, visit information and footer. Every visible control must have an implemented behavior or a valid destination. Additional commerce, authentication, payment, reservations backend and newsletter services are outside this initial homepage scope.

[Research brief](../../../research/design-directions/07-bakery-brunch/design-brief.md) supplies the creative context. Keep the same fictional café identity and common sample menu across variants so clients compare design rather than different businesses. Clearly label the shared sample data as a demo. Replace it with verified business content before a real launch.

## 3. Folder ownership and deliverables

Target folder: `designs/bakery-brunch/`. Its existing `docs/` is the handoff. During implementation add a route entry, `components/`, `styles/`, `assets/` and optional `motion/` or `scene/` modules. Exact extensions depend on the framework decision in the shared plan.

- Route entry composes this design's sections in its own order; do not reduce the page to a shared hero with a new palette.
- `styles/` owns locally scoped tokens, layout, responsive rules and interaction states.
- `assets/` holds acquired images and original art; attach provenance entries in [the asset checklist](asset-checklist.md).
- `components/` owns the sections below; reuse accessible low-level controls without forcing a common visual layout.
- `docs/verification.md` will hold real implementation screenshots, checks and unresolved issues. Do not prefill passing results.

## 4. Visual tokens and responsive rules

Candidate palette: **#FFF8EB / #3E2920 / #A94F31 / #DABF8C**. Candidate typography: **DM Serif Display / Manrope**. Confirm font availability and exact licensing during asset acquisition. Use semantic names such as surface, ink, action, muted and border; test foreground/background pairs instead of assuming the palette is accessible.

Create type, spacing, radius, border, shadow and container tokens before detailed styling. Establish mobile, medium and wide compositions using content-driven breakpoints. Inspect at 320, 390, 768, 1024 and 1440 CSS pixels; these are test widths, not a requirement to create five breakpoints. Use fluid type within safe readable bounds. Keep body text at least 16px as a project target and avoid long all-cap paragraphs.

Plan a normal-flow fallback for every overlapping composition. Reserve dimensions for images. On phones show the primary action early, stack text before supporting media when appropriate and use no horizontal page overflow. At 200% zoom, preserve the menu, directions and gallery-return control.

## 5. Homepage section implementation

Build semantic structure and real-text content first, then imagery and styling, then motion. Treat each row as a separately reviewable task.

| Order | Section component | Implementation detail |
|---|---|---|
| 1 | `FoodHero` | Large appetizing photograph with title and Menu/Visit actions on a readable panel; do not place thin type over busy pastry textures. |
| 2 | `DailySpecialties` | A clear list/grid of confirmed specialties and availability; sample items must be identified as demo content. |
| 3 | `BrunchAndDrinks` | Food and drink categories with prices, portion or size details where supplied and a clear category selector. |
| 4 | `BakingStory` | Real baking-process image and concise explanation of the kitchen or ingredients. |
| 5 | `PickupInformation` | Include pickup instructions only when real; no simulated successful orders or inert preorder form. |
| 6 | `BakeryVisit` | Hours, address, contact and any actual pickup/access details. |
| 7 | `BakeryFooter` | Warm surface with practical links and optional real preorder link. |

Completion evidence: full-page desktop and mobile captures showing the entire sequence, including footer. A polished hero alone does not complete this design.

## 6. Navigation and visitor interactions

- Build this design's header with links to actual sections. The main Menu action scrolls to a readable menu preview/full menu section within the homepage scope.
- Apply header-offset anchor positioning and expose a skip link. Preserve useful browser Back/Forward behavior.
- Mobile navigation uses a labeled toggle with expanded state. If modal, trap focus appropriately, close on Escape and restore focus; if inline, keep normal document focus behavior.
- Use the shared fixed “Change design” control with a style-safe high-contrast surface. It opens the gallery, sets focus to its heading and preserves which design was selected.
- Gallery or menu controls must work with keyboard and touch. No information is hover-only. Provide visible focus and accurate selected/expanded states.
- Phone/email links work only with supplied demo/real values; do not invent a live business destination. An unconfigured directions action must explain the demo state rather than sending users to a random address.

## 7. Content and asset production

- **Hero food image:** Actual hero dish/pastry, landscape and portrait crops with natural color.
- **Menu food set:** Consistent photographed portions; no misleading oversized generated dishes.
- **Baking process:** Permission-cleared hands/process and an honest kitchen detail.
- **Optional render:** A stylized croissant/espresso still life used as brand art, not a substitute for accurate menu imagery.

For each asset record creator, item URL or source, rights, download/creation date, intended section, alt text, crop and exported sizes. Produce mobile and desktop variants only where cropping requires them. Prefer modern image formats with a reliable fallback where needed. Do not bake headlines, prices or actionable labels into raster images.

Before implementation, check that the selected content can fit both the largest and smallest layouts. Use long product names and multi-line addresses in layout checks. Never publish fabricated reviews, awards, history or sourcing claims.

## 8. Motion and transition implementation

Use short card fades and small image zoom on hover where supported. Keep daily offerings static and accessible. Do not rotate products automatically or animate availability messages.

Motion is enhancement: render content visible by default, then activate effects after initialization. Use a single owner per animated property and clean up listeners/observers on route changes. Honor reduced motion on first load and when the preference changes. Disable decorative movement, smooth-scroll interpolation and camera motion for that preference. Restore focus after route transitions, not in the middle of an animation.

Record each implemented effect in [the motion specification](motion-spec.md) with trigger, affected element, cleanup and fallback. Compare the page with motion disabled before accepting the added complexity.

## 9. Accessibility and semantic implementation

Use one meaningful h1, ordered headings, header/nav/main/footer landmarks and semantic links/buttons. Decorative images get empty alt text; informative images need concise contextual descriptions. Form controls, if any, need labels and error states. Do not use color alone for selection, availability or dietary meaning.

Measure normal text contrast against the WCAG AA target of 4.5:1 and applicable large text/UI contrast at 3:1. Prefer approximately 44px tap targets, preserve keyboard focus and validate reading order at each layout change. Check reduced motion, zoom, menu operation and gallery return manually. Automated results supplement rather than replace manual checks.

## 10. Loading, performance and error states

Prioritize title, primary actions and hero poster. Lazy-load lower images and this design's optional runtime modules. Reserve all media space to avoid shifting text. Avoid downloading assets for the other seven homepages when this route opens.

Initial image budget: hero poster approximately 150–300KB where visual quality permits; do not treat that as an achieved measurement. Target LCP ≤2.5s, INP ≤200ms and CLS ≤0.1 using appropriate field data when available; lab checks are provisional. Record the test device/network and separate cold from warm runs.

If a font fails, the fallback must preserve layout. If an image fails, retain a useful frame and readable surrounding content. If a motion/3D module fails, the static homepage still works. On repeated design switches, cancel pending effects and prevent stale asset completion from modifying another route.

## 11. Ordered execution milestones

1. Register the route and create this design's structural section components. Verify direct entry and gallery return before polish.
2. Bind shared sample content and implement semantic menu, contact and visit information.
3. Define tokens and complete a static mobile composition, including footer and navigation states.
4. Complete the wide and intermediate compositions with acquired, provenance-recorded media.
5. Implement keyboard, touch, category controls and any lightbox behavior; verify focus management.
6. Add only this design's specified motion or 3D enhancement, including cleanup and fallbacks.
7. Capture all target widths; resolve layout, accessibility and performance problems.
8. Integrate its final gallery thumbnail and truthful design summary, then complete the shared gate below.

Sequencing note: Implement after the shared menu data model is stable; use this page to validate food-heavy content, dietary labels and operational copy.

## 12. Design-specific verification and risks

- [ ] Food images keep useful crops without implying inaccurate portions.
- [ ] Category changes preserve focus and visible headings.
- [ ] Pickup language never promises an order flow that does not exist.
- [ ] Every section is present on mobile and desktop; no placeholder buttons or dead links remain.
- [ ] Long names, missing images, fallback fonts and reduced motion do not break the page.
- [ ] Entering this route directly and switching away/back preserves correct design styles.
- [ ] Only the currently selected homepage owns active effects and event handlers.

Store actual screenshots, measured sizes and unresolved defects in `docs/verification.md` during implementation. Do not mark a requirement passed merely because the relevant CSS or component exists.

## 13. Dependencies and decisions before final polish

Requires the shared registry, router, content fixture, return control and asset conventions. Brand name, location, menu/prices, rights-cleared photography and operational links remain content inputs. Choose font files after confirming rights. The framework choice is provisional; do not add Angular and React stacks together. Additional services need a separate scope decision.

If a live asset or motion feature is unavailable, complete a visually intentional static version and record the specific limitation. Do not hide a missing feature behind a nonfunctional control.

## 14. Completion and cross-design acceptance gate

- [ ] The gallery opens this design and the persistent “Change design” control returns to the gallery.
- [ ] Direct links, reloads, first visits, saved selections and browser Back/Forward follow the shared routing rules.
- [ ] The full responsive homepage has a distinct composition, typography, imagery, navigation treatment and footer.
- [ ] All visible actions work; demo content and unavailable real-world services are identified accurately.
- [ ] Keyboard, touch, reduced motion, media failure and route cleanup checks pass with recorded evidence.
- [ ] Only necessary assets load; observed performance and any limits are recorded rather than assumed.
- [ ] Screenshots and verification notes are saved, and the gallery preview matches the implemented homepage.
