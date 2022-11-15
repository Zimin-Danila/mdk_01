class OnlyOne:
    class __OnlyOne:
        def __init__(self, arg):
            self.val = arg
        instance = None
        def __init__(self, arg):
            if not OnlyOne.instance:
                OnlyOne.instance = OnlyOne.__OnlyOne(arg)
            else:
                OnlyOne.instance.val = arg
        def __str__(self):
            return repr(OnlyOne.instance.val)
if __name__ == '__main__':
 x = OnlyOne('one')
 print(x)
 y = OnlyOne('two')
 print(y)
 z = OnlyOne('three')
 print(z)
 print(x)
 print(y)