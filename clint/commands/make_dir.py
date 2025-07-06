from pathlib import Path
from rich.console import Console
from rich.panel import Panel

console = Console()

def run(args: str):
    name = args.strip()

    if not name:
        console.print(
            Panel("[bold red]Erreur : nom de dossier manquant[/bold red]", title="⛔ Erreur", border_style="red")
        )
        return

    path = Path(name)

    if path.exists():
        if path.is_dir():
            console.print(
                Panel(
                    f"[yellow]⚠ Le dossier existe déjà :[/yellow]\n[b]{path.resolve()}[/b]",
                    title="📁 Dossier existant",
                    border_style="yellow"
                )
            )
        else:
            console.print(
                Panel(
                    f"[red]❌ Un fichier avec ce nom existe déjà :[/red]\n[b]{path.resolve()}[/b]",
                    title="⛔ Conflit",
                    border_style="red"
                )
            )
        return

    try:
        path.mkdir(parents=True, exist_ok=False)
        console.print(
            Panel(
                f"[green]✓ Dossier créé avec succès :[/green]\n[b]{path.resolve()}[/b]",
                title="📁 Création",
                border_style="green"
            )
        )
    except Exception as e:
        console.print(
            Panel(
                f"[bold red]Impossible de créer le dossier :[/bold red]\n{e}",
                title="❌ Échec",
                border_style="red"
            )
        )
