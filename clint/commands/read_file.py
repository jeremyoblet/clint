from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from base_command import BaseCommand
from context import GLOBAL_CONTEXT

console = Console()

class ReadFileCommand(BaseCommand):
    name = "read"
    help = "Lit et affiche le contenu d’un fichier texte."

    def run(self, args: str):
        name = args.strip()
        if not name:
            console.print(Panel("[bold red]Nom du fichier manquant[/bold red]", title="⛔ Erreur"))
            return

        path = (GLOBAL_CONTEXT.cwd / name).expanduser().resolve()

        if not path.exists():
            console.print(Panel(f"[red]Le fichier n'existe pas : {path}[/red]", title="❌ Erreur"))
            return

        if not path.is_file():
            console.print(Panel(f"[red]Ce n’est pas un fichier : {path}[/red]", title="❌ Erreur"))
            return

        try:
            content = path.read_text(encoding="utf-8")
            console.rule(f"[bold blue]{path.name}")
            console.print(content)
            console.rule()
        except Exception as e:
            console.print(Panel(f"[red]Erreur de lecture : {e}[/red]", title="❌"))
