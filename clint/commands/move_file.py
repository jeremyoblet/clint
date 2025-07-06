from pathlib import Path
import shutil
from rich.console import Console
from rich.panel import Panel
from base_command import BaseCommand
from context import ShellContext

console = Console()

class MoveCommand(BaseCommand):
    name = "move"
    help = "Déplace un fichier ou un dossier.\nUsage : move <source> <destination>"

    def run(self, args: str, context: ShellContext):
        parts = args.strip().split()
        if len(parts) != 2:
            console.print(Panel("[bold red]Usage : move <source> <destination>[/bold red]", title="⛔ Erreur"))
            return

        src_str, dst_str = parts
        src_path = (context.cwd / src_str).expanduser().resolve()
        dst_path = (context.cwd / dst_str).expanduser().resolve()

        if not src_path.exists():
            console.print(Panel(f"[red]Le fichier ou dossier source n'existe pas : {src_path}[/red]", title="❌ Erreur"))
            return

        try:
            shutil.move(str(src_path), str(dst_path))
            icon = "📁" if src_path.is_dir() else "📄"
            console.print(Panel(
                f"[green]✓ {icon} Déplacé vers : {dst_path}[/green]",
                title="📦 Déplacement réussi", border_style="green"
            ))
        except Exception as e:
            console.print(Panel(f"[red]Erreur lors du déplacement : {e}[/red]", title="❌ Erreur"))
