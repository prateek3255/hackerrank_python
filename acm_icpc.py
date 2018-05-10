#https://www.hackerrank.com/challenges/acm-icpc-team/problem
n,m=map(int,input().split())
l=[]
for _ in range(n):
    l.append(input())
comb=[]
for i in range(n):
    for j in range(i,n):
        comb.append(bin(int(l[i],2)|int(l[j],2)).count('1'))
print(max(comb),comb)
print(comb.count(max(comb)))

