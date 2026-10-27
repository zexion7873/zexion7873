import re
import unittest

from radar import meter, meter_full, render


def repo(stars, momentum):
    return {"repo": "a/b", "link": None, "starsPerWeek": stars, "momentum": momentum, "summary": "s", "take": "t"}


def rects(svg):
    return [dict(re.findall(r'(\w+)="([^"]+)"', r)) for r in re.findall(r"<rect [^>]+/>", svg)]


class MeterTest(unittest.TestCase):
    def test_baseline_above_leader_sets_full(self):
        # #1 has 10,000 this week; #2 usually does 20,000 (8,000 / 0.4) but slipped.
        repos = [repo(10000, 2.0), repo(8000, 0.4)]
        self.assertEqual(meter_full(repos), 20000)
        track, fill, *tick = rects(meter(repos[1], meter_full(repos)))
        self.assertEqual(fill["width"], "48")  # 120 * 8000 / 20000
        self.assertEqual(tick[1]["x"], "118")  # baseline = full: the last 2px, not past the end
        self.assertEqual(tick[1]["fill"], "#8a8a8a")  # on the bare track, so grey

    def test_tick_inside_fill_is_white(self):
        repos = [repo(15072, 15072 / 4805)]
        track, fill, *tick = rects(meter(repos[0], meter_full(repos)))
        self.assertEqual(fill["width"], "120")
        self.assertEqual(tick[1]["x"], "37")  # round(120 * 4805 / 15072) - 1
        self.assertEqual(tick[1]["fill"], "#fff")

    def test_no_momentum_draws_no_tick(self):
        self.assertEqual(len(rects(meter(repo(5000, None), 5000))), 2)

    def test_label_only_when_hot(self):
        out = render({"week": "2026-10-26", "repos": [repo(9000, 3.14), repo(8000, 1.12), repo(7000, None)]})
        self.assertIn("×3.1 vs its avg", out)
        self.assertEqual(out.count("vs its avg"), 1)

    def test_missing_momentum_key_fails(self):
        with self.assertRaises(KeyError):
            meter_full([{"starsPerWeek": 100}])


if __name__ == "__main__":
    unittest.main()
