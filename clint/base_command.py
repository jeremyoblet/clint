from abc import ABC, abstractmethod

from context import ShellContext

class BaseCommand(ABC):
    name: str = ""
    help: str = ""

    def show_help(self):
        from rich.panel import Panel
        from rich.console import Console

        console = Console()
        console.print(Panel(
            self.help or "(Aucune aide disponible)",
            title=f"❓ Aide : {self.name}",
            border_style="green",
            expand=True
        ))

    def check_help(self, args: str) -> bool:
        if "--help" in args.split():
            self.show_help()
            return True
        return False
    
    @abstractmethod
    def run(self, args: str, context: ShellContext):
        raise NotImplementedError

