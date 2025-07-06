from pathlib import Path
from prompt_toolkit.completion import PathCompleter, Completion
from prompt_toolkit.formatted_text import FormattedText

class SmartPathCompleter(PathCompleter):
    def get_completions(self, document, complete_event):
        seen = set()

        for comp in super().get_completions(document, complete_event):
            text = comp.text
            path = Path(text).expanduser()
            name = path.name

            if path.is_dir() and not text.endswith("/"):
                new_text = text + "/"
                if new_text not in seen:
                    seen.add(new_text)
                    yield Completion(
                        new_text,
                        start_position=comp.start_position,
                        display=FormattedText([
                            ("ansiblue bold", name),
                            ("ansicyan", "/")
                        ]),
                        display_meta="📁 dossier"
                    )
            elif text not in seen:
                seen.add(text)
                style = "ansigray" if path.is_file() else ""
                yield Completion(
                    text,
                    start_position=comp.start_position,
                    display=FormattedText([(style, name)]),
                    display_meta="📄 fichier" if path.is_file() else ""
                )
