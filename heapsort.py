def heapify(a,i,n):
    l=2*i+1
    r=2*i+2
    p=i
    if r<n and a[r]>a[p]:
        p=r
    if l<n and a[l]>a[p]:
        p=l
    if i ==p:
        return
    a[p],a[i]=a[i],a[p]
    heapify(a,p,n)

def maxheap(a,n):
    for i in range(n//2+1,0,-1):
        heapify(a,i,n) 
def heapsort(a):
    n=len(a)
    while(n>=1):
        a[0],a[n-1]=a[n-1],a[0]
        n=n-1
        heapify(a,0,n)
a=[40,30,50,60,35,49,65,55,25,28]
maxheap(a,len(a))
print(a)
heapsort(a)
print(a)