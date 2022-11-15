class SingletonDecorator:
    def __init__(self,klass):
        self.klass = klass
        self.instance = None
    def __call__(self,*args,**kwds):
        if self.instance == None:
            self.instance = self.klass(*args,**kwds)
        return self.instance
class foo: pass
if __name__ == '__main__':
    foo = SingletonDecorator(foo)
    x = foo()
    y = foo()
    z = foo()
    x.val = 'one'
    y.val = 'two'
    z.val = 'three'
    print(x.val)
    print(y.val)
    print(z.val)