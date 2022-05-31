from abc import ABC, abstractmethod

class Beverage(ABC):
    _description: str

    def __init__(self) -> None:
        self._description(self) -> None:

    def getDescription(self) -> str:
        return self._description

    @abstractmethod
    def cost(self) -> float:
        pass