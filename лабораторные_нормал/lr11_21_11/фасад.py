class A:
    def __init__(self, x): pass
class B:
    def __init__(self, x): pass
class C:
    def __init__(self, x): pass
        # self.x = x
class Facade:
    def makeA(x): return A(x)
    makeA = staticmethod(makeA)
    def makeB(x): return B(x)
    makeB = staticmethod(makeB)
    def makeC(x): return C(x)
    makeC = staticmethod(makeC)
if __name__ == '__main__':
    a = Facade.makeA(1)
    b = Facade.makeB(1)
    c = Facade.makeC(1.0)