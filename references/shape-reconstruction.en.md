# Custom shapes: detection, decomposition, and reconstruction

[简体中文](shape-reconstruction.md)

Read this when a reference contains segmented rings, ribbons, wave dividers, angled panels, badges, custom icons, or other distinctive contours. **Establish presence before deciding how to reuse a component.** These examples are not a default decoration library.

## 1. Detect and interpret

Inspect both the whole page and relevant crops. Assign component IDs `S1…` and associate them with content modules `M…`:

| Status | Record and action |
|---|---|
| Present | Record the source page/crop, outline, parts, and function; proceed to decomposition |
| Absent | Record absence only within sufficiently clear inspected regions; do not add a motif for visual interest |
| Uncertain | Mark blur, occlusion, or cropping as unknown; do not equate uncertainty with absence or invent missing folds or segments |

Identify the function: decoration, title/abstract separator, content container, relationship diagram, data chart, disciplinary illustration, or identity mark. A component may serve several functions.

- **Four-part ring:** Four parallel categories, a four-step cycle, and four percentages have different meanings. Circular placement alone does not establish a cycle; equal areas do not establish equal data values. Use labels, arrows, captions, and text to determine meaning, or mark it unknown.
- **Ribbon:** Determine whether it contains the title/abstract or merely separates regions; which tails fold behind the foreground; and whether it sets the starting boundary for the body text.
- **Custom icon:** Distinguish a generic geometric symbol from a disciplinary symbol with a fixed meaning or an illustration/identity asset requiring a source file. Check disciplinary symbols against the supplied research; resemblance is insufficient.

Check semantic compatibility again during transfer. A four-part reference ring must not force the target study to invent a fourth contribution. Adjust the segment count or choose a layout appropriate to the target relationships, recording the reason. Statistical sector sizes must come from actual target data.

## 2. Record an executable component specification

For repeated components, record a base definition and observed variants rather than averaging them into one style. A complex component may have a separate SVG; parameters and a short explanation can suffice for a simple one.

| Field | What to capture |
|---|---|
| Identity and evidence | `S1`, component family, associated modules, source page/bounds/crop, evidence level for each observation |
| Geometry | Local `viewBox`; center, inner/outer radii, angles, segment count, gaps, notches, corners; proportions and allowed variation |
| Topology | Holes, connections/disconnections, containment, touching, overlap, and occlusion; front and rear edges |
| Appearance | Semantic fill/stroke colors, line width, caps, gradient direction/stops, opacity, and whether shadows actually exist |
| Anchors and layers | Attached module/edge, alignment axes, relative offsets, and back-to-front drawing order |
| Text safe area | Region available for titles/labels, padding, wrapping and leader-line rules; decoration-only regions |
| Content mapping | Target ID for every segment/label; arrow direction and relationship type |
| Implementation and fallback | Output tool, editing model, dependent files, unrecoverable details, and proposed approximation |

Local normalized coordinates are useful, but retain their mapping to the sheet. “Ribbon-like,” “futuristic,” and “a ring” are insufficient specifications. Preserve paths or reproducible parameters when the contour matters. Parameters estimated from an image remain estimates.

## 3. Choose an implementation by structure

| Actual object | Preferred implementation | What to verify |
|---|---|---|
| Original SVG/PDF decoration with permission to reuse | Extract paths, groups, transforms, and clipping; inspect dependencies before reuse | Exclude unrelated research text/figures and identity marks; verify vector content rather than relying on the PDF extension |
| Segmented ring, petals, curved arrow, custom badge | Parametric SVG `path`; `A` for arcs, `C/Q` for curves, combined with basic shapes | A genuinely transparent hole, separate segments, correct ordering and direction |
| Ribbon, fold, angled boundary, wave divider | Layered SVG polygons/curves; CSS `clip-path` for simple silhouettes | Keep editable text in a separate safe area so clipping the shape does not clip the text |
| Ordinary rounded box, straight band, simple cut corner | HTML/CSS or native shapes in the target editor | Avoid unnecessary paths or shadows absent from the reference |
| Original photographic illustration, texture, or 3D decoration | High-resolution source asset, or a generated standalone image when stylistic approximation is allowed | Generated imagery must not carry exact segments, experimental data, equations, or final body copy; document approximation |
| Requested LaTeX / PPTX delivery | TikZ, native editable shapes/text boxes, or SVG supported by the target tool | Scalable SVG does not guarantee individually editable paths in PowerPoint; supply source files according to editing requirements |

Complexity alone does not justify image generation. Prefer deterministic geometry for exact holes, partitions, connections, and labels. Trace free-form contours with control points when needed: fit the silhouette and principal turns before details, avoiding low-resolution antialiasing noise.

Whichever tool is selected, prototype the hardest component and check it in the **actual export renderer** before building the full page. Record unsupported filters, masks, or fonts. If necessary, rasterize only a decorative layer while preserving clear body text, equations, data charts, and labels.

## 4. Two executable geometric starting points

[make_motif.py](../scripts/make_motif.py) uses only the Python standard library and writes standalone SVG without font or image dependencies. It provides equal schematic ring segments and a folded ribbon; reconstruct other shapes from observation. All dimensions and colors below are demonstration parameters, not extracted measurements.

Run from the skill directory with an existing output directory. The script does not overwrite files; use a new output filename for an iteration.

### Segmented ring

```bash
python scripts/make_motif.py ring --segments 4 --outer 100 --inner 62 --gap 6 --start -90 --colors '#315C7D' '#3F9090' '#D59B63' '#9A7FA4' --output ring.svg
```

`start` uses 0° pointing right and increases clockwise with SVG's downward y-axis; `gap` is the total angular gap at each boundary. Construct each sector as outer arc → radial edge → reversed inner arc → closed path. This produces a real hole instead of covering the center with a background-colored disk.

Polar coordinates are `x = cx + r*cos(θ)` and `y = cy + r*sin(θ)`. Sector k runs from `start + k*360/n + gap/2` to `start + (k+1)*360/n - gap/2`. Set the large-arc flag according to whether the effective span exceeds 180° and reverse the inner arc's sweep. A full unsegmented circle needs two half-circle arcs or compound circles; a single arc with identical endpoints does not draw a complete ring.

Keep text in a separate layer and map every segment to a target ID. Use external labels with leader lines or adjust the layout when text does not fit; do not distort the ring. Add arrows only when both reference and target establish a process relationship. This script produces an equal-part schematic, not a statistical chart.

### Folded ribbon

```bash
python scripts/make_motif.py ribbon --width 420 --height 64 --tail 38 --fold 18 --color '#315C7D' --fold-color '#203D52' --output ribbon.svg
```

Draw rear tails → shaded folds → front band. Place the title or abstract as separate editable text inside the safe rectangle recorded in the SVG. Tails must not obscure body text; check band height against the actual line count. This example has folds; if the reference has only a wave or diagonal divider, rebuild that boundary without adding tails.

## 5. Component acceptance

- Compare reference and reconstruction at the same aspect ratio: silhouette, holes, segment count, touching edges, and occlusion.
- After parameter changes, confirm circularity, transparent holes, consistent gaps, and connected ribbon folds.
- Check safe-area placement, occluded labels, and incorrect label/leader attachments.
- Confirm that cycles, directions, proportions, and parallel relationships agree with the target content graph.
- Inspect arrows, masks, transparency, stroke widths, and fonts in the exported PDF; verify the actual editing requirement.

Geometry reference: [W3C SVG Paths](https://www.w3.org/TR/SVG2/paths.html). Adoption conditions and appearance must come from the current poster, not from these examples or another design system.
