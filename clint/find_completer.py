from prompt_toolkit.completion import Completer, Completion, merge_completers, WordCompleter
from smart_path_completer import SmartPathCompleter

class FindCompleter(Completer):
    def __init__(self):
        self.patterns = WordCompleter(["*.py", "*.txt", "*.md", "*.*"], ignore_case=True)
        self.path_completer = SmartPathCompleter(only_directories=True)

    def get_completions(self, document, complete_event):
        words = document.text_before_cursor.strip().split()

        if not words or words == ["find"]:
            # Suggest patterns and flags
            yield from self.patterns.get_completions(document, complete_event)
            yield Completion("--from", display_meta="répertoire de recherche")
            yield Completion("--depth", display_meta="profondeur max")
            return

        if "--from" in words:
            from_index = words.index("--from")
            if len(words) == from_index + 1 or (len(words) == from_index + 2 and not words[-1].startswith("--")):
                # Complétion de chemin attendue
                yield from self.path_completer.get_completions(document, complete_event)
                return

        # Complétion par défaut sinon
        yield from self.patterns.get_completions(document, complete_event)
