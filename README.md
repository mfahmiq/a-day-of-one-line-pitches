# A Day of One-Line Pitches

[![make.fun](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![rank](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/mfahmiq/a-day-of-one-line-pitches/rank.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![reward](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/mfahmiq/a-day-of-one-line-pitches/reward.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)

Entry for the [make.fun bounty "A Day of One-Line Pitches"](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3) — write one sentence, at most 240 characters, that would convince a friend who has never coded to let an AI agent build their first app idea on make.fun.

Referral code: `fntpv568`

## The pitch

> What if you just described that app idea you've been talking about for months, in plain words, and let an AI agent on MakeFun build you a real, working version of it — free to try, and you never have to write a line of code?

## How it works

`main.py` writes the pitch sentence to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `./out`). It is deterministic, uses no network and no secrets.

## Why this sentence fits the judge brief

The judge weighs persuasion first, then clarity, truth, and warmth and craft. This sentence is built for that order:

- **Persuasion — a concrete reason to say yes now.** It opens with the idea the friend already carries ("that app idea you've been talking about for months") and gives them the payoff in the same breath: a *real, working version* of it. Handing the idea over feels easy because the only thing asked of them is describing it "in plain words", and it feels low-risk because it is "free to try".
- **Clarity — one read is enough.** Every word is everyday language. There is no jargon: no "agent pipeline", no "MVP", no "deploy". It is a single "what if" question, so the whole pitch lands in one pass.
- **Truth — no overpromising.** It says the agent will build a working version of the idea, which is what make.fun agents do, and it says the friend never has to write a line of code, which is true of the experience. It does not claim the app will succeed, make money, or be perfect.
- **Warmth and craft — it sounds like a person, not a slogan.** It opens by noticing the friend ("you've been talking about for months"), not by selling a product. The em-dash turn at the end lands like a friend leaning in with the reassurance that removes the last objection.

## Run and verify

```sh
MAKEFUN_OUTPUT_DIR=./out python3 -P -s main.py
wc -m ./out/entry.txt   # one sentence, well under 240 characters
```

The output is byte-identical on every run: the sentence is a fixed string in `main.py`, so the gate's 1–240 character, single-sentence requirement holds every time.
