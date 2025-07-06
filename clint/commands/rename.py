from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from base_command import BaseCommand
from context import ShellContext

console = Console()

class RenameCommand(BaseCommand):
    name = "rename"
    help = "Renomme un fichier ou un dossier.\nUsage : rename <ancien_nom> <nouveau_nom>"

    def run(self, args: str, context: ShellContext):
        parts = args.strip().split()
        if len(parts) != 2:
            console.print(Panel("[bold red]Usage : rename <ancien_nom> <nouveau_nom>[/bold red]", title="⛔ Erreur"))
            return

        old_str, new_str = parts
        old_path = (context.cwd / old_str).expanduser().resolve()
        new_path = (context.cwd / new_str).expanduser().resolve()

        if not old_path.exists():
            console.print(Panel(f"[red]Le fichier ou dossier à renommer n'existe pas : {old_path}[/red]", title="❌ Erreur"))
            return

        if new_path.exists():
            console.print(Panel(f"[red]Un fichier ou dossier existe déjà à ce nom : {new_path}[/red]", title="⚠️ Conflit"))
            return

        try:
            old_path.rename(new_path)
            icon = "📄" if new_path.is_file() else "📁"
            console.print(Panel(
                f"[green]✓ {icon} Renommé :[/green]\n[bold]{old_path.name} ➜ {new_path.name}[/bold]",
                title="✏️ Renommage réussi", border_style="green"
            ))
        except Exception as e:
            console.print(Panel(f"[red]Erreur lors du renommage : {e}[/red]", title="❌ Erreur"))
