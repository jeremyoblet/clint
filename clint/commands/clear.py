import os
import platform
from base_command import BaseCommand

class ClearCommand(BaseCommand):
    name = "clear"
    help = "Efface l’écran du terminal."

    def run(self, args: str):
        system = platform.system()
        if system == "Windows":
            os.system("cls")
        else:
            os.system("clear")

# À ajouter dans command_list.py
