from __future__ import generators
import random
# The shop hierarchy cannot be changed:
class Project(object):
    def accept(self, visitor):
        visitor.visit(self)
    def working(self, worker):
        print(self, 'работает с', worker)
    def bre_ak(self, vladik):
        print(self, 'отдыхает с', vladik)
    def __str__(self):
        return self.__class__.__name__

class Dwarf(Project): pass
class Elf(Project): pass
class Troll(Project): pass

class Visitor:
    def __str__(self):
        return self.__class__.__name__
class Engineer(Visitor): pass
class Marketing(Visitor): pass
class Manager(Visitor): pass


class Dwarf(Engineer):
    def visit(self, shop):
        shop.working(self)

class Elf(Marketing):
    def visit(self, shop):
        shop.working(self)

class Troll(Manager):
    def visit(self, shop):
        shop.bre_ak(self)

def mythical_creatures(n):
    creatures = Project.__subclasses__()
    for i in range(n):
        yield random.choice(creatures)()


if __name__ == '__main__':
    dwarf = Dwarf()
    elf = Elf()
    troll = Troll()
    for creatures in mythical_creatures(3):
        creatures.accept(dwarf)
        creatures.accept(elf)
        creatures.accept(troll)
    
    