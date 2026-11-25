import unittest

from materials import read_feed


class InputsTest(unittest.TestCase):
    def test_alerts_span_route_and_ownership_changes(self):
        links = [r for r in read_feed("topology") if r["service"] == "summarizer" and r["flow"] == "interactive"]
        reports = [r for r in read_feed("alerts") if r["service"] == "summarizer"]
        self.assertEqual(links[0]["active_to_min"], links[1]["active_from_min"])
        late = next(r for r in reports if r["evidence"] == "front-2")
        self.assertLess(late["occurred_min"], links[1]["active_from_min"])
        self.assertGreater(late["observed_min"], links[1]["active_from_min"])
        calls = list(read_feed("pager"))
        self.assertTrue(any(r["kind"] == "delivery" for r in calls))
        handover = next(r["end_min"] for r in read_feed("ownership") if r["service"] == "summarizer")
        self.assertTrue(any(r["observed_min"] > handover and r["actor"] == "wei" and r["kind"] == "ack" for r in calls))

