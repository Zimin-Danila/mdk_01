class OnlyOne:
    class __OnlyOne:
        def __init__(self):
            self.val = None
        def __str__(self):
            return self.val
        instance = None
        def __new__(cls):
            if not OnlyOne.instance:
                OnlyOne.instance = OnlyOne.__OnlyOne()
            return OnlyOne.instance
if __name__ == '__main__':
    x = OnlyOne()
    x.val = 'one'
    print(x)
    y = OnlyOne()
    y.val = 'two'
    print(y)
    z = OnlyOne()
    z.val = 'three'
    print(z)
    print(x)
    print(y)