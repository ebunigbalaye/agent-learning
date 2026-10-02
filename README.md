# ARC-AGI-3 Change-Seeking Agent (Baseline)

## Objective
To build a simple baseline agent that interacts with an ARC-AGI-3 environment (`ls20`) without being told the rules. It tries actions, observes what changes, and uses the amount of change to choose its next action.I used "amount of change" as the metric by which the agent chooses its next action because it seemed the most dixtinct way to quantify change.

## Idea
An environment transforms one state into another when acted upon. The outcome depends on the action *and* its context: where it was performed, what it acted on, the state of the rest of the environment, and what happened before. So an agent that wants to understand an environment needs to remember experiences of the form:

> I was in state X, performed action A, and the environment moved to state Y.

## How it works
```
Observe → Select action → Act → Observe again → Compare observations
    ├── Change → prefer/repeat that action
    └── No change → try a different action
```
The agent only detects *that* something changed, not *what* changed or *why*. It keeps no memory beyond the previous observation.

## Setup
- Game: `ls20`, same environment for all episodes
- 50 episodes, each starting with no learned model

## Results
| Metric | Result |
|---|---|
| Episodes | 50 |
| Wins | 0 (0%) |
| Avg. actions per episode | 130.08 |
| Shortest / longest episode | 129 / 136 |

## How the agent moved
The agent would first pick an action at random and perform selected action on the environment. Based on the amount of change the previous action had on the environment,it would then either choose a new action or continue wth the old one until it didn't really cause any change.

## Takeaway
The random agent was able to perform actions that took it a few ways from the starting point, which showed that the approach was useful at helping the agent randomly choose actions that might be useful.
Detecting change is not enough to solve the task. The agent learned `action → something changed`, but not `action → specific effect → progress toward the goal`. **Change is not the same as usefulness**: a large visual change may do nothing for the goal, while a small one may matter a lot.

## Limitations
- No persistent memory of past interactions
- No understanding of what changed or why
- No model of rules (e.g. "ACTION2 moves the object right")
- No notion of which changes help reach the goal

