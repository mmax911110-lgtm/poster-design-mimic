# Poster Design Mimic

[简体中文](README.md)

Turn a reference academic poster into a reusable `POSTER-DESIGN.md`, then arrange new research material with the same visual language and a sound argument structure.

![A reference poster PDF transformed into a POSTER-DESIGN.md report of visual style and content relationships](assets/pdf-to-report.svg)

Inspired by the text-based design specifications in [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md), this independent skill adds three things that academic posters need: **relationships between the reference poster's content modules**, **a reading path**, and **a claim-to-evidence map for the new research**. It is not an official VoltAgent extension.

## Why content architecture matters

Color, typography, and a grid describe how a poster looks. They do not explain:

- what each section of the reference poster is trying to answer;
- whether sections motivate, address, produce, support, qualify, contrast, parallel, or summarize one another;
- where readers enter and how they reach the evidence and conclusion; or
- which arrangements are reusable design patterns and which details belong only to the reference study.

Recording those relationships lets a new poster preserve the style without scrambling the target study's logic.

## Preserving distinctive shapes and layout

First check whether the reference contains segmented rings, ribbons, wave dividers, shaped containers, or custom icons. When present, record geometry, connections and occlusion, text safe areas, and semantic function; do not add absent features. The bundled Python script creates editable SVG starting points for schematic rings and ribbons from explicit parameters. Statistical charts still require actual data.

Fidelity checks also cover title typography and wrapping, density, whitespace, component variants, and asset dependencies. Prototype difficult elements, then compare the full page and final PDF. Blurred references, missing fonts, or unavailable original illustrations limit achievable fidelity; record the specific differences.

## Install and use

Place the entire `poster-design-mimic/` directory in a tool's skill directory if it supports `SKILL.md`. For WorkBuddy, an example location is `~/.workbuddy/skills/poster-design-mimic/`. Start a new session and provide the reference poster, the research material to use, the target size, required output format, and any authorship or anonymity rules.

Example request:

> Use poster-design-mimic to extract the design and content relationships from this reference poster into POSTER-DESIGN.md. Then make an A0 poster from my abstract, Figures 1–3, and conclusion. Do not reuse the reference poster's research data.

You can request only `POSTER-DESIGN.md` when you have a reference poster but no new study yet. An existing specification can be reused for another study. Without a reference poster, [archetypes.md](references/archetypes.en.md) offers original starting points.

## Files

| File | Purpose |
|---|---|
| [SKILL.en.md](SKILL.en.md) | Entry point, workflow, and boundaries |
| [poster-design-schema.en.md](references/poster-design-schema.en.md) | Extraction template, relationship graph, and evidence levels |
| [content-architecture-example.en.md](references/content-architecture-example.en.md) | Fictional example of mapping reference relationships to a new study |
| [build-guide.en.md](references/build-guide.en.md) | HTML/CSS production and export checks |
| [shape-reconstruction.en.md](references/shape-reconstruction.en.md) | Custom-shape detection, geometry, and implementation choices |
| [fidelity-review.en.md](references/fidelity-review.en.md) | Defining features, prototypes, assets, and fidelity comparison |
| [make_motif.py](scripts/make_motif.py) | Equal schematic ring / folded ribbon SVG from explicit parameters; Python standard library only |
| [archetypes.en.md](references/archetypes.en.md) | Layout archetypes for work without a reference |

## Typical outputs

- `POSTER-DESIGN.md`: reusable visual specification and content architecture.
- `poster.html`: editable source for a poster-production task.
- `poster.pdf`: print or submission file when requested.

Names and formats may follow the user's requirements. Text, data, figures, and logos from the reference poster are never treated as facts about the new study.

## License

[MIT License](LICENSE). You may use, modify, and distribute this project, including commercially, as long as you retain the copyright and license notices.
