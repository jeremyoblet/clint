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
        "  --head N    Affiche les N premières lignes (ex: --head 10)\n"
        "  --tail N    Affiche les N dernières lignes (ex: --tail=5)\n"
        "  --numbers   Numérote les lignes"
    )

    def run(self, args: str, context):
        if self.check_help(args):
            return

        parts = args.strip().split()
        if not parts:
            console.print(Panel("[bold red]Nom du fichier manquant[/bold red]", title="⛔ Erreur", border_style="red"))
            return

        filename = None
        options = {"head": None, "tail": None, "numbers": False}

        i = 0
        while i < len(parts):
            part = parts[i]

            if part == "--head":
                i += 1
                if i < len(parts) and parts[i].isdigit():
                    options["head"] = int(parts[i])
                else:
                    options["head"] = 10
            elif part.startswith("--head="):
                try:
                    options["head"] = int(part.split("=", 1)[1])
                except ValueError:
                    pass
            elif part.startswith("--head") and part[6:].isdigit():
                options["head"] = int(part[6:])

            elif part == "--tail":
                i += 1
                if i < len(parts) and parts[i].isdigit():
                    options["tail"] = int(parts[i])
                else:
                    options["tail"] = 10
            elif part.startswith("--tail="):
                try:
                    options["tail"] = int(part.split("=", 1)[1])
                except ValueError:
                    pass
            elif part.startswith("--tail") and part[6:].isdigit():
                options["tail"] = int(part[6:])

            elif part == "--numbers":
                options["numbers"] = True

            elif not filename:
                filename = part

            i += 1

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

            # Appliquer head ou tail (priorité au head)
            if options["head"] is not None:
                lines = lines[:options["head"]]
            elif options["tail"] is not None:
                lines = lines[-options["tail"]:]

            # Ajouter numéros de ligne si demandé
            if options["numbers"]:
                width = len(str(len(lines)))
                lines = [f"[dim]{str(i + 1).rjust(width)}[/dim] {line}" for i, line in enumerate(lines)]

            content = "\n".join(lines) if lines else "[dim](Fichier vide)"
            console.print(Panel(
                content,
                title=f"📄 {path.name}",
                border_style="blue",
                expand=True
            ))
        except Exception as e:
            console.print(Panel(f"[red]Erreur de lecture : {e}[/red]", title="❌", border_style="red"))
