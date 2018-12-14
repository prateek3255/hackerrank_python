#https://www.hackerrank.com/contests/projecteuler/challenges/euler001

def fun(n):
    s=set()
    x=(n-1)//3
    for i in range(1,x+1):
        s.add(3*i)
    y=(n-1)//5
    for i in range(1,y+1):
        s.add(5*i)
    print(sum(s))

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    fun(n)


