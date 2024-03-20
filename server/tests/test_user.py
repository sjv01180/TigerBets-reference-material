import unittest
import json

from test_utils import *


class TestUser(unittest.TestCase):
    def clear_data(self):
        url = "http://localhost:8080/users/clear"
        post_rest_call(self, url)

    def test_login(self):
        self.clear_data()

        url = "http://localhost:8080/users/login"
        params = json.dumps({"username": "aaa"})
        headers = {'Content-Type': 'application/json'}

        post_rest_call(self, url, params, headers, 401)

        url = "http://localhost:8080/users/register"
        params = json.dumps({"username": "aaa", "fullname": "test", "email": "abc@gmail.com"})
        headers = {'Content-Type': 'application/json'}

        response = post_rest_call(self, url, params, headers, 200)
        self.assertEqual("aaa", response["user"]["username"])

        url = "http://localhost:8080/users/login"
        params = json.dumps({"username": "aaa"})
        headers = {'Content-Type': 'application/json'}

        response = post_rest_call(self, url, params, headers, 200)
        self.assertEqual("aaa", response["user"]["username"])
        self.assertTrue(len(response["session_id"]) > 0)

    def test_register(self):
        self.clear_data()

        url = "http://localhost:8080/users/register"
        params = json.dumps({"username": "aaa", "fullname": "test", "email": "abc@gmail.com"})
        headers = {'Content-Type': 'application/json'}

        response = post_rest_call(self, url, params, headers, 200)
        self.assertEqual("aaa", response["user"]["username"])

        response = post_rest_call(self, url, params, headers, 401)
        self.assertEqual("username exists", response["error"])
