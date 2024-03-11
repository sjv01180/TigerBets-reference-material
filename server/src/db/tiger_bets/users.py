from dataclasses import dataclass

from ..db_utils import *


def rebuild_user_tables():
    exec_sql_file("src/db/sql/user.sql")


def populate_user_table():
    exec_sql_file("data/populate_user.sql")