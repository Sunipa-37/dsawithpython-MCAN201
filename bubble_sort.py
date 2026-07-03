l=[12,30,45,10,56,70,80,90]
n=len(l)
for i in range(n):
    ptr=0
    while(ptr<n-i-1):
        if l[ptr]>l[ptr+1]:
            l[ptr],l[ptr+1]=l[ptr+1],l[ptr]
        ptr+=1
print(l)