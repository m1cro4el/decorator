from Beverage import Beverage

class Espresso(Beverage):
     def __init__(self) -> None:
        self._description = "Espresso"
    
    def cost(self) -> float:
        return 100