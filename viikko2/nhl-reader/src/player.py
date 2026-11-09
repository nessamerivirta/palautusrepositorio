class Player: # pylint: disable=too-few-public-methods
    def __init__(self, data):
        self.name = data['name']
        self.nationality = data['nationality']
        self.assists = data['assists']
        self.goals = data['goals']
        self.team = data['team']
        self.games = data['games']
        self.points = self.assists + self.goals

    def __str__(self):
        return f"{self.name:20} {self.team:15} {self.goals} + {self.assists} = {self.points}"
