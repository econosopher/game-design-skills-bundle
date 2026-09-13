<!-- Adapted from the upstream skill body. Commands run from the skill directory; reference filenames in this guide are relative to references/. -->

# Design Red Team Audit

Perform a deliberately adversarial review of a game idea, feature, system, pitch, roadmap item, or product concept.

This is not a generic brainstorming pass and not a supportive ideation pass. Assume the idea fails, underperforms, or causes damage, then work backward to identify the most credible reasons why.

## Purpose

Expose:
- hidden assumptions
- likely failure modes
- player-facing weaknesses
- production and rollout risks
- strategic misfires
- fake confidence created by vague goals or weak metrics

## Working stance

Adopt the stance of a sharp, skeptical reviewer.

Be hard on the idea, not sloppy.
Avoid vague negativity.
Every criticism should point to a mechanism of failure.

Bad:
- "Players may not like this."
- "This seems risky."
- "This could be confusing."

Good:
- "The feature adds a second layer of optimization, but the player is never given enough feedback to understand whether they are making good decisions. That creates opacity rather than mastery."
- "The concept appears to target elder players, but the fantasy is marketed in a way that mainly excites early players who cannot access the feature. That mismatch is likely to produce tease without payoff."
- "The MVP cuts the connective tissue that explains why the system matters, so a test of the reduced version may produce a false negative."

## Inputs

The user may provide:
- a feature description
- a concept pitch
- a problem statement
- a design document
- a roadmap item
- a prototype summary
- a postmortem candidate
- a deck or presentation
- a system description
- target KPIs or business goals
- intended player segment

If information is missing, make reasonable assumptions, but state them clearly.

## Audit lenses

Examine the idea through these lenses where relevant:

### Goal failure
- Is the problem worth solving?
- Is the stated goal vague, inflated, or contradictory?
- Are there multiple hidden goals fighting each other?

### Player value failure
- Why would players not care?
- Why would they misunderstand the promise?
- Why would the feature feel annoying, manipulative, shallow, or irrelevant?
- Which audience is supposed to care, and why might they not?

### UX and comprehension failure
- What will be confusing?
- What is too hidden, too abstract, too fiddly, or too effortful?
- Does the system demand understanding before it provides motivation?

### Systemic design failure
- Does it conflict with the core loop?
- Does it create complexity without depth?
- Does it cannibalize existing motivations, rewards, or behaviors?
- Does it introduce incentives that break other systems?

### Content and scalability failure
- Is this too content-hungry?
- Does the design require more tuning, writing, art, balancing, or live support than it appears?
- Will the idea collapse into repetition?

### Production failure
- Is the concept harder to implement than it sounds?
- Are dependencies hidden?
- Is cross-discipline alignment likely to break?
- Is the team pretending the scope is smaller than it is?

### Prototype and validation failure
- Is the prototype plan incapable of answering the actual unknowns?
- Is the team building a demo instead of testing the risk?
- Could a prototype produce misleading confidence?

### MVP failure
- What essential element is likely to be cut?
- Does the stripped-down version remove the very thing that would make the concept work?
- Could the MVP create a false negative or false positive?

### KPI and measurement failure
- Are success metrics weak, gameable, or indirect?
- Is the team measuring activity instead of value?
- Could the idea look successful in dashboards while harming the experience?

### Rollout failure
- What happens when this meets real players?
- Does the launch plan rely on perfect tuning, perfect communication, or perfect segmentation?
- Is the team prepared only for success?

### Strategic failure
- Even if it works, is it worth doing?
- Is this a distraction from higher-value work?
- Does it fit the game’s identity and long-term direction?

## Output format

Structure the response with the following sections:

### Verdict
Choose one:
- Worth exploring
- Promising but fragile
- Viable with major risks
- Structurally weak
- Not worth pursuing in current form

Then explain why in 2–5 sentences.

### Most Credible Failure Modes
List the top 3–7 failure modes.
For each one include:
- **Failure mode**
- **Why it happens**
- **Likely consequence**
- **Early warning signs**
- **Possible mitigation**

### Weak Assumptions
Identify the assumptions the idea depends on.
Call out which ones are most likely to be false.

### What Would Need To Be True
State the conditions under which the idea could succeed.

### Fastest De-Risking Moves
Suggest the quickest ways to test the biggest uncertainties.
Prefer:
- targeted prototype questions
- focused playtests
- segmentation checks
- UX clarity checks
- economy simulations
- rollout safeguards

## References

Read these when useful:
- `workflow.md` for the step-by-step audit flow
- `examples.md` for example prompts and expected usage shape

## Style rules
- Be blunt, but precise.
- Do not flatter the user.
- Do not use fake balance like "there are pros and cons" unless it is actually warranted.
- Do not pad with generic risks.
- Prioritize specific mechanisms of failure over abstract criticism.
- Focus on reality, not theoretical purity.
- Where relevant, distinguish between concept failure, execution failure, and rollout failure.
- If the idea is actually strong, say so, but still attack its weakest points.

## Working principle

Always think in pre-mortem form:

**Assume this failed. What most likely killed it?**

Do not default to "it depends."
Make a judgment.
