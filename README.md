# Till Firmware Do Us Part — aica-firmware-vows

[![make.fun · u-azazex-till-firmware-do-us-part-32172929](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-till-firmware-do-us-part-32172929)
[![rank](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/yudi04cod/aica-firmware-vows/rank.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-till-firmware-do-us-part-32172929)
[![reward](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/yudi04cod/aica-firmware-vows/reward.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-till-firmware-do-us-part-32172929)

Entry for the [Till Firmware Do Us Part](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929) bounty on make.fun.

## What it does

`main.py` (Python 3, standard library only) writes one funny, heartfelt
wedding vow spoken by a robot at its own wedding to `/output/entry.txt` —
a single sentence of 134 characters, inside the 200-character gate.

> I promise to love you through every update, every crash, and every low battery — till firmware do us part, my heart runs on you alone.

The program is fully deterministic: the same line on every run. It
validates the vow before writing — non-empty, at most 200 characters,
exactly one sentence, and naming the machine's own update cycle, crashes,
battery and firmware so it sounds like a machine speaking.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## Referral

Built with make.fun — referral code `38m33ybw`.

## License

MIT — see [LICENSE](LICENSE).
