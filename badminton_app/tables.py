from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.columns import Columns
from rich import box


def print_log(session_manager) -> Table:
    sessions = session_manager.sessions_chronological
    table = Table(box=box.ROUNDED)

    table.add_column("Date", no_wrap=True)
    table.add_column("Booked")
    table.add_column("Played")

    for s in sessions:
        who_booked = ", ".join(sorted(player.name for player in s.who_booked))
        who_played = ", ".join(sorted(player.name for player in s.who_played))

        table.add_row(s.date, who_booked, who_played)
    
    #console = Console()
    #console.print(table)
    return table


def print_processed(player_registry) -> Table:
    table = Table(box=box.ROUNDED)
    table.add_column("Name", no_wrap=True)
    table.add_column("Sessions played", justify="right", width=15)
    table.add_column("Sessions booked", justify="right", width=15)
    table.add_column("Sessions since last booking", justify="right", width=15)
    table.add_column("Bookings per session", justify="right", width=15)
    table.add_column("Due to book?")

    rows = []
    for player in sorted(
        player_registry.all(), 
        key=lambda p: (-1* p.sessions_since_last_booking, p.bookings_per_session, p.most_recent_booking)
    ):
        rows.append([
            player.name,
            str(player.times_played),
            str(player.times_booked),
            str(player.sessions_since_last_booking),
            str(round(player.bookings_per_session, 2)),
            player.due_to_book
        ])

    for row in rows:
        table.add_row(row[0], row[1], row[2], row[3], row[4], row[5])

    #console = Console()
    #console.print(table)
    return table

def print_both(session_manager, player_registry):
    log_sheet   = print_log(session_manager)
    stats       = print_processed(player_registry)

    panel = Panel.fit(
        Columns([log_sheet, stats]),
        box=box.MINIMAL,
        border_style="none"
        )

    console = Console()
    console.print(panel)
    



def print_log_numbered(session_manager) -> None:
    n = 1

    for s in session_manager.sessions_chronological:
        who_booked = ", ".join(sorted(player.name for player in s.who_booked))
        who_played = ", ".join(sorted(player.name for player in s.who_played))

        print(f"{n}{".":2}{s.date:8}|{who_booked:15}|{who_played}")
        n += 1

    