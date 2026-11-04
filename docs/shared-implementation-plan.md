# Shared café showcase implementation plan

Status: documentation only · 5 November 2026

## 1. Product contract

Build one website with an eight-card opening gallery, eight independently composed café homepages and a persistent “Change design” control. Each design owns its own source/assets/docs folder. Preserve the research folder. This milestone is homepage-only: build complete homepages and their section interactions, not eight separate commerce systems.

Use the same sample café name, location placeholder, menu and prices across designs for a fair comparison. Show “Café design demo — sample content” in a restrained common disclosure. Do not fabricate a real address, working order flow or customer review. Avoid presenting the showcase itself as a real operating café.

## 2. Architecture decision and assumptions

The user has not confirmed Angular as a framework requirement. Keep the plan framework-neutral until implementation setup. A lightweight static application with route modules, scoped CSS and shared content is the default candidate for this bounded showcase. If Angular is selected, use a single Angular app with lazy feature routes and isolated styles; do not create eight Angular apps. Do not introduce a React-only animation dependency into an Angular implementation.

Before creating dependencies, verify current official framework documentation, package compatibility, library licenses and hosting fallback support. No package installation, framework scaffold, implementation code or deployment is part of this planning task.

Proposed source responsibilities:

```text
docs/                         shared plan and comparison index
design-gallery/               gallery composition and preview cards
shared/
  content/                    common demo café data
  routing/                    route parser/router integration
  registry/                   eight validated design entries
  components/                 return control and accessible primitives
  styles/                     reset, focus and shell-only rules
designs/<design-id>/
  docs/                       existing per-design planning documents
  components/                 independently composed homepage sections
  styles/                     scoped tokens and responsive rules
  assets/                     design-owned optimized exports
  motion/                     optional enhancement modules
  scene/                      cinematic design only if justified
research/                     retained evidence and references
```

The folders outside docs/research above are planned. Each design's docs folder already exists. Keep typography and page tokens scoped to that design root; avoid global headings, buttons or body backgrounds that leak into another design. The gallery uses a neutral identity of its own.

## 3. Routing and selection state

Reserve `/designs/` for the gallery and `/designs/<id>/` for a homepage. `/` is a resolver: on a fresh visit show the gallery; on a later root visit with a valid remembered selection redirect to its homepage. Use router navigation/replacement appropriately so the root redirect does not produce an extra Back step. Direct route intent always outranks saved state.

| Situation | Expected result |
|---|---|
| First load of `/`, no saved design | Gallery, main heading focused only after app navigation as appropriate |
| Root load with valid saved design | That homepage |
| Direct `/designs/` with any saved value | Gallery; never automatically bounce back to saved design |
| Direct valid homepage route | Requested homepage; save that selection as the current design |
| Gallery card activation | Navigate to card's route, save its ID, scroll to top and focus page heading |
| Change design button | Navigate to gallery, preserve selection highlight and focus gallery heading |
| Browser Back/Forward | Respect route history; saved selection must not override the URL |
| Invalid saved ID | Ignore/clear it and show the gallery at root |
| Unknown homepage ID | Useful not-found message with gallery link; do not crash or silently show another design |
| Storage unavailable | Navigation still works; preference simply does not persist |
| Reload a valid nested route | Same homepage, provided hosting rewrites/routes are configured correctly |

Store only a schema version and selected design ID in browser storage. Never store authoritative content or route history there. Validate the ID against the registry before using it. Isolate storage access in a small adapter with exception handling. No account or backend is needed.

## 4. Gallery implementation

Use a neutral studio-like surface, a concise heading explaining the showcase and eight preview cards. Each card contains a real final thumbnail, design name, one-sentence style description, motion level and a clear “Explore design” link. Mark the current selection with text and styling, not color alone. Use a three/four-column wide layout only when cards remain readable; collapse to two and then one column based on available width.

Initially use the original research boards as clearly identified placeholders. Replace them with captures of each implemented page before completion. Do not represent conceptual boards as final website screenshots. Gallery thumbnails should load without initializing eight homepages or their animation engines.

Cards are semantic links with an obvious focus state. Avoid nested buttons inside a large clickable card unless structure is unambiguous. Provide the full design label to assistive technology. Hover may reveal polish but cannot hide essential text or the activation path.

## 5. Persistent design-return control

Label it “Change design”; a grid icon may supplement the text. Place it in a stable screen corner with safe-area spacing and an opaque high-contrast surface independent of the page palette. On very narrow screens allow a compact bottom bar or header location while keeping the label clear. Test it above cookie banners or mobile navigation if such elements are later added.

It must not cover menu prices, footer links or floating primary actions. Support keyboard and touch. Give content enough breathing room near its position. It is a navigation link to the gallery; normal browser link behaviors should remain available. Do not clear the saved preference merely because the gallery is opened.

## 6. Registry and content contracts

Each registry entry needs a stable ID, name, route, thumbnail, short description, motion level and lazy page loader. Validate uniqueness of IDs/routes and that every card has a loadable target. Optional metadata includes palette and research/plan links for development; do not expose implementation jargon in café visitor flows.

Shared café content should include:

- Brand name, short description and demo disclosure.
- Menu categories and items: ID, name, description, price/currency, size, dietary tags and availability where known.
- Location: text address, venue timezone, weekly hours, exceptional hours, phone, email, external directions URL and verified access notes.
- Optional story, gallery captions and genuine external social links.

No date-sensitive “Open now” status until reliable venue timezone and exception data exist. Store amounts consistently and format them for the selected locale. Unknown dietary information remains unknown; do not infer allergy safety. Use shared content helpers but independent section markup and composition.

## 7. Shared behavior versus design independence

Share routing, persistence, data, accessible dialog primitives, image conventions and failure handling. Keep hero composition, section rhythm, navigation appearance, menu treatment, gallery arrangement and footer composition local to each design. A single universal homepage component with eight CSS classes does not satisfy the brief.

Common controls can accept appearance hooks while preserving semantics. Each homepage must be independently runnable through its direct route and must not depend on visiting another design first. Motion hooks need explicit teardown ownership.

## 8. Loading and media strategy

Render a useful shell immediately. Load only the selected homepage's styles, images and optional motion/3D modules. Avoid eagerly importing scene libraries at application root. Gallery media are small thumbnails. The cinematic route renders a matching poster before optional model loading; ordinary routes do not fetch its GLB or runtime.

Use responsive image sources, explicit dimensions, useful alt text and priority only for the current hero. Reserve typography space where feasible and keep font weight sets small. Test cold-load and repeated-switch memory behavior separately. Performance targets from existing research remain targets, not results.

## 9. Execution order and dependencies

1. Confirm route strategy/framework/preview support; choose a supported package set from current official docs at implementation time.
2. Create the shared content fixture, unique registry and neutral shell.
3. Build gallery links and basic route entries for all eight IDs. Verify URL/history/storage behavior using simple structural pages.
4. Implement Warm Editorial end-to-end, including mobile navigation, complete menu and footer.
5. Implement Japanese Minimal and Botanical Calm to validate independent layouts and image treatments.
6. Implement Heritage Classic and Bakery & Brunch for centered typography and food-heavy content.
7. Implement Playful Retro and Industrial Coffee Lab for more graphic compositions.
8. Complete Dark Cinematic as a static homepage, then evaluate its isolated 3D proof of concept. Keep the static route usable throughout.
9. Capture final gallery previews, run the cross-design checks and resolve observed defects.
10. Prepare local handoff and a deployment configuration after the build scope is complete; actual hosting follows the selected workflow during implementation.

Numbering of design folders is for comparison, not a mandatory coding order. Do not add motion before a complete static composition. Per-design implementation plans refine the tasks for each route.

## 10. Meaningful verification plan

Automate the central state/routing cases because a failure affects all eight routes: fresh root entry, remembered entry, explicit gallery access, direct design entry, invalid ID, unavailable storage and Back/Forward. Add an end-to-end traversal selecting each design and returning to the gallery. Test every nested route on the actual preview/hosting configuration.

Manual checks: responsive composition at the specified widths; keyboard-only use; focus visibility and restoration; mobile menu; reduced motion; image/font failure; touch interaction; menu readability and final footer; switching away from active scenes. Capture at least one full desktop and mobile page per design plus the gallery.

Measure that ordinary designs do not load the cinematic runtime and that switching removes old observers, listeners and canvases. Use performance tools on a representative midrange phone or clearly documented approximation; desktop scores alone do not establish mobile quality. Add targeted tests for observed defects; avoid tests that only repeat CSS values.

Completion evidence goes in each design's `docs/verification.md` and a shared `docs/verification-summary.md` during implementation. These files must contain actual results and unresolved limitations, not prewritten passes.

## 11. Risks and handling

| Risk | Handling |
|---|---|
| Eight designs collapse into palette swaps | Review full composition, menu, navigation and footer side by side |
| Page styles leak after switching | Scope tokens/styles; test A → B → A and refresh on B |
| Saved selection traps visitors outside gallery | Explicit gallery route outranks remembered choice |
| Eight designs load all assets up front | Lazy route modules and media; inspect network requests |
| 3D blocks practical tasks | HTML content plus poster; optional scene; context-loss fallback |
| Business content is missing | Consistent clearly labeled sample fixture; replace before real launch |
| Angular wording remains ambiguous | Treat framework as provisional; use a single app once selected |
| Stock venue images mislead | Use them only as labeled demo imagery; acquire actual venue photos for launch |

## 12. Scope completion gate

All eight plans must pass their common final gate. The gallery, URL behavior, state persistence and shared controls must also pass. No dead controls, false successful submissions, fabricated testimonials or invisible content awaiting failed animations. Document remaining content and deployment limitations explicitly. This planning task ends with reviewable documents; building the actual website is the next stage.
