from rich.console import Console
from rich.panel import Panel
from base_command import BaseCommand
from context import GLOBAL_CONTEXT

console = Console()

class HereCommand(BaseCommand):
    name = "here"
    help = "Affiche le répertoire courant (équivalent de 'pwd')."

    def run(self, args: str):
        self.check_help(args)

        current_path = GLOBAL_CONTEXT.cwd.resolve()
        console.print(Panel(str(current_path), title="📍 Répertoire actuel", border_style="blue"))
