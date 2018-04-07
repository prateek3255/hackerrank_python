#https://www.hackerrank.com/challenges/picking-numbers/problem

t=int(input())
a=list(map(int,input().split()))
arr=list(map(lambda x : [x],a))
for i in a:
    for j in arr:
        f=True
        for k in j:
            if not(abs(i-k))<=1:
                f=False
                break
        if f:
            j.append(i)
l=[len(i) for i in arr]
print(max(l)-1)
    