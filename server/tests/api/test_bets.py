import unittest
from src.db.db_utils import exec_sql_file
from tests.test_utils import *


class TestExample(unittest.TestCase):
    def setUp(self):
        """
        Initialize DB using API call
        """
        post_rest_call(self, "http://localhost:8080/manage/init")
        exec_sql_file("data/test_data.sql")
        print("DB is reset")

    def test_list_bets(self):
        """
        List all the bets
        """
        result = get_rest_call(self, "http://localhost:8080/bets")
        self.assertEqual(len(result), 2)

    def test_bet_create(self):
        """
        Add an record to bets
        """
        data = {
            "user_id": "e6594402-9d10-48bb-bf0b-ed97394a9555",
            "event_id": "1e49f61a-0dbf-4a93-a6e2-21480cee3b32",
            "team_id": "e7a81594-cee6-4c7d-aa7d-9bfa3fbbab1c",
            "points": "10",
        }
        result = post_rest_call(self, "http://localhost:8080/bets", params=data)
        self.assertEqual(result, {"message": "Bet created."})

    def test_delete_bet(self):
        """
        Delete a bet
        """
        result = delete_rest_call(
            self, "http://localhost:8080/bets/bb818b19-f0fa-4388-832e-b5888519fc7f"
        )
        self.assertEqual(result, {"message": "Bet deleted."})

    def test_bet_detail(self):
        """
        Get the details of a bet
        """
        result = get_rest_call(
            self, "http://localhost:8080/bets/8df7f992-d6b7-4654-9e3f-9dedbf4c54bf"
        )
        print(result)
        self.assertEqual(
            result,
            ['8df7f992-d6b7-4654-9e3f-9dedbf4c54bf', 'a01aee32-6489-4162-b6be-c8a86bb6ef7e', '6d83e946-46c5-494e-a788-bf3e85a466a4', '61c70f68-a3a5-404e-9102-a9effbb5b386', 25]
        )

    def test_edit_bet(self):
        """
        Edit a bet
        """
        new_vals = {"team_id": "61c70f68-a3a5-404e-9102-a9effbb5b386", "points": 12, "event_id": "1e49f61a-0dbf-4a93-a6e2-21480cee3b32"}

        res_put = put_rest_call(
            self,
            "http://localhost:8080/bets/8df7f992-d6b7-4654-9e3f-9dedbf4c54bf",
            params=new_vals,
        )
        # Check if response is correct
        self.assertEqual(res_put, {"0": "Success"})
