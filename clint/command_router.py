from typing import List

class Router:
    def __init__(self, command_classes, context):
        # dictionnaire nom ➜ classe (pas instance)
        self.command_classes = {cls.name: cls for cls in command_classes}
        self.context = context

    def find_match(self, input_str: str):
        input_str = input_str.strip()
        for name, cls in self.command_classes.items():
            if input_str.startswith(name):
                args = input_str[len(name):].strip()
                return cls, args
        return None, input_str

    def execute(self, input_str: str):
        CommandClass, args = self.find_match(input_str)
        if CommandClass:
            instance = CommandClass()
            return instance.run(args, self.context)
        else:
            print(f"[Erreur] Commande inconnue : {input_str}")
