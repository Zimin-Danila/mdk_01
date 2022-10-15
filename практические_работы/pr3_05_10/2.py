with open(r"C:\Programming\MDK\MDK_01_01\lr7_04_10\zadanie2\zadanie2.txt") as f:
    n = f.read()
    f.close()
    x = input()
    #    O(n)
    for i in n:
        #   O(1)
        if(i == x):
            print("Yes")
            # O(1)
            break