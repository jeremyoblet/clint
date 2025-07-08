from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from base_command import BaseCommand

console = Console()

class FindCommand(BaseCommand):
    name = "find"
    help = (
        "Recherche récursive de fichiers avec filtre de profondeur et contenu.\n"
        "Usage : find \"pattern\" [--from dossier] [--depth N] [--contains \"texte\"] [--content]\n"
        "Exemple : find \"*.py\" --from src --depth 2 --contains \"def\" --content"
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
        show_content = False

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
            elif parts[i] == "--content":
                show_content = True
            i += 1

        def search_with_depth(root: Path, pattern: str, current_depth: int = 0):
            matches = []
            if max_depth is not None and current_depth > max_depth:
                return matches

            for item in root.iterdir():
                if item.is_file() and fnmatch.fnmatch(item.name, pattern):
                    if contains:
                        try:
                            text = item.read_text(encoding="utf-8")
                            if contains in text:
                                matches.append(item)
                        except Exception:
                            continue  # Ignore fichiers illisibles (binaire, etc.)
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

        if contains and show_content:
            from rich.markup import escape
            from rich.text import Text

            all_text = Text()
            found_any = False

            for match in matches:
                abs_path = context.cwd / match
                try:
                    lines = abs_path.read_text(encoding="utf-8").splitlines()
                except Exception:
                    continue

                lines_found = []

                for i, line in enumerate(lines):
                    if contains in line:
                        found_any = True
                        lineno = str(i + 1).rjust(4)
                        # Construction ligne avec mise en forme
                        line_text = Text()
                        line_text.append(f"{lineno} ", style="dim")

                        start = 0
                        while True:
                            idx = line.find(contains, start)
                            if idx == -1:
                                line_text.append(line[start:])
                                break
                            line_text.append(line[start:idx])
                            line_text.append(contains, style="orange1")
                            start = idx + len(contains)

                        lines_found.append(line_text)

                if lines_found:
                    all_text.append(Text(f"\n{match}\n", style="bold blue"))
                    for line_text in lines_found:
                        all_text.append(line_text)
                        all_text.append("\n")

            if not found_any:
                all_text.append("[dim](Aucune ligne correspondante)[/dim]")

            console.print(Panel(
                all_text,
                title=f"📂 Résultats avec contenu : {len(matches)} fichier(s)",
                border_style="green",
                expand=True
            ))

        elif contains:
            output = "\n".join(str(p) for p in matches)
            console.print(Panel(
                output or "[dim](Aucun fichier correspondant au filtre --contains)[/dim]",
                title=f"📂 {len(matches)} fichier(s) trouvés contenant \"{contains}\"",
                border_style="green",
                expand=True
            ))
