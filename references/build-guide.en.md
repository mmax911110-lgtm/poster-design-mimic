# Academic poster build guide

[简体中文](build-guide.md)

Before production, read the project's `POSTER-DESIGN.md`, especially its reference content architecture, target content graph and mapping, and deviation log. Treat that specification as authoritative. The code below illustrates structure; replace its values with the extracted design decisions.

## 1. Arrange the argument before styling it

1. Build each module from the target content graph: title, claim, evidence, caption, qualification, and source. Do not copy reference claims or values into a new study. For requested same-content reconstruction, the original content is the target material.
2. Use the relationship edges to decide placement: the order of steps, common labels for comparisons, proximity between figures and claims, and proximity between qualifications and conclusions. Sketch a wireframe and trace the reading path from entry to exit.
3. Apply the visual tokens to reproduce hierarchy, proportions, and component rules. When the target size changes, adjust absolute values and record meaningful deviations.
4. Render, inspect, and export. If content overflows, first tighten redundant prose or reorganize modules and whitespace. Do not discard evidence or qualifications or make text unreadable.

If the reference layout conflicts with the target study's logic, preserve its recognizable visual grammar while changing columns, spans, or module counts as needed.

## 2. HTML/CSS starting point

```html
<main class="poster">
  <header class="poster-title" data-module="T0">...</header>
  <section class="problem" data-module="T1">...</section>
  <section class="method" data-module="T2">...</section>
  <figure class="evidence" data-module="T3">
    <img src="figure.svg" alt="Summary of what the figure shows">
    <figcaption>Figure number, measure, units, and relevant conditions</figcaption>
  </figure>
  <section class="conclusion" data-module="T4" aria-describedby="limit-T5">...</section>
  <p class="limitation" id="limit-T5" data-module="T5">...</p>
</main>
```

The `data-module` attributes connect the source-material IDs, mapping table, and final HTML for inspection. Alt text should describe the figure's actual content; the caption should explain its relationship to the claim.

```css
@page {
  size: 841mm 1189mm; /* Replace with the target sheet size */
  margin: 0;
}

:root {
  --canvas: #fff;
  --ink: #1a1a1a;
  --accent: #0b4f8a;
  --panel: #f5f7fa;
  --font-body: Arial, sans-serif;
  --title-size: 90pt;
  --section-size: 38pt;
  --body-size: 24pt;
  --caption-size: 17pt;
  --margin: 35mm;
  --gutter: 16mm;
  --section-gap: 24mm;
}

* { box-sizing: border-box; }
html, body { margin: 0; }
body {
  background: var(--canvas);
  color: var(--ink);
  font-family: var(--font-body);
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}
.poster {
  width: 841mm;
  height: 1189mm;
  padding: var(--margin);
  display: grid;
  align-content: start;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: var(--section-gap) var(--gutter);
}
.poster-title { grid-column: 1 / -1; font-size: var(--title-size); }
.poster section h2 { font-size: var(--section-size); }
.poster section p { font-size: var(--body-size); }
.poster figcaption { font-size: var(--caption-size); }
.evidence img { display: block; max-width: 100%; height: auto; }
```

Colors, sizes, column counts, and spans in the final file must come from `POSTER-DESIGN.md`. Use CSS variables for repeated values. A component-specific value with a documented reason can stay in the component; not every number needs a token. CSS pixels are allowed internally, but verify paper size, page margins, and print typography in physical units.

A fixed canvas height exposes capacity problems. Resolve overflow through layout rather than hiding it with `overflow: hidden` or allowing unlimited page growth followed by print scaling. This is only a grid starting point; set actual row sizes and module positions from the specification.

If the reference uses a full-width color band or bleed, implement it according to the printer's actual requirements. Negative margins do not create a valid print bleed by themselves. For a bleed-ready PDF, confirm both trim size and bleed size.

## 3. Charts, photographs, and fonts

First use [fidelity-review.md](fidelity-review.en.md) to identify fidelity priorities and check distinctive components and text capacity. When custom shapes are present, read [shape-reconstruction.md](shape-reconstruction.en.md). Build ring sectors as separate arc paths and ribbon faces in layer order; keep text and labels independent. Do not introduce shapes absent from the reference merely because a template provides them.

- **Statistical charts and diagrams:** Prefer user-provided vector files or redraw from actual data. Keep scales, units, color meanings, and legend conventions consistent. Overlay plots or share axes only when measures and statistical definitions are compatible.
- **Experimental photographs, micrographs, and scans:** These are inherently pixel-based and may remain raster images at sufficient resolution. Cropping must retain scale bars, labels, and essential experimental conditions.
- **Figure-to-text links:** Each figure needs a locatable claim or explanation. Put conditions and uncertainties in the caption or adjacent text. Avoid placing a figure in one column and its explanation at the far end of the poster.
- **Fonts:** Preserve the reference's type family, weight, and width character where possible. If a font is unavailable, choose a substitute and inspect line breaks, symbols, and mixed-language text. Do not bake editable text into a generated image.
- **Factual integrity:** Do not draw plausible-looking curves when data is missing, or borrow values or images from the reference poster to fill a gap.

## 4. Export and page checks

In browser print preview, choose the target sheet size, no additional margins, and background graphics; confirm the expected page count. For automated export, use a browser PDF interface that honors CSS `@page`, then inspect the actual PDF dimensions. Browser versions may differ in scaling and color handling. Use a physical proof print when the production context warrants one.

Check before delivery:

- [ ] The reading path from the title matches the specification; cross-column elements do not break the argument.
- [ ] Every target module has a source; each central claim has evidence or is explicitly marked as needing it.
- [ ] Method and result, figure and caption, and qualification and qualified claim remain paired.
- [ ] Comparisons use compatible measures, units, samples, and axes; parallel items do not acquire unsupported visual ranking.
- [ ] No reference research facts, names, logos, or figures were mixed into a new study; requested same-content reconstruction retains its original content accurately.
- [ ] No placeholder text, broken images, overflow, awkward wrapping, or unintended extra page remains.
- [ ] Distinctive silhouettes, partitions/holes, occlusion, and text safe areas match the specification; no unobserved decoration was introduced.
- [ ] Page thumbnails and key crops were compared for title wrapping, text/figure density, focus, and component variants; necessary deviations are recorded.
- [ ] Actual PDF renders were checked for arrows, clipping/masks, transparency, and fonts; source files and required assets resolve within the delivery.
- [ ] The PDF's physical size, page count, backgrounds, and fonts are correct; figures remain clear when enlarged.
- [ ] Authors, affiliations, acknowledgments, and anonymity follow the user's material and venue rules.

A reduced preview helps reveal the overall hierarchy, but a screen zoom percentage does not equal a fixed viewing distance. Judge legibility against the final sheet and display environment.
