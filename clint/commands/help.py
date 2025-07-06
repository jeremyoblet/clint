from rich.console import Console
from rich.table import Table

console = Console()

def run(args: str = ""):
    table = Table(title="📚 Aide - Commandes disponibles", border_style="cyan")

    table.add_column("Commande", style="magenta", no_wrap=True)
    table.add_column("Description", style="white")

    table.add_row("make -file <nom>", "Crée un fichier vide avec le nom donné")
    table.add_row("make -dir <nom>", "Crée un dossier (avec parents si besoin)")
    table.add_row("list [chemin]", "Liste le contenu d'un dossier sous forme de tableau")
    table.add_row("clear", "Efface l’écran du terminal")
    table.add_row("help", "Affiche cette aide")
    table.add_row("exit / quit", "Ferme le terminal")

    console.print(table)
