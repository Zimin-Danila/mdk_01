grades = [5, 4, 5, 3, 2, 5, 4, 3, 5, 5, 4, 2, 2, 3]
print(f'Средний балл: {round((sum(grades) / len(grades)), 2)}')
print(*grades, sep=';')
