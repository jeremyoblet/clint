from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from base_command import BaseCommand
import command_list

console = Console()

class HelpCommand(BaseCommand):
    name = "help"
    help = "Affiche la liste des commandes disponibles."

    def run(self, args: str):
        table = Table(
            show_header=True,
            header_style="bold blue",
            box=None,
            pad_edge=False,
            expand=False,
        )

        table.add_column("Commande", style="bold green", no_wrap=True)
        table.add_column("Description", style="dim")

        for CommandClass in command_list.COMMAND_CLASSES:
            table.add_row(CommandClass.name, CommandClass.help)

        panel = Panel(
            table,
            title="🆘 Aide - Commandes disponibles",
            border_style="green",
            expand=True  # ✅ occupe toute la largeur de la console
        )

        console.print(panel)
