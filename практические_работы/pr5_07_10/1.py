        # O(n)
def factorial(n):
        # O(1)
    if (n <= 1):
        return 1
    else:
                # O(n*fact(n-1))
        return (n * factorial(n-1))
    # O(1)
n = int(input("Введите число:"))
print("Факториал числа равен:")
print(factorial(n))