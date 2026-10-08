# POSTER-DESIGN.md: extraction specification and content architecture

Use this reference to turn a poster image or PDF into a reusable `POSTER-DESIGN.md`. Record **observed facts, the basis for interpretations, and unknowns**. Tables below show fields, not defaults: include only elements present in the actual reference and do not copy illustrative values as measurements.

## 1. Deliverable structure

```text
1. Source and scope of observation
2. Visual tokens and relationships between them
3. Reference poster content architecture: module inventory, typed edges, reading path
4. Reusable layout rules versus study-specific facts
5. Target content graph and module mapping (only when new material is provided)
6. Deviations, unknowns, and verification checklist
```

**Analyze the reference poster itself in section 3 before handling the user's new study in section 5.** Keep those layers separate. A “result” in the reference is a role in the layout, not a result that can be reused in the new study.

## 2. Source and evidence levels

At the start of the file, identify the reference file or URL, page count, resolution or vector properties, target size if known, and extraction date. Mark each consequential observation with one of these labels:

| Label | Meaning | Example |
|---|---|---|
| `[Measured]` | A property read directly from a source file, or a value explicitly provided by the user | Font size extracted from a PDF; user-specified paper size |
| `[Estimated]` | A value approximated from raster pixels, visible proportions, or partial samples | Outer margin is about 4% of the sheet width |
| `[Inferred]` | An interpretation of visible content or intended reading behavior | An arrow appears to indicate process order |
| `[Unknown]` | Not reliably legible or determinable | Axis labels in a blurred figure; missing conclusion text |

If the user accepts a visual estimate, record “accepted estimate”; do not relabel it `[Measured]`. Never reconstruct scientific numbers, claims, or causal relationships from illegible marks.

## 3. Visual tokens and their relationships

YAML frontmatter is a convenient place for visual tokens, followed by prose rules. Give values units or normalized proportions. For a low-resolution reference, proportional estimates are usually more defensible than precise millimeter claims. This block illustrates fields only:

```yaml
---
version: 1
source: "reference-poster.pdf"
canvas:
  width_mm: 841
  height_mm: 1189
  orientation: portrait
  margin_mm: 35
  columns: 3
  gutter_mm: 16
colors:
  canvas: "#FFFFFF"
  ink: "#1A1A1A"
  accent: "#0B4F8A"
  panel: "#F5F7FA"
typography:
  title: {size_pt: 90, weight: 700, family: "sans-serif"}
  section: {size_pt: 38, weight: 700, family: "sans-serif"}
  body: {size_pt: 24, weight: 400, family: "sans-serif"}
  caption: {size_pt: 17, weight: 400, family: "sans-serif"}
spacing:
  section_gap_mm: 24
  panel_padding_mm: 12
charts:
  axis_label_pt: 18
  line_width_pt: 1.5
---
```

**How to collect evidence:**

- Record the sheet and each visible module's bounding box `(x, y, w, h)`, normalized to 0–1 relative to sheet width and height. Retain the pixel coordinates used for measurement so later readers can audit the estimate.
- A PDF or vector source may expose font, color, and path properties. Mark only properties actually read from the file as `[Measured]`. Scaling, compression, and color management make exact claims from screenshots unreliable.
- Dominant-color clustering can help identify semantic colors in a raster image. Exclude photographs and chart series; otherwise their colors may be mistaken for the poster palette.
- Extract the type scale, column widths, section gaps, whitespace ratio, borders and corners, chart marks, caption placement, and font families. Do not add components merely because they appear in this template.
- If the reference uses more than one accent, record each accent's role and placement. Do not erase a real second accent to satisfy a generic “one accent” rule.

Beyond isolated tokens, describe **relationships**: title-to-body size ratio, column-width ratio, colored-area share, where a primary color repeats, which decorations are absent, and where rules have exceptions. These relationships constrain style drift better than individual hex values.

Example:

```markdown
## Visual relationships
- Title/body size is approximately 3.7:1 [Estimated; basis: sampled pixel letter heights].
- Dark blue appears only in the title band and section headings [Measured; basis: inspected page 1].
- The conclusion spans two columns; captions sit below figures [Estimated; basis: M5/M6 bounds].
- No card shadows appear on the inspected reference page [Measured; scope: that page].
```

When resizing, prioritize relative hierarchy, semantic color roles, whitespace rhythm, and the spatial relationship between evidence and conclusion. Absolute font sizes, spacing, and column counts may change with sheet size and content; record material deviations. Assess legibility against the final sheet, likely viewing distance, and a print proof rather than a universal minimum-size table.

## 4. Reference poster content architecture

### 4.1 Module inventory

Assign IDs to every distinguishable block: title, abstract, background, problem, method, workflow diagram, each major result figure, conclusion, qualifications, and so on. **Do more than transcribe section headings**: state what question each block answers and what it contributes to the argument.

| ID | Original heading or visible cue | Role / question answered | Legible content summary | Normalized bounds | Visual weight | Evidence |
|---|---|---|---|---|---|---|
| M1 | Fill from the reference | Background: why this study? | Only what can be read | `x,y,w,h` | High / medium / low, with basis | Page/crop and evidence label |

Possible roles include context, problem/hypothesis, objective, method/system, experimental setup, result, evidence figure, comparison, mechanism, conclusion, limitation, future work, authorship, and source. A module may have several roles, but distinguish a **figure as evidence** from the **claim made about the figure**.

**Keep two orders separate:**

- `reading_order`: what a reader is likely to see first based on placement, numbering, arrows, color bands, or visual weight.
- `argument_order`: what motivates, produces, or supports what. A large result number may be seen first even though it depends on a method shown to its left.

### 4.2 Typed relationship edges

Write `from → to` with a relationship type and evidence. For motivates, addresses, produces, and precedes, the arrow follows the narrative sequence. For supports and qualifies, it points from evidence or condition to the claim it supports or limits. Contrast and parallel are symmetric and may be written `A ↔ B`. Capture every relationship that affects placement; do not force unrelated blocks into one chain.

| Type | Direction and meaning | Typical layout consequence |
|---|---|---|
| `motivates` | Context → problem or objective | Keep them near; let the problem stand out |
| `addresses` | Problem → method responding to it | Preserve problem-to-method reading direction |
| `produces` | Method or experiment → data | Place a result figure near the method or setup |
| `supports` | Data or figure → claim | Keep evidence adjacent to, or clearly linked with, the claim |
| `qualifies` | Condition or uncertainty → limited claim | Keep the qualification close to its target |
| `contrasts` | Comparable items A ↔ B | Group or align them; share axes only when valid |
| `parallels` | Same-level items A ↔ B | Give them equivalent visual treatment |
| `precedes` | Step A → step B | Use numbering, arrows, or unambiguous order |
| `summarizes` | Several results → conclusion | Form a visible point of synthesis |

Use this structure in the delivered `POSTER-DESIGN.md`:

```markdown
## Reference content architecture
### Modules
| ID | Heading/cue | Role | Question answered | Position | Weight | Evidence and confidence |
|---|---|---|---|---|---|---|
| ... |

### Logical relationships
| From → To | Type | Text/graphic evidence | Layout constraint | Confidence |
|---|---|---|---|---|
| M2 → M3 | addresses | Numbering/text in the reference | Problem before method; a span may cross columns if the path stays clear | [Inferred] |

### Reading path
Entry: ...
Main path: M1 → M2 → M3 → M5
Branch: M3 → M4 (method details); M5 ↔ M6 (comparison)
Exit: ...
Basis: numbering/arrows/alignment/visual weight; uncertain transitions: ...
```

Every arrow's meaning should be defined in the edge table. Proximity alone establishes at most **visual adjacency**, not `supports` or causation. If reference text is unreadable, record the visible scan pattern (for example, “wide upper block → three parallel lower blocks”) and label the logical relationship `[Unknown]`. Inspect spanning figures, grouped panels, workflows, conclusion boxes, and footnotes carefully; they often encode hidden relationships. For a worked example, read [content-architecture-example.md](content-architecture-example.md).

### 4.3 Information versus visual hierarchy

Rank these separately:

1. What claim, result, or evidence does the reference seem to prioritize? Is that judgment based on wording, position, size, area, or color?
2. What is visually largest? It may be a title or a brand mark, not the most important scientific conclusion.
3. Where is each figure explained, and where are its scope conditions? If separated, record the pattern and the risk of misreading.

Write an “information → visual carrier” table from actual observation. Do not impose a fixed order such as “title first, results second, background fourth” on every reference.

### 4.4 Reusable layout grammar

Before introducing target material, summarize what the reference teaches about *arrangement* and what belongs only to its study:

| Observed pattern and evidence | Reusable layout function | Reference-specific content not transferred | Conditions for reuse |
|---|---|---|---|
| Wide figure beside a narrow conclusion block; M4/M5 bounds | Keep evidence and synthesis easy to compare | Original measurements, figure labels, and conclusion text | Target has evidence that actually supports the nearby claim |

This ledger becomes section 4 of the delivered `POSTER-DESIGN.md`. A layout relation can be reusable even when the number of modules changes; a scientific claim is never reusable merely because its box is prominent.

## 5. Transfer to new research material

Build the target content graph first and **attach a source to every scientific assertion**:

| Target ID | Claim/information | Role | Source page/section/figure/data | Supporting target IDs | Qualification | Priority |
|---|---|---|---|---|---|---|
| T1 | Fill from the user's material | Conclusion | Paper §4 / Fig. 2 | T2 | T3 | High |

Then map the target graph to reusable roles from the reference:

| Reference module/relationship | Reusable function | Target IDs | Reason for adjustment |
|---|---|---|---|
| M3 → M5 (`supports`) | Put evidence near the conclusion it supports | T2 → T5 | The target figure is wide and spans two columns |

**Transfer the grammar, not the reference study's facts.** A pattern such as “problem block → wide method diagram → grouped results → spanning conclusion” may transfer. Its original values, experimental names, control groups, and citations may not. If the target has no parallel experiment, do not invent one to fill a second column. Use that space for valid method detail or whitespace, keep the reading path clear, and document the change.

Let the graph determine spatial decisions rather than simply matching rectangle counts:

- `supports`: Keep figure and claim close; write a caption that explains what the figure actually establishes.
- `qualifies`: Place conditions next to the relevant number, figure, or conclusion in legible type.
- `contrasts`: Use one visual group and compatible labels; share an axis only when measures and units permit it.
- `precedes`: Match the visual order of method steps to the real sequence.
- `parallels`: Preserve equal standing rather than implying an unsupported ranking through size.
- `summarizes`: Let the conclusion point back to evidence instead of becoming a slogan.

Handle authors, affiliations, QR codes, and funding details according to the user's material and venue rules. Never carry them over from the reference poster.

## 6. Verification and unknowns

End `POSTER-DESIGN.md` with:

```markdown
## Unknowns and items to verify
| Item | Current judgment | Evidence/gap | Effect on generation | Resolution |
|---|---|---|---|---|

## Deviation log
| Reference rule | Target implementation | Reason | Effect on argument path |
|---|---|---|---|
```

Before finishing, ask:

- Are the module inventory, typed edges, and reading path all present?
- Does every edge cite text, numbering, an arrow, or graphic grouping? Was mere adjacency mistaken for causation?
- Are the reference poster's content structure and the target study's facts kept separate?
- Can every target claim be traced to the user's material and, where needed, to supporting data or a figure?
- Are qualifications, comparisons, and step order expressed correctly in the layout?
- Are illegible items still marked unknown, and are material deviations recorded?
