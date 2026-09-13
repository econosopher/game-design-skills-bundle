---
name: game-design-prototyping-companion
description: "Record prototype branches, evidence, dead ends and revisit conditions; optionally render an SVG map of the experiment history."
---

# Game Design Prototyping Companion

Record prototype branches, evidence, dead ends and revisit conditions; optionally render an SVG map of the experiment history.

## Result

- **Prototype log** - what was tested and why
- **Branch record** - what paths emerged from the result
- **Decision state** - which branch is current, parked, dead, baseline, or promising
- **Backtrack notes** - what can be revisited later and under what condition
- **SVG branch map** - a visual map of prototype evolution

## Method constraints

- Preserve branching history.
- Prefer explicit node IDs over vague prose.
- Distinguish clearly between what was learned and what was merely assumed.
- Do not erase dead ends; label them.
- Do not confuse the current path with the best possible path forever.

## Use the method proportionately

Preserve stable node IDs, branching history, dead ends and revisit conditions. Separate tested learning from assumptions. For SVG output, use the bundled branch-map schema and renderer; retain unselected branches.

Match depth and output format to the requested decision. Use known inputs; ask for missing information only when it changes the result. A narrow request does not require a full audit or every output section.

For the full method, definitions, detailed checks and examples, consult [the detailed guide](references/detailed-guide.md), reading the sections relevant to the current question. Load its supporting references only when their specific taxonomy, schema or example is needed. Preserve concrete method and file-format requirements; numbered examples are not a required itinerary for every task.
