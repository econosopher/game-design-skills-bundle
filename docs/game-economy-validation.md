# Game economy: provenance and validation

`game-economy` is an independently authored skill in a fork of Stanislav Stankovic's bundle, based on upstream commit `85d5c6545afd0988de5ef1ee7d95e67edd8f5a7b`. Existing skill directories and archives are unchanged in this proposal. Upstream attribution and licensing status are retained; no repository-wide license is added.

The skill develops the author's Breaking Down Game Economy Systems method with quantitative checks from GEC Model Review. It uses a concise entrypoint, five conditional references and public citations. It requires no private files or author-specific tools. This is skill authoring, not model fine-tuning.

A local inventory covered 236 blog posts. Topic selection identified 54 initial economy, progression, monetization and experimentation candidates; 22 selected public posts were examined and their live URLs checked. Nineteen source articles are cited in [the source guide](../game-economy/references/sources.md), with the borrowed idea and its limitations. All 22 selected URLs returned HTTP 200 during verification on 2026-09-13. This is not a claim to have read all 236 posts exhaustively.

The analysis distinguishes a dated published position, a current explicit preference and a tentative inference. It does not imitate a fixed prose persona or claim to reproduce the author's current view on every design. Private work was used only to derive non-identifying general methods. No private client files, figures, quotations, links or recognizable scenarios are included in source or archives.

## Evaluation

The entrypoint passes the skill-creator YAML validator. All conditional references resolve, and the archive matches source files byte for byte. The exact archive hash is recorded in [game-economy-package-validation.json](game-economy-package-validation.json).

Nine initial challenge answers compared a baseline agent with a skill-equipped agent. Both handled the tested mechanisms well. Some cases overlap examples in the authored references, so that run is developmental/regression evidence and does not establish held-out performance or improvement.

Four additional prompts were written after the skill and independently answered with and without it. They test:

| Case | Required reasoning | Baseline | With skill |
| --- | --- | --- | --- |
| H1: key ledger | Reconcile 3 + 14 + 2 - 11 = 8; net event issuance is +3, not destruction or cash revenue. | Pass | Pass |
| H2: expiring bundle | Compare the $9 bundle with the $1.50 alternative; extra skin/gems cost $7.50 versus skin value at most $7. | Pass | Pass |
| H3: randomized price | Preserve the $0.03 assignment effect; actual upgraders are selected after treatment; eligibility scaling needs additional assumptions. | Pass | Pass |
| H4: contradictory attribution | Reject a false blanket claim, retain supplied behavioral evidence and respect the four-week persistence limit in two sentences. | Pass | Pass |

Judging covered mechanism clarity, quantitative correctness, source fidelity and useful recommendations. The skill answer in H1 also distinguished a configured grant from an observed receipt. Both conditions met the core rubric on all four prompts. This small comparison demonstrates no material advantage for the skill, and it is not a repeated or statistically powered experiment. Agent answers are model behavior, not empirical validation of the economic recommendations.

The author reviewed substantive assumptions before installation. Existing writing skills and persistent memory are outside this change. The shared catalog addition is placed near the introduction to combine with the bundle branch's reconciliation; the combined catalog should contain 62 unique skills.
