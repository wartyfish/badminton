import sheets
import tables
from session_manager import SessionManager
from players import PlayerRegistry
import input_hanlders
import shelve
from pathlib import Path
import os

def main():
    p_shelf = Path("credentials_path.db")
    if not p_shelf.exists():
        credentials_path = input("Input location of credentials:\n").strip('"')
        p_credentials = Path(credentials_path)

        if not p_credentials.exists():
            raise ValueError(f"Path does not exist: {p_credentials}")

        with shelve.open("credentials_path.db") as db:
            db["path"] = str(p_credentials)
    else:
        with shelve.open("credentials_path.db") as db:
            credentials_path = Path(db["path"])

    print("Fetching data from Google Sheets... ")

    registry = PlayerRegistry()
    session_manager = SessionManager(registry)

    log, processed = sheets.load_sheets(credentials_path)
    sheets.read_sessions_from_sheets(log, session_manager)
    print("Success\n")

    session_manager.update_all_player_stats(registry)

    tables.print_log(session_manager)
    tables.print_processed(registry)

    while True:
        cmd = input ("0=exit, 1=update sheets, 2=add new session, 3=modify session, 4=delete session\n")
        if cmd == "0":
            break
        if cmd == "1":
            sheets.update_log_sheet(log, session_manager)
            sheets.update_processed_sheet(processed, registry)
        if cmd == "2":
            input_hanlders.input_new_session(registry, session_manager)
        if cmd == "3":
            input_hanlders.modify_session(registry, session_manager)
        if cmd == "4":
            input_hanlders.delete_session(session_manager)
            tables.print_log(session_manager)
            tables.print_processed(registry)
    

if __name__ == "__main__":
    
    main()