import unittest
from src.db.db_utils import exec_sql_file
from tests.test_utils import *

class TestEventManagement(unittest.TestCase):
    def setUp(self):
        """
        Initialize DB using API call
        """
        post_rest_call(self, "http://localhost:8080/manage/init")
        exec_sql_file("data/populate_event.sql")
        print("DB is reset")

    def test_list_events(self):
        """
        List all the events
        """
        result = get_rest_call(self, "http://localhost:8080/events")
        self.assertTrue(len(result) > 0)

    def test_event_creation(self):
        """
        create an new event
        """
        data = {
            "event_name": "New Event",
            "team_a_id": "4a0c8c25-e548-4110-a3a9-f44f6a4256a4",
            "team_b_id": "5e1dbdd3-aa30-456b-9820-e3e7825b9bb9"
        }
        result = post_rest_call(self, "http://localhost:8080/events", params=data)
        self.assertEqual(result, {"message": "Event created."})

    def test_edit_event(self):
        """
        Edit an event
        """
        new_vals = {"event_name": "Updated Event Name"}

        res_put = put_rest_call(
            self,
            "http://localhost:8080/events/c7fd33bc-f8c4-4b5e-b1aa-9f2e4c4a6b88",
            params=new_vals,
        )
        self.assertEqual(res_put, {"0": "Success"})

    def test_delete_event(self):
        """
        Delete an event
        """
        result = delete_rest_call(self, "http://localhost:8080/events/a7a3afc2-3f4a-4aeb-8c06-9e667c5b4f67")
        self.assertIn("Event deleted", result['message'])

    def test_event_detail(self):
        """
        Get the details of an event
        """
        event_id = "8df7f992-d6b7-4654-9e3f-9dedbf4c54bf"
        result = get_rest_call(self, f"http://localhost:8080/events/{event_id}")
        self.assertIn("RIT Random Event", result)

if __name__ == '__main__':
    unittest.main()
