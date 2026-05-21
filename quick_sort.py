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
a=[0,17,-3,90,-14,0,1,100]
print(a)
l=0
r=7
quick_Sort(a,l,r)
print(a)