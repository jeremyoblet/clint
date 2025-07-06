from abc import ABC, abstractmethod

class BaseCommand(ABC):
    name: str = ""
    help: str = ""

    @abstractmethod
    def run(self, args: str):
        ...
