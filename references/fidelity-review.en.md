# Fidelity: specification, prototypes, and comparison

[简体中文](fidelity-review.md)

Similar colors and an absence of overflow do not establish fidelity. Define what is being reproduced, then verify that its defining features survive.

## 1. Define the comparison target

Infer from the request whether the task reconstructs the same poster or transfers its style to new research. The former permits module-by-module alignment; the latter allows different content and module counts while preserving evidenced visual features and applicable relationships. Establish the requested dimensions, format, editing scope, and acceptable approximation; proceed when the user has already supplied sufficient information.

Create a short feature table for the elements that actually determine resemblance, without a fixed feature count:

| Feature and evidence | Preservation condition | Allowed variation | Substitution to avoid | Comparison region |
|---|---|---|---|---|
| Example: an angled band above the abstract | Present in this reference, with a corresponding separation function in the target | Width adapts to the page | Silently replacing it with a generic rounded card | Source page/crop |

Distinguish consequential discrepancies from minor ones. Do not reproduce a small shadow while losing the principal silhouette. Ambiguous evidence does not support a claim of pixel-exact reproduction.

## 2. Frequently missed visual information

| Level | Additional observations |
|---|---|
| Whole-page composition | Position and area of major color fields, asymmetric balance, main figure scale, title-band height, content and whitespace distribution |
| Type and text layout | Family and substitute, glyph width/weight, case, leading, tracking, alignment, title line count and breaks; equal character counts do not imply equal English/Chinese text area |
| Content density | Available module area, approximate body line counts, text-to-figure ratio, caption space and retained whitespace; these are observations, not universal word limits |
| Layers and combinations | Foreground/background, touching and overlap, clipping windows, anchors between components, local variants of recurring components |
| Chart interiors | Axes, grids, line styles, markers, legends, error bars, panel letters, and caption proportions; transferring appearance must preserve data encoding |
| Surfaces and details | Stroke widths/caps, gradient stops/direction, opacity, shadows, texture scale; do not add effects absent from the reference |

Do not treat perspective, paper curvature, or glare in a scan/photograph as design. Prefer the original PDF; if correcting an image, retain the original and record the correction and uncertainty. With multiple references, attribute each rule to its source instead of averaging conflicting styles.

## 3. Validate difficult elements before completing the page

Prototype only what resolves an actual uncertainty: a distinctive title/divider, difficult text block, or chart. A simple reference does not need a component library. See [shape-reconstruction.md](shape-reconstruction.en.md) for custom geometry.

Use real target text to test capacity. When it does not fit, address redundant wording, internal spacing, and module area/organization while retaining important evidence and qualifications. Record necessary departures from the reference. Do not silently compress glyphs or rings horizontally or crop overflowing body text.

Once the chosen tool can deliver the needed shapes and text, complete the page using the same specification. Keep asset paths resolvable; record font availability, authorized source assets, and external dependencies. A font name or source-image path without an obtainable asset is not a reusable specification.

## 4. Compare and correct

Inspect in this order, correcting the largest consequential discrepancy first:

1. **Page thumbnails:** Match canvas aspect ratio and display scale. Compare silhouette, color-field area, focus, whitespace, and reading path.
2. **Component crops:** Compare distinctive geometry, composition, typography, and wrapping. Aligned overlays can help for identical-content reconstruction. For new-content transfer, compare roles, proportions, and structure rather than penalizing new words/data with whole-image pixel differences.
3. **Final export:** Render the delivered PDF for inspection; an HTML preview is insufficient. Check arrowheads, holes, clipping, folds, transparency, and fonts for loss or distortion.

Record remaining differences as “location → reference feature → discrepancy → cause/next action,” distinguishing unclear evidence, missing assets, content adaptation, and tool limitations. Resolve fixable critical discrepancies before delivery. Explain constraints such as missing assets rather than iterating blindly or reporting an unvalidated similarity percentage.

## 5. What was adapted from the inspiration repository

This independently written guide adapts documentation practices rather than applying website brand rules to posters:

- [Mastercard example](https://github.com/VoltAgent/awesome-design-md/blob/main/design-md/mastercard/DESIGN.md): grouped descriptions of circular crops, attached elements, and connecting arcs inform poster anchors, layers, and adoption conditions.
- [Clay example](https://github.com/VoltAgent/awesome-design-md/blob/main/design-md/clay/DESIGN.md): distinguishing parameterized styling from standalone illustrations informs the geometry-versus-source-asset inventory.
- [Stripe example](https://github.com/VoltAgent/awesome-design-md/blob/main/design-md/stripe/DESIGN.md): gradient backgrounds and surface layers motivate recording extent, stacking, and implementation without copying its palette or web layout.
- [Contribution guide](https://github.com/VoltAgent/awesome-design-md/blob/main/CONTRIBUTING.md): checking specifications against the original and updating previews informs prototype and final-export comparison.

These are the repository authors' design analyses, not official specifications from the brands. Their current values and technical assertions also require verification before being applied as poster rules.
