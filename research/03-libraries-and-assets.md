# Libraries, tools and asset resources

Reviewed: 5 November 2026. Links point to official documentation or primary project repositories. Version numbers, package compatibility, subscriptions and export limits must be checked when implementation begins. No dependency has been installed or selected permanently.

## Motion and 3D shortlist

| Resource | Useful capability | Candidate use | Tradeoff / selection advice |
|---|---|---|---|
| [CSS / Web Animations via MDN](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API) | Native transitions and optional view transitions | Buttons, small fades, progressive page transitions | Use the simplest native option first; feature-detect view transitions |
| [Motion for React](https://motion.dev/docs/react) | Component, layout, gesture and scroll animation | Menu panel, cards and UI state changes | Good React UI option; paid extras are separate from core library choices |
| [GSAP ScrollTrigger](https://gsap.com/docs/v3/Plugins/ScrollTrigger/) | Timelines, scroll-linked sequences and pinning | One coffee storytelling scene | More coordination and cleanup; avoid duplicating Motion's ownership |
| [Lenis](https://github.com/darkroomengineering/lenis) | Smooth-scroll interpolation | Optional desktop polish | Native scroll is the baseline; integration needs testing |
| [Three.js](https://threejs.org/docs/) | General-purpose browser 3D | Custom cup, camera and materials | Most flexibility; requires 3D engineering |
| [React Three Fiber](https://github.com/pmndrs/react-three-fiber) | React renderer for Three.js | A React-based interactive hero | Check React/Fiber compatibility; not a replacement for Three.js concepts |
| [Drei](https://drei.docs.pmnd.rs/) | Helpers in the React Three ecosystem | Model loading, controls and scene helpers | Docs landing page returned no readable text; review needed for selected helpers |
| [Spline](https://docs.spline.design/) | Visual scene authoring and web publishing | Fast design exploration | Check export, hosting, branding and account requirements before committing |
| [model-viewer](https://modelviewer.dev/) | Display an interactive model and optional AR | A single cup or packaged product viewer | Simpler than a custom narrative scene; unnecessary if a still is enough |
| [Rive](https://rive.app/docs/getting-started/introduction) | Interactive authored animation and state changes | Small animated brand mark or character | Additional authoring workflow; optional rather than core |
| [glTF Transform](https://gltf-transform.dev/) | Inspect and optimize glTF assets | Asset conditioning before delivery | Compare quality and transfer size after optimization |
| [Draco](https://github.com/google/draco) | Geometry compression | Reduce mesh transfer size | Adds decoder work; benchmark end-to-end benefit |

Suggested alternatives, not a shopping list to install together:

- Simple expressive site: native CSS, selective Motion if React is used, static 3D renders.
- Recommended interactive exploration: Three.js with React Three Fiber and selected Drei helpers for one scene; Motion for ordinary React UI. Add ScrollTrigger only if the approved scene needs its timeline control.
- Designer-led exploration: Spline scene with a poster fallback, after checking export and runtime constraints.
- Product-viewer route: model-viewer when inspecting a model is the main interaction.

Do not choose React, a router, a CMS or a hosting service solely to use one effect. Framework and deployment choices belong in the later implementation plan.

## Licensing checkpoints

Primary project repositories expose their licenses: [Motion](https://github.com/motiondivision/motion), [Lenis](https://github.com/darkroomengineering/lenis), [React Three Fiber](https://github.com/pmndrs/react-three-fiber). Verify the exact acquired package license and preserve required notices. GSAP has its own [standard license](https://gsap.com/community/standard-license/); do not describe it as MIT or assume all redistribution scenarios are identical. Spline and Rive editor/export services may have separate commercial terms from runtime code. No price or unlimited-export claim is being made here.

## Photography and materials collection

| Resource | Direct collection / item | Why it is useful | Acquisition status |
|---|---|---|---|
| Unsplash | [Coffee-shop interiors](https://unsplash.com/s/photos/coffee-shop-interior) | Explore warm lighting, room composition and human scale | Link collection only; distinguish free items from Unsplash+ |
| Unsplash / Clifford | [Interior with hanging bulbs and table](https://unsplash.com/photos/cafe-interior-with-hanging-bulbs-and-table-VobvKmG-StA) | Specific reference for warm wood, pendant lighting and venue depth | Item page reviewed; not downloaded |
| Pexels | [Café interior collection](https://www.pexels.com/search/cafe%20interior/) | Photography and related motion footage discovery | Link collection only |
| Pexels / Augustinus Martinus Noppé | [Thai café with wood and plants](https://www.pexels.com/photo/coffee-shop-interior-12097683/) | Specific botanical and seating reference | Item page reviewed; not downloaded |
| Poly Haven | [Models, textures and HDRIs](https://polyhaven.com/) | Neutral lighting environments, wood and ceramic material resources | License page reviewed; individual assets still to select |

[Poly Haven's asset license](https://polyhaven.com/license) is CC0. Pexels permits free use and modification subject to its [restrictions](https://www.pexels.com/license/), including misleading endorsement. Review the relevant [Unsplash license](https://unsplash.com/license) and item tier before using an image; the license page's extracted text was incomplete. Real venue photos are preferred for launch. Competitor images remain references, not reusable project assets.

Do not bulk-download collections. At acquisition time record item URL, creator, license, date, original filename, modifications and intended use. Review people, logos and property in the image. No specific downloadable cup model has yet passed a geometry and license review.

## Asset briefs for later creation

These are briefs, not generated assets. No image generation was performed during research.

### Hero cup render

Matte ivory ceramic latte cup and saucer, realistic espresso and simple latte art, subtle handmade surface, soft morning window light, warm cream setting, gentle contact shadow, product on right, generous clean space on left for HTML headline, no text, no logo, no people. Deliver desktop landscape and mobile portrait compositions, plus a transparent variant if needed.

### Supporting food composition

One croissant and a small ceramic espresso cup on warm parchment, natural crumb detail, restrained styling, same lighting direction and material palette as hero. Deliver menu-card and editorial crops. Match real offerings before production use.

### Coffee bean accents

Small consistent set of roasted bean views, realistic matte surface and restrained highlights, isolated background or transparent output. Use as secondary decoration; avoid a full-screen particle storm.

### Interactive model brief

Deliver an optimized GLB with complete cup and saucer geometry, clean normals, sensible object names, compact textures and matching poster. Include an unbranded material unless approved branding is supplied. Test the underside and all allowed camera angles. Make steam a removable effect, not a geometry requirement. Include source project and asset license records.

### Real venue photography shot list

Exterior with entrance visible; wide seating view; counter and barista; signature drink close-up; two or three food items; an honest detail of the café's materials; any step-free entrance or access feature being described. Capture landscape and portrait crops with space for nearby text.

## Learning and verification resources

- [React Three Fiber performance](https://r3f.docs.pmnd.rs/advanced/scaling-performance): rendering demand, resource reuse and adaptive quality.
- [Web Vitals](https://web.dev/articles/vitals): user experience performance metrics.
- [WCAG quick reference](https://www.w3.org/WAI/WCAG22/quickref/): accessibility criteria.
- [Reduced motion](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion): honor the visitor's preference.
- [Local business structured data](https://developers.google.com/search/docs/appearance/structured-data/local-business): accurate local discovery information.
