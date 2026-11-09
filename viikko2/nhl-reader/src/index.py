from rich.prompt import Prompt
from rich.table import Table
from rich.console import Console

from player_reader import PlayerReader
from player_stats import PlayerStats


def main():
    console = Console()

    season = Prompt.ask(
        "Season",
        choices = ["2022-23", "2023-24", "2024-25", "2025-26"],
        default = "2024-25"
    )

    nationality = Prompt.ask(
        "Nationality",
        choices = ["FIN", "SWE", "USA", "CAN"],
        default = "FIN"
    )

    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nationality)

    table = Table(title=f"Season {season} players from {nationality}")
    
    table.add_column("Player", style="light_coral", header_style="bold white")
    table.add_column("Team", style="plum2", header_style="bold white")
    table.add_column("Assists", style="dark_slate_gray3", header_style="bold white", justify="right")
    table.add_column("Goals", style="dark_slate_gray3", header_style="bold white", justify="right")
    table.add_column("Points", style="dark_slate_gray3", header_style="bold white", justify="right")

    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.points)
        )

    console.print(table)

if __name__ == "__main__":
    main()
