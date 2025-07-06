import os

from prompt_toolkit import prompt
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.history import FileHistory

from completer import completer
from command_router import run_command

HISTORY_PATH = os.path.expanduser("~/.mysh_history")

def main():
    while True:
        try:
            user_input = prompt(
                HTML("<ansigreen>mysh</ansigreen><ansiblue> ❯ </ansiblue>"),
                completer=completer,
                history=FileHistory(HISTORY_PATH)
            ).strip()

            if user_input in {"exit", "quit"}:
                break

            func, args = run_command(user_input)
            if func:
                func(args)
            else:
                print(f"[Erreur] Commande inconnue : {user_input}")

        except KeyboardInterrupt:
            print("\n[Terminal fermé]")
            break

if __name__ == "__main__":
    main()
