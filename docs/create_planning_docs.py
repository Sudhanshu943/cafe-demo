"""Create the documentation-only implementation handoff for eight café designs."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DESIGNS = [
('warm-editorial','Warm Editorial','01-warm-editorial',
 'An asymmetric magazine-like composition: live headline on the left, a large ceramic cup on the right, alternating editorial photo stories below.',
 '#F6F0E6 / #241A16 / #24483C / #C58A52','Fraunces / Manrope',
 [('EditorialHero','Two-column hero with a short welcoming headline, two clear actions and grounded ceramic-cup art. Keep the cup clear of copy and preserve space as fonts load.'),('VisitStrip','A quiet horizontal address/hours row immediately after the hero; wrap into labeled rows on phones.'),('SignatureSelection','Three large portrait product cards with real-text taste notes and prices; use a normal grid rather than an automatic carousel.'),('CraftFeature','Offset landscape photo with a narrow text column and one concrete craft detail. Reverse the visual balance from the hero.'),('SpaceGallery','One wide room photo and two supporting details with captions; optional accessible lightbox.'),('VisitPanel','Warm paper surface, text address, hours and directions; map preview is supplementary.'),('EditorialFooter','Forest surface, cream type, three balanced link groups and a compact utility row.')],
 [('Hero still life','Desktop and mobile cup-and-saucer renders with identical lighting; poster is the primary deliverable.'),('Venue images','Exterior, wide seating image and material detail in warm daylight.'),('Drink cards','Three consistent photographs with natural food color and unobstructed framing.')],
 'Use CSS for controls and one-time 16px/450ms section reveals. Cup may settle over 650ms; optional tiny pointer tilt only on fine pointers. Avoid scroll pinning.',
 ['Cup never overlaps the title at intermediate widths.','Alternating photo/text sections collapse in a meaningful reading order.','Warm decorative accents never become low-contrast menu text.'],
 'Implement first after the shell: it establishes a useful content baseline while keeping the most complex 3D work out of the critical path.'),
('japanese-minimal','Japanese Minimal','02-japanese-minimal',
 'Architecture takes priority: large whitespace, fine rules, precise alignment, restrained type and an uncluttered architectural hero.',
 '#FAFAF7 / #20231F / #9CADA2 / #D9D6CE','DM Sans with a restrained serif accent',
 [('ArchitecturalHero','A large uncropped venue image with a small editorial introduction and obvious Menu/Directions actions outside the image.'),('LocationEssentials','A compact label/value grid for address, hours and contact; no decorative text ticker.'),('PrecisionMenu','Fine-rule menu rows grouped by category, generous line spacing and a consistent price column.'),('CoffeePhilosophy','Short copy with one detail photograph; avoid an oversized generic brand manifesto.'),('ArchitectureGallery','Two or three generous images with meaningful captions and controlled aspect ratios.'),('QuietVisit','Simple address and hours layout with an external directions link.'),('MinimalFooter','Light surface and thin separators; repeat practical links without a large marketing block.')],
 [('Architecture hero','An actual venue photograph with clean perspective and mobile crop.'),('Porcelain accent','Optional single still render of a sculptural cup; no live canvas required.'),('Interior details','Two honest photographs showing seating and materials.')],
 'Use instant navigation feedback and optional 200ms opacity fades. Keep images static while reading; no pinned stories, smooth-scroll engine or automatic image sliders.',
 ['Whitespace does not push menu and visit actions out of reach.','Fine rules and secondary text remain visible at low brightness.','Architecture image maintains a useful composition on narrow phones.'],
 'Build after Warm Editorial to prove the shared shell supports a materially different light, architecture-first composition.'),
('botanical-calm','Botanical Calm','03-botanical-calm',
 'A daylight garden mood with soft image windows, green surfaces and an orderly menu grid; organic accents remain secondary to content.',
 '#FAF8F1 / #173E32 / #B8C7AE / #D9B998','DM Serif Display / DM Sans',
 [('GardenHero','Two-column introduction with a softly arched or rounded venue image, seasonal drink detail and Menu/Visit actions.'),('SeasonalDrinks','A stable grid for coffee and matcha with readable taste tags and prices; do not imply health benefits.'),('BrunchPairings','Pair two real food items with drinks using large images and compact explanatory copy.'),('GardenStory','One image and a concise account of the space; any sustainability claim requires supplied evidence.'),('CalmGallery','A rhythm of wide seating views and botanical details, with captions rather than overlay text.'),('AccessAndVisit','Hours, address, access details and contact in a high-contrast panel.'),('BotanicalFooter','Deep green with cream text and a restrained original botanical line illustration.')],
 [('Seasonal still life','Matcha bowl or latte render with soft daylight, separate from actual menu photographs.'),('Garden photography','Real foliage, seating, exterior and step-free access when applicable.'),('Botanical ornament','One original SVG line drawing; mark decorative art as hidden from assistive technology.')],
 'Use 350–500ms soft reveals and at most one subtle decorative leaf drift. Do not move foliage over text. Reduced motion removes drift and reveals; native scroll throughout.',
 ['Green-on-green combinations pass measured contrast in every control state.','Rounded photo masks do not hide important venue details.','Decorative leaves do not intercept pointer events or create overflow.'],
 'Implement after the first two to establish organic image framing and seasonal content without introducing a new rendering engine.'),
('playful-retro','Playful Retro','04-playful-retro',
 'A graphic poster composition with oversized display type, offset cutouts, outlined cards and a limited sticker vocabulary; strong order beneath the playful surface.',
 '#FFF1D8 / #432E36 / #C7472F / #A6C6DA','Rounded display candidate / plain readable sans-serif',
 [('PosterHero','Bold headline, one hero drink cutout and at most two decorative stickers; keep action labels conventional.'),('SeasonalSpotlight','One high-contrast seasonal feature with availability and real price, not an endlessly moving banner.'),('OutlinedBestsellers','Four strong bordered cards with consistent product scale and orderly text.'),('PairingBoard','Food/drink pairings on a structured grid with restrained alternating backgrounds.'),('CommunityBoard','Real event cards or a clearly labeled sample-content block; hide if there is no relevant content.'),('VisitCard','A large legible address/hours block and unmistakable directions action.'),('PosterFooter','Bold color block with large Menu/Visit links and smaller utilities.')],
 [('Product cutouts','Consistent light direction and clean transparent edges for drinks and pastry.'),('Brand stickers','Three original vector motifs maximum, plus a simple custom wordmark placeholder.'),('Social photographs','Permission-cleared people and genuine venue activity for launch.')],
 'Allow one short sticker pop and 150–220ms control responses. Optional light spring on art only. Avoid drag-only controls, bouncing prices and moving navigation targets.',
 ['Rotated stickers stay inside the viewport at 320px.','Bold composition still has an obvious first heading and primary action.','Graphic background patterns do not reduce menu legibility.'],
 'Build once the restrained designs work; use it to verify that the shell does not force every homepage into identical sections and geometry.'),
('dark-cinematic-3d','Dark Cinematic 3D','05-dark-cinematic-3d',
 'A dark product stage with directional light, strong type and one short coffee-ritual scene, followed by calm practical menu and visit surfaces.',
 '#151311 / #EEE5D7 / #B97848 / #797C62','Editorial serif candidate / Manrope',
 [('CinematicHero','HTML title and actions over or alongside a matching poster; mount the optional cup canvas in a reserved frame without blocking interactions.'),('EssentialVisitRow','Immediately accessible address, hours and menu path outside the canvas.'),('SignatureDrinks','Readable product grid; use a calmer lighter surface if needed to balance the dark opening.'),('BrewSequence','Optional three-stage beans/brew/cup narrative with text in normal document flow and an enhanced short desktop timeline.'),('VenueReality','Real venue photos and concise copy connect the stylized scene to the actual experience.'),('GroundedVisit','Static high-contrast contact, hours and directions.'),('CinematicFooter','Quiet dark footer with stable links; no moving particles near utilities.')],
 [('Hero GLB','Complete cup and saucer, clean normals, controlled camera limits and compact textures. Include source and provenance.'),('Matching poster','Desktop/mobile stills from the same camera and lighting as the live scene.'),('Environment','A licensed compact lighting environment or baked lighting; no unnecessary large HDRI transfer.'),('Venue photographs','Real room and exterior images for trust and grounding.')],
 'Start with the static poster. Prototype one optional cup turn; introduce a scroll timeline only if justified. Keep one render loop, stop offscreen, handle context loss and dispose scene resources on route exit. Reduced motion always gets the poster.',
 ['Menu and directions work before the 3D runtime loads and after a failed GLB fetch.','Rapid route switching releases canvases, listeners and renderer resources.','The poster stays until the first correct frame is ready without layout shift.','A narrow phone gets all brewing stages without pinning or horizontal scrolling.'],
 'Build the static version alongside other pages; integrate live 3D last, after a device-tested proof of concept passes its fallback and loading checks.'),
('heritage-classic','Heritage Classic','06-heritage-classic',
 'A centered masthead and balanced editorial frame, classical serif type, real architectural photography and restrained ornamental rules.',
 '#F4EBDD / #39271F / #722F37 / #B39360','Cormorant Garamond / contemporary readable sans-serif',
 [('MastheadHero','Centered identity, short invitation, framed venue photograph and clear Menu/Visit actions. Do not fabricate a founding date.'),('SpecialtySalon','A balanced three-card composition for pastry, coffee and the café experience.'),('HistoryFeature','Use supplied verifiable history with licensed archival imagery; otherwise use a present-day craft story.'),('ClassicMenu','Clearly grouped menu rows with consistent price alignment and generous line spacing.'),('RoomsGallery','A measured gallery of actual rooms and service details.'),('VisitOrReserve','Show a real booking link only if operational; otherwise directions and contact remain primary.'),('HeritageFooter','Burgundy or espresso surface, cream text and understated utility row.')],
 [('Venue portrait','A real façade or salon photograph with architectural detail.'),('Service still life','Porcelain espresso set or pastry image with consistent warm lighting.'),('Ornaments','Original thin vector borders; no copied historic crest.'),('Archive optional','Only documented photographs with permission and accurate captions.')],
 'Use 200–350ms fades and restrained image reveals. Keep masthead and menu stable. Avoid page-turn gimmicks, autoplay slideshows and large animated ornamentation.',
 ['Serif headings remain readable at mobile sizes and zoom.','Ornamental borders never function as the only grouping signal.','Gold accents are decorative unless a specific foreground pair passes contrast.'],
 'Implement after the minimal layout; reuse data and utility behavior while preserving the distinctive centered framing and typographic rhythm.'),
('bakery-brunch','Bakery & Brunch','07-bakery-brunch',
 'Food-first imagery, warm type and large category blocks make breakfast and pastry immediately tangible while emphasizing availability and visit information.',
 '#FFF8EB / #3E2920 / #A94F31 / #DABF8C','DM Serif Display / Manrope',
 [('FoodHero','Large appetizing photograph with title and Menu/Visit actions on a readable panel; do not place thin type over busy pastry textures.'),('DailySpecialties','A clear list/grid of confirmed specialties and availability; sample items must be identified as demo content.'),('BrunchAndDrinks','Food and drink categories with prices, portion or size details where supplied and a clear category selector.'),('BakingStory','Real baking-process image and concise explanation of the kitchen or ingredients.'),('PickupInformation','Include pickup instructions only when real; no simulated successful orders or inert preorder form.'),('BakeryVisit','Hours, address, contact and any actual pickup/access details.'),('BakeryFooter','Warm surface with practical links and optional real preorder link.')],
 [('Hero food image','Actual hero dish/pastry, landscape and portrait crops with natural color.'),('Menu food set','Consistent photographed portions; no misleading oversized generated dishes.'),('Baking process','Permission-cleared hands/process and an honest kitchen detail.'),('Optional render','A stylized croissant/espresso still life used as brand art, not a substitute for accurate menu imagery.')],
 'Use short card fades and small image zoom on hover where supported. Keep daily offerings static and accessible. Do not rotate products automatically or animate availability messages.',
 ['Food images keep useful crops without implying inaccurate portions.','Category changes preserve focus and visible headings.','Pickup language never promises an order flow that does not exist.'],
 'Implement after the shared menu data model is stable; use this page to validate food-heavy content, dietary labels and operational copy.'),
('industrial-coffee-lab','Industrial Coffee Lab',None,
 'A technical coffee-studio identity: exposed grid, bold sans-serif, monospace labels and steel-gray surfaces balanced by human venue photography.',
 '#E8E6E0 / #202322 / #A83220 / #B7BCB8','Bold grotesk sans-serif candidate / monospace labels',
 [('LabHero','An offset grid with a large typographic statement, equipment or cup photograph and a compact process label. Primary actions remain plain Menu/Visit.'),('ServiceStatus','A labeled essentials grid for hours and address. Avoid fake live counters or invented telemetry.'),('TasteMatrix','A readable set of drinks with short flavor descriptions and prices; technical details are optional and accurate.'),('ProcessLedger','Three compact stages explaining grind, extraction and service; no unsupported precision claims.'),('EquipmentAndSpace','Documentary photography of equipment and people, not a wall of spec jargon.'),('LabVisit','Strong address/hours block and accessible directions link.'),('UtilityFooter','Steel or ink surface, clear grid lines and a compact utility index.')],
 [('Equipment photograph','Permission-cleared espresso machine or grinder with uncluttered background.'),('Technical diagrams','Original SVG process marks; include text explanations for meaningful information.'),('Cup art','Optional clay or brushed-metal product still; no full interactive laboratory environment.'),('Human venue shot','Real people/space to keep the identity approachable.')],
 'Use short linear or ease-out transitions and one optional SVG line-draw for the process diagram. No scrambling menu text, flashing indicators or animated fake data.',
 ['Monospace labels remain readable and secondary to product names.','Grid lines do not create accidental table semantics for layout.','Technical styling remains welcoming and does not obscure menu or address.'],
 'Implement as the eighth distinct composition after the common content rules are proven; keep it lighter than the cinematic route.'),
]

for slug,name,research,concept,palette,fonts,sections,assets,motion,checks,order in DESIGNS:
    folder=ROOT/'designs'/slug/'docs'; folder.mkdir(parents=True,exist_ok=True)
    reference=f'[Research brief](../../../research/design-directions/{research}/design-brief.md)' if research else '[Design-specific research and brief](research-and-brief.md)'
    rows='\n'.join(f'| {i+1} | `{component}` | {task} |' for i,(component,task) in enumerate(sections))
    checklist='\n'.join(f'- [ ] {x}' for x in checks)
    assetlist='\n'.join(f'- **{title}:** {description}' for title,description in assets)
    text=f'''# {name} — detailed implementation plan

Status: planned, not implemented · 5 November 2026

## 1. Shared foundation and design-gallery contract

Use the common application shell, shared café content contract, gallery routing and persistent “Change design” control defined in [the shared implementation plan](../../../docs/shared-implementation-plan.md). Keep this design’s layout, style tokens, sections, assets and motion in its own folder. This first milestone and the final completion gate are identical across all eight plans.

Deliverable: a direct `/designs/{slug}/` entry, a gallery card, a validated registry record and a page that can return to `/designs/` without reloading the application unnecessarily. Essential content and navigation must work before optional motion loads.

## 2. Design objective and scope

{concept}

Build a complete responsive homepage containing navigation, meaningful product/menu content, story/space content, visit information and footer. Every visible control must have an implemented behavior or a valid destination. Additional commerce, authentication, payment, reservations backend and newsletter services are outside this initial homepage scope.

{reference} supplies the creative context. Keep the same fictional café identity and common sample menu across variants so clients compare design rather than different businesses. Clearly label the shared sample data as a demo. Replace it with verified business content before a real launch.

## 3. Folder ownership and deliverables

Target folder: `designs/{slug}/`. Its existing `docs/` is the handoff. During implementation add a route entry, `components/`, `styles/`, `assets/` and optional `motion/` or `scene/` modules. Exact extensions depend on the framework decision in the shared plan.

- Route entry composes this design's sections in its own order; do not reduce the page to a shared hero with a new palette.
- `styles/` owns locally scoped tokens, layout, responsive rules and interaction states.
- `assets/` holds acquired images and original art; attach provenance entries in [the asset checklist](asset-checklist.md).
- `components/` owns the sections below; reuse accessible low-level controls without forcing a common visual layout.
- `docs/verification.md` will hold real implementation screenshots, checks and unresolved issues. Do not prefill passing results.

## 4. Visual tokens and responsive rules

Candidate palette: **{palette}**. Candidate typography: **{fonts}**. Confirm font availability and exact licensing during asset acquisition. Use semantic names such as surface, ink, action, muted and border; test foreground/background pairs instead of assuming the palette is accessible.

Create type, spacing, radius, border, shadow and container tokens before detailed styling. Establish mobile, medium and wide compositions using content-driven breakpoints. Inspect at 320, 390, 768, 1024 and 1440 CSS pixels; these are test widths, not a requirement to create five breakpoints. Use fluid type within safe readable bounds. Keep body text at least 16px as a project target and avoid long all-cap paragraphs.

Plan a normal-flow fallback for every overlapping composition. Reserve dimensions for images. On phones show the primary action early, stack text before supporting media when appropriate and use no horizontal page overflow. At 200% zoom, preserve the menu, directions and gallery-return control.

## 5. Homepage section implementation

Build semantic structure and real-text content first, then imagery and styling, then motion. Treat each row as a separately reviewable task.

| Order | Section component | Implementation detail |
|---|---|---|
{rows}

Completion evidence: full-page desktop and mobile captures showing the entire sequence, including footer. A polished hero alone does not complete this design.

## 6. Navigation and visitor interactions

- Build this design's header with links to actual sections. The main Menu action scrolls to a readable menu preview/full menu section within the homepage scope.
- Apply header-offset anchor positioning and expose a skip link. Preserve useful browser Back/Forward behavior.
- Mobile navigation uses a labeled toggle with expanded state. If modal, trap focus appropriately, close on Escape and restore focus; if inline, keep normal document focus behavior.
- Use the shared fixed “Change design” control with a style-safe high-contrast surface. It opens the gallery, sets focus to its heading and preserves which design was selected.
- Gallery or menu controls must work with keyboard and touch. No information is hover-only. Provide visible focus and accurate selected/expanded states.
- Phone/email links work only with supplied demo/real values; do not invent a live business destination. An unconfigured directions action must explain the demo state rather than sending users to a random address.

## 7. Content and asset production

{assetlist}

For each asset record creator, item URL or source, rights, download/creation date, intended section, alt text, crop and exported sizes. Produce mobile and desktop variants only where cropping requires them. Prefer modern image formats with a reliable fallback where needed. Do not bake headlines, prices or actionable labels into raster images.

Before implementation, check that the selected content can fit both the largest and smallest layouts. Use long product names and multi-line addresses in layout checks. Never publish fabricated reviews, awards, history or sourcing claims.

## 8. Motion and transition implementation

{motion}

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

Sequencing note: {order}

## 12. Design-specific verification and risks

{checklist}
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
'''
    (folder/'implementation-plan.md').write_text(text,encoding='utf-8')
    (folder/'asset-checklist.md').write_text(f'''# {name} — asset checklist

Status: requirements only; nothing acquired by this plan.

{assetlist}

## Acquisition record template

| Asset ID | Section | Creator/source URL | Rights/license | Date acquired | Source filename | Export sizes/bytes | Alt text | Status |
|---|---|---|---|---|---|---|---|---|
| To assign | To assign | To collect | To verify | — | — | To measure | To write | Pending |

## Delivery checks

- [ ] Hero has a useful mobile crop and reserved aspect ratio.
- [ ] All meaningful image descriptions are supplied; purely decorative art is identified.
- [ ] Fonts include required license notices and a fallback stack.
- [ ] No copied competitor logos, screenshots or artwork are used as production assets.
- [ ] Sources, optimized exports and any 3D poster/model pairs are clearly distinguished.
- [ ] Sample gallery thumbnail is replaced by a capture of the implemented design.
''',encoding='utf-8')
    (folder/'motion-spec.md').write_text(f'''# {name} — motion specification

Status: proposed, not implemented.

{motion}

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
''',encoding='utf-8')

industrial=ROOT/'designs/industrial-coffee-lab/docs/research-and-brief.md'
industrial.write_text('''# Industrial Coffee Lab — eighth design brief

Added for the eight-design showcase on 5 November 2026. This direction is original synthesis; it has not undergone a new rendered competitor audit.

Steel-gray surfaces, exposed layout rules, a bold grotesk headline and small monospace labels form a technical coffee-studio identity. Pair equipment images with people and seating so the page stays inviting. The composition differs from Dark Cinematic: it is a bright documentary grid rather than a dark animated product stage.

## Existing collected references

- [doubleshot](https://www.doubleshot.cz/en): earlier text review found coffee, gear, courses and locations. Useful content reference; current visual styling is unverified.
- [Stumptown](https://www.stumptowncoffee.com/): earlier text review found learning, coffee descriptions and locations. Useful for approachable specialty-coffee language.
- [Onyx](https://onyxcoffeelab.com/): earlier text review found craft and flavor storytelling. The steel-grid treatment is our proposal, not an observed Onyx layout.
- [Shared libraries and asset sources](../../../research/03-libraries-and-assets.md): select ordinary images and original SVG diagrams first; a live 3D scene is not required.

Palette: gray `#E8E6E0`, ink `#202322`, rust `#A83220`, steel `#B7BCB8`. Test specific contrast pairs. No images or fonts have been acquired. Visual reference review, exact font selection and asset sourcing remain implementation prerequisites.
''',encoding='utf-8')
print('Created eight design docs folders, each with implementation plan, asset checklist and motion specification.')
