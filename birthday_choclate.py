#https://www.hackerrank.com/challenges/the-birthday-bar/problem

def solve(n, s, d, m):
    count=0
    for i in range(n):
        if (i+m)<=n:
            if d==sum(s[i:i+m]):
                count+=1
        else:
            break
    return count        
            

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)