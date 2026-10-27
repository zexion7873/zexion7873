"""Rewrite README.md's radar block, and its banner SVGs, from GitHub Radar's /api/latest-week.

Usage: python3 .github/scripts/radar.py [README path]
RADAR_URL overrides the site origin (e.g. http://localhost:3000 for a local run).
"""

import html
import json
import os
import re
import sys
import urllib.request
from datetime import date

SITE = os.environ.get("RADAR_URL", "https://whyisthistrending.vercel.app")
START, END = "<!-- radar:start -->", "<!-- radar:end -->"
BANNERS = {"light": "assets/radar-light.svg", "dark": "assets/radar-dark.svg"}

# The site's Broadsheet tokens (github-radar-ui app/globals.css), light and dark.
PALETTE = {
    "light": {"bg": "#fdfbf7", "border": "#d4cdbf", "fg": "#1a1714", "muted": "#7a7268", "accent": "#b84e2b"},
    "dark": {"bg": "#1c1a16", "border": "#35322d", "fg": "#ece6db", "muted": "#928a7d", "accent": "#d4643f"},
}

# The site's icon (github-radar-ui app/icon.svg): the R is outlined, so no font is needed.
MARK = """<rect width="32" height="32" fill="#1a1714"/>
<path d="M14.9 6.4 A6 6 0 0 1 20.9 12.4" fill="none" stroke="#d4643f" stroke-width="1.8" stroke-linecap="round"/>
<path d="M14.9 3.4 A9 9 0 0 1 23.9 12.4" fill="none" stroke="#d4643f" stroke-width="1.8" stroke-linecap="round"/>
<path fill="#f7f4ef" d="M14.05 23.50L8.23 23.50L8.23 23.27L8.70 23.11Q9.16 22.95 9.30 22.69Q9.43 22.43 9.43 21.95L9.43 10.07Q9.43 9.61 9.31 9.35Q9.18 9.09 8.75 8.93L8.23 8.73L8.23 8.50L14.73 8.50Q17.41 8.50 18.84 9.51Q20.27 10.52 20.27 12.32Q20.27 13.32 19.52 14.32Q18.77 15.32 17.16 15.86L20.32 22.14Q20.52 22.52 20.78 22.76Q21.05 23 21.48 23.18L21.77 23.30L21.77 23.50L17.70 23.50L14.34 16.34L12.80 16.34L12.80 21.95Q12.80 22.39 12.93 22.66Q13.07 22.93 13.50 23.07L14.05 23.27L14.05 23.50ZM12.80 8.95L12.80 15.89L13.89 15.89Q15.52 15.89 16.25 15.01Q16.98 14.14 16.98 12.41Q16.98 10.66 16.30 9.81Q15.61 8.95 14 8.95Z"/>
<circle cx="14.9" cy="12.4" r="1.4" fill="#d4643f"/>"""

SERIF = "Georgia, 'Times New Roman', serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"


def clean(s: str) -> str:
    # Escaping `<` keeps agent-written text from ever forging the END marker.
    return html.escape(" ".join(s.split()), quote=False)


def banner(week: str, theme: str) -> str:
    # ASCII only: an SVG loaded via <img> renders with the viewer's fonts, so CJK would clip.
    c = PALETTE[theme]
    label = date.fromisoformat(week).strftime("%b %-d, %Y")
    arcs = "\n".join(
        f'<circle cx="720" cy="170" r="{r}" fill="none" stroke="{c["accent"]}" stroke-opacity="{o}" stroke-width="2"/>'
        for r, o in ((70, 0.55), (115, 0.35), (160, 0.2), (205, 0.1))
    )
    # The <img> scales to the column, so on a phone every size here shrinks ~2.3x.
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="720" height="140" viewBox="0 0 720 140">
<defs><clipPath id="card"><rect x="1" y="1" width="718" height="138" rx="12"/></clipPath></defs>
<rect x="1" y="1" width="718" height="138" rx="12" fill="{c["bg"]}" stroke="{c["border"]}" stroke-width="2"/>
<g clip-path="url(#card)">
{arcs}
<circle cx="660" cy="114" r="6" fill="{c["accent"]}"/>
</g>
<g transform="translate(26 26) scale(2.75)">
{MARK}
</g>
<text x="138" y="56" font-family="{MONO}" font-size="20" letter-spacing="2" fill="{c["accent"]}">WEEKLY TOP 3</text>
<text x="138" y="104" font-family="{SERIF}" font-size="44" fill="{c["fg"]}">Week of {label}</text>
</svg>
"""


def render(data: dict) -> str:
    label = date.fromisoformat(data["week"]).strftime("%b %-d, %Y")
    lines = [
        # 600 matches the perchling GIF above it, which is 600px wide natively.
        f'<p align="center"><a href="{SITE}/trending"><picture>'
        f'<source media="(prefers-color-scheme: dark)" srcset="{BANNERS["dark"]}">'
        f'<img src="{BANNERS["light"]}" width="600" alt="GitHub Radar, week of {label}: the top three trending repos">'
        "</picture></a></p>",
        "",
        "Picked, summarized and roasted by scheduled agents, with no one in the loop."
        " Summaries and takes are their own words, in Traditional Chinese, unedited."
        f" [Full chart →]({SITE}/trending)",
        "",
    ]
    for i, r in enumerate(data["repos"], 1):
        link = r["link"] or f"https://github.com/{r['repo']}"
        # No-break spaces keep the pill on one line on a phone.
        stars = f" · `★ {r['starsPerWeek']:,} / wk`" if r["starsPerWeek"] else ""
        lines += [
            f"{i}. **[{clean(r['repo'])}]({link})**{stars}<br>",
            f"   {clean(r['summary'])}",
            "",
            f"   > {clean(r['take'])}",
            "",
        ]
    return "\n".join(lines).rstrip()


def main() -> None:
    path = sys.argv[1] if len(sys.argv) > 1 else "README.md"
    with urllib.request.urlopen(f"{SITE}/api/latest-week", timeout=60) as res:
        data = json.load(res)  # a 503 raises HTTPError, so the README is never blanked
    if not data["repos"]:
        sys.exit("radar returned no repos")

    with open(path, encoding="utf-8") as f:
        readme = f.read()
    pattern = re.compile(re.escape(START) + ".*?" + re.escape(END), re.S)
    if not pattern.search(readme):
        sys.exit(f"{path} has no {START} … {END} block")

    root = os.path.dirname(path)
    os.makedirs(os.path.join(root, "assets"), exist_ok=True)
    for theme, rel in BANNERS.items():
        with open(os.path.join(root, rel), "w", encoding="utf-8") as f:
            f.write(banner(data["week"], theme))
    block = f"{START}\n{render(data)}\n{END}"
    with open(path, "w", encoding="utf-8") as f:
        f.write(pattern.sub(lambda _: block, readme, count=1))


if __name__ == "__main__":
    main()
