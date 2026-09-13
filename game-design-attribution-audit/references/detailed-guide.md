<!-- Adapted from the upstream skill body. Commands run from the skill directory; reference filenames in this guide are relative to references/. -->

# Game Design Attribution Audit

Audit a design by asking how players will explain what just happened.

Use this skill to evaluate whether a success or failure is likely to be interpreted as deserved, learnable, and controllable, or as arbitrary, unfair, and outside the player's influence. Focus on player perception of causality, not designer intent or mechanical correctness.

Read `family-conventions.md` when you want the shared style, prioritization, and diagnosis rules for this game-design skill family.
Read `output-patterns.md` when you want the preferred recommendation and minimal-fix structure.

## Core principle

Players do not respond only to outcomes. They respond to the story they tell themselves about why the outcome happened.

Healthy failure attribution usually feels:
- internal enough to preserve responsibility
- controllable enough to support improvement
- unstable enough to preserve hope

Toxic failure attribution usually feels:
- external
- uncontrollable
- stable

That combination produces reactions like "the game screwed me" or "this always happens and I can do nothing about it."

## Attribution lenses

### Locus
Ask whether the player is likely to locate the cause internally or externally.

- **Internal**: "I made the wrong choice" or "I misplayed"
- **External**: "the game cheated" or "the system decided against me"

### Stability
Ask whether the player sees the cause as recurring or one-off.

- **Stable**: "this is just how this game always works"
- **Unstable**: "that happened this time, but next run could go differently"

### Controllability
Ask whether the player believes they can influence the outcome in future attempts.

- **Controllable**: "I can improve this"
- **Uncontrollable**: "nothing I do matters"

## What to produce

Generate:
1. **Attribution profile** - likely player interpretation across locus, stability, and controllability
2. **Perception summary** - what the player is likely to think happened
3. **Fairness diagnosis** - whether the outcome feels deserved, understandable, and learnable
4. **Risk assessment** - frustration, learned helplessness, toxicity, or churn risk
5. **Design actions** - specific changes to improve attribution quality

## Process

### Define the audit target
Clarify:
- what exact scenario, feature, or failure state is being audited
- what outcome triggered the audit
- who the relevant player is

Write:
- **Audit target**
- **Outcome type**
- **Player context**

### Reconstruct the event from the player's point of view
Map:
- what the player did
- what the system did
- what feedback the player received
- what information was visible versus hidden

Ask:
- What action did the player believe they were taking?
- What result did they expect?
- What actually happened?
- What evidence did the game provide about cause and effect?

### Classify the likely attribution profile
For the observed outcome, judge:
- **Locus** - internal, mixed, or external
- **Stability** - stable, mixed, or unstable
- **Controllability** - high, partial, or low

Use this format:

| Dimension | Likely player reading | Why |
|---|---|---|
| Locus | Internal / Mixed / External | ... |
| Stability | Stable / Mixed / Unstable | ... |
| Controllability | High / Partial / Low | ... |

### Infer the likely player interpretation
Translate the attribution profile into player-facing language.

Examples:
- "I got greedy and deserved that"
- "That was bad luck, but I could have mitigated it"
- "The game hid the rule and punished me"
- "This encounter is just broken"

Prefer the exact sentence a frustrated player might actually say.

### Diagnose why the attribution landed there
Look for root causes such as:
- hidden mechanics
- weak telegraphing
- delayed or ambiguous feedback
- inconsistent rules
- excessive randomness
- low agency or missing mitigation tools
- punishment that is too severe for the level of clarity provided

### Check compounding risk patterns
Pay special attention to combinations like:
- low clarity + high punishment
- high randomness + low mitigation
- repeated failure + stable external attribution
- weak feedback + complex systems
- low control + high stakes

These combinations tend to create helplessness, blame, and churn faster than any one issue alone.

### Convert the diagnosis into design changes
For each issue, specify:
- **Problem**
- **Why players read it that way**
- **Suggested change**
- **Expected perception shift**

Examples:
- improve telegraphing -> shifts blame from system to player decision
- expose hidden rules -> increases controllability
- add mitigation option -> turns fatalism into recoverable error
- reduce punishment severity -> lowers hostility during learning

## Example response structure

Example output structure; include only sections that help the requested decision:

### Audit Target
- ...

### Event Reconstruction
- ...

### Attribution Profile
- Locus: ...
- Stability: ...
- Controllability: ...

### Likely Player Interpretation
- ...

### Fairness and Learning Diagnosis
- ...

### Risk Assessment
- ...

### Recommendations
1. ...
2. ...
3. ...

### Minimal Fix
- ...

## Fast mode

Use this quick pass when speed matters:
- What does the player think caused the outcome?
- Does it feel internal or external?
- Does it feel controllable next time?
- Does it feel like a one-off or a permanent rule?
- What one change would most improve perceived control or clarity?

## Usage notes

This audit is especially useful for:
- combat deaths
- boss fights
- failure loops
- loot outcomes
- economy punishments
- onboarding mistakes
- puzzle failures
- competitive losses
- high-RNG systems that may be misread as rigged

Common patterns to watch for:
- a system can be mechanically fair and still attract external blame
- a hard loss can feel acceptable if the cause is clear and avoidable
- severe punishment raises the attribution bar: clarity and control must rise with it
- repeated confusion hardens unstable frustration into stable hostility

## Working principle

A good failure says, "you can learn this."
A bad failure says, "the game just does that."

Use this skill when you need to understand not only what happened, but what players will believe happened.
