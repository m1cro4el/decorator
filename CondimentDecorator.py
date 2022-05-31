from abc import ABC, abstractmethod
import re
from Beverage import Beverage

class CondimentDecorator(Beverage, ABC)
    @abstractmethod
    def getDescription(self) -> str:
        return self._description