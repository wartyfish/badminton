import datetime
import tables
from datetime import datetime, timedelta
import os

import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def input_new_session(registry, session_manager):
    while True:
        while True:
            date = input("Input date: (dd/mm/yy), or press 1 for next Wed: ")
            if date == "1":
                today = datetime.today()
                days_ahead = (2 - today.weekday() + 7) % 7
                days_ahead = 7 if days_ahead == 0 else days_ahead
                date = today + timedelta(days=days_ahead) 
                date = datetime.strftime(date, "%d/%m/%y")
                print(f"Date = {date}")
                break
            else:
                try:
                    datetime.strptime(date, "%d/%m/%y")
                    break
                except:
                    print("Date must be dd/mm/yy")
        
        played = input("Who played (comma seperated):\n").split(", ")
        booked_raw = input("Who booked (optional, comma seperated):\n").strip()
        booked = booked_raw.split(", ") if booked_raw else []

        cmd = input("0=exit, 1=commit, 2=reject ")
        if cmd == "0":
            new_session = session_manager.new_session(date, played, booked)
            session_manager.update_player_stats(registry, new_session)
        
            tables.print_log(session_manager)
            tables.print_processed(registry)

            break
        if cmd == "1":
            break

def session_selector(session_manager):
    numbered_sessions = dict(zip(range(1, len(session_manager.sessions_chronological)+1), session_manager.sessions_chronological))

    print("Select session to modify:")
    tables.print_log_numbered(session_manager)
    print("0=exit")

    # validate input
    while True:
        select = input()
        try:
            select = int(select)
            if select == 0:
                return None
            
            if select in numbered_sessions:
                selected_session = numbered_sessions[select]
                break
            else:
                print("Session not found")
        except ValueError:
            print("Input integer")
    
    return selected_session

def modify_session(registry, session_manager):
    selected = session_selector(session_manager)
    
    if selected == None:
        return None

    print()
    print(selected)
    print()
    while True:
        print("Enter fields to change their value. Enter or delete players by entering their name.")

        date = input("Date (dd/mm/yy): ").strip()
        if date == "0":
            break
        booked = input("Who booked: ").strip().split(", ")
        if booked == "0":
            break
        played = input("Who played: ").strip().split(", ")
        if played == "0":
            break

        selected_who_played = [p.name for p in selected.who_played]
        selected_who_booked = [p.name for p in selected.who_booked]

        print()
        print("Changes: ")

        if date != "":
            try:
                datetime.strptime(date, "%d/%m/%y")
                print(f"{selected.date} → {date}")
            except Exception as e:
                print(f"Exception: {e}")
                print("Date must be dd/mm/yy")
        else:
            date = selected.date

        if len(booked) > 0:
            added_b   = [p for p in booked if p not in selected_who_booked]
            if len(added_b) > 0:
                if added_b[0] == "":       # does this block actually do anything?
                    added_b.clear()
            removed_b = [p for p in booked if p in selected_who_booked]

            if len(added_b) > 0:
                print(f"Who booked: + {", ".join(p for p in added_b)}")
            if len(removed_b) > 0:
                print(f"Who booked: - {", ".join(p for p in removed_b)}")
        
        if len(played) > 0:
            added_p =   [p for p in played if p not in selected_who_played]
            if len(added_p) > 0:
                if added_p[0] == "":
                    added_p.clear()

            removed_p = [p for p in played if p in selected_who_played]

            if len(added_p) > 0:
                print(f"Who played: + {", ".join(p for p in added_p)}")
            if len(removed_p) > 0:
                print(f"Who played: - {", ".join(p for p in removed_p)}")        

        cmd = input("0=exit, 1=commit, 2=reject ")

        if cmd == "0":
            break
        if cmd == "1":
            new_booked = [p.name for p in selected.who_booked] + added_b
            for p in removed_b:
                if p in new_booked:
                    new_booked.remove(p)
                    print(p, "removed")

            new_played = [p.name for p in selected.who_played] + added_p
            for p in removed_p:
                if p in new_played:
                    new_played.remove(p)
                    print(p,"removed")

            session_manager.delete_session(selected)

            new_session = session_manager.new_session(date, new_played, new_booked)

            session_manager.reset_all_player_stats(registry)
            session_manager.update_all_player_stats(registry)

            tables.print_log(session_manager)
            print()
            tables.print_processed(registry)

            break

    
def delete_session(session_manager): 
    selected = session_selector(session_manager)  
        
    confirmation = input(f"0=confirm, 1=reject\n{selected}")
    print()
    if confirmation == "0":
        session_manager.delete_session(selected)
        print("Session deleted.")

    
def print_log(session_manager, chunk_increment=10):
    chunk_size = chunk_increment
    unprinted_sessions = tables.print_log(session_manager)
    
    while unprinted_sessions > 0:
        next_chunk = min(unprinted_sessions)
        cmd = input(f"Print {next_chunk} more rows? (y/n) ").strip().lower()
        if cmd == "y":
            chunk_size += next_chunk
            clear()
            unprinted_sessions = tables.print_log(session_manager)
        else:
            clear()
            tables.print_log(session_manager)
            break
