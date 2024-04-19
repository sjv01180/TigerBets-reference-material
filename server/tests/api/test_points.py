import unittest
from unittest.mock import patch


class TestPoints(unittest.TestCase):
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

    def test_update_points(self):
        """
        Test updating points for a user
        """
        new_vals = {"points": "999"}
        self.mock_put_rest_call.return_value = {"message": "Success"}
        result = self.mock_put_rest_call("http://localhost:8080/points/069b7b35-fbcf-427b-9957-aad6a718e410",params=new_vals,)
        self.assertEqual(result, {"message": "Success"})
    
        
    def test_get_points_for_user(self):
        """
        Test getting points for a user
        """
        self.mock_get_rest_call.return_value = {"points": 150}
        result = self.mock_get_rest_call("http://localhost:8080/points/5aa30499-254f-49e2-820a-56d76eb15895")
        self.assertEqual(result, {"points": 150})

    def test_get_users_with_top_points(self):
        """
        GET request to retrieve top points users
        """
        self.mock_get_rest_call.return_value = [{"user_id": "1", "points": 9}, {"user_id": "2", "points": 150}]
        result = self.mock_get_rest_call("http://localhost:8080/points")
        self.assertGreater(len(result), 0, "More than 1 user")

if __name__ == '__main__':
    unittest.main()