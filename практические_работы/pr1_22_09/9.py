from math import factorial
n = int(input())
sum = 0
for i in range(1, n+1):
    sum += factorial(i)
print(sum)