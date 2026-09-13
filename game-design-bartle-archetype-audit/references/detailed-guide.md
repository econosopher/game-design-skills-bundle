## Evidence boundary

These are historical design hypotheses from [Bartle's MUD taxonomy](https://mud.co.uk/richard/hcds.htm), developed from discussion among experienced players in one commercial MUD. They are not a universal psychometric classifier, population shares or calibrated retention model. Treat the preference descriptions and interaction patterns below as candidate mechanisms to test in the current audience. Intentional unequal coverage can be appropriate. Do not infer a human trait or diagnosis from a play action.

<!-- Adapted from the upstream skill body. Commands run from the skill directory; reference filenames in this guide are relative to references/. -->

# Game Design Bartle Archetype Audit

Audit a design by asking which Bartle-type players it serves, frustrates, excludes, or accidentally overfeeds.

Use this skill to evaluate how a game or feature lands with four classic player archetype lenses:
- **Achievers** - driven by progress, status, optimization, completion, and measurable advancement
- **Explorers** - driven by discovery, experimentation, hidden depth, and systemic curiosity
- **Socializers** - driven by connection, expression, cooperation, recognition, and shared play
- **Killers** - driven by domination, disruption, competition, advantage, and impact over others

Treat these as motivational lenses, not rigid personality boxes.

## Core principle

A feature rarely serves all player archetypes equally.

That is not automatically a problem. The real question is whether the imbalance is intentional and compatible with the broader game. A design can succeed by strongly serving one archetype, but it can also fail by unintentionally alienating others or by overfeeding one motivational pattern until it distorts the whole experience.

## What to produce

Generate:
1. **Audit target** - what is being reviewed and what it is supposed to do
2. **Archetype-by-archetype reading** - how each Bartle lens experiences the design
3. **Motivational profile** - which archetypes are strongly served, weakly served, or actively harmed
4. **Imbalance diagnosis** - where the design overcommits, neglects, or creates conflicts with the intended experience
5. **Recommendations** - what to strengthen, soften, separate, or clarify

## Process

### Define the audit target
Clarify:
- what is being audited
- what the feature or system is supposed to achieve
- what player segment it seems primarily aimed at
- whether it is core, optional, early-game, mid-game, endgame, or event-based

### Audit for Achievers
Ask:
- Does this provide clear goals, progress, ranks, milestones, or measurable completion?
- Is advancement legible and satisfying?
- Are there optimization hooks or mastery ladders?
- Does the system reward effort and planning in a visible way?
- Does it create grind without meaningful payoff?

Look for:
- progression clarity
- completion pressure
- reward cadence
- rank/status markers
- optimization opportunities
- scoreboard or collection incentives

### Audit for Explorers
Ask:
- Does this create opportunities for discovery, experimentation, hidden depth, or surprising interactions?
- Is there anything to uncover, test, or learn beyond the obvious path?
- Does the feature reward curiosity, or punish deviation from the intended route?
- Is the system too solved, too explicit, or too shallow to explore?

Look for:
- secrets or hidden layers
- systemic depth
- expressive experimentation
- optional discovery
- mystery and possibility
- non-obvious interactions

### Audit for Socializers
Ask:
- Does this support cooperation, expression, social recognition, gifting, helping, belonging, or conversation?
- Are there reasons to share, show, support, or coordinate?
- Does it create social presence or only social metrics?
- Does the system feel socially alive or socially sterile?

Look for:
- communication value
- collaboration loops
- group identity
- mutual dependency
- recognition and expression
- emotionally meaningful social rituals

### Audit for Killers
Ask:
- Does this allow players to dominate, disrupt, outplay, pressure, or visibly outperform others?
- Is there direct or indirect competition?
- Does the system create status through relative power?
- How does competition affect the intended audience and other participants?
- Could killer-facing incentives distort the feature for everyone else?

Look for:
- PvP or rivalry energy
- visible advantage
- denial or disruption power
- dominance loops
- competitive prestige
- asymmetric leverage over others

### Build the archetype profile
For each archetype, rate the design as:
- **Strongly served**
- **Moderately served**
- **Weakly served**
- **Actively frustrated**

Use this format:

| Archetype | Rating | Why | Likely Response |
|---|---|---|---|
| Achievers | ... | ... | ... |
| Explorers | ... | ... | ... |
| Socializers | ... | ... | ... |
| Killers | ... | ... | ... |

### Diagnose imbalance and cross-archetype friction
Ask:
- Is the feature clearly built for one archetype while pretending to serve all?
- Does one archetype's reward structure damage another's experience?
- Is the design too narrow for the place it occupies in the game?
- Does the game need this system to be broad, or is specialization acceptable here?

Common imbalance patterns:
- **Achiever trap** - everything becomes checklist, grind, ranking, and completion pressure
- **Explorer starvation** - system is legible but dead, with nothing to discover or test
- **Social shell** - other people are visible, but there is no real social meaning
- **Killer contamination** - competitive pressure warps a space that should feel safe, expressive, or cooperative
- **False inclusivity** - feature signals broad appeal but meaningfully serves only one player type

### Convert findings into design actions
For each major issue, specify:
- **Archetype affected**
- **Current issue**
- **Design cause**
- **Suggested change**
- **Expected effect**

## Example response structure

### Audit Target
- ...

### Achievers
- Strengths: ...
- Weaknesses: ...

### Explorers
- Strengths: ...
- Weaknesses: ...

### Socializers
- Strengths: ...
- Weaknesses: ...

### Killers
- Strengths: ...
- Weaknesses: ...

### Archetype Profile
- ...

### Imbalance Diagnosis
- ...

### Recommendations
1. ...
2. ...
3. ...

## Fast mode
- Which archetype is this mainly serving?
- Which archetype is getting the least value?
- Which archetype could be actively harmed by this design?
- Is that imbalance intentional and acceptable?
- What one change would improve the weakest archetype fit without breaking the strongest one?

## References

Read these when useful:
- `bartle-notes.md` for a concise interpretation of the four archetypes in game-design terms
- `failure-patterns.md` for common archetype imbalance shapes

## Working principle

A feature does not need to satisfy every Bartle archetype equally.
But if it strongly privileges one motivational type, that should be by design, not by accident.
