a = ['Даня', 'Никита', 'Николай','Филипп']
b = list(map(lambda x: hash(x), a))
print('Исходный список')
print(a)
print('Конечный список')
print(b)