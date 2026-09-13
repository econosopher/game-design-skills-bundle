<!-- Adapted from the upstream skill body. Commands run from the skill directory; reference filenames in this guide are relative to references/. -->

# Game Design One Thing To Remove

Improve the design by cutting one thing, not by adding three more.

Use this skill when a design would likely become better through subtraction. The goal is not to nitpick random dislikes. The goal is to identify the one removal with the highest leverage: the thing whose absence would most improve clarity, pacing, focus, emotional impact, usability, production efficiency, or strategic coherence.

Read `removal-lenses.md` when deciding what kind of thing is most worth cutting.
Read `evaluation-patterns.md` when you need the exact output pattern.

## What to produce

Produce:
1. **Design read** - what the design is trying to do
2. **Removal candidate** - the one thing to remove
3. **Why this removal has highest leverage** - why this cut matters more than others
4. **What improves if removed** - concrete downstream effects
5. **Tradeoff** - what value is lost too
6. **Value-preserving alternative** - how to keep the good part without the bad part, if needed
7. **Verdict** - remove now, prototype without it, or cut later if evidence confirms

## Process

### Understand what the design is trying to achieve
Clarify:
- the intended player experience
- the core loop or promise
- which parts feel central versus decorative
- what business, retention, content, or production realities matter

### Look for subtractive opportunities
Check whether the design contains:
- redundant mechanics
- duplicate progression layers
- false choices
- low-value friction
- weak reward currencies
- tutorial clutter
- content burdens that add little value
- fantasy dilution
- complexity that does not create meaningful depth

### Identify the highest-leverage removal
Pick one thing only.
Do not list five cuts unless the user explicitly asks.
Choose the removal whose absence would improve the design most significantly.

Good candidates include:
- one mechanic
- one progression layer
- one UI step
- one rule or constraint
- one reward type
- one content dependency
- one feature that muddies the fantasy

### Explain the mechanism of improvement
Do not say only that the design becomes “cleaner.”
Explain exactly what improves, such as:
- comprehension
- pacing
- motivation
- readability
- strategic clarity
- production sustainability
- onboarding burden
- player trust
- emotional focus

### Acknowledge the loss honestly
A good cut may still remove something useful.
State what is lost and whether that loss matters.
If appropriate, suggest a lighter substitute that preserves the upside without keeping the full problematic element.

### Make a practical recommendation
End with a decision such as:
- remove now
- prototype without it
- keep for now, but cut if testing confirms the issue

## Example response structure

### Design Read
- ...

### One Thing I Would Remove
- ...

### Why This Is the Highest-Leverage Cut
- ...

### What Improves If Removed
- ...

### What You Lose
- ...

### How To Preserve the Good Part Without the Bad Part
- ...

### Verdict
- ...

## Fast mode
- What is the design trying to do?
- What single element is hurting it most?
- Why is that element more worth cutting than anything else?
- What gets better if it disappears?
- What should replace it, if anything?

## Style rules
- Be decisive.
- Pick one thing.
- Prefer mechanism over taste.
- Do not recommend removal just because something is complex; complexity is acceptable if it creates real value.
- Distinguish between elegant subtraction and destructive oversimplification.
- If nothing should be removed, say that clearly and explain why.

## Working principle

Many designs get worse because every problem is answered with addition.
Sometimes the best improvement is subtraction with intent.
