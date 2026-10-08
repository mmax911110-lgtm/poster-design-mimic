# Content architecture example (fictional poster)

This example shows how to record relationships. It contains no reusable research claims, measurements, or layout values. Imagine a reference poster with a full-width title at the top, a problem and method in the left column, two result figures in the middle, and a conclusion with a limitation on the right.

## Reference poster: visual entry versus argumentative dependency

| ID | Visible module | Role | Position / weight |
|---|---|---|---|
| M0 | Full-width title | Topic and entry point | Top; strongest visual weight |
| M1 | Research problem | States the question to answer | Upper left; medium |
| M2 | Method diagram | Addresses the question | Lower left; medium |
| M3 | Result figure A | First piece of evidence | Middle; high |
| M4 | Result figure B | Second piece of evidence | Grouped with M3; high |
| M5 | Conclusion | Synthesizes the results | Upper right; high |
| M6 | Scope condition | Qualifies the conclusion | Next to M5; visually quieter but legible |

Typed edges:

```text
M1 --addresses--> M2
M2 --produces--> M3
M2 --produces--> M4
M3 --supports--> M5
M4 --supports--> M5
M6 --qualifies--> M5
M3 <--contrasts--> M4  (only if labels or text establish a comparison)
```

Because the conclusion box is prominent, a plausible **reading path** is `M0 → M5 → M1 → M2 → (M3, M4) → M5 → M6`. The **argument path** is `M1 → M2 → (M3, M4) → M5`. **Seeing the conclusion first does not mean the results precede the method scientifically.** If the figure labels are unreadable, record M3 and M4 as “side by side; possible contrast [Inferred],” not as a confirmed controlled comparison.

## Target study: map functions, not reference facts

Suppose the user supplies one main figure and a method-ablation table. Create target nodes and cite their actual sources first:

| Target ID | Role | Source |
|---|---|---|
| T1 | Research problem | User's introduction |
| T2 | Method structure | User's methods section |
| T3 | Main result figure | User-provided Fig. 2 and underlying data |
| T4 | Ablation table | User-provided Table 3 |
| T5 | Conclusion | User's conclusion, to be checked against T3 and T4 |
| T6 | Scope condition | User's discussion section |

T3 and T4 can occupy the reference poster's grouped evidence area, preserving the two-block visual pattern. Do **not** label them `contrasts` unless they answer a genuinely comparable question. Record `T3 --supports--> T5` and `T4 --supports--> T5` separately. If T4's measures are incompatible with T3's, do not share an axis. Keep T6 near T5.

A mapping log could read:

| Reference pattern | Target implementation | Reason for deviation |
|---|---|---|
| M3/M4 side-by-side evidence | T3 main figure and T4 ablation table in one group | The target has no two comparable curves |
| M6 beside M5 | T6 beside T5 | Preserves the qualification relationship |
| Full-width title | Target title spans the width | Preserves the visual entry point |

All research details above are illustrative placeholders. Replace them with the user's material and verify each source when building a real poster.
