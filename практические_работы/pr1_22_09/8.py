a, b, c = int(input()), int(input()), int(input())
if (a>100) and (b>100):
    print("YES")
else:
    print("NO")
if a % 2 == 0 and b % 2 == 0:
    print("NO")
else:
    print("YES")
if a > 0 or b > 0:
    print("YES")
else:
    print("NO")
if a%3 == 0 and b%3 == 0 and c%3 == 0:
    print("YES")
else:
    print("NO")
if ((a<50) and (b>=50) and (c>=50)) or ((a>50) and (b<50) and (c>=50)) or ((a>=50) and (b>=50) and (c<50)):
    print("YES")
else:
    print("NO")
if (a<0) or (b<0) or (c<0):
    print("YES")
else:
    print("NO")

