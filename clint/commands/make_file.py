from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from base_command import BaseCommand
from context import ShellContext

console = Console()

class MakeFileCommand(BaseCommand):
    name = "make -file"
    help = "Crée un fichier vide."

    def run(self, args: str, context: ShellContext):
        if self.check_help(args):
            return

        name = args.strip()
        if not name:
            console.print(Panel("[bold red]Nom manquant[/bold red]", title="⛔ Erreur"))
            return

        path = (context.cwd / name).expanduser().resolve()

        if path.exists():
            console.print(Panel(
                f"[yellow]⚠ Existe déjà : {path}[/yellow]",
                title="⚠ Attention"
            ))
        else:
            try:
                path.parent.mkdir(parents=True, exist_ok=True)  # au cas où les dossiers n'existent pas
                path.touch()
                console.print(Panel(
                    f"[green]✓ Créé : {path}[/green]",
                    title="📄 Fichier"
                ))
            except Exception as e:
                console.print(Panel(f"[red]Erreur : {e}[/red]", title="❌"))
