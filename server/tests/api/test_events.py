import unittest
from unittest.mock import patch, MagicMock
from src.db.db_utils import exec_sql_file
from tests.test_utils import *


class TestEventManagement(unittest.TestCase):
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

    def test_list_events(self):
        """
        List all the events
        """
        self.mock_get_rest_call.return_value = [{"event_id": "1"}, {"event_id": "2"}]
        result = self.mock_get_rest_call("http://localhost:8080/events")
        self.assertTrue(len(result) > 0)

    def test_event_creation(self):
        """
        Create a new event
        """
        data = {
            "event_name": "New Event",
            "team_a_id": "4a0c8c25-e548-4110-a3a9-f44f6a4256a4",
            "team_b_id": "5e1dbdd3-aa30-456b-9820-e3e7825b9bb9"
        }
        self.mock_post_rest_call.return_value = {"message": "Event created."}
        result = self.mock_post_rest_call("http://localhost:8080/events", params=data)
        self.assertEqual(result, {"message": "Event created."})

    def test_edit_event(self):
        """
        Edit an event
        """
        new_vals = {"event_name": "Updated Event Name"}

        self.mock_put_rest_call.return_value = {"0": "Success"}
        res_put = self.mock_put_rest_call(
            "http://localhost:8080/events/c7fd33bc-f8c4-4b5e-b1aa-9f2e4c4a6b88",
            params=new_vals,
        )
        self.assertEqual(res_put, {"0": "Success"})

    def test_delete_event(self):
        """
        Delete an event
        """
        self.mock_delete_rest_call.return_value = {"message": "Event deleted."}
        result = self.mock_delete_rest_call("http://localhost:8080/events/a7a3afc2-3f4a-4aeb-8c06-9e667c5b4f67")
        self.assertIn("Event deleted", result['message'])

    def test_event_detail(self):
        """
        Get the details of an event
        """
        event_id = "8df7f992-d6b7-4654-9e3f-9dedbf4c54bf"
        self.mock_get_rest_call.return_value = {"event_name": "RIT Random Event"}
        result = self.mock_get_rest_call(f"http://localhost:8080/events/{event_id}")
        self.assertIn("event_name", result)
        self.assertEqual(result["event_name"], "RIT Random Event")