import os

from prompt_toolkit import prompt
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.history import FileHistory

from completer import completer

from commands.command_list import COMMAND_CLASSES
from command_router import Router


HISTORY_PATH = os.path.expanduser("~/.mysh_history")

def main():
    router = Router(COMMAND_CLASSES)

    while True:
        try:
            user_input = prompt(
                HTML("<ansigreen>mysh</ansigreen><ansiblue> ❯ </ansiblue>"),
                completer=completer,
                history=FileHistory(HISTORY_PATH)
            ).strip()

            if user_input in {"exit", "quit"}:
                break

            router.execute(user_input)


        except KeyboardInterrupt:
            print("\n[Terminal closed]")
            break

if __name__ == "__main__":
    main()
