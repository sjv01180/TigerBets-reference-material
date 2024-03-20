from ..db_utils import *
import random
from dataclasses import dataclass

@dataclass
class Event:
    event_id: str
    event_name: str
    team_a_id: str
    team_b_id: str
    event_result: str = None

def rebuild_event_tables():
    exec_sql_file("src/db/sql/events.sql")

def create_event(event_name, team_a_id, team_b_id):
    """
    Create an event and specify the details
    """
    check_existing_event_sql = """
        SELECT event_id FROM events
        WHERE 
        event_name = %s AND team_a_id = %s AND team_b_id = %s;
    """
    existing_event = exec_get_one(check_existing_event_sql, (event_name, team_a_id, team_b_id))
    
    if existing_event:
        return {"error": "Event already exists."}

    create_event_sql = """
        INSERT INTO events (event_name, team_a_id, team_b_id)
        VALUES (%s, %s, %s) 
        RETURNING event_id;
    """
    
    exec_commit(create_event_sql, (event_name, team_a_id, team_b_id))
    return {"message": "Event created."}



def edit_event(event_id, event_data):
    """
    Edit details of an event.
    """
    event_name = event_data.get("event_name")
    team_a_id = event_data.get("team_a_id")
    team_b_id = event_data.get("team_b_id")

    edit_event_sql = """
        UPDATE events SET 
        event_name = %s, 
        team_a_id = %s, 
        team_b_id = %s
        WHERE event_id = %s;
    """
    try:
        exec_commit(edit_event_sql, (event_name, team_a_id, team_b_id, event_id))
    except Exception as err:
        print("Error updating event: ", err)
        return {500: err}
    
    return "Success"


def list_events():
    """
    Edit all events
    """
    list_events_sql = "SELECT * FROM events;"
    events = exec_get_all(list_events_sql)
    return events

def get_event_details(event_id):
    """
    Get all details of an event based on id
    """
    get_event_sql = "SELECT * FROM events WHERE event_id = %s;"
    event_details = exec_get_one(get_event_sql, (event_id,))
    return event_details

def delete_event(event_id):
    """
    Delete event by id
    """
    delete_event_sql = "DELETE FROM events WHERE event_id = %s;"
    exec_commit(delete_event_sql % ("'" + event_id + "'"))
    return {"message": "Event deleted."}

def assign_random_event_results():
    """
    Assigns a result to each event in the database.
    """
    events = list_events()
    for event in events:
        event_id = event[0] 
        result = random.choice(['first', 'second'])
        update_event_result_sql = """
            UPDATE events
            SET event_result = %s
            WHERE event_id = %s;
        """
        exec_commit(update_event_result_sql, (result, event_id))

def list_events_with_team_names():
    """
    Retrieves a list of event details and names.
    """
    list_events_sql = """
        SELECT e.event_name, t1.team_name as team_a_name, t2.team_name as team_b_name, e.event_result
        FROM events e
        JOIN team t1 ON e.team_a_id = t1.team_id
        JOIN team t2 ON e.team_b_id = t2.team_id;
    """
    return exec_get_all(list_events_sql)
