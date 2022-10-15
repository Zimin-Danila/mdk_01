n = int(input())
lst = [64, 32, 16, 8, 4, 2, 1]
ans = []
while n>0:
 for i in lst:
   if n >= i:
     n -= i
     ans.append(i)
     break  
print(f'Понадобится {len(ans)}шт. купюр, а именно:')
print(*ans)
