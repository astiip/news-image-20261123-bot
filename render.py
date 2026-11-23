#!/usr/bin/env python3
"""Render the news-image-20261123 entry: Monday 23 November 2026 in one image.

Draws a 1024x1024 PNG with PIL (build-time only). The entrypoint main.py
is a stdlib-only copy program; this file is the generator, kept in the
repo so the build is reproducible and reviewable.

Design ("The Monday Ledger"): a warm cream page with a giant serif
masthead date, a full-width illustrated banner for the NATO lead, two
illustrated leads side by side, a six-tile number strip, a Fri-to-Mon
timeline, eight medium cards in a two-column grid, and a bottom band with
a numbered ALSO ON index, a dotted world map with numbered pins, a red
DATE CHECK box, and a sources + tag-legend footer.

Every story below was verified from this session's own searches for
23 November 2026 (Monday leads, weekend follow-ups honestly dated).
Figures that could not be verified were dropped; see verify.py.
Where reports differ (Banten missing toll), the card says so.
"""

import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

PAPER = (247, 241, 227)
INK = (20, 38, 74)
NAVY = (20, 38, 74)
RED = (179, 39, 30)
TEAL = (23, 126, 122)
GOLD = (217, 164, 65)
GRAY = (107, 114, 128)
LINE = (203, 199, 186)
CARD = (255, 255, 255)
SKY = (214, 228, 238)
SEA = (38, 84, 124)
PILL_CONF = (23, 126, 122)
PILL_REP = (176, 124, 20)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


F_SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
F_SANS = lambda s: font("DejaVuSans.ttf", s)
F_SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)

# ---------------------------------------------------------------- stories
# n, region, day, pill, title, deck, source, pin (lon, lat), art
LEADS = [
    dict(n=1, region="EUROPE", day="MON 23 NOV", pill="CONFIRMED",
         title="NATO meets today over Poland airspace breach",
         deck=("Three Kh-101 cruise missiles crossed into Poland on "
               "Friday; one spent about three minutes over the country. "
               "No one was hurt. NATO's Rutte: the alliance 'will defend "
               "every inch of Polish territory.' All 32 NATO states sit "
               "at the council; Poland will ask allies for more Eastern "
               "Sentry forces."),
         source="Reuters · NATO", pin=(4.35, 50.85), art="nato"),
    dict(n=2, region="ASIA", day="MON 23 NOV", pill="CONFIRMED",
         title="Nepal's PM meets Modi in Delhi",
         deck=("Balendra Shah's first bilateral trip abroad since March, "
               "with a 34-member delegation. Talks and MoUs on education, "
               "health, agriculture and disaster management — plus a "
               "Joint Vision Document."),
         source="MEA · Reuters", pin=(77.2, 28.6), art="delhi"),
    dict(n=3, region="ASIA", day="MON 23 NOV", pill="REPORTED",
         title="Search resumes at dawn in Banten",
         deck=("Rescuers return at 7am to the Milkita candy factory in "
               "Cikande, Serang. At least 3 dead; 36 missing per Basarnas "
               "— police and the owner say ~50. Figures differ. DNA "
               "checks take 2–3 weeks; cause unknown."),
         source="Basarnas · AP", pin=(106.1, -6.1), art="banten"),
]

# n, region, day, pill, title, deck1, deck2 (deck2 opens with the dateline),
# icon, pin (lon, lat)
CARDS = [
    dict(n=4, region="EUROPE", day="SUN 22 NOV", pill="CONFIRMED",
         title="COP31 collapses",
         deck1="Climate talks end with no deal in Antalya;",
         deck2="SUN 22 NOV · no fossil fuels; first failure since 2009",
         icon="globe", pin=(30.7, 36.9)),
    dict(n=5, region="AMERICAS", day="SUN 22 NOV", pill="CONFIRMED",
         title="Democrats clinch 258",
         deck1="Chuck Hubbard beats Virginia Foxx in North Carolina;",
         deck2="SUN 22 NOV · +44 seats — largest majority since 1992",
         icon="capitol", pin=(-79.0, 35.5)),
    dict(n=6, region="EUROPE", day="SUN 22 NOV", pill="REPORTED",
         title="Dymer strike",
         deck1="Russian drone collapses part of a 5-storey block;",
         deck2="SUN 22 NOV · 14 unaccounted; 9 out; 161 of 186 downed",
         icon="drone", pin=(30.2, 50.8)),
    dict(n=7, region="MIDDLE EAST", day="SUN 22 NOV", pill="REPORTED",
         title="Tanker incident",
         deck1="Iranian media: two supertankers on fire near Hormuz;",
         deck2="SUN 22 NOV · UKMTO tanker incident; link unclear",
         icon="tanker", pin=(57.5, 25.3)),
    dict(n=8, region="ASIA", day="SUN 22 NOV", pill="CONFIRMED",
         title="Seoul minister quits",
         deck1="Minister Choi Kyo-jin resigns over AI-cheating",
         deck2="SUN 22 NOV · accepted within the hour; 111 cases",
         icon="pencil", pin=(127.0, 37.5)),
    dict(n=9, region="EUROPE", day="SUN 22 NOV", pill="CONFIRMED",
         title="Sparta II under tow",
         deck1="Russian vessel begins towing the fire-damaged ship",
         deck2="SUN 22 NOV · out of Finnish waters; 16 crew safe",
         icon="tug", pin=(24.0, 60.0)),
    dict(n=10, region="ASIA", day="MON 23 NOV", pill="CONFIRMED",
         title="Manila opens farm talks",
         deck1="Philippines and the FAO open farm",
         deck2="MON 23 NOV · modernisation talks, Parañaque, 23–26",
         icon="wheat", pin=(121.0, 14.6)),
    dict(n=11, region="OCEANIA", day="MON 23 NOV", pill="CONFIRMED",
         title="NZ 119/2, trailing by 233",
         deck1="NZ resume 119/2, trailing by 233, batting to save it",
         deck2="MON 23 NOV · after India's 720/9; Rahul 136, Pant 128",
         icon="bat", pin=(174.8, -41.3)),
]

# n, one-line index text, day
INDEX = [
    (12, "Sea-Tac ICE arrests called 'outrageous'", "MON 23 NOV"),
    (13, "Myanmar govt: ASEAN summit call 'unfair'", "SAT 21 NOV"),
    (14, "El Chapo Isidro captured; 11 dead", "FRI 20 NOV"),
    (15, "UN robot talks end — 2 more years", "SAT 21 NOV"),
    (16, "ICJ: Myanmar guilty of Rohingya genocide", "THU 19 NOV"),
    (17, "FBI probes breach of its crime database", "SUN 22 NOV"),
    (18, "Verstappen wins the Las Vegas GP", "SAT 21 NOV"),
    (19, "Liverpool beat 10-man Man Utd", "SUN 22 NOV"),
    (20, "'Sunrise on the Reaping' tops box office", "SUN 22 NOV"),
    (21, "Miley Cyrus marries Maxx Morando", "SUN 22 NOV"),
    (22, "Nasdaq fell ~10%; Anthropic's record IPO", "FRI 20 NOV"),
    (23, "Lisbon march over living costs", "SUN 22 NOV"),
]

# The same 12 index stories as full records, for verification and the
# region counts. No map pin: the map pins only the 11 lead/card places.
INDEX_STORIES = [
    dict(n=12, region="AMERICAS", day="MON 23 NOV",
         title="Sea-Tac ICE arrests called 'outrageous'",
         deck="Senator-elect calls the Sea-Tac ICE arrests outrageous; "
              "ex-White House chief of staff urges Democrats to repeal "
              "tariff rises; El-Sayed and Van Hollen press an Iran war "
              "funding curb.",
         source="Wire reports", pin=None),
    dict(n=13, region="ASIA", day="SAT 21 NOV",
         title="Myanmar govt: ASEAN summit call 'unfair'",
         deck="Army-backed government calls the ASEAN summit decision "
              "unfair and imbalanced.",
         source="Wire reports", pin=None),
    dict(n=14, region="AMERICAS", day="FRI 20 NOV",
         title="El Chapo Isidro captured; 11 dead",
         deck="Captured Friday in Sinaloa; 11 dead (7 gunmen, 4 soldiers). "
              "FBI Top-10 fugitive, $5m reward.",
         source="Wire reports", pin=None),
    dict(n=15, region="EUROPE", day="SAT 21 NOV",
         title="UN robot talks end — 2 more years",
         deck="UN killer-robot talks in Geneva end Saturday: 128 states "
              "agree a 2-year process, no binding rules.",
         source="Wire reports", pin=None),
    dict(n=16, region="EUROPE", day="THU 19 NOV",
         title="ICJ: Myanmar guilty of Rohingya genocide",
         deck="The Hague: ICJ ruled Thursday Myanmar committed genocide "
              "against the Rohingya (9–6); reparations ordered.",
         source="Wire reports", pin=None),
    dict(n=17, region="AMERICAS", day="SUN 22 NOV",
         title="FBI probes breach of its crime database",
         deck="FBI probes an apparent breach of its criminal database; "
              "the DNI confirmed the incident on Sunday.",
         source="Wire reports", pin=None),
    dict(n=18, region="AMERICAS", day="SAT 21 NOV",
         title="Verstappen wins the Las Vegas GP",
         deck="Verstappen wins the Las Vegas Grand Prix on Saturday.",
         source="Wire reports", pin=None),
    dict(n=19, region="EUROPE", day="SUN 22 NOV",
         title="Liverpool beat 10-man Man Utd",
         deck="Liverpool beat 10-man Manchester United in Pochettino's "
              "first match, on Sunday.",
         source="Wire reports", pin=None),
    dict(n=20, region="AMERICAS", day="SUN 22 NOV",
         title="'Sunrise on the Reaping' tops box office",
         deck="Tops the North America box office, ~$120m opening weekend.",
         source="Wire reports", pin=None),
    dict(n=21, region="AMERICAS", day="SUN 22 NOV",
         title="Miley Cyrus marries Maxx Morando",
         deck="Miley Cyrus marries Maxx Morando on Sunday.",
         source="Wire reports", pin=None),
    dict(n=22, region="AMERICAS", day="FRI 20 NOV",
         title="Nasdaq fell ~10%; Anthropic's record IPO",
         deck="Nasdaq fell about 10% on the week as Anthropic made its "
              "record IPO debut on Friday.",
         source="Wire reports", pin=None),
    dict(n=23, region="EUROPE", day="SUN 22 NOV",
         title="Lisbon march over living costs",
         deck="Thousands march in Lisbon over living costs on Sunday.",
         source="Wire reports", pin=None),
]

# number, label, caption — all figures verified in this session's searches
NUMBERS = [
    ("3", "KH-101 MISSILES", "over Poland, Fri 20 Nov"),
    ("32", "NATO STATES", "at Monday's council"),
    ("34", "NEPAL DELEGATES", "in Delhi with PM Shah"),
    ("36", "MISSING IN BANTEN", "Basarnas count"),
    ("119/2", "NZ RESUME", "233 behind, day 5"),
    ("23–26", "FARM TALKS", "Manila, Philippines"),
]

# day, items, is_today
TIMELINE = [
    ("FRI 20 NOV", ["3 Russian objects cross into Poland"], False),
    ("SAT 21 NOV", ["Sparta II drone strike, Baltic",
                     "El Chapo Isidro captured — 11 dead",
                     "UN robot talks end — 2 more years"], False),
    ("SUN 22 NOV", ["COP31 collapses, no deal",
                     "Democrats clinch 258th seat",
                     "Dymer strike, 14 unaccounted",
                     "Korea minister quits"], False),
    ("MON 23 NOV", ["NATO meets in Brussels",
                     "Nepal–Modi talks in Delhi",
                     "Banten search resumes"], True),
]

REGIONS = [("EUROPE", 8), ("ASIA", 5), ("AMERICAS", 8),
           ("MIDDLE EAST", 1), ("OCEANIA", 1)]

DATE_CHECK_HEAD = "DATE CHECK — This page is MONDAY 23 NOVEMBER 2026."
DATE_CHECK_BODY = (
    "Sunday follow-ups carry their own SUN dateline. NOT Monday's news, so "
    "NOT shown as such: COP31 collapse (Sun) · Democrats' 258th seat (Sun) "
    "· Dymer strike (Sun) · Korea minister (Sun) · Sparta II strike "
    "(Sat 21 Nov) · El Chapo capture (Fri 20 Nov) · UN robot talks (Sat) "
    "· ICJ ruling (Thu 19 Nov) · Anthropic IPO (Fri).")

SOURCES_LINE = (
    "Sources: AP · Reuters · AFP · UKMTO · Basarnas · NATO · MEA — figures "
    "as reported 23 Nov 2026, 07:05 WIB; where reports differ, the card "
    "says so.")
LEGEND_LINE = (
    "CONFIRMED = officially confirmed · REPORTED = reported, tolls may "
    "change · CLAIM = one side's claim, unverified")

STORIES = LEADS + CARDS + INDEX_STORIES


def all_stories():
    """Every numbered story on the page, 1..23."""
    out = []
    for s in STORIES:
        deck = s.get("deck") or (s.get("deck1", "") + " " + s.get("deck2", ""))
        out.append((s["n"], s["region"], s["title"], deck,
                    s.get("source", "Wire reports")))
    for n, text, day in INDEX:
        out.append((n, None, text, "", "Wire reports"))
    return out


# ---------------------------------------------------------------- helpers
def wrap(draw, text, fnt, max_w):
    """Greedy word wrap to a pixel width; returns a list of lines."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def fit(draw, text, fnt, max_w, suffix="…"):
    """Truncate one line to a pixel width, adding an ellipsis."""
    if draw.textlength(text, font=fnt) <= max_w:
        return text
    while text and draw.textlength(text + suffix, font=fnt) > max_w:
        text = text[:-1]
    return text + suffix


def rrect(d, box, r, **kw):
    d.rounded_rectangle(box, radius=r, **kw)


def text(d, xy, s, fnt, fill):
    d.text(xy, s, font=fnt, fill=fill)


def pill(d, x, y, label, fill, fg=(255, 255, 255)):
    """Small confidence pill, right-aligned to x (its right edge)."""
    fnt = F_SANS_B(8)
    w = d.textlength(label, font=fnt) + 12
    rrect(d, [x - w, y, x, y + 16], 8, fill=fill)
    d.text((x - w + 6, y + 4), label, font=fnt, fill=fg)
    return w


PILL_FILL = {"CONFIRMED": PILL_CONF, "REPORTED": PILL_REP, "CLAIM": RED}

# ---------------------------------------------------------------- illustrations
# All art is original flat drawing with PIL primitives — no copied images.
# New compositions, drawn for this day only.

def draw_nato(d, x, y, w, h):
    """Dusk sky, NATO compass star, three missile streaks, Brussels arcade."""
    d.rectangle([x, y, x + w, y + h], fill=(28, 38, 66))
    d.rectangle([x, y + h - 52, x + w, y + h], fill=(44, 54, 88))
    # stars
    for sx, sy in [(24, 14), (70, 26), (120, 10), (200, 20), (260, 12),
                   (320, 24), (40, 44), (300, 44), (170, 34)]:
        d.ellipse([x + sx - 1, y + sy - 1, x + sx + 1, y + sy + 1],
                  fill=(247, 241, 227))
    # NATO compass star, left of centre
    cx, cy, r = x + 118, y + h // 2 - 6, 52
    d.polygon([(cx, cy - r), (cx + 11, cy - 11), (cx + r, cy),
               (cx + 11, cy + 11), (cx, cy + r), (cx - 11, cy + 11),
               (cx - r, cy), (cx - 11, cy - 11)], fill=(247, 241, 227))
    d.ellipse([cx - 9, cy - 9, cx + 9, cy + 9], fill=(28, 38, 66))
    # three missile streaks crossing the sky, top right
    for i, (ox, oy) in enumerate([(0, 0), (-46, 26), (-92, 52)]):
        x1, y1 = x + w - 26 + ox, y + 16 + oy
        x2, y2 = x + w - 108 + ox, y + 62 + oy
        d.line([(x1, y1), (x2, y2)], fill=(217, 84, 30), width=3)
        d.ellipse([x2 - 4, y2 - 4, x2 + 4, y2 + 4], fill=(247, 197, 66))
        for k in range(1, 4):
            tx = x1 + (x2 - x1) * k // 4
            ty = y1 + (y2 - y1) * k // 4
            d.ellipse([tx - 1, ty - 1, tx + 1, ty + 1], fill=(247, 197, 66))
    # ground + Brussels arcade silhouette
    d.rectangle([x, y + h - 34, x + w, y + h], fill=(12, 18, 32))
    for i in range(6):
        ax = x + 14 + i * 56
        d.rectangle([ax, y + h - 30, ax + 44, y + h - 6], fill=(64, 74, 102))
        d.pieslice([ax + 10, y + h - 28, ax + 34, y + h - 4], 180, 360,
                   fill=(247, 197, 66))
    # small flag poles on the arcade
    for fx in (x + 30, x + 330):
        d.line([(fx, y + h - 62), (fx, y + h - 30)], fill=(247, 241, 227),
               width=2)
        d.polygon([(fx, y + h - 62), (fx + 18, y + h - 56),
                   (fx, y + h - 50)], fill=RED)


def draw_delhi(d, x, y, w, h):
    """Pale sky, Himalaya snow peaks, India Gate arch, two small flags."""
    d.rectangle([x, y, x + w, y + h], fill=(232, 236, 222))
    # sun
    sx, sy, sr = x + w - 34, y + 14, 11
    d.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=GOLD)
    # Himalaya: three peaks, snow caps
    gh = int(h * 0.62)
    for px, pw, ph in [(0, 150, 46), (110, 190, 56), (280, 170, 48)]:
        bx = x + px
        d.polygon([(bx, y + h - 10), (bx + pw // 2, y + h - 10 - ph),
                   (bx + pw, y + h - 10)], fill=(90, 110, 140))
        d.polygon([(bx + pw // 2 - 12, y + h - 10 - ph + 16),
                   (bx + pw // 2, y + h - 10 - ph),
                   (bx + pw // 2 + 12, y + h - 10 - ph + 16)],
                  fill=(255, 255, 255))
    # ground
    d.rectangle([x, y + h - 10, x + w, y + h], fill=(198, 164, 110))
    # India Gate arch, right of centre
    ax, aw, ah = x + w - 150, 74, int(h * 0.66)
    ay = y + h - 10 - ah
    d.rectangle([ax, ay, ax + aw, y + h - 10], fill=(198, 164, 110))
    d.rectangle([ax - 6, ay - 6, ax + aw + 6, ay + 4], fill=(178, 142, 92))
    d.pieslice([ax + 20, ay + 16, ax + aw - 20, ay + 62], 180, 360,
               fill=(232, 236, 222))
    d.rectangle([ax + 20, ay + 38, ax + aw - 20, y + h - 10],
                fill=(232, 236, 222))
    # flag poles: Nepal crimson pennon, India tricolour
    for fx, kind in ((ax - 34, "nepal"), (ax + aw + 22, "india")):
        d.line([(fx, y + h - 44), (fx, y + h - 10)], fill=INK, width=2)
        if kind == "nepal":
            d.polygon([(fx, y + h - 44), (fx + 16, y + h - 38),
                       (fx, y + h - 32)], fill=(220, 20, 60))
            d.polygon([(fx, y + h - 32), (fx + 14, y + h - 27),
                       (fx, y + h - 22)], fill=(220, 20, 60))
        else:
            for j, col in enumerate(((255, 153, 51), (255, 255, 255),
                                     (19, 136, 8))):
                d.rectangle([fx, y + h - 44 + j * 6, fx + 18,
                             y + h - 38 + j * 6], fill=col)


def draw_banten(d, x, y, w, h):
    """Dawn sky, candy factory with sawtooth roof, searchlight beams."""
    # dawn bands
    d.rectangle([x, y, x + w, y + h], fill=(240, 170, 90))
    d.rectangle([x, y + h // 3, x + w, y + h], fill=(245, 205, 140))
    d.rectangle([x, y + 2 * h // 3, x + w, y + h], fill=(250, 232, 190))
    # low sun
    sx, sy, sr = x + w - 60, y + 16, 12
    d.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=(230, 120, 40))
    # searchlight beams from the factory roof
    fx, fy = x + 40, y + h - 26
    d.polygon([(fx, fy), (fx + 90, y + 8), (fx + 120, y + 8)],
              fill=(250, 240, 180))
    d.polygon([(fx + w - 90, fy), (fx + w - 190, y + 12),
               (fx + w - 160, y + 12)], fill=(250, 240, 180))
    # factory block with sawtooth roof
    d.rectangle([x + 24, y + h - 26, x + w - 24, y + h - 8], fill=(90, 80, 70))
    for i in range(5):
        tx = x + 24 + i * ((w - 48) // 5)
        d.polygon([(tx, y + h - 26), (tx + (w - 48) // 10, y + h - 40),
                   (tx + (w - 48) // 5, y + h - 26)], fill=(70, 62, 54))
    for i in range(6):
        wx = x + 36 + i * ((w - 72) // 6)
        d.rectangle([wx, y + h - 20, wx + 12, y + h - 12], fill=GOLD)
    # ground + three rescue figures with white helmets
    d.rectangle([x, y + h - 8, x + w, y + h], fill=(70, 62, 54))
    for px in (x + w - 120, x + w - 96, x + w - 72):
        d.ellipse([px - 3, y + h - 26, px + 3, y + h - 20], fill=(255, 255, 255))
        d.rectangle([px - 3, y + h - 20, px + 3, y + h - 8], fill=NAVY)


def draw_icon(d, x, y, s, kind, bg):
    """40px flat icon on a rounded square."""
    rrect(d, [x, y, x + s, y + s], 8, fill=bg)
    cx, cy = x + s // 2, y + s // 2
    white = (255, 255, 255)
    if kind == "globe":  # COP31
        d.ellipse([cx - 12, cy - 12, cx + 12, cy + 12], fill=white)
        d.ellipse([cx - 12, cy - 12, cx + 12, cy + 12], outline=bg, width=1)
        d.arc([cx - 12, cy - 12, cx + 12, cy + 12], 200, 340, fill=TEAL,
              width=2)
        d.ellipse([cx - 8, cy - 7, cx - 1, cy + 1], fill=(74, 160, 90))
        d.ellipse([cx + 2, cy + 3, cx + 9, cy + 10], fill=(74, 160, 90))
    elif kind == "capitol":  # Democrats
        d.pieslice([cx - 10, cy - 13, cx + 10, cy + 1], 180, 360, fill=white)
        d.rectangle([cx - 11, cy - 1, cx + 11, cy + 2], fill=white)
        for i in range(3):
            px = cx - 9 + i * 8
            d.rectangle([px, cy + 3, px + 3, cy + 11], fill=white)
        d.rectangle([cx - 13, cy + 11, cx + 13, cy + 13], fill=white)
    elif kind == "drone":  # Dymer
        d.line([(cx - 11, cy - 11), (cx + 11, cy + 11)], fill=white, width=3)
        d.line([(cx + 11, cy - 11), (cx - 11, cy + 11)], fill=white, width=3)
        for px, py in [(cx - 11, cy - 11), (cx + 11, cy - 11),
                       (cx - 11, cy + 11), (cx + 11, cy + 11)]:
            d.ellipse([px - 4, py - 4, px + 4, py + 4], outline=white, width=2)
        d.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=white)
    elif kind == "tanker":  # Hormuz
        d.polygon([(cx - 13, cy - 2), (cx + 13, cy - 2), (cx + 9, cy + 8),
                   (cx - 9, cy + 8)], fill=white)
        d.rectangle([cx - 4, cy - 10, cx + 8, cy - 2], fill=white)
        d.polygon([(cx - 6, cy - 10), (cx - 2, cy - 18), (cx + 2, cy - 10)],
                  fill=(247, 197, 66))
        d.arc([cx - 14, cy + 9, cx - 2, cy + 15], 0, 180, fill=white, width=2)
        d.arc([cx + 2, cy + 9, cx + 14, cy + 15], 0, 180, fill=white, width=2)
    elif kind == "pencil":  # Seoul exam
        d.polygon([(cx - 9, cy + 9), (cx - 12, cy + 2), (cx + 2, cy - 12),
                   (cx + 9, cy - 12), (cx + 12, cy - 5), (cx - 2, cy + 12)],
                  fill=white)
        d.polygon([(cx - 9, cy + 9), (cx - 12, cy + 2), (cx - 6, cy + 6)],
                  fill=(247, 197, 66))
        d.line([(cx - 12, cy + 2), (cx + 2, cy - 12)], fill=GOLD, width=2)
    elif kind == "tug":  # Sparta II
        d.polygon([(cx - 13, cy - 2), (cx + 13, cy - 2), (cx + 9, cy + 8),
                   (cx - 9, cy + 8)], fill=white)
        d.rectangle([cx - 6, cy - 10, cx + 4, cy - 2], fill=white)
        d.rectangle([cx + 6, cy - 13, cx + 10, cy - 2], fill=RED)
        for ox, oy, r in [(8, -18, 3), (12, -24, 4)]:
            d.ellipse([cx + ox - r, cy + oy - r, cx + ox + r, cy + oy + r],
                      fill=(200, 200, 200))
        d.arc([cx - 14, cy + 9, cx - 2, cy + 15], 0, 180, fill=white, width=2)
        d.arc([cx + 2, cy + 9, cx + 14, cy + 15], 0, 180, fill=white, width=2)
    elif kind == "wheat":  # Manila farm talks
        d.line([(cx, cy - 12), (cx, cy + 13)], fill=white, width=2)
        for j in range(3):
            wy = cy - 10 + j * 7
            d.ellipse([cx - 7, wy - 3, cx - 1, wy + 3], fill=white)
            d.ellipse([cx + 1, wy - 3, cx + 7, wy + 3], fill=white)
        d.ellipse([cx - 3, cy - 14, cx + 3, cy - 8], fill=white)
    elif kind == "bat":  # Wellington cricket
        d.polygon([(cx - 10, cy + 12), (cx - 2, cy + 12), (cx + 10, cy - 10),
                   (cx + 4, cy - 12)], fill=white)
        d.line([(cx - 10, cy + 12), (cx - 13, cy + 14)], fill=white, width=3)
        d.ellipse([cx + 6, cy + 6, cx + 14, cy + 14], fill=RED)


# ---------------------------------------------------------------- dotted map
CONTINENTS = [
    # North America
    [(-168, 66), (-140, 70), (-120, 71), (-100, 73), (-85, 74), (-75, 72),
     (-65, 62), (-55, 52), (-60, 46), (-70, 42), (-75, 35), (-81, 31),
     (-90, 29), (-97, 26), (-105, 22), (-112, 25), (-117, 33), (-124, 42),
     (-125, 49), (-135, 58), (-152, 60), (-165, 60)],
    # Greenland
    [(-55, 60), (-40, 64), (-30, 68), (-22, 74), (-40, 78), (-58, 74),
     (-60, 70)],
    # South America
    [(-79, 9), (-72, 12), (-62, 10), (-52, 5), (-50, -5), (-40, -10),
     (-35, -20), (-40, -30), (-48, -28), (-58, -35), (-65, -40),
     (-70, -50), (-73, -38), (-72, -28), (-70, -18), (-77, -12),
     (-81, -4), (-80, 4)],
    # Europe
    [(-10, 36), (-9, 43), (-2, 48), (2, 51), (7, 54), (10, 57), (18, 56),
     (21, 55), (24, 59), (30, 60), (28, 62), (22, 66), (18, 70), (10, 64),
     (5, 58), (-5, 57), (-10, 50), (-10, 43)],
    # Africa
    [(-6, 35), (10, 37), (20, 32), (32, 31), (35, 28), (40, 20), (43, 12),
     (48, 11), (51, 10), (44, 2), (40, -6), (40, -16), (35, -26),
     (30, -33), (20, -35), (15, -30), (12, -18), (13, -10), (9, 4),
     (-2, 5), (-8, 5), (-15, 11), (-17, 15), (-16, 21), (-15, 28),
     (-10, 31)],
    # Asia
    [(30, 62), (45, 68), (60, 69), (75, 72), (95, 75), (115, 76),
     (135, 72), (155, 70), (170, 66), (178, 65), (168, 60), (158, 52),
     (142, 50), (140, 40), (133, 34), (127, 38), (122, 38), (120, 30),
     (114, 22), (108, 18), (105, 10), (100, 8), (97, 15), (92, 21),
     (87, 21), (80, 14), (77, 8), (74, 14), (70, 20), (65, 25), (60, 25),
     (55, 26), (50, 29), (48, 30), (43, 29), (39, 31), (35, 36),
     (30, 36), (28, 41), (30, 46), (32, 52)],
    # Australia
    [(114, -22), (114, -31), (116, -35), (122, -34), (129, -32),
     (135, -35), (140, -38), (146, -39), (150, -37), (153, -32),
     (153, -27), (150, -22), (146, -19), (142, -14), (142, -11),
     (136, -12), (132, -12), (128, -14), (123, -17), (118, -20)],
]

ISLANDS = [  # (lon, lat, rx, ry) ellipses in mask space
    (102, -2, 7, 3), (113, -7, 6, 2), (122, -8, 5, 2), (131, -3, 6, 2),
    (140, -4, 5, 2), (127, 1, 4, 2), (-2, 54, 2, 3), (139, 38, 2, 4),
    (167, -42, 2, 3), (174, -39, 2, 2),
]


def build_land_mask(mw=180, mh=90):
    """Small bitmap of land, drawn from the continent polygons."""
    mask = Image.new("L", (mw, mh), 0)
    md = ImageDraw.Draw(mask)

    def px(lon, lat):
        return ((lon + 180) / 360 * mw, (90 - lat) / 180 * mh)

    for poly in CONTINENTS:
        md.polygon([px(lon, lat) for lon, lat in poly], fill=255)
    for lon, lat, rx, ry in ISLANDS:
        cx, cy = px(lon, lat)
        sx, sy = mw / 360, mh / 180
        md.ellipse([cx - rx * sx, cy - ry * sy, cx + rx * sx, cy + ry * sy],
                   fill=255)
    return mask


def draw_map(d, x, y, w, h, pins):
    """Dotted world map with numbered pins. pins: list of (n, lon, lat)."""
    mask = build_land_mask()
    mw, mh = mask.size
    step = 5
    dot = (148, 163, 184)
    for gy in range(y + 2, y + h - 2, step):
        for gx in range(x + 2, x + w - 2, step):
            mx = int((gx - x) / w * mw)
            my = int((gy - y) / h * mh)
            if mask.getpixel((mx, my)):
                d.ellipse([gx - 1, gy - 1, gx + 1, gy + 1], fill=dot)
    # pins: small red circles, white number; nudges keep the Gulf and
    # Europe clusters readable
    nudges = {1: (-14, -8), 6: (12, -10), 4: (10, 10), 9: (-6, 10),
              7: (-12, 8), 2: (8, -8), 8: (6, -10), 10: (-8, 8),
              11: (-16, -4)}
    f_pin = F_SANS_B(8)
    for n, lon, lat in pins:
        px = x + (lon + 180) / 360 * w
        py = y + (75 - lat) / 130 * h
        dx, dy = nudges.get(n, (0, 0))
        px, py = px + dx, py + dy
        d.ellipse([px - 7, py - 7, px + 7, py + 7], fill=RED,
                  outline=(255, 255, 255), width=1)
        tw = d.textlength(str(n), font=f_pin)
        d.text((px - tw / 2, py - 6), str(n), font=f_pin, fill=(255, 255, 255))

# ---------------------------------------------------------------- layout
ART = {"nato": draw_nato, "delhi": draw_delhi, "banten": draw_banten}

ICON_BG = {"globe": TEAL, "capitol": NAVY, "drone": RED, "tanker": SEA,
           "pencil": GOLD, "tug": NAVY, "wheat": TEAL, "bat": INK}


def draw_masthead(d):
    kicker = "THE MONDAY LEDGER"
    kw = d.textlength(kicker, font=F_SANS_B(15))
    d.text(((W - kw) / 2, 8), kicker, font=F_SANS_B(15), fill=RED)
    date = "MONDAY 23 NOVEMBER 2026"
    dw = d.textlength(date, font=F_SERIF_B(42))
    d.text(((W - dw) / 2, 26), date, font=F_SERIF_B(42), fill=NAVY)
    d.rectangle([12, 76, 1012, 79], fill=RED)
    stand = ("NATO meets in Brussels · Nepal–Modi talks in Delhi · Banten "
             "search resumes — the weekend's news, dated as it happened")
    sw = d.textlength(stand, font=F_SANS(12))
    d.text(((W - sw) / 2, 84), stand, font=F_SANS(12), fill=(60, 60, 60))


def draw_lead1(d, s):
    rrect(d, [12, 104, 1012, 288], 4, fill=CARD, outline=LINE, width=1)
    ART[s["art"]](d, 12, 104, 360, 184)
    tx = 388
    text(d, (tx, 112), "%d · %s · %s" % (s["n"], s["region"], s["day"]),
         F_SANS_B(11), RED)
    pill(d, 1004, 110, s["pill"], PILL_FILL[s["pill"]])
    ty = 132
    for line in wrap(d, s["title"], F_SERIF_B(30), 604):
        text(d, (tx, ty), line, F_SERIF_B(30), INK)
        ty += 36
    ty = 208
    for line in wrap(d, s["deck"], F_SANS(13), 604):
        text(d, (tx, ty), line, F_SANS(13), (40, 40, 40))
        ty += 17
    text(d, (tx, 276), "Source: " + s["source"], F_SANS(9), GRAY)


def draw_leads23(d):
    for i, s in enumerate(LEADS[1:]):
        x = 12 + i * 504
        rrect(d, [x, 296, x + 496, 468], 4, fill=CARD, outline=LINE, width=1)
        ART[s["art"]](d, x, 296, 496, 62)
        text(d, (x + 12, 364), "%d · %s · %s" % (s["n"], s["region"], s["day"]),
             F_SANS_B(10), RED)
        pill(d, x + 488, 362, s["pill"], PILL_FILL[s["pill"]])
        text(d, (x + 12, 380), fit(d, s["title"], F_SERIF_B(22), 472),
             F_SERIF_B(22), INK)
        ty = 406
        for line in wrap(d, s["deck"], F_SANS(13), 472)[:3]:
            text(d, (x + 12, ty), line, F_SANS(13), (40, 40, 40))
            ty += 16
        text(d, (x + 12, 456), "Source: " + s["source"], F_SANS(8), GRAY)


def draw_numbers(d):
    tw = 160
    for i, (num, label, cap) in enumerate(NUMBERS):
        x = 12 + i * (tw + 8)
        rrect(d, [x, 476, x + tw, 526], 6, fill=CARD, outline=LINE, width=1)
        f_num = F_SANS_B(24 if len(num) <= 3 else 20)
        nw = d.textlength(num, font=f_num)
        d.text((x + (tw - nw) / 2, 480), num, font=f_num, fill=INK)
        lw = d.textlength(label, font=F_SANS_B(9))
        d.text((x + (tw - lw) / 2, 506), label, font=F_SANS_B(9), fill=INK)
        cw = d.textlength(cap, font=F_SANS(9))
        d.text((x + (tw - cw) / 2, 517), cap, font=F_SANS(9), fill=GRAY)


def draw_timeline(d):
    text(d, (12, 536), "THE WEEKEND INTO MONDAY", F_SANS_B(11), INK)
    for i, (day, items, today) in enumerate(TIMELINE):
        x = 12 + i * 250
        if i:
            d.line([(x - 4, 552), (x - 4, 610)], fill=LINE, width=1)
        text(d, (x, 552), day, F_SANS_B(12), RED if today else INK)
        for j, item in enumerate(items):
            text(d, (x, 567 + j * 11),
                 fit(d, item, F_SANS(11), 242), F_SANS(11), (40, 40, 40))


def draw_cards(d):
    for i, s in enumerate(CARDS):
        col, row = i % 2, i // 2
        x = 12 + col * 506
        y = 620 + row * 57
        rrect(d, [x, y, x + 494, y + 57], 4, fill=CARD, outline=LINE, width=1)
        draw_icon(d, x + 4, y + 8, 40, s["icon"], ICON_BG[s["icon"]])
        pw = d.textlength(s["pill"], font=F_SANS_B(8)) + 12
        title = "%d · %s" % (s["n"], s["title"])
        text(d, (x + 50, y + 4),
             fit(d, title, F_SANS_B(22), 440 - pw - 10), F_SANS_B(22), INK)
        pill(d, x + 488, y + 5, s["pill"], PILL_FILL[s["pill"]])
        text(d, (x + 50, y + 27), fit(d, s["deck1"], F_SANS(15), 440),
             F_SANS(15), (40, 40, 40))
        text(d, (x + 50, y + 42), fit(d, s["deck2"], F_SANS(15), 440),
             F_SANS(15), (40, 40, 40))


def draw_bottom(d):
    text(d, (12, 853), "ALSO ON — 12 MORE STORIES", F_SANS_B(12), INK)
    text(d, (684, 853), "WHERE IT HAPPENED · 11 PLACES PINNED",
         F_SANS_B(11), INK)
    d.line([(12, 868), (660, 868)], fill=LINE, width=1)
    d.line([(684, 868), (1012, 868)], fill=LINE, width=1)
    for i, (n, txt, day) in enumerate(INDEX):
        col, row = (0, i) if i < 6 else (1, i - 6)
        x = 12 if col == 0 else 340
        y = 872 + row * 14
        num = "%d · " % n
        d.text((x, y), num, font=F_SANS_B(10), fill=RED)
        nx = x + d.textlength(num, font=F_SANS_B(10))
        line = fit(d, txt + " — " + day, F_SANS(10), 320 - (nx - x) - 4)
        d.text((nx, y), line, font=F_SANS(10), fill=(40, 40, 40))
    # map
    pins = [(s["n"], s["pin"][0], s["pin"][1]) for s in STORIES if s.get("pin")]
    draw_map(d, 684, 872, 328, 82, pins)
    # DATE CHECK
    d.rectangle([12, 958, 1012, 1002], fill=(250, 235, 232),
                outline=RED, width=2)
    text(d, (20, 962), DATE_CHECK_HEAD, F_SANS_B(11), RED)
    ty = 976
    for line in wrap(d, DATE_CHECK_BODY, F_SANS(11), 972):
        text(d, (20, ty), line, F_SANS(11), (40, 40, 40))
        ty += 12
    # footer
    text(d, (12, 1005), SOURCES_LINE, F_SANS(9), GRAY)
    text(d, (12, 1014), LEGEND_LINE, F_SANS(9), GRAY)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    draw_masthead(d)
    draw_lead1(d, LEADS[0])
    draw_leads23(d)
    draw_numbers(d)
    draw_timeline(d)
    draw_cards(d)
    draw_bottom(d)
    img.save(OUT, optimize=True)
    import hashlib
    b = open(OUT, "rb").read()
    print("entry.png: %dx%d, %d bytes, sha256 %s"
          % (img.size[0], img.size[1], len(b), hashlib.sha256(b).hexdigest()))
    assert len(b) <= 1048576, "entry.png over 1 MiB"


if __name__ == "__main__":
    main()
