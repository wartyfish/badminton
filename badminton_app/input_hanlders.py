import datetime
import tables

def input_new_session(registry, session_manager):
    while True:
        while True:
            date = input("Date (dd/mm/yy): ")
            try:
                datetime.datetime.strptime(date, "%d/%m/%y")
                break
            except:
                print("Date must be dd/mm/yy")
        
        played = input("Who played (comma seperated):\n").split(", ")
        booked_raw = input("Who booked (optional, comma seperated):\n").strip()
        booked = booked_raw.split(", ") if booked_raw else []

        cmd = input("Commit? [y/n] ").lower()
        if cmd == "y":
            new_session = session_manager.new_session(date, played, booked)
            session_manager.update_player_stats(new_session)
        
            tables.print_log(session_manager)
            tables.print_processed(registry)

            break

def modify_session(registry, session_manager):
    date = input("Enter date or 1 for most recent session: ")
    if date == "1":
        session = session_manager.sessions_sorted[0]
    else:
        for s in session_manager.sessions:
            if date == s.date:
                session = s
    
def delete_session(session_manager):   
    date = input("Enter date or 1 for most recent session: ")
    if date == "1":
        session = session_manager.sessions_sorted[0]
    else:
        for s in session_manager.sessions:
            if date == s.date:
                session = s

    confirmation = input(f"Delete\n{session}?\n(y/n) ").lower()
    if confirmation == "y":
        session_manager.delete_session(session)
        print("Session deleted")
    