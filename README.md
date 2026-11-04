# Morrow — eight café directions

One design gallery and eight independently composed responsive café homepages. Built with native JavaScript modules and scoped CSS; no framework installation is required. Three.js is vendored and loaded only after activating the cinematic design's 3D cup.

## Run locally

Requires Node.js. From this folder:

```sh
npm run dev
```

Open `http://127.0.0.1:4173/designs/`. The explicit gallery route always opens the collection. Root visits remember the last selected design when browser storage is available. Every design also has its own `/designs/<id>/` URL.

```sh
npm test
npm run build
```

The build produces `dist/`, including an HTML entry for each design route and the gallery. Deploy the contents as a static site; unknown routes should serve `404.html` or use the included SPA rewrite if supported. Never serve this source folder as a production public root because it includes research and development documents. The development server is bound to loopback.

## Project layout

- `design-gallery/`: neutral collection page and its own styling.
- `designs/`: eight source modules with independent compositions and styles, plus per-design `docs/`.
- `shared/`: content, routing, registry, accessible interaction helpers and base styles.
- `assets/`: locally stored stock photos, original screenshot previews, self-hosted fonts and on-demand Three.js runtime.
- `docs/`: shared plans, verification summary and screenshots.
- `research/`: original research and visual direction boards.

## Implemented interactions

Gallery selection, remembered design, explicit gallery return, browser history navigation, mobile menu with Escape behavior, keyboard/touch menu filters, image lightboxes on gallery sections, informative visit/about dialogs and an optional drag/arrow-key 3D cup. Motion respects reduced-motion CSS and the cinematic scene checks that preference before loading. Essential content stays outside canvas.

## Demo content and assets

Morrow is fictional. Prices, menu and opening hours are samples; there is no live venue, checkout or booking backend. The visit action explains this instead of providing invented contact details. Stock photography is illustrative. Asset source URLs are recorded in `assets/provenance.json`; font and Three.js licenses are retained alongside the files. The coffee-cup illustration is original CSS artwork, and the interactive cup uses original procedural geometry.

See [verification results](docs/verification-summary.md) for completed checks and remaining production-readiness limits. Original planning documents remain available in [the planning index](docs/README.md).
