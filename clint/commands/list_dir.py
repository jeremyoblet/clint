from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from base_command import BaseCommand

console = Console()

class ListDirCommand(BaseCommand):
    name = "list"
    help = "Liste les fichiers et dossiers d’un répertoire."

    def run(self, args: str):
        target = Path(args.strip()) if args.strip() else Path.cwd()

        if not target.exists():
            console.print(Panel(f"[red]Le chemin n'existe pas : {target}[/red]", title="❌ Erreur"))
            return

        if not target.is_dir():
            console.print(Panel(f"[red]Ce n’est pas un dossier : {target}[/red]", title="❌ Erreur"))
            return

        items = sorted(target.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower()))

        if not items:
            console.print(Panel(f"[yellow]Le dossier est vide : {target.resolve()}[/yellow]", title="📂 Vide"))
            return

        table = Table(title=f"📁 Contenu de {target.resolve()}", show_lines=False)
        table.add_column("Nom", style="bold")
        table.add_column("Type", style="dim")

        for item in items:
            item_type = "Dossier" if item.is_dir() else "Fichier"
            table.add_row(item.name, item_type)

        console.print(table)

# N’oublie pas d’ajouter ListDirCommand dans command_list.py
