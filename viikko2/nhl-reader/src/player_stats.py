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
