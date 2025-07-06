from pathlib import Path
from rich.console import Console
from rich.tree import Tree as RichTree
from base_command import BaseCommand
from context import GLOBAL_CONTEXT

console = Console()

class TreeCommand(BaseCommand):
    name = "tree"
    help = "Affiche l’arborescence du dossier courant ou d’un chemin donné."

    def run(self, args: str):
        path_str = args.strip()
        root = (GLOBAL_CONTEXT.cwd / path_str).resolve() if path_str else GLOBAL_CONTEXT.cwd.resolve()

        if not root.exists():
            console.print(f"[red]Le chemin n'existe pas : {root}[/red]")
            return

        if not root.is_dir():
            console.print(f"[red]Ce n’est pas un dossier : {root}[/red]")
            return

        tree = RichTree(f"📂 [bold]{root.name}[/bold]", guide_style="bold bright_blue")
        self.build_tree(tree, root)
        console.print(tree)

    def build_tree(self, tree_node, path: Path, level=1, max_depth=3):
        if level > max_depth:
            return

        entries = sorted(path.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower()))

        for entry in entries:
            label = f"[bold]{entry.name}[/bold]" if entry.is_dir() else entry.name
            branch = tree_node.add(label)
            if entry.is_dir():
                self.build_tree(branch, entry, level + 1)
