import json
import unittest
from unittest.mock import patch, MagicMock
from tests.test_utils import *


class TestUser(unittest.TestCase):
    def setUp(self):
        """
        Initialize mock API calls
        """
        self.mock_post_rest_call = patch('tests.test_utils.post_rest_call').start()

    def tearDown(self):
        """
        Stop mocking
        """
        patch.stopall()

    @unittest.skip("skip until mocked")
    def test_login(self):
        # Mocking clear data
        self.mock_post_rest_call.return_value = None

        # Mocking registration
        self.mock_post_rest_call.side_effect = [
            {"user": {"username": "aaa"}, "status_code": 200},  # Successful registration
            {"user": {"username": "aaa", "session_id": "fake_session_id"}, "status_code": 200}  # Successful login
        ]

        url = "http://localhost:8080/users/login"
        params = json.dumps({"username": "aaa"})
        headers = {'Content-Type': 'application/json'}

        response = post_rest_call(self, url, params, headers, 200)
        self.assertEqual("aaa", response["user"]["username"])
        self.assertTrue(len(response["session_id"]) > 0)

    @unittest.skip("skip until mocked")
    def test_register(self):
        # Mocking registration
        self.mock_post_rest_call.return_value = {"user": {"username": "abc"}, "status_code": 200}  # Successful registration

        url = "http://localhost:8080/users/register"
        params = json.dumps({"username": "abc", "fullname": "test", "email": "abc@gmail.com"})
        headers = {'Content-Type': 'application/json'}

        # Mocking duplicate registration
        self.mock_post_rest_call.return_value = {"error": "username exists", "status_code": 401}

        response = post_rest_call(self, url, params, headers, 401)
        self.assertEqual("username exists", response["error"])
