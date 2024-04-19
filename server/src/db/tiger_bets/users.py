from dataclasses import dataclass
from ..db_utils import exec_get_all, exec_sql_file, exec_commit, exec_get_one
import secrets
import hashlib

def rebuild_user_tables():
    exec_sql_file("src/db/sql/user.sql")


def populate_user_table():
    exec_sql_file("data/populate_user.sql")


def recreate_user_table():
    """
    recreate user table if need
    """
    rebuild_user_tables()
    populate_user_table()

def clear_users():
    """
    clear users data
    """
    sql = "delete from users"
    exec_commit(sql)

class User:
    """
    class for user
    """
    def __init__(self, uid: str, username: str, full_name: str, email: str, is_deleted: bool = False, is_admin: bool = False):
        """
        constructor
        :param username:
        """
        if username is None or full_name is None or email is None:
            raise ValueError

        self.uid = uid
        self.username = username.strip()
        self.full_name = full_name.strip()
        self.email = email.strip()
        self.is_deleted = is_deleted
        self.is_admin = is_admin

        if len(self.username) == 0 or len(self.full_name) == 0 or len(self.email) == 0:
            raise ValueError

    def to_json(self):
        return {"username": self.username, "full_name": self.full_name, "email": self.email}
    
def _hash_string(input: str) -> str:
    """
    internal helper function to salt and hash strings. Eliminates DRY and localizes salting algorithm in one place
    :param input:
    :return str:
    """
    newpass = hashlib.sha512()
    newpass.update(b"Marco")
    newpass.update(input.encode())
    newpass.update(b"Pollo")
    return newpass.hexdigest()

def _get_user_by_session(session: str) -> User:
    """
    get user by session id
    :param session:
    :return: user
    """
    select_sql = "SELECT user_id, user_name, full_name, email, is_deleted, is_admin FROM users WHERE session_id = %s"
    res = exec_get_one(select_sql, (session,))
    if res is None:
        return res
    return User(res[0], res[1], res[2], res[3], res[4], res[5])

def _get_user_by_username(username: str) -> User:
    """
    get user by username
    :param username:
    :return: user
    """
    # Added is_deleted param to returning user object. 
    # Not sure how we want to handle deleted users, but I think we can add some sort of special label to the frontend or something
    select_sql = "SELECT user_id, user_name, full_name, email, is_deleted FROM users WHERE user_name = %s"
    res = exec_get_one(select_sql, (username,))
    if res is None:
        return res

    return User(res[0], res[1], res[2], res[3], res[4])

def _cancel_session_by_uid(uid: str) -> bool:
    """
    removes session from user by username
    :param uid:
    """

    # might be redundant and may replace matching from username to session id. Let me know in the pull request feedback
    update_sql = "UPDATE users SET session_id = NULL WHERE user_id = %s"
    exec_commit(update_sql, (uid,))
    return True

#========PUBLIC USER FUNCTIONS==========

def create_user(user: User, password: str) -> bool:
    """
    create a new account
    :param user:
    :param password
    :return: True if create success
    """
    if _get_user_by_username(user.username) is not None:
        return False
    
    hashed_pass = _hash_string(password)
    insert_sql = """
        INSERT INTO users (user_name, full_name, email, password) VALUES (%s, %s, %s, %s)
    """
    exec_commit(insert_sql, (user.username, user.full_name, user.email, hashed_pass,))
    return True

def validate_user(username: str, password: str) -> bool:
    """
    checks if username and password points to a valid account
    :param username:
    :param password:
    :return: True if username and password is valid, False otherwise
    """
    cur_user = _get_user_by_username(username)
    if cur_user is None:
        return False
    hashed_pass = _hash_string(password)
    validate_sql = "SELECT user_name FROM users WHERE user_id = %s AND password = %s"
    user_status = exec_get_one(validate_sql, (cur_user.uid, hashed_pass,))
    if user_status is None:
        return False
    return True

def invalidate_user(session: str) -> bool:
    """
    destroy auth session of user for logging off
    :param username:
    :param session:
    :return: True if session destroyed successfully, false otherwise
    """
    cur_user = _get_user_by_session(session)
    if cur_user is None:
        return False
    return _cancel_session_by_uid(cur_user.uid)

def get_user(username: str, session: str) -> User | None:
    """
    Finds user by username. Public rendition of _get_user_by_username
    :param username:
    :param session:
    :return: user
    """
    cur_user = _get_user_by_session(session)
    if cur_user is None:
        return None
    return _get_user_by_username(username)

def update_user_session_id(username: str) -> str:
    """
    update user session_id
    """
    session_id = secrets.token_hex(128)
    update_sql = "UPDATE users SET session_id = %s WHERE user_name = %s"
    exec_commit(update_sql, (session_id, username))
    return session_id

def update_user(new_user_name: str, new_full_name: str, new_email: str, session: str) -> bool:
    """
    update public information about a user. Here, the user makes changes to their own account
    :param new_user_name:
    :param new_full_name:
    :param new_email:
    :param session:
    :return: True if update ran successfully, False otherwise
    """
    cur_user = _get_user_by_session(session)
    if (cur_user is None or cur_user.is_deleted):
        return False
    update_user = "UPDATE users SET user_name = %s, full_name = %s, email = %s WHERE user_id = %s"
    exec_commit(update_user, (new_user_name, new_full_name, new_email, cur_user.uid,))
    return True

def delete_user(session: str) -> bool:
    """
    deletes user from system. Here, the user chooses to delete their own account
    :param session:
    :return: True if successfully deleted user, False otherwise
    """
    cur_user = _get_user_by_session(session)
    if (cur_user is None or cur_user.is_deleted is True):
        return False
    update_delete_sql = "UPDATE users SET is_deleted = true WHERE session_id = %s"
    exec_commit(update_delete_sql, (session,))
    return True

#========ADMIN-ONLY USER FUNCTIONS==========

def create_user_admin(user: User, password: str) -> bool:
    """
    create a new admin account. Ideally, we'd want to create these accounts internally.
    For the sake of api testing, this function will be present
    :param user:
    :param password
    :return: True if create success
    """
    if _get_user_by_username(user.username) is not None:
        return False
    
    hashed_pass = _hash_string(password)
    insert_sql = """
        INSERT INTO users (user_name, full_name, email, password, is_admin) VALUES (%s, %s, %s, %s, true)
    """
    exec_commit(insert_sql, (user.username, user.full_name, user.email, hashed_pass,))
    return True

def get_users_by_query(query: str, session: str) -> list[User] | None:
    """
    grabs a list of users based on a query. If no search query was specified, grab all users in the system
    must be an admin in order to invoke this function 
    :param query:
    :param session:
    return a list of user objects matching the query.
    """
    cur_user = _get_user_by_session(session)
    if (cur_user is None or cur_user.is_deleted or not cur_user.is_admin):
        return None
    select_users_match = "SELECT user_name, full_name, email, is_deleted FROM users WHERE user_name LIKE %s"
    result = exec_get_all(select_users_match, (query + '%',))
    user_group = []
    for usr in result:
        user_group.append(User("uid", usr[0], usr[1], usr[2], usr[3]).to_json())
    return user_group

def update_user_admin(selected_user: str, new_user_name: str, new_full_name: str, new_email: str, session: str) -> bool:
    """
    updates public information about a user. Here, the admin can change full_name and email of any user.
    must be an admin in order to invoke this function 
    :param selected_user:
    :param new_user_name:
    :param new_full_name:
    :param new_email:
    :param session:
    :return: True if successfully updated user, False otherwise
    """
    cur_admin = _get_user_by_session(session)
    if (cur_admin is None or cur_admin.is_deleted or not cur_admin.is_admin):
        return False
    target_user = _get_user_by_username(selected_user)
    update_sql = "UPDATE users SET user_name = %s, full_name = %s, email = %s WHERE user_id = %s"
    exec_commit(update_sql, (new_user_name, new_full_name, new_email, target_user.uid,))
    return True

def delete_user_admin(username: str, session: str) -> bool:
    """
    deletes user from system. Here, the admin can delete any user.
    must be an admin in order to invoke this function 
    :param session:
    :return: True if successfully deleted user, False otherwise
    """
    cur_user = _get_user_by_session(session)
    if (cur_user is None or cur_user.is_deleted or not cur_user.is_admin):
        return False
    target_user = _get_user_by_username(username)
    update_delete_sql = "UPDATE users SET is_deleted = true WHERE user_id = %s"
    exec_commit(update_delete_sql, (target_user.uid,))
    return True
    

#===========================================
recreate_user_table()
