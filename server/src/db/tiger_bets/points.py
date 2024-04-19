from ..db_utils import exec_get_all, exec_sql_file, exec_commit, exec_get_one
import random
from dataclasses import dataclass

@dataclass
class Point:
    points_id: str
    user_id: str
    points: int
    
def rebuild_bet_tables():
    exec_sql_file("src/db/sql/points.sql")
    exec_sql_file("data/populate_points.sql")


def update_points(user_id, new_points):
    """
    Update points for a user.
    """
    update_points_sql = """
        UPDATE points
        SET points = points + %s
        WHERE user_id = %s
        RETURNING id;
    """
    exec_commit(update_points_sql, (new_points, user_id))
    return {"message": "Success"}

def get_points_for_user(user_id):
    """
    Get points for a user.
    """
    get_points_sql = """
        SELECT points
        FROM points
        WHERE user_id = %s;
    """
    points = exec_get_one(get_points_sql, (user_id,))
    if not points:
        return {"error": "User not found."}
    return {"points": points}

def get_users_with_top_points():
    """
    Top 10 users by points.
    """
    get_top_users_sql = """
        SELECT user_id, points
        FROM points
        ORDER BY points DESC
        LIMIT 10;
    """
    top_users = exec_get_all(get_top_users_sql)
    return [{"user_id": user[0], "points": user[1]} for user in top_users]
