# Café website design research

Date: 5 November 2026

## 1. Desired visitor experience

The site should make someone want to taste the coffee and visit the space, while helping them answer practical questions quickly: What can I order? How much does it cost? Where are you? Are you open? Can I reserve or order ahead?

The proposed balance is an expressive first impression followed by calm, readable information. A technically impressive scene has value when it communicates coffee, craft or atmosphere. Its value must eventually be tested through menu visits, directions clicks, bookings and orders rather than assumed from visual complexity.

Working assumption: a café with a physical venue, drinks and food. Location count, audience, brand and ordering capability are unconfirmed. Recommendations below are original design proposals unless explicitly identified as source observations.

## 2. Current reference sample

The following are live brands whose page content was reviewed. No visual screenshot audit or animation measurement was performed. Each proposed improvement is an opportunity for our project, not a verified defect in the referenced site.

| Reference | Observed content and structure | What to learn | Opportunity for our project |
|---|---|---|---|
| [Onyx Coffee Lab](https://onyxcoffeelab.com/) | Featured coffees, flavor descriptions, sourcing language and café-related storytelling | Give signature products a distinctive story | Pair craft storytelling with a short route to an in-café menu |
| [La Cabra](https://lacabra.com/) | Coffee, subscriptions, shop, learning and location navigation; bakery and venue stories | Connect coffee, ceramics and physical space | Use a smaller navigation hierarchy suitable for one café |
| [Blue Bottle](https://bluebottlecoffee.com/us/eng) | Seasonal offerings, product collections, subscriptions and a café finder | Connect seasonal products with a visit action | Keep one primary hero message and show local visit information early |
| [% Arabica US locations](https://arabicacoffeeus.com/pages/locations) | Address, daily hours and directions per venue | Make each location actionable | Include accessible text address and holiday-hours handling |
| [Third Wave Coffee](https://thirdwavecoffee.in/) | Bestsellers, flavor and roast descriptions, brewing guides, café links and coffee quiz | Give beginners useful product language | Offer concise taste tags alongside a clear drinks-and-food menu |

The sample contains several roaster and retail businesses, so its ecommerce emphasis should not automatically become our café's information architecture. Recurring content patterns are product highlights, seasonal storytelling, locations and coffee education. Visual trends such as exact palette, spacing, hover effects and cinematic scrolling are not established by text extraction.

## 3. Three visual directions to explore

| Direction | Palette proposals | Type direction | Imagery and personality | Suitability |
|---|---|---|---|---|
| Warm editorial — recommended | Cream `#F6F0E6`, espresso `#241A16`, forest `#24483C`, caramel `#C58A52`, paper `#E5D8C6` | Expressive serif headings with a clean sans-serif body | Matte ceramics, warm daylight, paper and wood | Welcoming neighborhood café with premium craft |
| Botanical modern | Ivory `#FAF8F1`, deep green `#173E32`, sage `#B8C7AE`, charcoal `#202622` | Quiet serif or restrained sans-serif headings | Plants, matcha, pale stone, soft shadows | Calm café or garden setting |
| Midnight coffee studio | Ink `#151311`, oat `#EEE5D7`, copper `#B97848`, muted olive `#797C62` | Oversized display serif with compact sans-serif labels | Dramatic cup lighting and close-up coffee textures | Experimental specialty coffee or evening venue |

These palettes are suggestions; combinations have not been contrast-tested. Use espresso on cream for primary copy and cream on forest for primary buttons, subject to measurement. Caramel is a decorative accent until its specific use passes contrast checks. Aim for approximately 70% base, 20% supporting surfaces and 10% accent as a compositional starting point, not a rigid rule.

Typography candidates: Fraunces + Manrope for warmth; DM Serif Display + DM Sans for an editorial style; Cormorant Garamond + Inter for a more delicate identity. Verify the selected font files and licenses before acquisition. Start with two families and a small weight set. [Google Fonts Knowledge](https://fonts.google.com/knowledge) is a typography learning resource; named families are candidates, not acquired assets.

Proposed scale: body 16–18px, line-height 1.5–1.7; hero heading fluid from roughly 44px to 96px; readable paragraph width around 60–70 characters. Keep menu descriptions and prices easier to scan than decorative headlines.

## 4. Navigation

Desktop: brand mark on the left; Menu, Our Story, Gallery and Visit links; one strong action on the right. Choose Order Online only if a real ordering flow exists; otherwise use View Menu or Get Directions. Add Reservations only if the business actually accepts them.

Use a compact sticky header with a solid or sufficiently opaque background after scrolling. It must preserve text contrast over imagery. Keep it visible and predictable; header auto-hiding is optional and needs usability testing. Add a skip link and ensure anchors land below the sticky header.

Mobile: logo, a visible Menu shortcut and an accessible menu button. The expanded panel should have clear labels, a close control, keyboard support and proper focus management. A bottom action bar can hold Menu and Directions if it does not cover content or device safe areas. Do not require hover or dragging to reach anything.

## 5. Proposed homepage section treatments

This is a design catalogue for later planning, not a commitment to include every section.

| Section | Appearance and content | Visitor action | Motion direction |
|---|---|---|---|
| Hero | Large short headline, a sentence describing the café, cup visual, two actions; city or neighborhood visible | View menu; visit | Cup settles into place; brief heading reveal; immediate usable buttons |
| Visit essentials | Calm strip with address, hours and contact | Directions or call | Static; no information ticker |
| Signature drinks | Three to four substantial cards with image, name, taste notes and real price | See full menu | Small image lift on hover; clear focus state |
| Full menu preview | Readable drinks and food categories, dietary markers and prices | Browse menu | Brief category change; preserve focus and section position |
| Craft / story | Editorial image and text; one meaningful claim about the café | Learn more | Gentle one-time reveal; optional limited photo parallax |
| Brewing story | Three short stages such as bean, brew and cup | Explore craft if interested | Optional desktop scroll scene with equivalent static stages |
| Space / gallery | Mixed close-ups and wide venue shots; captions explaining seating or atmosphere | View gallery | Restrained reveal; accessible lightbox if useful |
| Community / reviews | Genuine attributable testimonials or real events | Event details | Static cards by default |
| Visit | Address, weekly hours, holiday exceptions, access details, contact and directions link | Navigate to venue | Static information; map loaded on demand |
| Final invitation | Short welcoming message and the chosen primary action | Menu, directions or booking | Minimal motion |
| Footer | Structured practical information with a quieter brand expression | Contact and utility links | Color or underline feedback only |

Menu details: use actual HTML text rather than an image-only menu or PDF-only menu. Include size, currency, availability and dietary information where confirmed. Separate hot/cold variants clearly. A downloadable PDF can be supplementary. Avoid inventing allergy assurances; explain how customers can ask staff.

Gallery details: use real venue photography for the real café. Stock imagery may establish a demo's style but should not imply that an unrelated interior is the venue. Use consistent warmth and believable food styling rather than heavy filters.

Reviews: do not fabricate quotes, star ratings, review counts, awards, sourcing claims or sustainability claims. A demo can use clearly labeled placeholders until real material is supplied.

## 6. Footer design

Proposed desktop layout: brand and one-line invitation; Explore links; Visit with address and hours; Contact and social links. A thin lower row holds copyright and relevant privacy, accessibility and legal links. On mobile, stack the groups and keep Visit expanded. Use a deep espresso or forest surface with readable light text.

Make telephone and email links actionable. Include the street address as text even if a map exists. Repeat Menu and Directions. Add newsletter signup only when there is a working subscription service and a clear explanation of what subscribers receive. Avoid a large inert signup form or decorative links.

## 7. Improvements worth testing

1. Show menu and visit information without forcing users through storytelling.
2. Use one distinctive visual motif: a ceramic cup, a circular coffee ring, or a restrained hand-drawn bean shape.
3. Translate coffee jargon into short taste descriptions and strength or sweetness cues where accurate.
4. Present real food and space photography alongside stylized 3D so the experience feels trustworthy.
5. Show prices and opening hours in readable text; derive open/closed status from the venue timezone and exceptions only if reliable data exists.
6. Let visitors navigate normally while optional motion adds atmosphere.
7. Keep the most dramatic sequence brief and away from menu, contact and booking tasks.

These are hypotheses, not demonstrated conversion improvements. Later compare task completion and interaction metrics with a simpler version.

## 8. Accessibility, performance and discoverability

Use [WCAG 2.2](https://www.w3.org/WAI/WCAG22/quickref/) as the accessibility reference. Targets include 4.5:1 contrast for normal text and 3:1 for large text; applicable UI components also need adequate contrast. Prefer touch controls around 44px even though WCAG 2.2 AA's minimum target-size criterion is 24 CSS pixels with exceptions. Preserve visible focus, keyboard order, semantic headings, labeled forms, useful alt text and zoom support. Provide pause/stop/hide controls where WCAG requires them for moving content.

Respect [prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion): remove parallax, looping steam, camera movement and animated scroll. Provide a poster image. Content must stay visible when animation code fails.

[Core Web Vitals](https://web.dev/articles/vitals) good thresholds are LCP ≤2.5s, INP ≤200ms and CLS ≤0.1, evaluated at the 75th percentile. These are goals, not measured project results. Start with a visible optimized hero poster and defer 3D; lazy-load below-fold media, reserve image dimensions and postpone map embeds. See the motion catalogue for proposed asset budgets.

Publish crawlable menu and location information, descriptive titles and consistent business details. Consider accurate local-business structured data using the appropriate café subtype. [Google's documentation](https://developers.google.com/search/docs/appearance/structured-data/local-business) explains eligibility and properties; structured data does not guarantee a rich result or search ranking.

## 9. Research limits

No customer interviews, analytics, device testing, rendered competitor audit or measured performance comparison has occurred. No attraction or conversion claim is proven. The next design stage should visually review desktop and mobile references, test a small 3D proof of concept and select a direction using the real brand and content.
