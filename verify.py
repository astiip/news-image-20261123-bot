#!/usr/bin/env python3
"""Verify the Monday Ledger entry: story set, numbers, DATE CHECK, image.

Every check is derived from render.py's own data tables, so a typo in the
data fails here instead of reaching the judge. Exits 0 and prints ALL PASSED
only when every check holds.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from render import (  # noqa: E402
    STORIES, LEADS, CARDS, INDEX, INDEX_STORIES, NUMBERS, REGIONS, TIMELINE,
    DATE_CHECK_HEAD, DATE_CHECK_BODY, SOURCES_LINE, LEGEND_LINE, OUT,
)

failures = []


def check(cond, label):
    print(("PASS " if cond else "FAIL ") + label)
    if not cond:
        failures.append(label)


DAYS = {"MON 23 NOV", "SUN 22 NOV", "SAT 21 NOV", "FRI 20 NOV", "THU 19 NOV"}


def main():
    # --- story set -------------------------------------------------------
    check(len(STORIES) == 23, "23 stories total")
    nums = sorted(s["n"] for s in STORIES)
    check(nums == list(range(1, 24)), "story numbers 1..23 unique, no gaps")
    check(all(s["title"] and s["day"] and s["region"]
              for s in STORIES),
          "every story has title, day, region")
    check(all(s.get("source") for s in LEADS + INDEX_STORIES),
          "every lead and index story has a source "
          "(cards share the footer sources line)")
    check(all(s["day"] in DAYS for s in STORIES),
          "every story day is an honest dateline")
    check(len(LEADS) == 3, "3 lead stories")
    check(all(s["day"] == "MON 23 NOV" for s in LEADS),
          "all 3 leads are Monday 23 Nov")
    check(len(CARDS) == 8, "8 medium cards")
    check(len(INDEX) == 12, "12 ALSO ON index items")
    check(all(len("%d · %s — %s" % (n, txt, day)) <= 70
              for n, txt, day in INDEX),
          "every ALSO ON index line <= 70 chars incl. number and date")
    check(all(c["icon"] for c in CARDS), "every card has an icon kind")
    check(all(s["art"] in ("nato", "delhi", "banten") for s in LEADS),
          "every lead has an illustration")
    check(all(s["pill"] in ("CONFIRMED", "REPORTED", "CLAIM")
              for s in LEADS + CARDS),
          "every lead and card carries a confidence pill")
    # cards: deck2 opens with the card's own dateline
    check(all(c["deck2"].startswith(c["day"]) for c in CARDS),
          "every card deck2 opens with its dateline")
    # legibility guard: card titles stay short enough for one 22px line
    check(all(len(c["title"]) <= 34 for c in CARDS),
          "every card title <= 34 chars")
    check(all(len(c["deck1"]) <= 60 and len(c["deck2"]) <= 60
              for c in CARDS),
          "every card deck line <= 60 chars")
    # pins: 11 places, matching the map header claim
    pins = [s for s in STORIES if s.get("pin")]
    check(len(pins) == 11, "11 map pins")

    # --- regions ---------------------------------------------------------
    check(sum(c for _, c in REGIONS) == 23, "region counts sum to 23")
    check(len(REGIONS) == 5, "5 regions")
    per_region = {}
    for s in STORIES:
        per_region[s["region"]] = per_region.get(s["region"], 0) + 1
    check(per_region == dict(REGIONS), "region counts match the story set")

    # --- number strip ----------------------------------------------------
    check(len(NUMBERS) == 6, "6 numbers on the strip")
    check([n for n, _, _ in NUMBERS] ==
          ["3", "32", "34", "36", "119/2", "23–26"],
          "strip figures are the verified ones")
    check("Three Kh-101" in LEADS[0]["deck"],
          "strip figure 3 ties to the NATO lead deck")
    check("32" in LEADS[0]["deck"],
          "strip figure 32 ties to the NATO lead deck")
    check("34" in LEADS[1]["deck"],
          "strip figure 34 ties to the Nepal lead deck")
    check("36 missing" in LEADS[2]["deck"],
          "strip figure 36 ties to the Banten lead deck")
    check("119/2" in CARDS[7]["deck1"],
          "strip figure 119/2 ties to the Wellington card")
    check("23–26" in CARDS[6]["deck2"],
          "strip figure 23–26 ties to the Manila card")

    # --- timeline --------------------------------------------------------
    check([d for d, _, _ in TIMELINE] ==
          ["FRI 20 NOV", "SAT 21 NOV", "SUN 22 NOV", "MON 23 NOV"],
          "timeline runs Fri 20 to Mon 23 Nov")
    check(TIMELINE[3][2] is True and all(not t[2] for t in TIMELINE[:3]),
          "only Monday is marked as today in the timeline")
    tl_text = " ".join(i for _, items, _ in TIMELINE for i in items)
    check("3 Russian objects cross into Poland" in tl_text,
          "timeline: Friday airspace crossing")
    check("COP31 collapses, no deal" in tl_text,
          "timeline: Sunday COP31 collapse")
    check("NATO meets in Brussels" in tl_text,
          "timeline: Monday NATO meeting")

    # --- DATE CHECK ------------------------------------------------------
    check("MONDAY 23 NOVEMBER 2026" in DATE_CHECK_HEAD,
          "DATE CHECK names Monday 23 November 2026")
    dc = DATE_CHECK_BODY
    for name in ("COP31 collapse", "258th seat", "Dymer strike",
                 "Korea minister", "Sparta II strike", "El Chapo capture",
                 "UN robot talks", "ICJ ruling", "Anthropic IPO"):
        check(name in dc, "DATE CHECK lists: %s" % name)

    # --- forbidden wrong figures -----------------------------------------
    text_all = " ".join(
        s["title"] + " " + (s.get("deck") or
                            s.get("deck1", "") + " " + s.get("deck2", ""))
        for s in STORIES)
    for bad in ("Article 4", "4 missiles", "37 missing", "50 missing",
                "TODO", "Lorem", "placeholder", "{owner}", "{repo}"):
        check(bad not in text_all, "wrong/placeholder text absent: %s" % bad)
    # The Banten toll conflict: Basarnas says 36, police/owner say ~50.
    # We print both and say figures differ; 50 must never stand as the toll.
    banten = [s for s in STORIES if s["n"] == 3][0]
    check("36 missing" in banten["deck"], "Banten card prints Basarnas 36")
    check("Figures differ" in banten["deck"],
          "Banten card says the figures differ")
    # Footer lines carry the brief's exact sources and legend.
    check(SOURCES_LINE.startswith("Sources: AP · Reuters · AFP · UKMTO"),
          "sources footer lists the verified wires")
    check("CONFIRMED = officially confirmed" in LEGEND_LINE
          and "REPORTED = reported" in LEGEND_LINE
          and "CLAIM = one side's claim" in LEGEND_LINE,
          "tag legend defines all three pills")

    # --- image -----------------------------------------------------------
    check(os.path.exists(OUT), "entry.png exists")
    if os.path.exists(OUT):
        with open(OUT, "rb") as f:
            head = f.read(8)
        check(head == b"\x89PNG\r\n\x1a\n", "entry.png is a PNG")
        size = os.path.getsize(OUT)
        check(size <= 1048576, "entry.png <= 1 MiB (%d bytes)" % size)
        from PIL import Image
        img = Image.open(OUT)
        check(img.size == (1024, 1024), "entry.png is 1024x1024")
        check(img.mode == "RGB", "entry.png is RGB")

    if failures:
        print("FAILED: %d check(s)" % len(failures))
        sys.exit(1)
    print("ALL PASSED")


if __name__ == "__main__":
    main()
