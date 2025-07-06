from rich.console import Console
from base_command import BaseCommand
import os

console = Console()

class ClearCommand(BaseCommand):
    name = "clear"
    help = "Nettoie l’écran du terminal."

    def run(self, args: str, context):  # Ajout de 'context'
        os.system('cls' if os.name == 'nt' else 'clear')
