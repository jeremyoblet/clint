from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from base_command import BaseCommand

console = Console()

class MakeFileCommand(BaseCommand):
    name = "make -file"
    help = "Crée un fichier vide."

    def run(self, args: str):
        name = args.strip()
        if not name:
            console.print(Panel("[bold red]Nom manquant[/bold red]", title="⛔ Erreur"))
            return
        path = Path(name)
        if path.exists():
            console.print(Panel(f"[yellow]⚠ Existe déjà : {path}[/yellow]", title="⚠ Attention"))
        else:
            try:
                path.touch()
                console.print(Panel(f"[green]✓ Créé : {path.resolve()}[/green]", title="📄 Fichier"))
            except Exception as e:
                console.print(Panel(f"[red]Erreur : {e}[/red]", title="❌"))