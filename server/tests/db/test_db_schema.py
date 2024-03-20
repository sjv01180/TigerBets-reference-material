import unittest
from tests.test_utils import *


class TestDBSchema(unittest.TestCase):
    def test_rebuild_tables(self):
        """Rebuild the tables"""
        post_rest_call(self, "http://localhost:8080/manage/init")
        bets = get_rest_call(self, "http://localhost:8080/bets")
        self.assertEqual(len(bets), 0)

    def test_rebuild_tables_is_idempotent(self):
        """Drop and rebuild the tables twice"""
        post_rest_call(self, "http://localhost:8080/manage/init")
        post_rest_call(self, "http://localhost:8080/manage/init")
        bets = get_rest_call(self, "http://localhost:8080/bets")
        self.assertEqual(len(bets), 0)
