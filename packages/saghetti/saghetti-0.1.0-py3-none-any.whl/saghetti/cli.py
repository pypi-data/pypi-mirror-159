import rich
import typer
from rich.panel import Panel

SAGHETTI = """
            ░░░░
              ░░░░
            ░░░░
                  ░░░░
      ░░░░          ░░░░
        ░░░░      ░░░░
      ░░░░

          ▓▓████▓▓▓▓████
        ██▓▓▓▓▓▓████▓▓▓▓▓▓
    ░░██▓▓░░██▓▓██▓▓▓▓██████
▒▒░░░░░░░░██░░░░░░▓▓▓▓░░░░░░░░▒▒
  ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░
"""


def main():
    rich.print(
        Panel(
            (
                f"{SAGHETTI}\n\n"
                "[green]Eat the saghetti to forgetti the regretti![/]\n\n"
                "Become a [bold]EuroPython[/] volunteer!\n\n"
                "Email us at volunteers@europython.eu"
            ),
            border_style="blue",
        )
    )


if __name__ == "__main__":
    typer.run(main)
