def conv(n,r):
    if n<r:
        return "0123456789ABCDEF"[n]
    else:
        k=n%r
        return conv(n//r,r)+"0123456789ABCDEF"[k]
        
print(conv(12,2))