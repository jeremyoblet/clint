from prompt_toolkit.completion import NestedCompleter
from find_completer import FindCompleter
from smart_path_completer import SmartPathCompleter

def build_completer(context):
    def p(**kwargs):
        return SmartPathCompleter(only_directories=kwargs.get("only_directories", False))

    return NestedCompleter.from_nested_dict({
        "find": FindCompleter(),
        "make": {
            "-file": p(only_directories=False),
            "-dir": p(only_directories=True),
        },
        "read": p(only_directories=False),
        "copy": p(only_directories=False),
        "go": p(only_directories=False),
        "here": None,
        "tree": p(only_directories=False),
        "move": p(only_directories=False),
        "rename": p(only_directories=False),
        "launch": p(only_directories=False),
        "remove": p(only_directories=False),
        "help": None,
        "exit": None,
    })
