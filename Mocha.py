from CondimentDecorator import CondimentDecorator
from Beverage import Beverage

class Mocha(CondimentDecorator):
    _beverage: Beverage

    def __init__(self, b: Beverage) -> None:
        self()._beverage = b

    def getDescription(self) -> str:
        return self._beverage.getDescription() +", Mocha"

    def cost(self) -> float:
        return 20 + self._beverage.cost()