from pathlib import Path
import subprocess
import sys
from base_command import BaseCommand
from rich.panel import Panel
from rich.console import Console

console = Console()

class LaunchCommand(BaseCommand):
    name = "launch"
    help = "Lance une application ou ouvre un fichier avec le programme associé."

    def run(self, args: str, context):
        if self.check_help(args):
            return

        target = args.strip()
        if not target:
            console.print(Panel(
                "[red]Nom de l'application ou fichier manquant[/red]",
                title="❌ Erreur",
                border_style="red"
            ))
            return

        path = (context.cwd / target).expanduser().resolve()

        try:
            if sys.platform.startswith("win"):
                if path.exists():
                    subprocess.Popen(f'"{path}"', shell=True)
                else:
                    subprocess.Popen(target, shell=True)
            else:
                if path.exists():
                    subprocess.Popen(["xdg-open", str(path)])
                else:
                    subprocess.Popen([target])
        except Exception as e:
            console.print(Panel(
                f"[red]Erreur : {e}[/red]",
                title="❌ Exception",
                border_style="red"
            ))
