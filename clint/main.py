import os
from shutil import get_terminal_size

from prompt_toolkit import PromptSession
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.history import FileHistory
from prompt_toolkit.shortcuts.prompt import CompleteStyle

from rich.console import Console

from completer import build_completer
from command_list import COMMAND_CLASSES
from command_router import Router
from style import custom_style
from clint_ascii import CLINT_ASCII
from context import ShellContext

HISTORY_PATH = os.path.expanduser("~/.mysh_history")
console = Console()
context = ShellContext()

def print_separator():
    width = get_terminal_size((100, 20)).columns
    console.print(" " * width, style="dim")


def main():
    router = Router(COMMAND_CLASSES, context)
    # console.print(CLINT_ASCII, style="bold green")

    session = PromptSession(
        completer=build_completer(context),
        complete_style=CompleteStyle.READLINE_LIKE,
        history=FileHistory(HISTORY_PATH),
        style=custom_style
    )
    
    while True:
        try:
            cwd_name = context.cwd.name or context.cwd.drive



            # ensuite, dans ta boucle :
            user_input = session.prompt(
                HTML(f"<ansigreen>{cwd_name}</ansigreen><ansiblue> ❯❯❯ </ansiblue>")
            ).strip()


            if user_input in {"exit", "quit"}:
                break

            router.execute(user_input)
            print_separator() 


        except KeyboardInterrupt:
            print("\n[Terminal closed]")
            break

if __name__ == "__main__":
    main()
