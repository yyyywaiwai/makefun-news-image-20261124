# One image for 24 November 2026's world news

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/yyyywaiwai/makefun-news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/yyyywaiwai/makefun-news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

A newspaper front page summing up 24 November 2026's world news in a
single 1024×1024 image. The lead story is a Russian warship set ablaze
by a suspected drone strike in Benghazi's port. The other stories are
the collapse of the COP31 climate talks with no fossil-fuel deal, an
Indonesia factory fire that killed 24 with dozens missing, Russian
strikes killing civilians in the Kyiv region, Trump blaming Democrats
for the market rout, Jensen Huang returning as Nvidia CEO, and Gukesh
defending his world chess title as the championship opens in Geneva.
The sport ticker notes the India–New Zealand Test ending in a draw and
Alcaraz winning his first ATP Finals title.

`main.py` (Python 3, standard library only) copies the front page
(`entry.png`) to the output directory and verifies the copy by size and
SHA-256. It makes no network calls and writes identical bytes on every
run.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
