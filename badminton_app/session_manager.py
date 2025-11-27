from models.session import Session
from prompt_toolkit.shortcuts import radiolist_dialog

class SessionManager:
    def __init__(self, registry):
        self.registry = registry
        self.sessions: list[Session] = []
    
    @property
    def sessions_sorted(self):
        if len(self.sessions) > 0:
            return sorted(self.sessions, key=lambda s: s.date_datetime, reverse=True)
        else:
            return self.sessions

    @property
    def is_most_recent_session_booked(self):
        if len(self.sessions_sorted[0].who_booked) == 0:
            return False
        else:
            return True

    def new_session(self, date: str, who_played: list, who_booked: list = None):
        if who_booked == None:
            who_booked = []
        
        played = [self.registry.get_or_create(name) for name in who_played]
        booked = [self.registry.get_or_create(name) for name in who_booked]

        session = Session(date, played, booked)
        self.sessions.append(session)

        return session

    def update_player_stats(self, registry, session: Session):
        if len(session.who_booked) == 0:
            to_book = [
                player for player in sorted(
                    session.who_played,
                    key = lambda p: (-1 * p.sessions_since_last_booking, p.bookings_per_session)
                )
            ][:2]

            for player in to_book:
                player.due_to_book = "yes"
            return 
        
        # update stats if players have booked
        else:  
            for player in registry.players:
                player.due_to_book = ""
            for player in session.who_played:
                player.times_played += 1
                player.sessions_played.append(session.date_datetime)
            
            for player in session.who_booked:
                player.times_booked += 1
                player.sessions_booked.append(session.date_datetime)
                # workaround to ensure sessions since last booking calculated correctly
                # even when player booked but didn't play
                if player not in session.who_played:
                    player.sessions_played.append(session.date_datetime)

    def update_all_player_stats(self, registry):
        reversed = self.sessions_sorted
        reversed.reverse()
        for session in reversed:
            self.update_player_stats(registry, session)

    def reset_all_player_stats(self, registry):
        for player in registry.players:
            registry.reset_player(player)


    def delete_session(self, session: Session):
        for player in session.who_played:
            player.times_played -= 1
            try:
                player.sessions_played.remove(session.date_datetime)
            except:
                pass
            
        for player in session.who_booked:
            player.times_booked -= 1
            try:
                player.sessions_booked.remove(session.date_datetime)
            except:
                pass

        self.sessions.remove(session)

    