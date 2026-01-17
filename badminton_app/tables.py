def print_log(session_manager, chunk_size: int = 10) -> int:
    sessions = session_manager.sessions_chronological
    total_sessions = len(sessions)
    lines_to_print = chunk_size
    unprinted_sessions = total_sessions - chunk_size

    def print_table(sessions,  number_of_lines):
        print(f"Date{" "*4}|Booked{" "*9}|Played")
            
        sessions

        starting_index = len(sessions) - number_of_lines 
        ending_index = starting_index + number_of_lines

        if starting_index < 0:
            starting_index = 0
            ending_index = len(sessions) - 1

        for s in sessions[starting_index: ending_index]:
            who_booked = ", ".join(sorted(player.name for player in s.who_booked))
            who_played = ", ".join(sorted(player.name for player in s.who_played))

            print(f"{s.date:8}|{who_booked:15}|{who_played}")

    print_table(sessions, lines_to_print)
    return unprinted_sessions



def print_processed(player_registry) -> None:
    rows = []

    for player in sorted(
        player_registry.all(), 
        key=lambda p: (-1* p.sessions_since_last_booking, p.bookings_per_session, p.most_recent_booking)
    ):
        rows.append([
            player.name,
            player.times_played,
            player.times_booked,
            player.sessions_since_last_booking,
            round(player.bookings_per_session, 2),
            player.due_to_book
        ])

    print(f"{" "*10}|{"Sessions".center(15)}|{"Sessions".center(15)}|{"Sessions since".center(15)}|{"Bookings per".center(15)}|{"Due to".center(10)}")
    print(f"{"Name".center(10)}|{"played".center(15)}|{"booked ".center(15)}|{"last booking".center(15)}|{"session".center(15)}|{"book?".center(10)}")

    for row in rows:
        print(f"{row[0]:9} |",end="")
        print(f"{row[1]:14} |",end="")
        print(f"{row[2]:14} |",end="")
        print(f"{row[3]:14} |",end="")
        print(f"{row[4]:14} |",end="")
        print(f"{row[5]:>9}")        

    print()

def print_log_numbered(session_manager) -> None:
    n = 1

    for s in session_manager.sessions_chronological:
        who_booked = ", ".join(sorted(player.name for player in s.who_booked))
        who_played = ", ".join(sorted(player.name for player in s.who_played))

        print(f"{n}{".":2}{s.date:8}|{who_booked:15}|{who_played}")
        n += 1

    