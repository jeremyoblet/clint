from prompt_toolkit.completion import WordCompleter
from commands import (
    make_file,
    make_dir,
    list_dir,
    clear,
    help as help_cmd,
)

custom_commands = [
    "make -file",
    "make -dir",
    "list",
    "help",
    "exit"
]

completer = WordCompleter(custom_commands, ignore_case=True)

def run_command(cmd: str):
    cmd = cmd.strip()

    if cmd.startswith("make -file"):
        return make_file.run, cmd.removeprefix("make -file").strip()

    if cmd.startswith("make -dir"):
        return make_dir.run, cmd.removeprefix("make -dir").strip()

    if cmd.startswith("list"):
        return list_dir.run, cmd.removeprefix("list").strip()
    
    if cmd.startswith("clear"):
        return clear.run, cmd.removeprefix("list").strip()

    if cmd == "help":
        return help_cmd.run, ""

    return None, cmd
