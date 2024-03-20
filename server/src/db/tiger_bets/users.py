from dataclasses import dataclass

from ..db_utils import *

import secrets

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


class User:
    """
    class for user
    """
    def __init__(self, username: str, full_name: str, email: str, is_deleted: bool = False):
        """
        constructor
        :param username:
        :param is_admin:
        """
        if username is None or full_name is None or email is None:
            raise ValueError

        self.username = username.strip()
        self.full_name = full_name.strip()
        self.email = email.strip()
        self.is_deleted = is_deleted

        if len(self.username) == 0 or len(self.full_name) == 0 or len(self.email) == 0:
            raise ValueError

    def to_json(self):
        return {"username": self.username, "full_name": self.full_name, "email": self.email}


def get_user_by_username(username: str) -> User:
    """
    get user by username
    :param username:
    :return: user
    """
    select_sql = "SELECT * FROM users WHERE user_name = %s"
    res = exec_get_one(select_sql, (username,))
    if res is None:
        return res

    return User(res[0], res[1], res[2], res[3])


def clear_users():
    """
    clear users data
    """
    sql = "delete from users"
    exec_commit(sql)


def create_user(user: User) -> bool:
    """
    create a new account
    :param user:
    :return: True if create success
    """
    if get_user_by_username(user.username) is not None:
        return False

    insert_sql = """
        insert into users (user_name, full_name, email, is_deleted) VALUES (%s, %s, %s, %s)
    """
    exec_commit(insert_sql, (user.username, user.full_name, user.email, user.is_deleted))

    return True


def update_user_session_id(user: User) -> str:
    """
    update user session_id
    """
    session_id = secrets.token_hex(16)
    update_sql = "update users set session_id = %s where user_name = %s"
    exec_commit(update_sql, (session_id, user.username))
    return session_id


recreate_user_table()
