#!/bin/python3
#https://www.hackerrank.com/challenges/bonetrousle/problem
import os
import sys

#
# Complete the bonetrousle function below.
#
def bonetrousle(n, k, b):
    x=sum(range(k-b+1,k+1))
    y=sum(range(1,b+1))
    if y<=n<=x:
        s=list(range(1,b+1))
        c=0
        while sum(s)!=n:
            if (sum(s)-s[c]+k-c)<n:
                s[c]=k-c
                c+=1
            else:
                s[c]=s[c]+n-sum(s)
                if (len(set(s))!=len(s)):
                    s[c]=s[c]+n-sum(s)-1
                c+=1
        return s
    else:
        return [-1]



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nkb = input().split()

        n = int(nkb[0])

        k = int(nkb[1])

        b = int(nkb[2])

        result = bonetrousle(n, k, b)

        print(' '.join(map(str, result)))

    #     fptr.write(' '.join(map(str, result)))
    #     fptr.write('\n')
    #
    # fptr.close()
