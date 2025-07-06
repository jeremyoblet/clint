from prompt_toolkit.completion import NestedCompleter, PathCompleter

from context import GLOBAL_CONTEXT


def build_completer():
    return NestedCompleter.from_nested_dict({
        "make": {
            "-file": PathCompleter(only_directories=False, get_paths=lambda: [str(GLOBAL_CONTEXT.cwd)]),
            "-dir": PathCompleter(only_directories=True, get_paths=lambda: [str(GLOBAL_CONTEXT.cwd)]),
        },
        "read": PathCompleter(only_directories=False, get_paths=lambda: [str(GLOBAL_CONTEXT.cwd)]),
        "copy": None,  # tu peux l’améliorer plus tard
        "go": PathCompleter(only_directories=True, get_paths=lambda: [str(GLOBAL_CONTEXT.cwd)]),
        "here": None,
        "tree": PathCompleter(only_directories=False, get_paths=lambda: [str(GLOBAL_CONTEXT.cwd)]),
        "help": None,
        "exit": None,
        "quit": None,
    })
