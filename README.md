# Poster Design Mimic

Turn a reference academic poster into a reusable `POSTER-DESIGN.md`, then arrange new research material with the same visual language and a sound argument structure.

Inspired by the text-based design specifications in [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md), this independent skill adds three things that academic posters need: **relationships between the reference poster's content modules**, **a reading path**, and **a claim-to-evidence map for the new research**. It is not an official VoltAgent extension.

## Why content architecture matters

Color, typography, and a grid describe how a poster looks. They do not explain:

- what each section of the reference poster is trying to answer;
- whether sections motivate, address, produce, support, qualify, contrast, parallel, or summarize one another;
- where readers enter and how they reach the evidence and conclusion; or
- which arrangements are reusable design patterns and which details belong only to the reference study.

Recording those relationships lets a new poster preserve the style without scrambling the target study's logic.

## Install and use

Place the entire `poster-design-mimic/` directory in a tool's skill directory if it supports `SKILL.md`. For WorkBuddy, an example location is `~/.workbuddy/skills/poster-design-mimic/`. Start a new session and provide the reference poster, the research material to use, the target size, required output format, and any authorship or anonymity rules.

Example request:

> Use poster-design-mimic to extract the design and content relationships from this reference poster into POSTER-DESIGN.md. Then make an A0 poster from my abstract, Figures 1–3, and conclusion. Do not reuse the reference poster's research data.

You can request only `POSTER-DESIGN.md` when you have a reference poster but no new study yet. An existing specification can be reused for another study. Without a reference poster, [archetypes.md](references/archetypes.md) offers original starting points.

## Files

| File | Purpose |
|---|---|
| [SKILL.md](SKILL.md) | Entry point, workflow, and boundaries |
| [poster-design-schema.md](references/poster-design-schema.md) | Extraction template, relationship graph, and evidence levels |
| [content-architecture-example.md](references/content-architecture-example.md) | Fictional example of mapping reference relationships to a new study |
| [build-guide.md](references/build-guide.md) | HTML/CSS production and export checks |
| [archetypes.md](references/archetypes.md) | Layout archetypes for work without a reference |

## Typical outputs

- `POSTER-DESIGN.md`: reusable visual specification and content architecture.
- `poster.html`: editable source for a poster-production task.
- `poster.pdf`: print or submission file when requested.

Names and formats may follow the user's requirements. Text, data, figures, and logos from the reference poster are never treated as facts about the new study.

## License

[MIT License](LICENSE). You may use, modify, and distribute this project, including commercially, as long as you retain the copyright and license notices.
