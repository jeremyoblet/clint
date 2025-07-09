from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from base_command import BaseCommand
from context import ShellContext

console = Console()

class SearchCommand(BaseCommand):
    name = "search"
    help = "Recherche récursive des fichiers/dossiers contenant un nom (équivalent locate).\nUtilisation : search <terme> [chemin_de_départ]"

    def run(self, args: str, context: ShellContext):
        self.check_help(args)

        parts = args.strip().split(maxsplit=1)
        if not parts:
            console.print(Panel("[red]Veuillez spécifier un terme à rechercher.[/red]", title="❌ Erreur", border_style="red"))
            return

        query = parts[0]
        root = context.cwd

        if len(parts) == 2:
            root = (context.cwd / parts[1]).expanduser().resolve()
            if not root.exists() or not root.is_dir():
                console.print(Panel(
                    f"[red]Le dossier de départ est invalide : {root}[/red]",
                    title="❌ Erreur",
                    border_style="red",
                    expand=True
                ))
                return

        console.print(Panel(
            f"Recherche de « [bold]{query}[/bold] » dans [blue]{root}[/blue]...",
            title="🔍 Recherche",
            border_style="blue",
            expand=True
        ))

        matches = []
        try:
            for path in root.rglob("*"):
                if query.lower() in path.name.lower():
                    matches.append(path)
        except Exception as e:
            console.print(Panel(
                f"[red]Erreur pendant la recherche : {e}[/red]",
                title="❌ Exception",
                border_style="red",
                expand=True
            ))
            return

        if not matches:
            console.print(Panel(
                f"[yellow]Aucun fichier ou dossier trouvé correspondant à « {query} »[/yellow]",
                title="🟡 Aucun résultat",
                border_style="yellow",
                expand=True
            ))
            return

        table = Table(show_header=True, header_style="bold blue", box=None, expand=True)
        table.add_column("Chemin", style="bold", overflow="fold")

        for match in matches:
            try:
                relative = match.relative_to(root)
            except ValueError:
                relative = match
            table.add_row(str(relative))

        console.print(Panel(
            table,
            title=f"Résultats pour « {query} »",
            border_style="blue",
            expand=True
        ))
