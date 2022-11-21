class WhatIHave:
    def g(self): pass
    def h(self): pass
class WhatIWant:
    def f(self): pass
class ProxyAdapter(WhatIWant):
    def __init__(self, whatIHave):
        self.whatIHave = whatIHave
    def f(self):
 #реализация поведения, используя методы в WhatIHave
        self.whatIHave.g()
        self.whatIHave.h()
class WhatIUse:
    def op(self, whatIWant):
        whatIWant.f()
#Вариант 2: построение адаптера, используя op()
class WhatIUse2(WhatIUse):
    def op(self, whatIHave):
        ProxyAdapter(whatIHave).f()
#Вариант 3: построение адаптера в WhatIHave
class WhatIHave2(WhatIHave, WhatIWant):
    def f(self):
        self.g()
        self.h()
#Вариант 4: использование вложенного класса
class WhatIHave3(WhatIHave):
    class InnerAdapter(WhatIWant):
        def __init__(self, outer):
            self.outer = outer
        def f(self):
            self.outer.g()
            self.outer.h()
    def whatIWant(self):
        return WhatIHave3.InnerAdapter(self)
if __name__ == '__main__':
    whatIUse = WhatIUse()
    whatIHave = WhatIHave()
    adapt= ProxyAdapter(whatIHave)
    whatIUse2 = WhatIUse2()
    whatIHave2 = WhatIHave2()
    whatIHave3 = WhatIHave3()
    whatIUse.op(adapt)
    #Вариант 2:
    whatIUse2.op(whatIHave)
    #Вариант 3:
    whatIUse.op(whatIHave2)
    #Вариант 4:
    whatIUse.op(whatIHave3.whatIWant())
