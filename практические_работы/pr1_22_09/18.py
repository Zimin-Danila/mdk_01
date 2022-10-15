from random import randint
from unittest import result
numbers = []
for i in range(10):
    numbers.append(randint(1, 20))
a = numbers 
result = []
for i in a:
    if i&1:
        result.append(i + 2)
    else:
        result.append(i * i)
print(result)

