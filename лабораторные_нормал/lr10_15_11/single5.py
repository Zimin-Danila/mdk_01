class SingletonMetaClass(type):
    def __init__(cls,name,bases,dict):
        super(SingletonMetaClass,cls)\
            .__init__(name,bases,dict)
        original_new = cls.__new__
        def my_new(cls,*args,**kwds):
            if cls.instance == None:
                cls.instance = \
                    original_new(cls,*args,**kwds)
            return cls.instance

        cls.instance = None
        cls.__new__ = staticmethod(my_new)
class bar(object):
    __metaclass__ = SingletonMetaClass
    def __init__(self,val):
        self.val = val
    def __str__(self):
        print(self)
        return self.val
if __name__ == '__main__':
    x = bar('one')
    y = bar('two')
    z = bar('three')
    print(x)
    print(y)
    print(z)