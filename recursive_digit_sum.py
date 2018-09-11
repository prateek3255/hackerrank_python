#https://www.hackerrank.com/challenges/recursive-digit-sum/problem
def superDigit(n, k):
    n = n * k
    if len(n) == 1:
        return n
    else:
        n = superDigit(str(sum(list(map(int, n)))), 1)
    return n




nk = input().split()

n = nk[0]

k = int(nk[1])

result = superDigit(n, k)

print(result)
