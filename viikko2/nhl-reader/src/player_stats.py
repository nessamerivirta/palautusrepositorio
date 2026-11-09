class PlayerStats: # pylint: disable=too-few-public-methods
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()
        finnish_players = []
        for player in players:
            if player.nationality == nationality:
                finnish_players.append(player)

        sorted_players = sorted(finnish_players, key = lambda player: player.points, reverse= True)

        return sorted_players
    
        def top_goal_scorers(self, how_many):
    """Palauttaa how_many eniten maaleja tehnyttä pelaajaa maalimäärän mukaan laskevassa järjestyksessä"""
            players = self.reader.get_players()
            sorted_players = sorted(players, key=lambda player: player.goals, reverse=True)
            return sorted_players[:how_many]