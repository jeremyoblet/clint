from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from base_command import BaseCommand
import command_list as command_list

console = Console()

class HelpCommand(BaseCommand):
    name = "help"
    help = "Affiche la liste des commandes disponibles."

    def run(self, args: str):
        table = Table(title="🆘 Aide - Commandes disponibles", show_lines=False)
        table.add_column("Commande", style="bold green")
        table.add_column("Description", style="dim")

        for CommandClass in command_list.COMMAND_CLASSES:
            table.add_row(CommandClass.name, CommandClass.help)

        console.print(table)

# À ajouter dans command_list.py
