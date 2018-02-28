#https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
import sys

def breakingRecords(score):
    high=score[0]
    low=score[0]
    h=0
    l=0
    for s in score:
        if high<s:
            h+=1
            high=s
        if low>s:
            l+=1
            low=s
    result=[h,l]
    return result

if __name__ == "__main__":
    n = int(input().strip())
    score = list(map(int, input().strip().split(' ')))
    result = breakingRecords(score)
    print (" ".join(map(str, result)))