class DrinkComponent:
 def getDescription(self):
    return self.__class__.__name__
 def getTotalCost(self):
    return self.__class__.cost
class Espresso(DrinkComponent):
    cost = 0.75
class EspressoConPanna(DrinkComponent):
    cost = 1.0
class Cappuccino(DrinkComponent):
    cost = 1.0
class CafeLatte(DrinkComponent):
    cost = 1.0
class CafeMocha(DrinkComponent):
    cost = 1.25
class Decorator(DrinkComponent):
    def __init__(self, drinkComponent):
        self.component = drinkComponent
    def getTotalCost(self):
        return self.component.getTotalCost() + DrinkComponent.getTotalCost(self)
    def getDescription(self):
        return self.component.getDescription() + ' ' + DrinkComponent.getDescription(self)
class ExtraEspresso(Decorator):
    cost = 0.75
    def __init__(self, drinkComponent):
        Decorator.__init__(self, drinkComponent)
class Whipped(Decorator):
    cost = 0.50
    def __init__(self, drinkComponent):
        Decorator.__init__(self, drinkComponent)
class Decaf(Decorator):
    cost = 0.0
    def __init__(self, drinkComponent):
        Decorator.__init__(self, drinkComponent)
class Dry(Decorator):
    cost = 0.0
    def __init__(self, drinkComponent):
        Decorator.__init__(self, drinkComponent)
class Wet(Decorator):
    cost = 0.0
    def __init__(self, drinkComponent):
        Decorator.__init__(self, drinkComponent)
class Syrop(Decorator):
    cost = 1000
    def __init__(self, drinkComponent):
        Decorator.__init__(self, drinkComponent)
if __name__ == '__main__':
    cappuccino = Cappuccino()
    print(cappuccino.getDescription() + ': $' + str(cappuccino.getTotalCost()))
    cafeMocha = Whipped(Decaf(CafeMocha()))
    print(cafeMocha.getDescription() + ': $' + str(cafeMocha.getTotalCost()))
    cafeLatte = Syrop(CafeLatte())
    print(cafeLatte.getDescription() + ': $' + str(cafeLatte.getTotalCost()))