import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_finds_player(self):
        player = self.stats.search("Gretzky")
        self.assertEqual(player.name, "Gretzky")

    def test_search_doensnt_find_player(self):
        player = self.stats.search("Selänne")
        self.assertIsNone(player)

    def test_team_has_players(self):
        team = self.stats.team("EDM")
        self.assertEqual(len(team), 3)

    def test_team_doesnt_have_players(self):
        team = self.stats.team("PHI")
        self.assertEqual(len(team), 0)

    def test_players_in_order(self):
        players = self.stats.top(3)
        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Lemieux", "Yzerman"]
        )

    def test_all_players_returned(self):
        players = self.stats.top(5)
        self.assertEqual(len(players), 5)

    def test_no_players_returned(self):
        players = self.stats.top(0)
        self.assertEqual(players, [])