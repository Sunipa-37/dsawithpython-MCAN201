l=[20,30,10,15,16,18,4,25]
n=len(l)
for i in range(0,n-1):
    for j in range(i+1,n):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print(l)