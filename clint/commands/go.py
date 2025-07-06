from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from base_command import BaseCommand
from context import GLOBAL_CONTEXT

console = Console()

class GoCommand(BaseCommand):
    name = "go"
    help = "Change le répertoire de travail (comme 'cd')."

    def run(self, args: str):
        self.check_help(args)
        path_str = args.strip() or "~"
        target_path = Path(path_str).expanduser().resolve()

        if not target_path.exists():
            console.print(Panel(
                f"[red]Le chemin n'existe pas : {target_path}[/red]",
                title="❌ Erreur",
                border_style="red"
            ))
            return

        if not target_path.is_dir():
            console.print(Panel(
                f"[red]Ce n’est pas un dossier : {target_path}[/red]",
                title="❌ Erreur",
                border_style="red"
            ))
            return

        GLOBAL_CONTEXT.cwd = target_path
        console.print(Panel(
            f"[green]Répertoire changé vers :[/green] {target_path}",
            title="📍 Nouveau dossier",
            border_style="cyan"
        ))

