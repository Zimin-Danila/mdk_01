n = int(input('Введите общее количество покупок: '))
a = {}
#          O(n)
for i in range(n):
    #     O(1)
    shopin = input()
    #                           O(N)
    f, tovar, amount = shopin.rsplit(maxsplit=3)
    #       O(1)
    amount = int(amount)
    #     O(N)
    if f not in a:
        #    O(1)
        a[f] = {tovar: amount}
    else:
        #          O(N)
        if tovar not in a[f]:
            #    O(1)
            a[f] |= {tovar: amount}
        else:
            #           O(1)
            a[f][tovar] += amount
#               O(N log N)
for f, shopin in sorted(a.items()):
    #
    print(f'{f}:')
    #                   O(N log N)
    for tovar, amount in sorted(shopin.items()):
        print(tovar, amount)