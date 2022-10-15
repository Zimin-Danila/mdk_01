n = int(input())
nn = n % 10
n //= 10
n = nn * 100 + n
print(n) 