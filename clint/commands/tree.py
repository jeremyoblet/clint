from pathlib import Path
from rich.console import Console
from rich.tree import Tree as RichTree
from rich.panel import Panel
from base_command import BaseCommand

console = Console()

class TreeCommand(BaseCommand):
    name = "tree"
    help = "Affiche l’arborescence du dossier courant ou d’un chemin donné."

    def run(self, args: str, context):
        if self.check_help(args):
            return

        path_str = args.strip()
        root = (context.cwd / path_str).resolve() if path_str else context.cwd.resolve()

        if not root.exists():
            console.print(Panel(f"[red]Le chemin n'existe pas : {root}[/red]", title="❌ Erreur", border_style="red"))
            return

        if not root.is_dir():
            console.print(Panel(f"[red]Ce n’est pas un dossier : {root}[/red]", title="❌ Erreur", border_style="red"))
            return

        tree = RichTree(f"📂 [yellow]{root.name}[/yellow]", guide_style="grey50")
        self.build_tree(tree, root)

        console.print(Panel(tree, title=f"📁 Arborescence de : {root}", border_style="blue", expand=True))

    def build_tree(self, tree_node, path: Path, level=1, max_depth=3):
        if level > max_depth:
            return

        entries = sorted(path.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower()))

        for entry in entries:
            if entry.is_dir():
                label = f"📁 [yellow]{entry.name}[/yellow]"
                branch = tree_node.add(label)
                self.build_tree(branch, entry, level + 1)
            else:
                label = f"📄 {entry.name}"
                tree_node.add(label)
