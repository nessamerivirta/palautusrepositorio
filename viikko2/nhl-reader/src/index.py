from rich.prompt import Prompt
from rich.table import Table
from rich.console import Console

from player_reader import PlayerReader
from player_stats import PlayerStats


def kysy_valinnat():
    season = Prompt.ask(
        "Season",
        choices=["2022-23", "2023-24", "2024-25", "2025-26"],
        default="2024-25"
    )

    nationality = Prompt.ask(
        "Nationality",
        choices=["FIN", "SWE", "USA", "CAN"],
        default="FIN"
    )

    return season, nationality


def luo_taulukko(season, nationality):
    table = Table(title=f"Season {season} players from {nationality}")

    table.add_column("Player", style="light_coral", header_style="bold white")
    table.add_column("Team", style="plum2", header_style="bold white")
    table.add_column("Assists", style="dark_slate_gray3",
                     header_style="bold white", justify="right")
    table.add_column("Goals", style="dark_slate_gray3",
                     header_style="bold white", justify="right")
    table.add_column("Points", style="dark_slate_gray3",
                     header_style="bold white", justify="right")

    return table


def lisaa_pelaajat(table, players):
    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.points)
        )


def main():
    console = Console()
    season, nationality = kysy_valinnat()

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nationality)

    table = luo_taulukko(season, nationality)
    lisaa_pelaajat(table, players)

    console.print(table)


if __name__ == "__main__":
    main()
