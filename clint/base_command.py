from abc import ABC, abstractmethod

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
        """Affiche l’aide si --help est présent dans les arguments."""
        if "--help" in args.split():
            self.show_help()
            return True
        return False
    
    @abstractmethod
    def run(self, args: str):
        raise NotImplementedError

