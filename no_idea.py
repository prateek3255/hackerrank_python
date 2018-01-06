n, m= input().split()
l=list(map(int,input().split()))
a=set(map(int,input().split()))
b=set(map(int,input().split()))
h=0
for i in l:
    if i in a:
        h=h+1
    elif i in b: 
        h=h-1
print(h)
