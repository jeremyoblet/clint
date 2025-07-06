from prompt_toolkit.completion import NestedCompleter, PathCompleter

file_completer = PathCompleter(only_directories=False)
dir_completer = PathCompleter(only_directories=True)

completer = NestedCompleter.from_nested_dict(
    {
    "make": 
        {
            "-file": file_completer,
            "-dir": dir_completer,
        },
    "list": dir_completer,
    "clear": None,
    "help": None,
    "exit": None,
    "quit": None,
})
