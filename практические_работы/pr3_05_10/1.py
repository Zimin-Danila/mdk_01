from random import randint

N = 10
a = []
#       O(N) = O(10)
for i in range(N):
    #   O(1)   O(1)
    a.append(randint(1, 99))
print(a)

#       O(N-1) = O(9)
for i in range(N-1):
    #     O(10-i-1) = O(1)
    for j in range(N-i-1):
        #       O(1)
        if a[j] > a[j+1]:
            #           O(1)
            a[j], a[j+1] = a[j+1], a[j]
print(a)