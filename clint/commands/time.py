from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from base_command import BaseCommand
from context import ShellContext

console = Console()

class TimeCommand(BaseCommand):
    name = "time"
    help = "Affiche la date et l'heure actuelles."

    def run(self, args: str, context: ShellContext):
        if self.check_help(args):
            return

        now = datetime.now()
        formatted = now.strftime("[bold]Date :[/bold] %A %d %B %Y\n[bold]Heure :[/bold] %H:%M:%S")

        console.print(Panel(
            formatted,
            title="Horloge système",
            border_style="blue",
            expand=True
        ))
