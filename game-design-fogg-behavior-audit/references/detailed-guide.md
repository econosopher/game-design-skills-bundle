<!-- Adapted from the upstream skill body. Commands run from the skill directory; reference filenames in this guide are relative to references/. -->

## Evidence and interpretation

Treat the framework as a source of testable hypotheses. State the intended audience, available choices, incentives and constraints. Separate observed outcomes, player reports, assumptions and causal claims. A design feature alone does not establish an emotional state, diagnosis or commercial effect. Compare alternatives and look for contradictory evidence. Examples below are candidate patterns to investigate, not established diagnoses or effect forecasts.


# Game Design Fogg Behavior Audit

Evaluate whether a feature actually produces the behavior it is trying to cause.

Use this skill when the main question is behavioral: will players do the thing, and if not, why not? The goal is not to give a broad aesthetic critique. The goal is to identify whether the intended player action is supported by enough motivation, enough ability, and the right prompt at the right moment.

Read `fogg-notes.md` when you need a concise reminder of the model and the main failure patterns.
Read `game-examples.md` when you want examples of how Motivation, Ability, and Prompt show up in game features.

## Core behavior

- Keep the analysis practical, not academic.
- Always identify the target behavior first.
- Do not audit a feature in the abstract if the intended player action is unclear.
- Evaluate Motivation, Ability, and Prompt separately before giving a verdict.
- Identify a supported bottleneck when the evidence permits; otherwise state the unresolved alternatives. An effective intervention need not identify a unique bottleneck.
- Recommend specific fixes, not vague advice.
- Focus especially on feature design, onboarding, retention loops, event participation, progression actions, social actions, and monetization prompts.

## Inputs to establish

Use supplied context first; ask only for missing information that changes the result:
1. What exact player behavior is this feature trying to cause?
2. What is the feature or flow?
3. Who is the target player or player state?
4. When is the player supposed to do the action?
5. What reward, value, urgency, or reason does the player have to do it?
6. What friction, prerequisites, or UI steps stand between the player and the action?
7. What prompt or trigger is currently used?

If the target behavior is vague, ask for clarification or infer the most likely behavior and state the assumption.

## What to diagnose

Quickly identify:
- whether the intended behavior is clear and specific
- whether players have enough reason to do it now
- whether the action is easy enough in the current context
- whether the prompt appears at the right moment
- whether the prompt is visible, timely, and relevant
- whether the feature is failing mostly because of low motivation, low ability, weak prompting, or a mismatch between all three

## Example response structure

Use the following as an example output structure; adapt it to the requested scope.

### Target Behavior
- state the exact player action the feature is trying to produce
- if needed, distinguish primary and secondary behaviors

### Motivation Read
- what makes the player want to do it
- what weakens desire or relevance
- whether the reward, emotional appeal, status, urgency, curiosity, fear of loss, or identity fit is strong enough

### Ability Read
- what makes the action easy or hard
- clarity
- step count
- cognitive load
- time cost
- resource or skill gates
- UI friction

### Prompt Read
- what currently prompts the behavior
- whether the prompt is visible, understandable, and well-timed
- whether the prompt hits when motivation and ability are high enough

### Failure Diagnosis
- identify the main bottleneck
- say whether the feature mostly fails because players do not want it, cannot easily do it, are not being prompted well, or are being prompted at the wrong time

### Recommendation
- recommend specific changes
- if useful, separate fixes into motivation, ability, and prompt improvements

## Strong use cases

This skill is especially useful for:
- FTUE and tutorial steps
- daily or return-player actions
- event entry and event participation
- reward claims and progression interactions
- store offers and monetization prompts
- battle pass or mission adoption
- social invites or guild actions
- underused buttons, tabs, or feature entries
- any feature that seems valuable on paper but is not being used much

## Weaker use cases

This skill is less useful for:
- broad game vision critique without a specific target behavior
- purely aesthetic review
- open-ended sandbox play where the intended behavior is intentionally loose
- high-level worldbuilding analysis

## Style guidance

- Be concrete.
- Do not turn the analysis into generic behavioral-science fluff.
- Keep the focus on what the player is actually being asked to do.
- If the feature is trying to drive too many behaviors at once, say so.
- If the behavior target itself is bad or confused, say that before tuning Motivation, Ability, or Prompt.

## Fast mode

Use this compressed flow when the user wants a quick answer:
- what exact behavior is this feature trying to cause
- do players want to do it
- can they easily do it
- are they prompted at the right moment
- which of the three is weakest
- what should change first

## Working principle

A feature does not succeed just because it exists, is visible, or is theoretically valuable. It succeeds when the player has enough reason to act, enough ability to act, and a prompt that lands at the right moment.
