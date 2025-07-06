from pathlib import Path
import os
from datetime import datetime
from shutil import get_terminal_size
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from base_command import BaseCommand
from context import GLOBAL_CONTEXT

console = Console()

class ListDirCommand(BaseCommand):
    name = "list"
    help = "Liste les fichiers et dossiers avec détails (responsive)."

    def run(self, args: str):
        self.check_help(args)
        target = (GLOBAL_CONTEXT.cwd / args.strip()).resolve() if args.strip() else GLOBAL_CONTEXT.cwd.resolve()

        if not target.exists():
            console.print(Panel(f"[red]Le chemin n'existe pas : {target}[/red]", title="❌ Erreur"))
            return

        if not target.is_dir():
            console.print(Panel(f"[red]Ce n’est pas un dossier : {target}[/red]", title="❌ Erreur"))
            return

        items = sorted(target.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower()))
        if not items:
            console.print(Panel(f"[yellow]Le dossier est vide : {target}[/yellow]", title="📂 Vide", expand=True))
            return

        term_width = get_terminal_size((100, 20)).columns
        padding = 2 * 2  # padding gauche/droite du Panel
        col_widths = {
            "size": 8,
            "mtime": 16,
            "perms": 5,
            "gap": 3  # espaces entre colonnes
        }

        # Calcul de la largeur disponible pour le nom
        available = term_width - padding - sum(col_widths.values()) - col_widths["gap"] * 3
        name_col_width = max(15, available)

        table = Table(
            show_header=True,
            header_style="bold blue",
            box=None,
            pad_edge=False,
            expand=False,
        )

        table.add_column("Nom", style="bold", overflow="ellipsis", max_width=name_col_width)
        table.add_column("Taille", justify="right", style="dim", no_wrap=True, width=col_widths["size"])
        table.add_column("Modifié", style="dim", no_wrap=True, width=col_widths["mtime"])
        table.add_column("Droits", style="dim", no_wrap=True, width=col_widths["perms"])

        for item in items:
            icon = "📁" if item.is_dir() else "📄"
            name = f"{icon} {item.name}"
            table.add_row(
                name,
                self._get_size(item),
                self._get_mtime(item),
                self._get_permissions(item),
            )

        console.print(Panel(
            table,
            title=f"📂 {target}",
            border_style="blue",
            expand=True  # ✅ occupe toute la largeur du terminal
        ))

    def _get_size(self, path: Path) -> str:
        try:
            size = path.stat().st_size
            for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
                if size < 1024.0:
                    return f"{size:.0f} {unit}"
                size /= 1024.0
        except Exception:
            return "?"
        return f"{size:.1f} TB"

    def _get_mtime(self, path: Path) -> str:
        try:
            ts = path.stat().st_mtime
            return datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M")
        except Exception:
            return "?"

    def _get_permissions(self, path: Path) -> str:
        try:
            return "".join([
                "r" if os.access(path, os.R_OK) else "-",
                "w" if os.access(path, os.W_OK) else "-",
                "x" if os.access(path, os.X_OK) else "-",
            ])
        except Exception:
            return "---"
