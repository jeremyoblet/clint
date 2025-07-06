from pathlib import Path
import shutil
from rich.console import Console
from rich.panel import Panel
from base_command import BaseCommand
from context import ShellContext

console = Console()

class RemoveCommand(BaseCommand):
    name = "remove"
    help = "Supprime un fichier ou un dossier (récursivement pour les dossiers)."

    def run(self, args: str, context: ShellContext):
        if self.check_help(args):
            return

        target_str = args.strip()
        if not target_str:
            console.print(Panel("[bold red]Nom du fichier ou dossier à supprimer manquant[/bold red]", title="⛔ Erreur"))
            return

        path = (context.cwd / target_str).expanduser().resolve()

        if not path.exists():
            console.print(Panel(f"[red]Le chemin n'existe pas : {path}[/red]", title="❌ Erreur"))
            return

        try:
            if path.is_file():
                path.unlink()
                console.print(Panel(f"[green]✓ Fichier supprimé : {path}[/green]", title="🗑️ Suppression"))
            elif path.is_dir():
                shutil.rmtree(path)
                console.print(Panel(f"[green]✓ Dossier supprimé avec son contenu : {path}[/green]", title="🗑️ Suppression récursive"))
            else:
                console.print(Panel(f"[red]Type de fichier inconnu : {path}[/red]", title="❌ Erreur"))
        except Exception as e:
            console.print(Panel(f"[red]Erreur lors de la suppression : {e}[/red]", title="❌ Exception"))
