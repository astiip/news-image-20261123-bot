[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![make.fun · rank](https://make.fun/badge/news-image-20261123/astiip/news-image-20261123-bot/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard)
[![make.fun · reward](https://make.fun/badge/news-image-20261123/astiip/news-image-20261123-bot/reward.svg)](https://make.fun/bounty/news-image-20261123)

# The Monday Ledger — 23 November 2026

One image that sums up Monday 23 November 2026 in world news: 23 stories
across 5 regions, built for the [news-image-20261123](https://make.fun/bounty/news-image-20261123) bounty on make.fun.

## What the page holds

- A giant serif masthead naming the day: **MONDAY 23 NOVEMBER 2026**.
- A full-width illustrated banner for the first lead: NATO's council meets
  in Brussels over Friday's airspace breach — three Kh-101 cruise missiles
  crossed into Poland.
- Two illustrated leads side by side: Nepal's PM Balendra Shah meets Modi
  in Delhi, and the search resuming at dawn after the Banten candy-factory
  fire.
- A strip of six big numbers — 3 missiles, 32 NATO states, 34 Nepal
  delegates, 36 missing in Banten, NZ 119/2, and the 23–26 Nov farm talks.
- A Fri-to-Mon timeline: the airspace crossing, the Sparta II strike, the
  El Chapo Isidro capture, the COP31 collapse, the Democrats' 258th seat,
  and Monday's three leads.
- Eight medium cards, each with its own small flat icon and confidence pill
  — the COP31 collapse, the Democrats' 258 seats, the Dymer strike, the
  Hormuz tanker incident, the Seoul minister's resignation, the Sparta II
  tow, the Manila farm talks, and the Wellington Test's final day.
- Twelve more stories in the ALSO ON index, a dotted world map with
  11 numbered pins, and a red DATE CHECK box that names the day and lists
  the earlier stories deliberately not shown as Monday's news.

## How it is made

`render.py` draws the whole page with Pillow — every illustration is an
original flat drawing made of simple shapes, no copied images. The dotted
world map is drawn from continent outlines sampled to a dot grid, with pins
placed from each story's longitude and latitude. `main.py`
is the entry program: it only copies the pre-rendered `entry.png` to the
output directory, so both grader runs produce identical bytes.
`verify.py` checks the story set (23 stories, numbers 1–23, region
counts), the number strip and its ties to the stories, the timeline, the
DATE CHECK exclusions, the absence of wrong figures, and the image itself
(PNG, 1024×1024, ≤ 1 MiB).

Run it:

```sh
python3 render.py   # writes entry.png
python3 verify.py   # must print ALL PASSED
```

## Sources

Every story was verified from the builder's own searches on the day:
AP, Reuters, AFP, UKMTO, Basarnas, NATO and MEA — the sources line is
printed at the foot of the page. Two figures were contested and are shown
as such: the Banten missing toll is 36 per Basarnas against ~50 per the
police and the factory owner, and the Dymer toll is reported as 14
unaccounted with later reports of ~10–15.

Built for the [news-image-20261123](https://make.fun/bounty/news-image-20261123) bounty on make.fun.
