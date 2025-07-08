from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from base_command import BaseCommand

console = Console()

class FindCommand(BaseCommand):
    name = "find"
    help = (
        "Recherche récursive de fichiers avec filtre de profondeur et contenu.\n"
        "Usage : find \"pattern\" [--from dossier] [--depth N] [--contains \"texte\"]\n"
        "Exemple : find \"*.py\" --from src --depth 2 --contains \"import\""
    )

    def run(self, args: str, context):
        if self.check_help(args):
            return

        import fnmatch

        parts = args.strip().split()
        if not parts:
            console.print(Panel(
                "[bold red]Pattern de recherche manquant[/bold red]",
                title="⛔ Erreur",
                border_style="red"
            ))
            return

        pattern = parts[0].strip('"').strip("'")
        search_root = context.cwd
        max_depth = None
        contains = None

        i = 1
        while i < len(parts):
            if parts[i] == "--from":
                i += 1
                if i < len(parts):
                    from_path = context.cwd / parts[i]
                    if not from_path.exists() or not from_path.is_dir():
                        console.print(Panel(
                            f"[red]Dossier invalide : {from_path}[/red]",
                            title="⛔ Erreur",
                            border_style="red"
                        ))
                        return
                    search_root = from_path
            elif parts[i] == "--depth":
                i += 1
                if i < len(parts):
                    try:
                        max_depth = int(parts[i])
                    except ValueError:
                        console.print(Panel(
                            f"[red]Profondeur invalide : {parts[i]}[/red]",
                            title="⛔ Erreur",
                            border_style="red"
                        ))
                        return
            elif parts[i] == "--contains":
                i += 1
                if i < len(parts):
                    contains = parts[i]
            i += 1

        def search_with_depth(root: Path, pattern: str, current_depth: int = 0):
            matches = []
            if max_depth is not None and current_depth > max_depth:
                return matches

            for item in root.iterdir():
                if item.is_file() and fnmatch.fnmatch(item.name, pattern):
                    if contains:
                        try:
                            if contains in item.read_text(encoding="utf-8"):
                                matches.append(item)
                        except Exception:
                            continue  # skip unreadable file
                    else:
                        matches.append(item)
                elif item.is_dir():
                    matches.extend(search_with_depth(item, pattern, current_depth + 1))
            return matches

        matches = search_with_depth(search_root, pattern)
        matches = sorted(p.relative_to(context.cwd) for p in matches)

        if not matches:
            console.print(Panel(
                f"[yellow]Aucun fichier trouvé pour :[/yellow] [b]{pattern}[/b]"
                + (f" contenant \"{contains}\"" if contains else ""),
                title="🔍 Aucun Résultat",
                border_style="yellow"
            ))
            return

        output = "\n".join(str(p) for p in matches)
        console.print(Panel(
            output,
            title=f"📂 {len(matches)} fichier(s) trouvés",
            border_style="green",
            expand=True
        ))
