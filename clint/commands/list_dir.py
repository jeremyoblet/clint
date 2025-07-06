from pathlib import Path
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import os
import stat

console = Console()

def human_readable_size(size_bytes):
    # Conversion en Ko/Mo/Go
    for unit in ['o', 'Ko', 'Mo', 'Go', 'To']:
        if size_bytes < 1024:
            return f"{size_bytes:.0f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.0f} To"

def get_permissions(path: Path) -> str:
    mode = path.stat().st_mode
    perms = ""
    perms += "r" if os.access(path, os.R_OK) else "-"
    perms += "w" if os.access(path, os.W_OK) else "-"
    perms += "x" if os.access(path, os.X_OK) else "-"
    return perms

def run(args: str):
    target = args.strip() or "."
    path = Path(target)

    if not path.exists():
        console.print(
            Panel(f"[bold red]Le dossier n'existe pas :[/bold red] {path}",
                  title="⛔ Erreur", border_style="red")
        )
        return

    if not path.is_dir():
        console.print(
            Panel(f"[bold yellow]Ce n'est pas un dossier :[/bold yellow] {path}",
                  title="⚠ Attention", border_style="yellow")
        )
        return

    entries = list(path.iterdir())
    if not entries:
        console.print(
            Panel(f"[italic]Le dossier est vide :[/italic] {path.resolve()}",
                  title="📂 Vide", border_style="blue")
        )
        return

    table = Table(title=f"📁 Contenu de : {path.resolve()}", border_style="green")
    table.add_column("Nom", style="cyan", no_wrap=True)
    table.add_column("Type", style="magenta")
    table.add_column("Taille", justify="right", style="yellow")
    table.add_column("Modifié le", style="white")
    table.add_column("Droits", style="bright_black", justify="center")

    for entry in sorted(entries):
        stat_info = entry.stat()
        entry_type = "📄 Fichier" if entry.is_file() else "📁 Dossier"
        size = human_readable_size(stat_info.st_size) if entry.is_file() else "-"
        modified = datetime.fromtimestamp(stat_info.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
        perms = get_permissions(entry)

        table.add_row(entry.name, entry_type, size, modified, perms)

    console.print(table)
