import os
from rich.console import Console

console = Console()

def run(args: str = ""):
    os.system("cls" if os.name == "nt" else "clear")
