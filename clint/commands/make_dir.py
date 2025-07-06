from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from base_command import BaseCommand
from context import ShellContext

console = Console()

class MakeDirCommand(BaseCommand):
    name = "make -dir"
    help = "Crée un dossier."

    def run(self, args: str, context: ShellContext):
        if self.check_help(args):
            return

        name = args.strip()
        if not name:
            console.print(Panel("[bold red]Nom du dossier manquant[/bold red]", title="⛔ Erreur"))
            return

        path = (context.cwd / name).expanduser().resolve()

        if path.exists():
            console.print(Panel(
                f"[yellow]⚠ Le dossier existe déjà : {path}[/yellow]",
                title="⚠ Attention"
            ))
        else:
            try:
                path.mkdir(parents=True, exist_ok=True)
                console.print(Panel(
                    f"[green]✓ Dossier créé : {path}[/green]",
                    title="📁 Dossier"
                ))
            except Exception as e:
                console.print(Panel(
                    f"[red]Erreur de création : {e}[/red]",
                    title="❌"
                ))
