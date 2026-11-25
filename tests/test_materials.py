import unittest

from materials import list_feeds, read_feed

FIELDS = {
    'topology': ('service', 'dependency', 'region', 'flow', 'active_from_min', 'active_to_min'),
    'ownership': ('service', 'start_min', 'end_min', 'primary', 'backup', 'urgent_ack_min', 'normal_ack_min', 'normal_independent_min'),
    'alerts': ('observed_min', 'occurred_min', 'service', 'region', 'flow', 'kind', 'severity', 'evidence'),
    'pager': ('observed_min', 'kind', 'reference', 'actor', 'scope', 'outcome'),
}


class MaterialTest(unittest.TestCase):
    def test_feed_fields(self):
        self.assertEqual(list_feeds(), sorted(FIELDS))
        for name, fields in FIELDS.items():
            with self.subTest(feed=name):
                records = list(read_feed(name))
                self.assertTrue(records)
                self.assertTrue(all(set(row) == set(fields) for row in records))
