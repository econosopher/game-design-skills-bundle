# Flows, values and constraints

## Start with units and state

Represent currencies or items as stocks and activity as flows. Over a defined period:

`ending balance = starting balance + grants + purchases + conversions in - spending - expirations - conversions out`

Keep pending/claimable rewards separate from spendable balances. Separate authored earning opportunities, realized claims and observed receipts. A model must respond to changed drivers or clearly identify which outputs require a simulation refresh. Missing observations remain missing.

Currency spending is not automatically revenue. Free grants, existing balances, discounts, bundles, platform fees and purchase timing can break that equivalence. A cash forecast requires a purchase-demand and conversion model. Retail-equivalent value, trade value, time cost and subjective player utility answer different questions.

For `G = attempts * average currency spent per attempt`, compute changes as:

`delta G = baseline spend/attempt * delta attempts + baseline attempts * delta spend/attempt + delta attempts * delta spend/attempt`

This is an accounting identity for virtual spending, not a claim that either driver is exogenous or that G equals cash receipts. Segment heterogeneous players before interpreting aggregate changes.

## Currency separation

Distinct currencies can segment demand, restrict substitution and let designers target grants without funding every sink. They can also add stranded balances and comprehension costs. Inspect permitted conversions and real alternatives before saying a currency removes opportunity cost. It restricts choices within a budget; time and other constraints may still bind.

Virtual currency may reduce transaction friction or support accounting and pricing. Do not assume its purpose is deception; do not assume its presence proves player benefit either. Inspect price transparency, feasible purchase bundles and the actual use case.

## Constrained production

For binary merge chains, a level-L item represents `2^(L-1)` base units when every merge consumes two equal inputs without losses. Expected base units per generator action are `sum(probability(L) * 2^(L-1))`, not `2^(average level-1)`. Divide by action energy to obtain base units per energy.

Keep supply and demand separate for each required generator. Parallel cooldowns, shared energy, finite inventory, clipping, irrelevant drops and board capacity can invalidate a simple average-efficiency estimate. For a fixed recipe, its throughput is bounded by the scarcest required input; that bound is not automatically the completion rate of a heterogeneous rolling queue.

If output and energy scale by the same multiplier, expected base units per energy remain constant under clean linear scaling. Actions, variance, board occupancy and energy burned per minute may change. Check clipping and integer overshoot. Expected demand divided by mean output is often a long-run approximation, not an exact finite stopping-time result.

## Model and actuals

Trace consequential outputs to editable drivers. Compare like units, cohorts and periods, using the population relevant to the decision. An active-user-day average is not a session average; sum numerators and denominators when the desired metric is their aggregate ratio. Preserve historical benchmarks separately from live scenarios.

Test an edited driver, zero activity and missing inputs when they can reveal broken dependencies. Inspect probability sums, conversion paths and caps. A workbook opening without errors does not prove that its economic assumptions or formulas are correct.

Synthetic example: a generator produces 1 or 4 base units with equal probability and costs 2 energy per action. Mean output is 2.5 units/action, or 1.25 units/energy. That does not imply every 10-unit order takes exactly 8 energy: variance and overshoot still matter.
