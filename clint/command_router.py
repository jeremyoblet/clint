from prompt_toolkit.completion import NestedCompleter, PathCompleter
from commands import make_file, make_dir, list_dir, clear, help as help_cmd

# On crée un PathCompleter pour compléter uniquement les fichiers ou dossiers
file_completer = PathCompleter(only_directories=False)
dir_completer = PathCompleter(only_directories=True)

completer = NestedCompleter.from_nested_dict({
    "make": {
        "-file": file_completer,
        "-dir": dir_completer,
    },
    "list": None,
    "clear": None,
    "help": None,
    "exit": None,
    "quit": None,
})
