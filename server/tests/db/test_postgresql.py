import unittest
from tests.test_utils import *


class TestPostgreSQL(unittest.TestCase):
    # Only for integration test
    def test_can_connect(self):
        # version = get_rest_call(self, "http://localhost:8080/manage/version")
        # self.assertTrue(version[0].startswith("PostgreSQL"))
        pass
