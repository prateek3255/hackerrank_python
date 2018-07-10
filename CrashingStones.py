import math
def lastStoneWeight(a):
    a.sort(reverse=True)
    while len(a)>1:
        x=a[0]
        a.remove(a[0])
        y=a[0]
        a.remove(a[0])
        if x!=y:
            a.insert(sortedInsert(a,abs(x-y)),abs(x-y))
    return a[0] if len(a)!=0 else 0

def sortedInsert(a,x):
    if len(a)==0:
        return 0
    else:
        high=len(a)-1
        low=0
        while True:
            mid=int((high+low)/2)
            if a[mid]==x:
                return mid
            elif a[mid]>x:
                low=mid+1
                if low>high:
                    return mid+1
            elif a[mid]<x:
                high=mid-1
                if low>high:
                    return mid


print(lastStoneWeight([2,4,5]))

