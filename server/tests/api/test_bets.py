import unittest
from unittest.mock import patch, MagicMock
from src.db.db_utils import exec_sql_file
from tests.test_utils import *


class TestExample(unittest.TestCase):
    def setUp(self):
        """
        Initialize mock API calls and DB setup
        """
        self.mock_post_rest_call = patch('tests.test_utils.post_rest_call').start()
        self.mock_get_rest_call = patch('tests.test_utils.get_rest_call').start()
        self.mock_delete_rest_call = patch('tests.test_utils.delete_rest_call').start()
        self.mock_put_rest_call = patch('tests.test_utils.put_rest_call').start()

    def tearDown(self):
        """
        Stop mocking
        """
        patch.stopall()

    def test_list_bets(self):
        """
        List all the bets
        """
        self.mock_get_rest_call.return_value = [{"bet_id": "1"}, {"bet_id": "2"}]
        result = self.mock_get_rest_call("http://localhost:8080/bets")
        self.assertEqual(len(result), 2)

    def test_bet_create(self):
        """
        Add a record to bets
        """
        data = {
            "user_id": "e6594402-9d10-48bb-bf0b-ed97394a9555",
            "event_id": "1e49f61a-0dbf-4a93-a6e2-21480cee3b32",
            "team_id": "e7a81594-cee6-4c7d-aa7d-9bfa3fbbab1c",
            "points": "10",
        }
        self.mock_post_rest_call.return_value = {"message": "Bet created."}
        result = self.mock_post_rest_call("http://localhost:8080/bets", params=data)
        self.assertEqual(result, {"message": "Bet created."})

    def test_delete_bet(self):
        """
        Delete a bet
        """
        self.mock_delete_rest_call.return_value = {"message": "Bet deleted."}
        result = self.mock_delete_rest_call(
            "http://localhost:8080/bets/bb818b19-f0fa-4388-832e-b5888519fc7f"
        )
        self.assertEqual(result, {"message": "Bet deleted."})

    def test_bet_detail(self):
        """
        Get the details of a bet
        """
        self.mock_get_rest_call.return_value = ['8df7f992-d6b7-4654-9e3f-9dedbf4c54bf', 'a01aee32-6489-4162-b6be-c8a86bb6ef7e', '6d83e946-46c5-494e-a788-bf3e85a466a4', '61c70f68-a3a5-404e-9102-a9effbb5b386', 25]
        result = self.mock_get_rest_call(
            "http://localhost:8080/bets/8df7f992-d6b7-4654-9e3f-9dedbf4c54bf"
        )
        self.assertEqual(
            result,
            ['8df7f992-d6b7-4654-9e3f-9dedbf4c54bf', 'a01aee32-6489-4162-b6be-c8a86bb6ef7e', '6d83e946-46c5-494e-a788-bf3e85a466a4', '61c70f68-a3a5-404e-9102-a9effbb5b386', 25]
        )

    def test_edit_bet(self):
        """
        Edit a bet
        """
        new_vals = {"team_id": "61c70f68-a3a5-404e-9102-a9effbb5b386", "points": 12, "event_id": "1e49f61a-0dbf-4a93-a6e2-21480cee3b32"}

        self.mock_put_rest_call.return_value = {"0": "Success"}
        res_put = self.mock_put_rest_call(
            "http://localhost:8080/bets/8df7f992-d6b7-4654-9e3f-9dedbf4c54bf",
            params=new_vals,
        )
        self.assertEqual(res_put, {"0": "Success"})
