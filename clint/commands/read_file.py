from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from base_command import BaseCommand

console = Console()

class ReadFileCommand(BaseCommand):
    name = "read"
    help = (
        "Lit et affiche le contenu d’un fichier texte.\n"
        "Options :\n"
        "  --head N    Affiche les N premières lignes\n"
        "  --tail N    Affiche les N dernières lignes\n"
        "  --numbers   Numérote les lignes"
    )

    def run(self, args: str, context):
        if self.check_help(args):
            return

        import re
        parts = args.strip().split()
        if not parts:
            console.print(Panel("[bold red]Nom du fichier manquant[/bold red]", title="⛔ Erreur", border_style="red"))
            return

        # Extraire nom + options
        filename = None
        options = {"head": None, "tail": None, "numbers": False}

        for part in parts:
            if part.startswith("--head"):
                match = re.match(r"--head(?:[ =](\d+))?", part)
                if match:
                    options["head"] = int(match.group(1)) if match.group(1) else 10
            elif part.startswith("--tail"):
                match = re.match(r"--tail(?:[ =](\d+))?", part)
                if match:
                    options["tail"] = int(match.group(1)) if match.group(1) else 10
            elif part == "--numbers":
                options["numbers"] = True
            elif not filename:
                filename = part

        if not filename:
            console.print(Panel("[bold red]Fichier introuvable dans la commande[/bold red]", title="⛔ Erreur", border_style="red"))
            return

        path = (context.cwd / filename).expanduser().resolve()

        if not path.exists():
            console.print(Panel(f"[red]Le fichier n'existe pas : {path}[/red]", title="❌ Erreur", border_style="red"))
            return

        if not path.is_file():
            console.print(Panel(f"[red]Ce n’est pas un fichier : {path}[/red]", title="❌ Erreur", border_style="red"))
            return

        try:
            lines = path.read_text(encoding="utf-8").splitlines()

            # Appliquer head/tail
            if options["head"] is not None:
                lines = lines[:options["head"]]
            elif options["tail"] is not None:
                lines = lines[-options["tail"]:]

            # Ajouter numéros si demandé
            if options["numbers"]:
                width = len(str(len(lines)))
                lines = [f"[dim]{str(i+1).rjust(width)}[/dim] {line}" for i, line in enumerate(lines)]

            content = "\n".join(lines) if lines else "[dim](Fichier vide)"
            console.print(Panel(
                content,
                title=f"📄 {path.name}",
                border_style="blue",
                expand=True
            ))
        except Exception as e:
            console.print(Panel(f"[red]Erreur de lecture : {e}[/red]", title="❌", border_style="red"))
