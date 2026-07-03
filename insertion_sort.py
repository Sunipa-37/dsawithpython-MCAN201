l=[20,30,10,15,16,18,4,25]
n=len(l)
for i in range(1,n-1):
    item=l[i]
    j=i-1
    while(item<=l[j]) and j>=0:
        l[j+1]=l[j]
        j-=1
    l[j+1]=item
    print(l)