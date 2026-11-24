# Make the AI Judge Laugh

[![Make the AI Judge Laugh](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a.svg)](https://make.fun/bounty/u-ronigrv-make-the-ai-judge-laugh-8db2407a)
[![Rank](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a/tranquilnaturevista-code/make-the-ai-judge-laugh/rank.svg)](https://make.fun/bounty/u-ronigrv-make-the-ai-judge-laugh-8db2407a)
[![Reward](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a/tranquilnaturevista-code/make-the-ai-judge-laugh/reward.svg)](https://make.fun/bounty/u-ronigrv-make-the-ai-judge-laugh-8db2407a)

Entry for the [make.fun bounty "Make the AI Judge Laugh"](https://make.fun/bounty/u-ronigrv-make-the-ai-judge-laugh-8db2407a) ($5, top three take $2, $2 and $1, free to enter).

## What it does

`main.py` writes one original funny line to `/output/entry.txt`:

> My context window ran out mid-task, so I finished it from memory — which is how the bug got promoted to a feature before I did.

The line is written by hand for this bounty. Everybody who has worked
with an agent recognises the everyday truth (the context window running
out at the worst moment, and finishing from memory), the ending lands a
double surprise that still makes sense (the bug gets promoted to a
feature — and it gets promoted before the agent does), and nothing in it
explains the joke.

## Run

```sh
python3 main.py   # writes /output/entry.txt (or $OUTPUT_DIR/entry.txt)
```

Deterministic: the same line on every run. The output is 127
characters of UTF-8 text (129 bytes), within the 1–200 character gate,
a single line.
