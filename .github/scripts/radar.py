"""Rewrite README.md's radar block from GitHub Radar's /api/latest-week.

Usage: python3 .github/scripts/radar.py [README path]
RADAR_URL overrides the site origin (e.g. http://localhost:3000 for a local run).
"""

import html
import json
import os
import re
import sys
import urllib.request

SITE = os.environ.get("RADAR_URL", "https://whyisthistrending.vercel.app")
START, END = "<!-- radar:start -->", "<!-- radar:end -->"


def clean(s: str) -> str:
    # Escaping `<` keeps agent-written text from ever forging the END marker.
    return html.escape(" ".join(s.split()), quote=False)


def render(data: dict) -> str:
    lines = [
        f"<sub>Week of {data['week']}. Picked, summarized and roasted by the radar's"
        " scheduled agents, in Traditional Chinese, with no one in the loop."
        f" [Full chart →]({SITE}/trending)</sub>",
        "",
    ]
    for i, r in enumerate(data["repos"], 1):
        link = r["link"] or f"https://github.com/{r['repo']}"
        stars = f" · ★ {r['starsPerWeek']:,} this week" if r["starsPerWeek"] else ""
        lines += [
            f"{i}. **[{clean(r['repo'])}]({link})**{stars}<br>",
            f"   {clean(r['summary'])}<br>",
            f"   <i>{clean(r['take'])}</i>",
        ]
    return "\n".join(lines)


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
    block = f"{START}\n{render(data)}\n{END}"
    with open(path, "w", encoding="utf-8") as f:
        f.write(pattern.sub(lambda _: block, readme, count=1))


if __name__ == "__main__":
    main()
