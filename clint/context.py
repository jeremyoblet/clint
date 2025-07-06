from pathlib import Path

class ShellContext:
    def __init__(self):
        self.cwd = Path.cwd()
