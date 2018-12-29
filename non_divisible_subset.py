#https://www.hackerrank.com/challenges/non-divisible-subset/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
from itertools import combinations

def satisfySubset(s,k):
    for i in list(combinations(s,2)):
        if (i[0]+i[1])%k==0:
            return False
    return True

def nonDivisibleSubset(k, S):
    for i in range(len(S),1,-1):
        l=list(combinations(S,i))
        for j in l:
            if satisfySubset(j,k):
                return len(j)
    return 1


if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    S = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, S)

    print(result)