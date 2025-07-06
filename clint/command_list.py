import importlib
import inspect
import pkgutil
from pathlib import Path

from base_command import BaseCommand
import commands  # le package `commands` (doit contenir __init__.py)

COMMAND_CLASSES = []

# Chemin absolu vers le dossier 'commands'
commands_path = Path(commands.__file__).parent

# Pour chaque module dans le package 'commands'
for _, module_name, is_pkg in pkgutil.iter_modules([str(commands_path)]):
    if is_pkg:
        continue

    full_module_name = f"commands.{module_name}"
    module = importlib.import_module(full_module_name)

    # Recherche des sous-classes de BaseCommand dans le module
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and issubclass(obj, BaseCommand) and obj is not BaseCommand:
            COMMAND_CLASSES.append(obj)
