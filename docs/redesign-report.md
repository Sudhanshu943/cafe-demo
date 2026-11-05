# Eight-design visual revision

Updated 5 November 2026. Scope: the local showcase requested in the chat. Existing research and planning documents remain preserved.

## What changed

The first implementation reused too many complete menu, story, visit and footer sections. This revision replaces those page-level blocks with independent compositions. Each design now has its own `homepage.js`, `homepage.css` and exported menu renderer. Existing `index.js`/`styles.css` files are small route entries.

| Design | New composition | Menu treatment | Character |
|---|---|---|---|
| Warm Editorial | Journal masthead, coffee-table cover, three-column editorial story, invitation | Newspaper-style sidebar and large numbered listings | Paper, olive, expressive serif |
| Japanese Minimal | Lettermark, vertical labels, architecture, quiet philosophy, offset photo diptych | Essential horizontal text rows | White space, restrained sans-serif |
| Botanical Calm | Full green conservatory, central arch and supporting imagery, full-width statement | Photo-led pantry cards | Forest, soft green, rounded organic shapes |
| Playful Retro | Oversized poster, tilted iced-coffee photograph, burst stickers, colourful bands | Bordered colour-block product tiles | Lavender, acid yellow, orange, bold sans-serif |
| Dark Cinematic | Centered headline and central interactive cup stage, dark craft feature, typographic interlude | Circular product thumbnails and spacious offering rows | Ink, brass, cinematic serif |
| Heritage Classic | Burgundy salon, ornamental frame, three arched photographs, invitation letter | Cream printed menu card with dotted price leaders | Classical serif, burgundy, gold accents |
| Bakery & Brunch | Full-bleed pastry photograph, morning counter, layered kitchen imagery, pairing spread | Image-and-description counter listings | Food-led, warm cream, terracotta |
| Industrial Coffee Lab | Technical masthead, large sans-serif statement, monochrome equipment, process diagram | Reference/profile/format/price specification grid | Steel, black, signal orange, monospace labels |

The shared code now provides data, small navigation/filter controls and interaction utilities, rather than dictating every homepage's section layout. The filter dispatcher calls the current design's renderer, so selecting a category preserves its unique menu presentation.

## Gallery

Default desktop view shows four columns and two rows for easier comparison. “Larger previews” switches to the original two-column presentation. The gallery has refreshed actual homepage captures and descriptions of the compositional differences. Mobile uses a compact two-column overview; larger previews remain available.

## Checks performed

- The existing ten automated routing, content and asset checks pass.
- All eight revised pages passed document overflow, heading-bound and loaded-image checks at 320, 390, 768 and 1024 pixels; desktop checks also passed at 1440 pixels.
- Matcha category rendering produced three items on all eight desktop pages.
- At mobile width, each gallery card opened its route, each navigation panel expanded, Escape was exercised, each kitchen filter produced three items and Change design returned to the gallery.
- Gallery layout controls were exercised; the large desktop view uses two columns and the overview uses four.
- The revised central 3D cup loaded, accepted ArrowRight input, and released its canvas and route stylesheet on gallery return.
- The visit dialog opened and dismissed with Escape.
- The final build completed successfully. The local preview server was restarted in a separate hidden background process after the earlier development session ended.

Evidence: [responsive results](screenshots/revision-2/responsive-results.json), [mobile journeys](screenshots/revision-2/journey-results.json). Gallery thumbnails in `assets/previews/` are the current captures. Earlier screenshot files belong to the first iteration; this revision uses viewport captures rather than claiming a new full-page audit.

This remains a fictional café demo with illustrative imagery, sample prices and no ordering or booking backend. Production field performance, a comprehensive accessibility audit and cross-browser/physical-device testing remain outside the completed visual comparison checks.
