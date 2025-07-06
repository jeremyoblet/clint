from pathlib import Path
import shutil
from rich.console import Console
from rich.panel import Panel
from base_command import BaseCommand
from context import GLOBAL_CONTEXT

console = Console()

class CopyFileCommand(BaseCommand):
    name = "copy"
    help = "Copie un fichier d’un chemin source vers une destination."

    def run(self, args: str):
        parts = args.strip().split()
        if len(parts) != 2:
            console.print(Panel("[bold red]Usage : copy <source> <destination>[/bold red]", title="⛔ Erreur"))
            return

        src_str, dst_str = parts
        src_path = (GLOBAL_CONTEXT.cwd / src_str).expanduser().resolve()
        dst_path = (GLOBAL_CONTEXT.cwd / dst_str).expanduser().resolve()

        if not src_path.exists():
            console.print(Panel(f"[red]Le fichier source n'existe pas : {src_path}[/red]", title="❌ Erreur"))
            return

        if not src_path.is_file():
            console.print(Panel(f"[red]Le fichier source n’est pas un fichier valide : {src_path}[/red]", title="❌"))
            return

        try:
            shutil.copy2(src_path, dst_path)
            console.print(Panel(
                f"[green]✓ Fichier copié vers : {dst_path}[/green]",
                title="📄 Copie réussie", border_style="green"))
        except Exception as e:
            console.print(Panel(f"[red]Erreur lors de la copie : {e}[/red]", title="❌ Erreur"))
