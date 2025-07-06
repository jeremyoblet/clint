# from prompt_toolkit.completion import NestedCompleter, PathCompleter

# from context import GLOBAL_CONTEXT


# def build_completer():
#     return NestedCompleter.from_nested_dict({
#         "make": {
#             "-file": PathCompleter(only_directories=False, get_paths=lambda: [str(GLOBAL_CONTEXT.cwd)]),
#             "-dir": PathCompleter(only_directories=True, get_paths=lambda: [str(GLOBAL_CONTEXT.cwd)]),
#         },
#         "read": PathCompleter(only_directories=False, get_paths=lambda: [str(GLOBAL_CONTEXT.cwd)]),
#         "copy": None,  # tu peux l’améliorer plus tard
#         "go": PathCompleter(only_directories=True, get_paths=lambda: [str(GLOBAL_CONTEXT.cwd)]),
#         "here": None,
#         "tree": PathCompleter(only_directories=False, get_paths=lambda: [str(GLOBAL_CONTEXT.cwd)]),
#         "help": None,
#         "exit": None,
#         "quit": None,
#     })

from prompt_toolkit.completion import NestedCompleter
from context import GLOBAL_CONTEXT
from smart_path_completer import SmartPathCompleter

def build_completer():
    def p(**kwargs):
        return SmartPathCompleter(get_paths=lambda: [str(GLOBAL_CONTEXT.cwd)], **kwargs)

    return NestedCompleter.from_nested_dict({
        "make": {
            "-file": p(only_directories=False),
            "-dir": p(only_directories=True),
        },
        "read": p(only_directories=False),
        "copy": None,
        "go": p(only_directories=True),
        "here": None,
        "tree": p(only_directories=False),
        "help": None,
        "exit": None,
        "quit": None,
    })
