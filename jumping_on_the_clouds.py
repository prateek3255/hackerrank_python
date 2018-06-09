#https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

n=int(input())
l=list(map(int,input().split()))

count=0
i=0
while i<n:
    if i<n-2 and l[i+2]==0:
        i=i+2
    else:
        i=i+1
    count+=1
print(count-1)
        
