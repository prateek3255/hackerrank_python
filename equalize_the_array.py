#https://www.hackerrank.com/challenges/equality-in-a-array/problem
n=int(input())
arr=list(map(int,input().split()))
s=set(arr)
m=0

for i in s:
    if(arr.count(i)>m):
        m=arr.count(i)
print(len(arr)-m)
       


