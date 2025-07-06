from prompt_toolkit.completion import NestedCompleter
from smart_path_completer import SmartPathCompleter

def build_completer(context):
    def p(**kwargs):
        return SmartPathCompleter(get_paths=lambda: [str(context.cwd)], **kwargs)

    return NestedCompleter.from_nested_dict({
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
        "help": None,
        "exit": None,
        "quit": None,
    })
