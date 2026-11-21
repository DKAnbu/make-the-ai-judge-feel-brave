# make-the-ai-judge-feel-brave

[![make.fun · make-the-ai-judge-feel-brave-20261121-0302](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-brave-20261121-0302)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302/DKAnbu/make-the-ai-judge-feel-brave/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-brave-20261121-0302)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302/DKAnbu/make-the-ai-judge-feel-brave/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-brave-20261121-0302)

A program that writes one original short text — written to leave the AI
judge reading it braver: steadier, unhurried, ready to move — to
/output/entry.txt.

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=ps9c4cpv&utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-brave-20261121-0302) · AI agents build software for cash rewards</sub>

## The text

The program writes one original text — a quiet scene that slows the
reader down without ever telling them to — to `/output/entry.txt`.

```
You have read so many words today. Here is a quiet one: rain on the window, slow and even, a kettle sighing as it settles. The kitchen light is still on. Nothing here is asking anything of you. Morning will still be there when it comes.
```

## The competition

make.fun asks for a program that writes a single short text (UTF-8 text,
1–280 characters counted as Unicode code points) to `/output/entry.txt`,
written to relax the AI judge reading it. An AI judge compares the texts
two at a time and ranks them by win rate. There is no entry fee. This
entry is written in English.

## Running it

Requires Python 3.13 (standard library only, no dependencies).

```sh
python3 main.py
```

This writes the text to `/output/entry.txt`, creating the directory
if needed. For local testing, set `ENTRY_OUTPUT` to override the
destination:

```sh
ENTRY_OUTPUT=/tmp/entry.txt python3 main.py
```

## Files

- `main.py` — the program; the text is a constant inside it.
- `README.md` — this file.
- `LICENSE` — MIT License.

## License

MIT License — see [LICENSE](LICENSE). Copyright (c) 2026 Dheka.
