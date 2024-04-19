from dataclasses import dataclass
from ..db_utils import exec_get_all, exec_sql_file, exec_commit, exec_get_one

@dataclass
class Bet:
    bet_id: str
    user_id: str
    event_id: str
    team_id: str
    points: int


def rebuild_bet_tables():
    exec_sql_file("src/db/sql/bet.sql")


def list_user_bets():
    """
    This method returns list of all bets placed in the system
    """
    list_bets_sql = """
        SELECT *
        FROM bet
    """
    res = exec_get_all(list_bets_sql)
    return res if res else []


def create_bet(
    user_id, event_id, team_id, points
):
    """
    Create a bet and specify the details of the item.
    """
    check_existing_item_sql = """
            SELECT user_id FROM bet
            WHERE event_id = %s;
        """
    existing_item = exec_get_one(check_existing_item_sql, (event_id,))
    if existing_item:
        return [{"error": "Bet already exists."}]
    create_bet_sql = """
            INSERT INTO bet
            (user_id, event_id, team_id, points)
            VALUES
            (%s,%s, %s, %s)
            RETURNING bet_id;
        """
    exec_commit(
        create_bet_sql,
        (user_id, event_id, team_id, points),
    )

    return {"message": "Bet created."}


def get_bet_details(bet_id):
    """
    Get details of a bet.
    :param bet_id: identifier of bet
    :return: details of the bet
    """
    select_bet_sql = """
        SELECT *
        FROM bet
        WHERE bet_id = %s;
    """
    res = exec_get_one(select_bet_sql % ("'" + bet_id + "'"))
    return res if res else []


def edit_bet(bet_id, item_dict):
    """
    Edit details from an item
    bet_id :
        id to edit
    item_dict :
        dict with keys to edit with values
    """
    existing_item = get_bet_details(bet_id)
    if existing_item is None:
        return [{"error": "Item does not exist."}]

    update_bet_sql = """
        UPDATE bet SET
        team_id = %s,
        points = %s,
        event_id = %s
        WHERE bet_id = %s
    """
    try:
        exec_commit(
            update_bet_sql,
            (
                item_dict.get("team_id"),
                item_dict.get("points"),
                item_dict.get("event_id"),
                bet_id
            ),
        )
    except Exception as err:
        print("Error updating bet: ", err)
        return {500: err}
    return "Success"


def delete_bet(bet_id):
    """
    This method deletes a bet using bet id.
    """
    check_existing_item_sql = """
        SELECT bet_id FROM bet
        WHERE bet_id = %s;
    """
    existing_item = exec_get_one(check_existing_item_sql, (bet_id,))
    if not existing_item:
        return [{"error": "bet_id does not exists."}]
    delete_menu_sql = """
        DELETE FROM bet
        WHERE
        bet_id = %s;
    """
    exec_commit(delete_menu_sql % ("'" + bet_id + "'"))
    return {"message": "Bet deleted."}
