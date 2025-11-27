from models.participant import Participant

class PlayerRegistry:
    def __init__(self):
        self.players = []
            
    def find(self, name:str) -> Participant | None:
        return next((p for p in self.players if p.name == name), None)
    
    def get_or_create(self, name: str) -> Participant:
        player = self.find(name)

        # create player if applicable
        if player is None:
            player = Participant(name)
            self.players.append(player)
        
        return player
    
    def all(self):
        return self.players
    
    def reset_player(self, player: Participant):
        player.times_played = 0
        player.times_booked = 0
        player.sessions_booked.clear()
        player.sessions_played.clear()
        player.due_to_book = ""