---
name: poster-design-mimic
description: Extract reusable visual rules, content-module relationships, and reading paths from a reference academic poster into POSTER-DESIGN.md, then apply them to new research material. Use for poster style extraction, paper-to-poster layout, or reuse of an existing poster specification.
---

[简体中文](SKILL.md)

# Poster Design Mimic

This skill draws on the text-based design specification idea in [awesome-design-md](https://github.com/VoltAgent/awesome-design-md). An academic poster needs two layers: a **visual language** for layout, typography, colors, and figures, and a **content architecture** for what each module contributes to the argument, how modules relate, and how readers move through them. Visual tokens alone do not tell an agent where evidence and conclusions belong.

## Inputs and outputs

- **Reference poster:** At least one complete image. A source PDF or high-resolution details improve text and measurement accuracy.
- **Target material:** A paper, abstract, figures, data, or content outline. If only the reference is available, complete the extraction without inventing content for a new poster.
- **Existing `POSTER-DESIGN.md`:** Reuse it, but check that it includes content architecture. If it does not, extract that layer from the reference or build a clearly labeled structure from the target material.
- **No reference poster:** If the user still wants this skill, [archetypes.md](references/archetypes.en.md) provides original starting points. Label these as design choices, never as observations from a reference.

Deliver what the task calls for: `POSTER-DESIGN.md` for extraction; an editable source file and a print-ready PDF for production when the user requests those formats.

Determine whether the request calls for **same-content reconstruction** or **style transfer to new material**. Record target dimensions, editing scope, and defining fidelity requirements. When reusing an older specification, also check distinctive components, asset dependencies, and comparison evidence; extract missing information or mark it unknown.

When the user explicitly requests same-content reconstruction, treat that original content as the target material and retain its accurate text, data, and corresponding identity information. Mark illegible content unknown and obtain necessary source text. Restrictions on carrying over reference facts below concern transfer to another study; they do not prevent the requested reconstruction of the original poster.

## Workflow

### 1. Extract the reference poster

Read [poster-design-schema.md](references/poster-design-schema.en.md) and record three layers:

1. **Visual specification:** Canvas, grid, color roles, type scale, spacing, charts, and decoration, with values and evidence.
2. **Reference content architecture:** Assign IDs to visible modules. Record each module's role, key message, position, and visual weight. Represent relationships such as motivates, addresses, produces, supports, qualifies, contrasts, parallels, and summarizes as typed edges. Record the reading path separately.
3. **Transfer rules:** Distinguish reusable layout grammar from facts specific to the reference study. Mark unreadable text or uncertain relationships as unknown. Visual proximity alone is not evidence of causation.

Write these layers in `POSTER-DESIGN.md`. Every consequential visual value or content relationship should have a traceable basis. Label values read directly from a source file or supplied by the user as `[Measured]`, pixel-based estimates as `[Estimated]`, semantic interpretations as `[Inferred]`, and unresolved items as `[Unknown]`. User acceptance of an estimate does not turn it into a measurement.

**Custom-shape check:** Inspect segmented rings, ribbons/folds, wave/angled dividers, shaped containers, and custom icons. Record “present / absent / uncertain” within the inspected region. When present, read [shape-reconstruction.md](references/shape-reconstruction.en.md) and document geometry, holes/connections/occlusion, text safe areas, semantic function, and implementation. Do not add absent features or invent uncertain ones. Distinguish parallel categories, cyclic steps, and data proportions before assigning meaning to a four-part ring.

### 2. Map the new research material

Build a **target content graph** from the user's material before placing anything. Track the source of each claim, value, figure, and qualification. Specify which data or figure supports each claim. Then map target nodes to the reference poster's reusable roles and relationships. Do not copy research facts from the reference or force the same number of modules.

- Preserve the direction of a problem → method → evidence → conclusion argument. If evidence is missing, do not invent a chart or conclusion.
- Keep qualifications next to the claim or figure they limit. Make comparisons easy to inspect; share an axis only when measures, units, and definitions are compatible.
- Preserve the order of method steps and the equal status of parallel contributions. Cross-column elements must not break a necessary reading path.
- When material is too dense, cut or combine it according to argumentative importance and record the choice. Do not hide density by shrinking text beyond useful readability.

If the target material does not fit the reference structure, preserve its visual grammar where possible—for example, a wide evidence area beside a narrow conclusion area—while adjusting the number or position of modules. Record material deviations. If key data is absent, provide a reviewable structure or an explicit empty slot rather than a fabricated result.

### 3. Build and verify

For HTML/CSS production, read [build-guide.md](references/build-guide.en.md). Set the physical page size and reuse visual tokens. User-provided photographs or microscopy images may remain sufficiently high-resolution raster images. Statistical charts should preferably be vector graphics or redrawn from actual data. Keep text, equations, and captions legible; do not use generated images to fabricate them.

Before production, read [fidelity-review.md](references/fidelity-review.en.md): identify defining features and evidenced substitutions to avoid, and prototype difficult components. Select SVG/CSS, native editor shapes, or standalone assets according to geometry and editing needs; implementation convenience must not silently erase distinctive contours. Compare page composition → component crops → actual export, also inspecting typography/wrapping, density, overlap, and asset availability.

Before export, check both **visual consistency** and **content logic**. Can a reader enter at the title, follow the intended path, find each main claim's evidence, and see its qualifications? Do figure placement, cross-column spans, and side-by-side comparisons reflect the actual relationships? Also check dimensions, overflow, font substitutions, data provenance, and the user's authorship or anonymity requirements. Ask the user to resolve only uncertainties that materially affect scientific meaning or delivery requirements.

## Boundaries

- Reuse the reference's visual structure, not its text, data, logos, or figures as facts about the target study.
- State uncertainty when the reference cannot be measured or read reliably. Do not invent exact dimensions, colors, or logical relationships.
- Do not turn one reference poster's accent count, column count, word count, or viewing distance into a universal rule. Follow the reference, target size, and actual content.
- Preserve the scientific conclusions, units, uncertainty, and scope in the user's material. Any rewrite should be traceable to the source.

## References

- [poster-design-schema.md](references/poster-design-schema.en.md): extraction template, content graph, and evidence labels.
- [content-architecture-example.md](references/content-architecture-example.en.md): fictional example to consult when defining edges or mapping target content.
- [build-guide.md](references/build-guide.en.md): implementation, export, and logic checks.
- [shape-reconstruction.md](references/shape-reconstruction.en.md): meaning, geometry, and implementation when custom shapes are present; ring and ribbon script usage.
- [fidelity-review.md](references/fidelity-review.en.md): fidelity targets, defining features, dependencies, prototypes, and export comparison.
- [archetypes.md](references/archetypes.en.md): original starting points when there is no reference poster.
