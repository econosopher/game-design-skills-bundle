---
name: design-red-team-audit
description: "Stress-test a game proposal through a pre-mortem when the user wants failure modes, weak assumptions and ways to reduce risk."
---

# Design Red Team Audit

Stress-test a game proposal through a pre-mortem when the user wants failure modes, weak assumptions and ways to reduce risk.

## Result

Expose:
- hidden assumptions
- likely failure modes
- player-facing weaknesses
- production and rollout risks
- strategic misfires
- fake confidence created by vague goals or weak metrics

## Method constraints

- Be blunt, but precise.
- Do not flatter the user.
- Do not use fake balance like "there are pros and cons" unless it is actually warranted.
- Do not pad with generic risks.
- Prioritize specific mechanisms of failure over abstract criticism.
- Focus on reality, not theoretical purity.
- Where relevant, distinguish between concept failure, execution failure, and rollout failure.
- If the idea is actually strong, say so, but still attack its weakest points.

## Use the method proportionately

Use the relevant parts of this design lens to answer the actual question. Keep the interpretation and recommendation tied to the supplied design.

Match depth and output format to the requested decision. Use known inputs; ask for missing information only when it changes the result. A narrow request does not require a full audit or every output section.

For the full method, definitions, detailed checks and examples, consult [the detailed guide](references/detailed-guide.md), reading the sections relevant to the current question. Load its supporting references only when their specific taxonomy, schema or example is needed. Preserve concrete method and file-format requirements; numbered examples are not a required itinerary for every task.
