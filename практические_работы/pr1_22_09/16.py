from collections import Counter
name = input()
my_list =[]
my_list.append(name)
count = 0
while name != "":
    name = input()
    if name in my_list:
        count += 1
        my_list.remove(name)
        continue
    else:
        my_list.append(name)
print(Counter)