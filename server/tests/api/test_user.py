import json
import unittest
from unittest.mock import patch
from tests.test_utils import post_rest_call


class TestUser(unittest.TestCase):
    def clear_data(self):
        url = "http://localhost:8080/users/clear"
        post_rest_call(self, url)

    def setUp(self):
        """
        Initialize mock API calls
        """
        self.mock_post_rest_call = patch('tests.test_utils.post_rest_call').start()
        self.mock_put_rest_call = patch('tests.test_utils.put_rest_call').start()

    def tearDown(self):
        """
        Stop mocking
        """
        patch.stopall()

    
    def test_register(self):
        """
        Register a new user account
        """

        # Mocking registration variables
        url = "http://localhost:8080/users/register"
        self.mock_post_rest_call.return_value = {"error": "Invalid parameters", "status_code": 400}
        input_valueerror = {"username": "err", "fullname": "test_error", "email": "err@evilemail.com", "password": 12345}
        input_valid = {"username": "aaa", "fullname": "test", "email": "abc@gmail.com", "password": "12345"}
        output_user = {"username": "aaa", "full_name": "test", "email": "abc@gmail.com"}

        # Mocking output validators
        self.mock_post_rest_call.side_effect = [
             {"error": "Invalid parameters", "status_code": 400},       # Invalid Input Values
             {"user": output_user, "status_code": 200},                 # Valid User Registration
             {"error": "username is not unique", "status_code": 401},   # Invalid Duplicate Registration
        ]

        # Mocking invalid input value
        result = self.mock_post_rest_call(url, params=input_valueerror)

        # Mocking valid user registration
        result = self.mock_post_rest_call(url, params=input_valid)
        self.assertEqual(result["user"]["username"], output_user["username"])
        self.assertEqual(result["user"]["full_name"], output_user["full_name"])
        self.assertEqual(result["user"]["email"], output_user["email"])

        # Mocking invalid duplicate registration
        result = self.mock_post_rest_call(url, params=input_valid)

    def test_login(self):
        """
        Log in a registered user to the system
        """

        # Mocking login variables
        url = "http://localhost:8080/users/login"
        input_register = {"username": "aaa", "fullname": "test", "email": "abc@gmail.com", "password": "12345"}
        input_valid = {"username": "aaa", "password": "12345"}
        input_unknown_user = {"username": "bbb", "password": "12345"}
        input_wrong_password = {"username": "aaa", "password": "54321"}
        output_user = {"username": "aaa", "full_name": "test", "email": "abc@gmail.com"}

        # Mocking output validators
        self.mock_post_rest_call.side_effect = [
             {"user": output_user, "status_code": 200},                                     # Valid User Registration
             {"user": output_user, "session_id": "fake_session_id", "status_code": 200},    # Valid User Login
             {"error": "username or password is incorrect", "status_code": 401},            # Invalid User Login 1
             {"error": "username or password is incorrect", "status_code": 401}             # Invalid User Login 2
        ]

        # Mocking User Registration
        self.mock_post_rest_call("http://localhost:8080/users/register", params=input_register)
        
        # Mocking Valid Login
        self.mock_post_rest_call(url, params=input_valid)
        
        # Mocking Invalid Login: Unknown User
        self.mock_post_rest_call(url, params=input_unknown_user)

        # Mocking Invalid Login: Wrong Password
        self.mock_post_rest_call(url, params=input_wrong_password)
       
    def test_logoff(self):
        """
        Log off a user account from the system
        """

        # Mocking logoff variables
        url = "http://localhost:8080/users/logoff"
        input_register = {"username": "aaa", "fullname": "test", "email": "abc@gmail.com", "password": "12345"}
        output_user = {"username": "aaa", "full_name": "test", "email": "abc@gmail.com"}
        input_login = {"username": "aaa", "password": "12345"}
        input_valid = {"session": "fake_session_id"}
        input_wrong_session_id = {"session": "dubious_session_id"}

        # Mocking output validators
        self.mock_post_rest_call.side_effect = [
             {"user": output_user, "status_code": 200},                                     # Valid User Registration
             {"user": output_user, "session_id": "fake_session_id", "status_code": 200},    # Valid User Login
             {"error": "user could not be logged off", "status_code": 401},                 # Invalid User Logoff Wrong Session
             {"success": "logoff successful", "status_code": 200},                          # Valid User Logoff
             {"error": "user could not be logged off", "status_code": 401}                  # Invalid User Logoff Duplicate
        ]
        
        # Mocking Register & Login
        self.mock_post_rest_call("http://localhost:8080/users/register", params=input_register)
        self.mock_post_rest_call("http://localhost:8080/users/login", params=input_login)
        
        # Mocking Invalid Logoff: Wrong Session
        self.mock_post_rest_call(url, params=input_wrong_session_id)

        # Mocking Valid Logoff
        self.mock_post_rest_call(url, params=input_valid)

        # Mocking Invalid Logoff: Duplicate
        self.mock_post_rest_call(url, params=input_valid)

    def test_find_user(self):
        """
        Search for a single user within the system
        """

        # Mocking find user variables
        url = "http://localhost:8080/users/find_user"
        input_register1 = {"username": "thing1", "fullname": "test1", "email": "abc1@gmail.com", "password": "12345"}
        input_login1 = {"username": "thing1", "password": "12345"}
        input_register2 = {"username": "thing2", "fullname": "test2", "email": "abc2@gmail.com", "password": "22222"}
        input_login2 = {"username": "thing2", "password": "22222"}
        output_user1 = {"username": "thing1", "full_name": "test1", "email": "abc1@gmail.com"}
        output_user2 = {"username": "thing2", "full_name": "test2", "email": "abc2@gmail.com"}
        input_valid_self = {"username": "thing1", "session": "fake_session_id1"}
        input_valid_other = {"username": "thing2", "session": "fake_session_id1"}
        input_wrong_session_id = {"username": "thing1", "session": "dubious_session_id"}
        input_unknown_user = {"username": "thing3", "session": "fake_session_id2"}

        # Mocking output validators
        self.mock_post_rest_call.side_effect = [
             {"user": output_user1, "status_code": 200},                                    # Valid User Registration 1
             {"user": output_user1, "session_id": "fake_session_id1", "status_code": 200},  # Valid User Login 1
             {"user": output_user2, "status_code": 200},                                    # Valid User Registration 2
             {"user": output_user2, "session_id": "fake_session_id2", "status_code": 200},  # Valid User Login 2
             {"error": "user could not be found", "status_code": 401},                      # Invalid Find User Bad Session
             {"error": "user could not be found", "status_code": 401},                      # Invalid Find User Unknown Username
             {"user": output_user1, "status_code": 200},                                    # Valid Find User Self
             {"user": output_user2, "status_code": 200}                                     # Valid Find User Other
        ]

        # Mocking Register & Login Account 1
        self.mock_post_rest_call("http://localhost:8080/users/register", params=input_register1)
        self.mock_post_rest_call("http://localhost:8080/users/login", params=input_login1)

        # Mocking Register & Login Account 2
        self.mock_post_rest_call("http://localhost:8080/users/register", params=input_register2)
        self.mock_post_rest_call("http://localhost:8080/users/login", params=input_login2)
        
        # Mocking Invalid Find User: Bad Session
        self.mock_post_rest_call(url, params=input_wrong_session_id)

        # Mocking Invalid Find User: Unknown Username
        self.mock_post_rest_call(url, params=input_unknown_user)

        # Mocking Valid Find User: Self
        result=self.mock_post_rest_call(url, params=input_valid_self)
        self.assertEqual(result["user"]["username"], output_user1["username"])
        self.assertEqual(result["user"]["full_name"], output_user1["full_name"])
        self.assertEqual(result["user"]["email"], output_user1["email"])
        
        # Mocking Valid Find User: Other
        result=self.mock_post_rest_call(url, params=input_valid_other)
        self.assertEqual(result["user"]["username"], output_user2["username"])
        self.assertEqual(result["user"]["full_name"], output_user2["full_name"])
        self.assertEqual(result["user"]["email"], output_user2["email"])

    def test_update(self):
        """
        Edit a user's account information as the user itself
        """

        # Mocking update variables
        url = "http://localhost:8080/users/update"
        input_register = {"username": "aaa", "fullname": "test", "email": "abc@gmail.com", "password": "12345"}
        output_user = {"username": "aaa", "full_name": "test", "email": "abc@gmail.com"}
        input_login = {"username": "aaa", "password": "12345"}
        input_valid = {"newuser": "fullstack", "newname": "Huell Schtakh", "newemail": "schtakh@test.com", "session": "fake_session_id"}
        input_wrong_session_id = {"newuser": "eventhandler", "newname": "Yvette Chandler", "newemail": "ychandler@test.com", "session": "dubious_session_id"}
        output_valid = {"username": "fullstack", "full_name": "Huell Schtakh", "email": "schtakh@test.com"}

        # Mocking output validators
        self.mock_post_rest_call.side_effect = [
             {"user": output_user, "status_code": 200},                                     # Valid User Registration
             {"user": output_user, "session_id": "fake_session_id", "status_code": 200},    # Valid User Login
        ]
        self.mock_put_rest_call.side_effect = [
            {"error": "failed to update user", "status_code": 401},                        # Invalid User Update Wrong Session
            {"user": output_valid, "status_code": 200}                                     # Valid User Update
        ]

        # Mocking Register & Login
        self.mock_post_rest_call("http://localhost:8080/users/register", params=input_register)
        self.mock_post_rest_call("http://localhost:8080/users/login", params=input_login)

        # Mocking Invalid Update: Wrong Session
        self.mock_put_rest_call(url, params=input_wrong_session_id)

        # Mocking Valid Update
        self.mock_put_rest_call(url, params=input_valid)

    def test_deactivate_account(self):
        """
        Removes user account from system
        """

        # Mocking update variables
        url = "http://localhost:8080/users/deactivate"
        input_register = {"username": "aaa", "fullname": "test", "email": "abc@gmail.com", "password": "12345"}
        output_user = {"username": "aaa", "full_name": "test", "email": "abc@gmail.com"}
        input_login = {"username": "aaa", "password": "12345"}
        input_valid = {"username": "aaa", "session": "fake_session_id"}
        input_update_invalid = {"newuser": "sloam", "newname": "Sandy Loam", "newemail": "sloam@test.com", "session": "fake_session_id"}
        input_wrong_session_id = {"username": "aaa", "session": "dubious_session_id"}
        
        # Mocking output validators
        self.mock_post_rest_call.side_effect = [
             {"user": output_user, "status_code": 200},                                     # Valid User Registration
             {"user": output_user, "session_id": "fake_session_id", "status_code": 200}     # Valid User Login
        ]
        self.mock_put_rest_call.side_effect = [
            {"error": "failed to delete", "status_code": 401},                        # Invalid User Deactivate: Wrong Session
            {"user": output_user, "status_code": 200},                                # Valid User Deactivate
            {"error": "failed to delete", "status_code": 401},                        # Invalid User Deactivate: Duplicate Deactivate
            {"error": "failed to update user", "status_code": 401},                   # Invalid User Update: Deactivated User 
        ]

        # Mocking Register & Login
        self.mock_post_rest_call("http://localhost:8080/users/register", params=input_register)
        self.mock_post_rest_call("http://localhost:8080/users/login", params=input_login)
        
        # Mocking Invalid User Deactivate: Wrong Session
        self.mock_put_rest_call(url, params=input_wrong_session_id)

        # Mocking Valid User Deactivate
        self.mock_put_rest_call(url, params=input_valid)

        # Mocking Invalid User Deactivate: Duplicate Deactivate
        self.mock_put_rest_call(url, params=input_valid)

        # Mocking Invalid User Update: Deactivated User
        self.mock_put_rest_call("http://localhost:8080/users/update", params=input_update_invalid)

    def test_admin_find_users(self):
        """
        Search for multiple users in system as an admin
        """ 

        # Mocking update variables
        url = "http://localhost:8080/users/admin/find_users"
        input_register_admin = {"username": "admin", "fullname": "admin", "email": "admin@admin.admin", "password": "admin"}
        input_login_admin = {"username": "admin", "password": "admin"}
        input_register1 = {"username": "thing1", "fullname": "test1", "email": "abc1@gmail.com", "password": "12345"}
        input_login1 = {"username": "thing1", "password": "12345"}
        input_register2 = {"username": "thing2", "fullname": "test2", "email": "abc2@gmail.com", "password": "22222"}
        input_login2 = {"username": "thing2", "password": "22222"}
        output_user_admin = {"username": "admin", "fullname": "admin", "email": "admin@admin.admin"}
        output_user1  = {"username": "thing1", "full_name": "test1", "email": "abc1@gmail.com"}
        output_user2 = {"username": "thing2", "full_name": "test2", "email": "abc2@gmail.com"}
        input_valid_all = {"username": "", "session": "fake_session_id_admin"}
        input_valid_some = {"username": "thing", "session": "fake_session_id_admin"}
        input_valid_self = {"username": "admin", "session": "fake_session_id_admin"}
        input_valid_other = {"username": "thing2", "session": "fake_session_id_admin"}
        input_wrong_session_id = {"username": "thing", "session": "dubious_session_id"}
        input_non_admin_session_id = {"username": "thing1", "session": "fake_session_id"}
        input_unknown_user = {"username": "thing3", "session": "fake_session_id_admin"}
        output_list_all = [output_user_admin, output_user1, output_user2]
        output_list_some = [output_user1, output_user2]

        # Mocking output validators
        self.mock_post_rest_call.side_effect = [
             {"user": output_user_admin, "status_code": 200},                                           # Valid User Registration Admin
             {"error": "username is not unique", "status_code": 401},                                   # Invalid User Registration Admin: Duplicate Admin
             {"user": output_user_admin, "session_id": "fake_session_id_admin", "status_code": 200},    # Valid User Login Admin
             {"user": output_user1, "status_code": 200},                                                # Valid User Registration 1
             {"user": output_user1, "session_id": "fake_session_id1", "status_code": 200},              # Valid User Login 1
             {"user": output_user2, "status_code": 200},                                                # Valid User Registration 2
             {"user": output_user2, "session_id": "fake_session_id2", "status_code": 200},              # Valid User Login 2
             {"error": "Invalid Request: user is not admin", "status_code": 401},                       # Invalid Find Users Bad Session
             {"error": "Invalid Request: user is not admin", "status_code": 401},                       # Invalid Find Users Non-Admin Session
             {"users": output_list_all, "status_code": 200},                                            # Valid Find Users All
             {"users": output_list_some, "status_code": 200},                                           # Valid Find Users Some
             {"users": [output_user_admin], "status_code": 200},                                        # Valid Find Users Self
             {"users": [output_user2], "status_code": 200},                                             # Valid Find Users Other
             {"users": [], "status_code": 200}                                                          # Valid Find Users None
        ]

        # Mocking Register & Login Account Admin
        self.mock_post_rest_call("http://localhost:8080/users/admin/register", params=input_register_admin)
        self.mock_post_rest_call("http://localhost:8080/users/admin/register", params=input_register_admin)
        self.mock_post_rest_call("http://localhost:8080/users/login", params=input_login_admin)

        # Mocking Register & Login Account 1
        self.mock_post_rest_call("http://localhost:8080/users/register", params=input_register1)
        self.mock_post_rest_call("http://localhost:8080/users/login", params=input_login1)

        # Mocking Register & Login Account 2
        self.mock_post_rest_call("http://localhost:8080/users/register", params=input_register2)
        self.mock_post_rest_call("http://localhost:8080/users/login", params=input_login2)

        # Mocking Invalid Find Users: Bad Session
        self.mock_post_rest_call(url, params=input_wrong_session_id)

        # Mocking Invalid Find Users: Non-Admin Session
        self.mock_post_rest_call(url, params=input_non_admin_session_id)

        # Mocking Valid Find Users: All
        self.mock_post_rest_call(url, params=input_valid_all)

        # Mocking Valid Find Users: Some
        self.mock_post_rest_call(url, params=input_valid_some)

        # Mocking Valid Find Users: Self
        self.mock_post_rest_call(url, params=input_valid_self)

        # Mocking Valid Find Users: Other
        self.mock_post_rest_call(url, params=input_valid_other)

        # Mocking Valid Find Users: None
        self.mock_post_rest_call(url, params=input_unknown_user)

    def test_admin_update(self):
        """
        Edit a user's account information as an admin
        """ 

        # Mocking update variables
        url = "http://localhost:8080/users/admin/update"
        input_register_admin = {"username": "admin", "fullname": "admin", "email": "admin@admin.admin", "password": "admin"}
        output_user_admin = {"username": "admin", "fullname": "admin", "email": "admin@admin.admin"}
        input_login_admin = {"username": "admin", "password": "admin"}
        input_register = {"username": "aaa", "fullname": "test", "email": "abc@gmail.com", "password": "12345"}
        output_user = {"username": "aaa", "full_name": "test", "email": "abc@gmail.com"}
        input_login = {"username": "aaa", "password": "12345"}
        input_valid = {"username": "aaa", "newuser": "fullstack", "newname": "Huell Schtakh", "newemail": "schtakh@test.com", "session": "fake_session_id_admin"}
        input_wrong_session_id = {"username": "aaa", "newuser": "eventhandler", "newname": "Yvette Chandler", "newemail": "ychandler@test.com", "session": "dubious_session_id"}
        input_non_admin_session_id = {"username": "aaa", "newuser": "eventhandler", "newname": "Yvette Chandler", "newemail": "ychandler@test.com", "session": "fake_session_id"}
        input_unknown_user = {"username": "bbb", "newuser": "eventhandler", "newname": "Yvette Chandler", "newemail": "ychandler@test.com", "session": "fake_session_id_admin"}
        output_valid = {"username": "fullstack", "full_name": "Huell Schtakh", "email": "schtakh@test.com"}
        
        # Mocking output validators
        self.mock_post_rest_call.side_effect = [
             {"user": output_user_admin, "status_code": 200},                                           # Valid User Registration Admin
             {"error": "username is not unique", "status_code": 401},                                   # Invalid User Registration Admin: Duplicate Admin
             {"user": output_user_admin, "session_id": "fake_session_id_admin", "status_code": 200},    # Valid User Login Admin
             {"user": output_user, "status_code": 200},                                                 # Valid User Registration
             {"user": output_user, "session_id": "fake_session_id", "status_code": 200}                 # Valid User Login
        ]

        self.mock_put_rest_call.side_effect = [
            {"error": "Invalid Request: user is not admin or target username not found", "status_code": 401},   # Invalid Admin Update Unknown User
            {"error": "Invalid Request: user is not admin or target username not found", "status_code": 401},   # Invalid Admin Update Bad Session
            {"error": "Invalid Request: user is not admin or target username not found", "status_code": 401},   # Invalid Admin Update Non Admin Session
            {"user": output_valid, "status_code": 200}                                                          # Valid Admin Update
        ]

        # Mocking Register & Login Account Admin
        self.mock_post_rest_call("http://localhost:8080/users/admin/register", params=input_register_admin)
        self.mock_post_rest_call("http://localhost:8080/users/admin/register", params=input_register_admin)
        self.mock_post_rest_call("http://localhost:8080/users/login", params=input_login_admin)

        # Mocking Register & Login Account 1
        self.mock_post_rest_call("http://localhost:8080/users/register", params=input_register)
        self.mock_post_rest_call("http://localhost:8080/users/login", params=input_login)
        
        # Mocking Invalid Admin Update Unknown User
        self.mock_put_rest_call(url, params=input_unknown_user)

        # Mocking Invalid Admin Update Bad Session
        self.mock_put_rest_call(url, params=input_wrong_session_id)

        # Mocking Invalid Admin Update Non Admin Session
        self.mock_put_rest_call(url, params=input_non_admin_session_id)

        # Mocking Valid Admin Update
        self.mock_put_rest_call(url, params=input_valid)
        
    def test_admin_deactivate(self):
        """
        Removes user account from system as Admin
        """

        # Mocking update variables
        url = "http://localhost:8080/users/admin/deactivate"
        input_register_admin = {"username": "admin", "fullname": "admin", "email": "admin@admin.admin", "password": "admin"}
        output_user_admin = {"username": "admin", "fullname": "admin", "email": "admin@admin.admin"}
        input_login_admin = {"username": "admin", "password": "admin"}
        input_register = {"username": "aaa", "fullname": "test", "email": "abc@gmail.com", "password": "12345"}
        output_user = {"username": "aaa", "full_name": "test", "email": "abc@gmail.com"}
        input_login = {"username": "aaa", "password": "12345"}
        input_valid = {"username": "aaa", "session": "fake_session_id_admin"}
        input_non_admin_session_id = {"username": "admin", "session": "fake_session_id"}
        input_wrong_session_id = {"username": "admin", "session": "dubious_session_id"}
        input_unknown_user = {"username": "bbb", "session": "fake_session_id_admin"}
        input_update_invalid = {"newuser": "sloam", "newname": "Sandy Loam", "newemail": "sloam@test.com", "session": "fake_session_id"}
        input_deactivate_invalid = {"username": "aaa", "session": "fake_session_id"}
        
        # Mocking output validators
        self.mock_post_rest_call.side_effect = [
             {"user": output_user_admin, "status_code": 200},                                           # Valid User Registration Admin
             {"error": "username is not unique", "status_code": 401},                                   # Invalid User Registration Admin: Duplicate Admin
             {"user": output_user_admin, "session_id": "fake_session_id_admin", "status_code": 200},    # Valid User Login Admin
             {"user": output_user, "status_code": 200},                                                 # Valid User Registration
             {"user": output_user, "session_id": "fake_session_id", "status_code": 200}                 # Valid User Login
        ]
        self.mock_put_rest_call.side_effect = [
            {"error": "Invalid Request: user is not admin or failed to delete target username", "status_code": 401}, # Invalid Admin Deactivate Unknown User
            {"error": "Invalid Request: user is not admin or failed to delete target username", "status_code": 401}, # Invalid Admin Deactivate Bad Session
            {"error": "Invalid Request: user is not admin or failed to delete target username", "status_code": 401}, # Invalid Admin Deactivate Non Admin Session
            {"user": output_user, "status_code": 200},                                                               # Valid Admin Deactivate
            {"error": "Invalid Request: user is not admin or failed to delete target username", "status_code": 401}, # Invalid Admin Deactivate User Already Deactivated
            {"error": "failed to delete", "status_code": 401},                        # Invalid User Deactivate: Duplicate Deactivate
            {"error": "failed to update", "status_code": 401},                        # Invalid User Update: Deactivated User 
        ]

        # Mocking Register & Login Account Admin
        self.mock_post_rest_call("http://localhost:8080/users/admin/register", params=input_register_admin)
        self.mock_post_rest_call("http://localhost:8080/users/admin/register", params=input_register_admin)
        self.mock_post_rest_call("http://localhost:8080/users/login", params=input_login_admin)

        # Mocking Register & Login Account
        self.mock_post_rest_call("http://localhost:8080/users/register", params=input_register)
        self.mock_post_rest_call("http://localhost:8080/users/login", params=input_login)

        # Mocking Invalid User Deactivate: Invalid Admin Deactivate Unknown User
        self.mock_put_rest_call(url, params=input_unknown_user)

        # Mocking Invalid Admin Deactivate Bad Session
        self.mock_put_rest_call(url, params=input_wrong_session_id)

        # Mocking Invalid Admin Deactivate
        self.mock_put_rest_call(url, params=input_non_admin_session_id)

        # Mocking Valid Admin Deactivate
        self.mock_put_rest_call(url, params=input_valid)

        # Mocking Invalid Admin Deactivate User Already Deactivated
        self.mock_put_rest_call(url, params=input_valid)

        # Mocking Invalid User Deactivate: Deactivated User
        self.mock_put_rest_call("http://localhost:8080/users/deactivate", params=input_deactivate_invalid)

        # Mocking Invalid User Update: Deactivated User
        self.mock_put_rest_call("http://localhost:8080/users/update", params=input_update_invalid)