def quick_Sort(a,l,r):
    if l<r:
        p=quick(a,l,r)
        quick_Sort(a,l,p-1)
        quick_Sort(a,p+1,r)
def quick(a,l,r):
    p=l
    left=l+1
    right=r
    while True:
        while right>=left and a[p]<=a[right]:
            right =right-1
        if a[p]>a[right]:
            a[p],a[right]=a[right],a[p]
            p=right
            right-=1
        if right<left:
            return p
        while right>=left and a[p]>=a[left]:
            left+=1
        if a[p]<a[left]:
            a[p],a[left]=a[left],a[p]
            p=left
            left+=1
        if right<left:
            return p
a=[53,10,15,6,100,-1,22,2,18,27]
print(a)
l=0
r=len(a)
quick_Sort(a,l,r-1)
print(a)