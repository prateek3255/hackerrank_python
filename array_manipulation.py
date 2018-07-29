#https://www.hackerrank.com/challenges/crush/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
def arrayManipulation(n,q):
    zeroes=[0 for i in range(n)]
    for i in q:
        zeroes[i[0]-1:i[1]]=[sum(x) for x in zip(zeroes[i[0]-1:i[1]],[i[2]]*(i[1]-i[0]+1))]
    return max(zeroes)



nm = input().split()

n = int(nm[0])

m = int(nm[1])

queries = []

for _ in range(m):
    queries.append(list(map(int, input().rstrip().split())))

result = arrayManipulation(n, queries)
print(result)