#https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
def countTriplets(arr,r):
    trip={}
    for i in arr:
        if i in trip:
            trip[i]+=1
        else:
            trip[i]=1
    count=0
    for i in arr:
        if i*r in trip and i*r*r in trip:
            count+=trip[i]*trip[i*r]*trip[i*r*r]
    return count

nr = input().rstrip().split()

n = int(nr[0])

r = int(nr[1])

arr = list(map(int, input().rstrip().split()))

ans = countTriplets(arr, r)

print(ans)