num = int(input('Введите число: '))
number_1 = num // 100
number_2 = num // 10 % 10
number_3 = num % 10
# a)
if number_1 == number_2 == number_3:
    print('a) Да')
else:
    print('a) Нет')
# б)
if number_1 == number_2 or number_1 == number_3 or number_2 == number_3:
    print('б) Да')
else:
    print('б) Нет')