n = int(input())
mass1 = []
mass2 = []
c = []
for i in range(1, n+1): 
    #print(i, end=' ')
    mass1.append(i)

for i in range(1, n+1): 
    #print(i, end=' ')
    mass2.append(i)
for i in range(0, n):
    c= str(mass1[i])+str(mass2[i])
    if i+1<n:
        print(c, end=', ')
    else:
        print(c, end=".")               