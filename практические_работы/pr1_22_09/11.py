b, k, t = int(), int(), int()
for b in range(0, 10):
    for k in range(0, 20):
        for t in range(0, 200):
            if 20*b+10*k+t==200 and b+k+t==100:
                print('Быков ', b, 'коров ', k,  'телят', t)
            else:
                continue