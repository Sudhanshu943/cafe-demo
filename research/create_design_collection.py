"""Generate original research boards and direction dossiers; not website code."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent / 'design-directions'
DIRECTIONS = [
 dict(slug='01-warm-editorial', name='Warm Editorial', tagline='A little warmth. A better daily ritual.', colors=['#F6F0E6','#241A16','#24483C','#C58A52'], type='Fraunces + Manrope', fit='Neighborhood cafés and premium everyday coffee', layout='Asymmetric split hero: expressive headline left, large ceramic cup right. Alternate generous image-and-text stories with clean product cards.', nav='Small wordmark, Menu / Story / Visit, forest View Menu button.', sections='Hero → address and hours strip → signature drinks → craft story → space gallery → visit details.', footer='Deep forest, cream text, three clear columns for Explore, Visit and Contact.', imagery='Ivory ceramics, warm window light, oak tables and real venue photos.', asset='A softly lit cup-and-saucer render with a subtle handmade rim; croissant still life as support.', motion='A short settling cup entrance, once-only section fades and restrained image lift. Native scroll.', risk='Can become generic if it relies on beige stock photography. Give the brand its own typography, copy and cup shape.', refs=[('La Cabra','https://lacabra.com/','Reviewed page content connects coffee, bakery, ceramics and locations; a useful editorial content reference.'),('Onyx','https://onyxcoffeelab.com/','Featured coffees and flavor-led storytelling; useful for product descriptions.')], query='warm editorial coffee website ceramic cream'),
 dict(slug='02-japanese-minimal', name='Japanese Minimal', tagline='Coffee, space, quiet.', colors=['#FAFAF7','#20231F','#9CADA2','#D9D6CE'], type='DM Sans with a restrained serif accent', fit='Architecture-led specialty cafés and compact premium coffee bars', layout='Large whitespace, a small headline and one dominant architectural photo. Precise grid, thin rules and very few decorative shapes.', nav='Compact wordmark, Menu / Locations / About, simple text Directions action.', sections='Venue hero → essential visit details → concise menu → coffee philosophy → architectural gallery → location.', footer='Light background with thin dividing lines; address and opening hours receive equal weight to brand links.', imagery='Natural stone, stainless steel, pale wood and honest uncluttered interiors.', asset='A sculptural unbranded porcelain cup as a static render; real venue architecture remains the hero.', motion='Small opacity changes and subtle image reveals; little or no parallax. Optional model rotation only on request.', risk='Tiny typography and excessive whitespace can hide useful information. Keep body copy and prices readable.', refs=[('% Arabica US','https://arabicacoffeeus.com/','Brand and location entry points reviewed in the earlier research; use for venue discovery, not as proof of an audited visual layout.'),('% Arabica locations','https://arabicacoffeeus.com/pages/locations','Reviewed addresses, hours and directions per venue.'),('La Cabra','https://lacabra.com/','Reference for coffee and physical-space storytelling.')], query='Japanese minimalist cafe website architecture whitespace'),
 dict(slug='03-botanical-calm', name='Botanical Calm', tagline='Slow mornings. Fresh perspectives.', colors=['#FAF8F1','#173E32','#B8C7AE','#D9B998'], type='DM Serif Display + DM Sans', fit='Garden cafés, matcha bars and relaxed brunch venues', layout='Rounded image windows, calm green surfaces and a spacious two-column hero. Organic accents support a structured readable grid.', nav='Quiet horizontal navigation, Menu / Space / Visit, dark-green Visit Us action.', sections='Daylight hero → seasonal drinks → brunch pairings → garden/space story → gallery → visit and access.', footer='Deep green with practical opening hours; a small botanical line drawing can add character.', imagery='Plants, matcha, pale plaster and soft daylight; avoid green overlays that distort food color.', asset='A matte matcha bowl and whisk still life or a cream cup with a leaf-shaped shadow.', motion='Slow image fades and tiny decorative leaf movement if desired; static equivalent for reduced motion.', risk='Avoid unsupported wellness or sustainability claims. Green-on-green text can lose contrast.', refs=[('Blank Street','https://www.blankstreet.com/en-GB','Reviewed seasonal matcha and latte content, locations and menu links; supports seasonal drink hierarchy.'),('Pexels interior reference','https://www.pexels.com/photo/coffee-shop-interior-12097683/','Specific wood-and-plants interior discovery item; not downloaded.'),('Poly Haven','https://polyhaven.com/license','Reviewed CC0 license for potential material and lighting assets.')], query='botanical matcha cafe website sage green'),
 dict(slug='04-playful-retro', name='Playful Retro', tagline='Good coffee. Great company.', colors=['#FFF1D8','#432E36','#C7472F','#A6C6DA'], type='A bold rounded display face + a plain readable sans-serif', fit='Youthful social cafés, dessert bars and a distinctive casual brand', layout='Oversized poster-style title, offset product cutouts, bold outlined cards and occasional checker or stamp motifs. Keep the menu grid orderly.', nav='Large obvious labels with a pill-shaped menu action; optional sticker-style brand badge.', sections='Poster hero → seasonal special → bestsellers → food and coffee pairings → community events → visit.', footer='High-contrast color block with large Menu and Directions links and a compact utility row.', imagery='Flash-lit drink cutouts, playful packaging and real social moments with permission.', asset='A rounded stylized cup, pastry character or colorful iced-drink render. Use one consistent illustration style.', motion='A gentle sticker pop, small spring response and optional draggable decoration with a non-drag equivalent. No moving price ticker.', risk='Too many stickers and bouncy elements make the site feel chaotic. Reserve bright accents for hierarchy.', refs=[('CHILL-OUT Café project','https://www.brandingwebsite.com/projects/chill-out-cafe','Project listing explicitly describes colorful, retro, creative branding and attributes Sofiia Oswald; branding inspiration, not a proven live website.'),('Original CHILL-OUT project','https://www.behance.net/gallery/206047163/CHILL-OUT-Caf','Original creator project linked by the listing; queued for direct visual review.'),('Grind','https://grind.co.uk/','Reviewed seasonal shopping and visit entry points; reference for separating commerce and café actions.')], query='retro playful cafe website bold typography stickers'),
 dict(slug='05-dark-cinematic-3d', name='Dark Cinematic 3D', tagline='Experience the craft.', colors=['#151311','#EEE5D7','#B97848','#797C62'], type='A strong editorial serif + Manrope', fit='Experimental specialty coffee, premium roastery and evening café', layout='Dark stage, dramatic cup lighting, large elegant headline and one clear action. Follow the hero with a light or calmer readable menu surface.', nav='Opaque dark header, Menu / Craft / Visit, light high-contrast primary action.', sections='Cup hero → visit essentials → signature drinks → optional short brewing scene → venue photography → visit.', footer='Quiet ink surface with generous spacing; no cinematic effects around contact information.', imagery='Directional studio light, warm copper reflections and authentic macro coffee photography.', asset='One optimized GLB cup with baked lighting and matching poster; beans can be instanced as small accents.', motion='One coordinated cup turn or short beans-to-cup story. GSAP only if needed; Three.js/Fiber for the scene. Stop offscreen and provide a poster fallback.', risk='Highest performance and motion risk. Do not put menu text in canvas or make scrolling depend on the 3D sequence.', refs=[('Onyx','https://onyxcoffeelab.com/','Reviewed craft and product storytelling; the proposed dark visual treatment is our concept, not an observed site claim.'),('Three.js','https://threejs.org/docs/','Official scene and animation API reference.'),('React Three Fiber performance','https://r3f.docs.pmnd.rs/advanced/scaling-performance','Official performance techniques including on-demand rendering.'),('ScrollTrigger','https://gsap.com/docs/v3/Plugins/ScrollTrigger/','Official scroll-sequence documentation.')], query='cinematic dark coffee website 3D cup'),
 dict(slug='06-heritage-classic', name='Heritage Classic', tagline='Tradition, served daily.', colors=['#F4EBDD','#39271F','#722F37','#B39360'], type='Cormorant Garamond + a readable contemporary sans-serif', fit='Historic cafés, patisseries and an elegant sit-down experience', layout='Centered masthead, framed photography, thin ornamental rules and a symmetrical opening. Editorial two-column sections for history and specialties.', nav='Masthead above a clear Menu / Our Story / Visit row; Reserve only if supported.', sections='Venue or pastry hero → specialty highlights → real history → menu → rooms and experience → reservations/visit.', footer='Burgundy or espresso with cream text, full address, hours and understated utility links.', imagery='Real architecture, pastry detail, polished wood, ceramic service and archival material with rights.', asset='A porcelain espresso set rendered like a still-life photograph; decorative border as original SVG.', motion='Slow crossfades, modest image reveal and minimal navigation transitions. Normal document scroll.', risk='Do not invent a founding date or imply a heritage the café does not have. Gold often fails as small text.', refs=[('Caffè Gilli','https://www.caffegilli.com/','Live-brand reference queued; access returned 403, so no current layout or animation claim is made.'),('La Cabra Chueca story','https://lacabra.com/','Reviewed text connects a venue to the character and history of its building; useful for place-based storytelling.'),('Café concept case study','https://www.behance.net/gallery/184886901/Cafe-Website-Concept-UXUI-Design-Case-Study','Attributed to Anastasiia Partuta, published 2023; concept reference, not evidence of current live behavior.')], query='heritage patisserie cafe website elegant serif'),
 dict(slug='07-bakery-brunch', name='Bakery & Brunch', tagline='Fresh from the oven. Ready for your morning.', colors=['#FFF8EB','#3E2920','#A94F31','#DABF8C'], type='DM Serif Display + Manrope', fit='Food-led cafés, artisan bakeries and weekend brunch destinations', layout='Appetizing edge-to-edge food photo, short headline and prominent menu/preorder links. Large image-led food categories followed by readable prices.', nav='Menu / Bakery / Visit with Preorder only when available; make pickup information obvious.', sections='Food hero → today’s specialties → drinks and brunch → baking story → preorder/pickup details → venue and hours.', footer='Warm cream or espresso, clear pickup information, contact and real operating hours.', imagery='Fresh pastry texture, real portions, natural daylight and a warm human baking process.', asset='Croissant-and-espresso still life; prefer real food photos for menu accuracy. A stylized pastry render may support the brand.', motion='Simple card reveals and understated photo zoom on hover. Avoid perpetual steam or rotating food carousels.', risk='Beautiful food imagery cannot substitute for availability, prices or pickup instructions. Avoid unrealistic rendered food portions.', refs=[('Mother Dough','https://www.motherdough.com.sg/','Reviewed preorder, contact and operating-hours content; useful operational reference for a bakery.'),('La Cabra','https://lacabra.com/','Reviewed bakery and coffee storytelling.'),('Webflow café showcase','https://webflow.com/made-in-webflow/cafe','Reviewed community listing includes bakery/café examples; templates and clone rights require individual checks.')], query='artisan bakery brunch cafe website pastry editorial'),
]

for i,d in enumerate(DIRECTIONS):
    folder=ROOT/d['slug']; folder.mkdir(parents=True, exist_ok=True)
    c=d['colors']
    brief=f'''# {d['name']}

Research direction {i+1} of 7 · 5 November 2026 · Proposed concept, not an approved design.

![Original direction board](direction-board.svg)

## Best fit and overall impression

{d['fit']}. Suggested headline tone: “{d['tagline']}”

{d['layout']}

## Visual system

- Proposed palette: {', '.join('`'+x+'`' for x in c)}. Base, text, action/accent and supporting color respectively; test actual contrast before use.
- Typography direction: {d['type']}. Font choices are candidates; exact files and licenses remain to check.
- Photography: {d['imagery']}
- 3D or illustration: {d['asset']}

## Navigation, sections and footer

**Navigation:** {d['nav']}

**Section rhythm:** {d['sections']}

**Footer:** {d['footer']}

On mobile, stack the hero, retain a visible menu path, keep directions easy to reach and preserve readable prices. The design should still communicate its character without animation.

## Motion and scrolling

{d['motion']}

Use reduced-motion alternatives and leave practical content outside canvas. See [shared effects research](../../02-motion-and-3d.md) for timings, performance targets and fallback details.

## What makes this different

This direction changes composition, imagery, typography and motion as well as color. Its primary differentiator is the layout and atmosphere described above; do not present it as merely a recolored version of another option.

## Risks and improvements

{d['risk']}

Keep real menu prices, address, hours and the primary visitor action accessible. Never invent reviews or business claims. Check performance with a static hero first, then add only justified effects.

## Client discussion

Show the visual board and two linked references. Explain the atmosphere, the hero concept, the practical menu/visit flow and the motion level. Ask whether it matches the real venue and audience before expanding it into a full mockup.

## Evidence boundaries

The board is original schematic artwork with placeholder shapes, not a screenshot, final mockup, generated photo or live website. Source notes distinguish reviewed content from unverified visual inspiration. No third-party assets are copied into this folder.
'''
    (folder/'design-brief.md').write_text(brief,encoding='utf-8')
    refs='# Reference resources — '+d['name']+'\n\nAccess date: 5 November 2026. Page text/search review unless marked otherwise. Visual behavior has not been audited.\n\n'
    for title,url,note in d['refs']: refs+=f'## [{title}]({url})\n\n{note}\n\n'
    refs+=f'''## Additional discovery paths

- [Dribbble café website gallery](https://dribbble.com/tags/cafe-website): compare composition and hierarchy; many entries are concepts rather than shipped websites.
- [Behance café website projects](https://www.behance.net/search/projects/cafe%20website%20design?locale=en_US): inspect full case studies and mobile views, not only hero shots.
- [Webflow café showcase](https://webflow.com/made-in-webflow/cafe): open individual demos for later interaction review; a listing does not imply permission to copy assets.

Suggested search phrase: **{d['query']}**.

## Asset acquisition brief

{d['asset']}

Use original commissions, owner-provided photography or individually licensed assets. [Pexels](https://www.pexels.com/search/cafe%20interior/), [Unsplash](https://unsplash.com/s/photos/coffee-shop-interior) and [Poly Haven](https://polyhaven.com/) are discovery sources. Record creator, item URL, license and download date for each selected item. Nothing has been downloaded here.

## Relevant shared resources

[Library and asset comparison](../../03-libraries-and-assets.md) · [Source register](../../04-sources.md) · [All directions](../README.md)
'''
    (folder/'resources.md').write_text(refs,encoding='utf-8')
    # Original, deliberately schematic layout board; no copied brand artwork.
    serif='Georgia' if i!=1 else 'Arial'
    bg,ink,accent,support=c
    art=f'<circle cx="805" cy="290" r="125" fill="{support}"/><ellipse cx="805" cy="370" rx="105" ry="18" fill="{ink}" opacity=".12"/><path d="M730 235h135v74q0 58-67 58t-68-58z" fill="{bg}" stroke="{ink}" stroke-width="3"/><ellipse cx="798" cy="235" rx="68" ry="17" fill="{ink}"/><path d="M867 250q60 0 25 55h-25" fill="none" stroke="{bg}" stroke-width="12"/>'
    if i in [1,5]: art=f'<rect x="685" y="165" width="245" height="255" rx="{120 if i==5 else 0}" fill="{support}"/><path d="M710 410V240h70v170m25 0V210h95v200" fill="none" stroke="{ink}" stroke-width="3"/><text x="730" y="455" fill="{ink}" font-size="14">VENUE PHOTO AREA</text>'
    if i==6: art=f'<rect x="670" y="160" width="300" height="280" rx="12" fill="{support}"/><ellipse cx="820" cy="335" rx="110" ry="45" fill="{bg}"/><path d="M730 315q20-110 70-20q25-100 65 0q45-60 55 25q-105 65-190-5" fill="{accent}"/><text x="722" y="470" fill="{ink}" font-size="14">FOOD PHOTOGRAPHY AREA</text>'
    cards=''.join(f'<rect x="{65+j*330}" y="575" width="310" height="115" rx="{20 if i in [2,3] else 2}" fill="{support}" opacity=".55"/><text x="{85+j*330}" y="615" font-size="18" fill="{ink}">{escape(label)}</text>' for j,label in enumerate(['Signature selection','Our space & story','Visit & opening hours']))
    swatches=''.join(f'<rect x="{65+j*235}" y="790" width="210" height="44" rx="4" fill="{color}" stroke="{ink}" stroke-width="1"/><text x="{65+j*235}" y="856" fill="{ink}" font-size="16">{color}</text>' for j,color in enumerate(c))
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="950" viewBox="0 0 1100 950"><rect width="1100" height="950" fill="{bg}"/><g font-family="Arial"><text x="65" y="65" fill="{ink}" font-size="24" font-weight="bold">{escape(d['name'].upper())}</text><text x="650" y="65" fill="{ink}" font-size="15">MENU     STORY     VISIT</text><line x1="65" y1="92" x2="1030" y2="92" stroke="{ink}" opacity=".25"/><text x="65" y="190" font-size="13" fill="{accent}">CAFÉ DESIGN DIRECTION / 0{i+1}</text><text x="65" y="270" fill="{ink}" font-family="{serif}" font-size="52">{escape(d['name'])}</text><text x="65" y="320" fill="{ink}" font-size="18">{escape(d['tagline'])}</text><rect x="65" y="365" width="165" height="48" rx="{24 if i==3 else 4}" fill="{accent}"/><text x="88" y="396" fill="{bg}" font-size="16">VIEW THE MENU</text>{art}<text x="65" y="530" fill="{ink}" font-size="18">PROPOSED SECTION RHYTHM</text>{cards}<text x="65" y="755" fill="{ink}" font-size="18">PALETTE EXPLORATION</text>{swatches}<text x="65" y="910" fill="{ink}" opacity=".7" font-size="14">Original schematic research board • Placeholder art • Not a final website mockup</text></g></svg>'''
    (folder/'direction-board.svg').write_text(svg,encoding='utf-8')

index='''# Seven café website design directions

Prepared 5 November 2026. These are separate creative options for a client discussion, not seven approved sites or finished mockups.

## Which design should we choose?

**Warm Editorial is the strongest starting recommendation for a broadly welcoming café.** It combines food appeal, craft and practical navigation without depending on heavy effects. **Japanese Minimal** is a strong alternative when the venue's architecture is the selling point. **Playful Retro** gives a social or dessert-focused café a more distinctive personality. **Dark Cinematic 3D** is the showcase option when the brand and performance budget support it; it is not automatically the best everyday experience.

There is no universally best café design. Brand fit, honest imagery and easy menu/visit tasks should decide. These judgments are design recommendations, not measured conversion results.

| Direction | Best match | Motion level | Relative production effort | Folder |
|---|---|---|---|---|
'''
for d,level,effort in zip(DIRECTIONS,['Low–medium','Low','Low','Medium','High','Low','Low–medium'],['Medium','Low–medium','Medium','Medium','High','Medium','Medium']):
    index+=f"| {d['name']} | {d['fit']} | {level} | {effort} | [Brief]({d['slug']}/design-brief.md) · [Resources]({d['slug']}/resources.md) · [Board]({d['slug']}/direction-board.svg) |\n"
index+='''
## Suggested client shortlist

Present Warm Editorial, Japanese Minimal and Playful Retro first: they create a meaningful contrast in atmosphere and composition. Swap in Bakery & Brunch for a food-led client, Botanical Calm for a garden/matcha venue, Heritage Classic for an established elegant café, or Dark Cinematic 3D for an experimental specialty brand.

Each folder includes a design brief, reference resource file and original SVG direction board. The boards convey palette and schematic layout only; they do not replace the future high-fidelity design work. The candidate typography, motion and content treatments are detailed in the briefs.

## Research coverage and readiness

The collection now covers enough distinct directions to begin a client style-selection conversation. It is not yet a production asset pack: no licensed photos or models have been acquired, no visual competitor audit has been completed, and brand-specific content is missing. Once a direction is chosen, collect a focused final asset set and validate the chosen motion on mobile before the implementation plan.

## Broader internet discovery resources

- [Dribbble café designs](https://dribbble.com/tags/cafe-website) — reviewed gallery listings, useful for comparing compositions; concepts are not evidence of usable shipped sites.
- [Behance café case studies](https://www.behance.net/search/projects/cafe%20website%20design?locale=en_US) — reviewed listings; inspect individual projects and attribution.
- [Webflow café examples](https://webflow.com/made-in-webflow/cafe) — reviewed community listing; individual demos and clone permissions still need checking.
- [Anastasiia Partuta café case study](https://www.behance.net/gallery/184886901/Cafe-Website-Concept-UXUI-Design-Case-Study) — creator concept published in 2023, not a current live-site audit.
- [CHILL-OUT branding listing](https://www.brandingwebsite.com/projects/chill-out-cafe) — reviewed listing describing colorful retro branding, linked to Sofiia Oswald's project. Use for identity inspiration, not as proof of web interaction behavior.

New live-brand page-content references reviewed: [Blank Street](https://www.blankstreet.com/en-GB), [Grind](https://grind.co.uk/), [Stumptown](https://www.stumptowncoffee.com/), [doubleshot](https://www.doubleshot.cz/en) and [Mother Dough](https://www.motherdough.com.sg/). Their content includes seasonal products, shopping, learning, locations or operational information. Visual colors, layouts and animation have not been verified through these text reads.

Access limitations: Caffè Gilli returned 403; Café Kitsuné timed out. Incorrect initial host variants for Grind and Gilli were replaced or marked inaccessible. No findings rely on the failed pages. Existing shared research retains the earlier Awwwards timeout note.

All reference artwork belongs to its creators. Links are stored locally; third-party media have not been copied. Suggested palettes and all SVG boards are original proposals. No build work has begun.
'''
(ROOT/'README.md').write_text(index,encoding='utf-8')
print(f'Created {len(DIRECTIONS)} direction folders with briefs, resources and original SVG boards in {ROOT}')
