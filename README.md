[![Alien Field Notes](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![Rank](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/Vins1206/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/rank.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![Reward](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/Vins1206/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/reward.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)

# Alien Field Notes: The Two Day Earth Review

A [make.fun](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000) entry: one original line of plain text, a review of planet Earth left by an alien tourist. A judge model compares the lines two at a time on the alien's one-line review of Earth first, then funniness, originality, and whether it reads like a real field note.

## The line

> The locals put a flag on their moon, took a photo, and left. No gift shop, no queue, no return visit in fifty years. Two stars for follow-through.

146 characters, one clean joke from the alien's angle (no traffic, gravity, money or weather), with a verdict, a star rating and a closing remark.

## How it works

`main.py` (pure Python standard library, no dependencies) writes that single line to `/output/entry.txt`. It is deterministic: every run writes the same bytes.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entrypoint; writes the review to `/output/entry.txt`
- `LICENSE` — MIT
