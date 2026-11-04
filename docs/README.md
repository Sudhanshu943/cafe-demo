# Eight-design café implementation documentation

Prepared 5 November 2026. Original plans are preserved below. The eight-design interactive demo is now implemented; see [verification results](verification-summary.md) and the root README for running it.

Start with [the shared implementation plan](shared-implementation-plan.md) for the gallery, routing, remembered selection, return button, folder ownership, shared data and verification strategy.

Each design has its **own `docs` folder** with a detailed implementation plan, asset checklist and motion specification. The plans use the same 14-section structure, the same first foundation milestone and the same final acceptance gate, while section composition and execution details differ. This is the interpretation of the request to keep the first and last points consistent across designs.

| Design | Implementation plan | Supporting documents |
|---|---|---|
| 01 Warm Editorial | [Detailed plan](../designs/warm-editorial/docs/implementation-plan.md) | [Assets](../designs/warm-editorial/docs/asset-checklist.md) · [Motion](../designs/warm-editorial/docs/motion-spec.md) |
| 02 Japanese Minimal | [Detailed plan](../designs/japanese-minimal/docs/implementation-plan.md) | [Assets](../designs/japanese-minimal/docs/asset-checklist.md) · [Motion](../designs/japanese-minimal/docs/motion-spec.md) |
| 03 Botanical Calm | [Detailed plan](../designs/botanical-calm/docs/implementation-plan.md) | [Assets](../designs/botanical-calm/docs/asset-checklist.md) · [Motion](../designs/botanical-calm/docs/motion-spec.md) |
| 04 Playful Retro | [Detailed plan](../designs/playful-retro/docs/implementation-plan.md) | [Assets](../designs/playful-retro/docs/asset-checklist.md) · [Motion](../designs/playful-retro/docs/motion-spec.md) |
| 05 Dark Cinematic 3D | [Detailed plan](../designs/dark-cinematic-3d/docs/implementation-plan.md) | [Assets](../designs/dark-cinematic-3d/docs/asset-checklist.md) · [Motion](../designs/dark-cinematic-3d/docs/motion-spec.md) |
| 06 Heritage Classic | [Detailed plan](../designs/heritage-classic/docs/implementation-plan.md) | [Assets](../designs/heritage-classic/docs/asset-checklist.md) · [Motion](../designs/heritage-classic/docs/motion-spec.md) |
| 07 Bakery & Brunch | [Detailed plan](../designs/bakery-brunch/docs/implementation-plan.md) | [Assets](../designs/bakery-brunch/docs/asset-checklist.md) · [Motion](../designs/bakery-brunch/docs/motion-spec.md) |
| 08 Industrial Coffee Lab | [Detailed plan](../designs/industrial-coffee-lab/docs/implementation-plan.md) | [Assets](../designs/industrial-coffee-lab/docs/asset-checklist.md) · [Motion](../designs/industrial-coffee-lab/docs/motion-spec.md) · [Brief](../designs/industrial-coffee-lab/docs/research-and-brief.md) |

## What each detailed plan covers

1. Shared foundation and design-gallery contract.
2. Design objective and scope.
3. Folder ownership and deliverables.
4. Visual tokens and responsive rules.
5. Design-specific homepage sections and component tasks.
6. Navigation and interactions.
7. Content and asset production.
8. Motion and transitions.
9. Accessibility and semantics.
10. Loading, performance and errors.
11. Ordered execution milestones.
12. Design-specific verification and risks.
13. Dependencies and pending decisions.
14. Common completion and cross-design acceptance gate.

## Decisions already reflected

The opening gallery contains eight designs. Each links to a distinct homepage. The persistent Change design link returns to the gallery. Root visits may remember the selected design, while explicit gallery and homepage URLs always work. Designs share content/utilities while owning their composition and styles. The eighth direction is Industrial Coffee Lab, as proposed in the preceding conversation.

## Pending inputs

Exact framework remains provisional because “Angular design” was not clarified. Real business name/content, rights-cleared final assets and operational ordering/booking destinations are not supplied. The plans specify safe demo behavior so these omissions do not require invented business information. Package versions and official framework guidance must be checked at implementation time.

[Original research collection](../research/README.md) · [Seven original visual research boards](../research/design-directions/README.md)
