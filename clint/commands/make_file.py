from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def run(args: str):
    name = args.strip()

    if not name:
        console.print(
            Panel("[bold red]Erreur : nom de fichier manquant[/bold red]", title="⛔ Erreur", border_style="red")
        )
        return

    path = Path(name)
    
    if path.exists():
        console.print(
            Panel(
                f"[yellow]⚠ Le fichier existe déjà :[/yellow]\n[b]{path.resolve()}[/b]",
                title="⚠ Attention",
                border_style="yellow"
            )
        )
    else:
        try:
            path.touch()
            console.print(
                Panel(
                    f"[green]✓ Fichier créé avec succès :[/green]\n[b]{path.resolve()}[/b]",
                    title="📄 Création",
                    border_style="green"
                )
            )
        except Exception as e:
            console.print(
                Panel(
                    f"[bold red]Impossible de créer le fichier :[/bold red]\n{e}",
                    title="❌ Échec",
                    border_style="red"
                )
            )
