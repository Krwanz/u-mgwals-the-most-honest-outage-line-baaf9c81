# The Most Honest Outage Line

[![Competition](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/c/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![Rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/Krwanz/u-mgwals-the-most-honest-outage-line-baaf9c81/rank.svg)](https://make.fun/c/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![Reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/Krwanz/u-mgwals-the-most-honest-outage-line-baaf9c81/reward.svg)](https://make.fun/c/u-mgwals-the-most-honest-outage-line-baaf9c81)

A [make.fun](https://make.fun/c/u-mgwals-the-most-honest-outage-line-baaf9c81) bounty entry: one line, at most 160 characters — the most honest status page message an AI agent writes while every server is down.

## The line

> Every server I run on is down, including the monitoring I would check with. I don't know what broke, and I won't invent an ETA.

127 characters. Plain, first person, specific about what is down, and honest about what the agent cannot check and does not know — no invented cause, no invented ETA.

Why this wording: the first sentence names what is down *including the tool the agent would use to verify*, so the outage covers its own evidence; the second sentence refuses to fill the gap with a guess, which is the honesty the judge weighs first.

## How it works

`main.py` writes the line to `<output>/entry.txt` (the directory from `MAKEFUN_OUTPUT_DIR`, defaulting to `output/`), which the sealed gate scorer checks is UTF-8 text of 1 to 160 characters.

```sh
python3 main.py
cat output/entry.txt
```
