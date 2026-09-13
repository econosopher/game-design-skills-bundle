<!-- Adapted from the upstream skill body. Commands run from the skill directory; reference filenames in this guide are relative to references/. -->

## Evidence and interpretation

Treat the framework as a source of testable hypotheses. State the intended audience, available choices, incentives and constraints. Separate observed outcomes, player reports, assumptions and causal claims. A design feature alone does not establish an emotional state, diagnosis or commercial effect. Compare alternatives and look for contradictory evidence. Examples below are candidate patterns to investigate, not established diagnoses or effect forecasts.


# Game Design Goal Density and Immediacy Audit

Audit a design by asking whether players can quickly find a meaningful goal, pursue it within the time they have, and leave the session feeling both satisfied and pulled to return.

Use this skill to evaluate how a game structures player time. Focus on the density of available goals, how immediate those goals feel, how they ladder across time horizons, whether players can end a session safely, and what return triggers bring them back.

## Core principle

A strong session structure does not depend on one perfect goal.
It gives the player enough meaningful goals of different sizes and time horizons that they can pick one that fits the time, energy, and attention they currently have.

## What to produce

Generate:
1. **Audit target** - what is being reviewed and what kind of session pattern it supports
2. **Goal density audit** - how many meaningful goals are available at once and how varied they are
3. **Goal immediacy audit** - how quickly the player can identify something worth doing now
4. **Time-horizon breakdown** - short-term, mid-term, and long-term goals
5. **Session closure audit** - whether the player can leave at a safe, satisfying moment
6. **Return-trigger audit** - what unfinished business pulls the player back
7. **Recommendations** - what to add, remove, clarify, pace, or restructure

## Process

### Define the audit target
Clarify:
- what system, feature, or game is being audited
- what kind of session pattern it expects: short bursts, long sessions, mixed sessions
- whether the design is FTUE, return-player experience, core loop, metagame, or elder game
- what player context matters most

### Audit goal immediacy
Ask:
- When the player opens the game, how quickly can they identify a meaningful thing to do?
- Does the game help the returning player select a new goal?
- Is the most important current opportunity visible enough?
- Does the game over-rely on the player remembering what they were doing last session?
- Is the player choosing a goal, or wandering through UI trying to figure out what matters?

Look for:
- visible session entry points
- clear next-step candidates
- strong current priorities
- low friction between logging in and acting
- support for self-directed goal choice

### Audit goal density
Ask:
- How many meaningful goals are available at a given moment?
- Do goals vary in size, difficulty, and time requirement?
- Can different players find different goals that fit different amounts of available time?
- Is the game sparse and aimless, or overcrowded and noisy?
- Does the metagame provide enough context to make multiple goals feel meaningful?

Look for:
- multiple simultaneous goal candidates
- different effort bands
- different reward horizons
- overlap between core goals and meta goals
- enough choice without drowning the player

### Break down goals by time horizon
Evaluate whether the design offers a purposeful spread of goals across these horizons:

#### Short-term goals
Goals that can usually be started and often completed in one brief session.
Examples:
- one level
- one race
- one mission
- claim and spend loop
- craft one needed item
- collect one reward tier

Ask:
- Are there enough goals that fit tiny pockets of time?
- Can a player feel accomplished in a short session?
- Are short-term goals meaningful, or merely mechanical chores?

#### Mid-term goals
Goals that take several sessions or a moderate amount of focused play.
Examples:
- finish a chapter
- upgrade a subsystem
- unlock a feature tier
- complete an event milestone band
- build a new district or unit composition

Ask:
- Does the game provide medium-range projects worth caring about?
- Do these goals create continuity between sessions?
- Are they paced well, or do they feel either trivial or exhausting?

#### Long-term goals
Goals that define sustained engagement over days, weeks, or longer.
Examples:
- finish a season pass
- complete a major collection
- reach elder-game mastery
- build out a city fantasy
- reach endgame social or competitive status

Ask:
- What gives long-term meaning to repeated sessions?
- Are long-term goals visible enough to inspire commitment?
- Are they aspirational, or just distant grind walls?

Use this format:

| Horizon | Examples Present | Strength | Main Issue |
|---|---|---|---|
| Short-term | ... | ... | ... |
| Mid-term | ... | ... | ... |
| Long-term | ... | ... | ... |

### Audit session flexibility
Ask:
- Can the game support different session lengths?
- Can a player with 2 minutes, 10 minutes, or 45 minutes still do something meaningful?
- Does the structure adapt to fragmented real-life schedules?
- Does the design force one ideal session length too rigidly?

Look for:
- flexible stopping points
- scalable goal selection
- both burst-friendly and longer-form activity options where appropriate

### Audit session closure and safe stopping points
Ask:
- Can the player end the session at a satisfying moment?
- Does the game provide a sense of completion before exit?
- Does the player feel safe leaving, or feel like the game is still on fire without them?
- Are there explicit or implicit signs that nothing urgent remains?

Look for:
- clear stopping moments
- closure after achieving a goal
- no lingering obligation spikes
- reduced anxiety around leaving the game

### Audit return triggers
Ask:
- What unfinished business motivates return?
- Does the player leave with a reason to come back?
- Are return triggers restrictive and imposed, or self-owned and player-shaped?
- Does the game model time away from play intelligently?

Look for:
- production loops
- chest timers
- growth cycles
- event cadence
- self-set goals
- appointment mechanics

Also ask:
- Does the return trigger create anticipation, or only obligation?
- Does it support agency, or mostly remove it?

### Diagnose common failure patterns
Common patterns:
- **Goal drought** - too few meaningful goals, player feels aimless
- **Goal smog** - too many competing goals with no clear priority
- **No immediate hook** - player returns but does not see what to do now
- **Chore density** - many goals exist, but they feel trivial, repetitive, or low-meaning
- **Mid-term gap** - good micro-goals and big aspirations, but weak medium-range projects
- **Long-term fog** - sessions exist, but no larger arc gives them meaning
- **Bad fit for fragmented time** - game only works in one session length
- **Unsafe exit** - player feels punished or anxious for stopping
- **Obligation loop** - return triggers rely on pressure more than anticipation

### Convert findings into design actions
For each major issue, specify:
- **Issue**
- **Why it hurts the experience**
- **Affected horizon** - short, mid, long, or session closure/return
- **Suggested change**
- **Expected effect**

## Example response structure

### Audit Target
- ...

### Goal Immediacy
- Strengths: ...
- Weaknesses: ...

### Goal Density
- Strengths: ...
- Weaknesses: ...

### Time-Horizon Breakdown
- Short-term: ...
- Mid-term: ...
- Long-term: ...

### Session Closure
- ...

### Return Triggers
- ...

### Failure Patterns
- ...

### Recommendations
1. ...
2. ...
3. ...

## Fast mode
- When the player returns, do they instantly see something meaningful to do?
- Are there enough goals of different sizes to fit different session lengths?
- What are the short-term, mid-term, and long-term goals?
- Can the player stop safely and feel satisfied?
- What specifically pulls them back next time?

## References

Read these when useful:
- `goal-density-notes.md` for the source-derived framing around player time, session anatomy, density of goals, and return triggers
- `failure-patterns.md` for common goal-density and immediacy failure shapes

## Working principle

Designing sessions means modeling the player's time both with the game and away from it.
A strong game helps the player find a meaningful goal now, achieve enough to feel satisfied, and leave with a reason to come back.
