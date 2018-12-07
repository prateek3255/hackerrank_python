#!/bin/python3
#https://www.hackerrank.com/challenges/larrys-array/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
import math
import os
import random
import re
import sys
from collections import deque

# Complete the larrysArray function below.
def larrysArray(A):
    s=sorted(A)
    for i in range(len(A)):
        while(s[i]!=A[i]):
            x=A.index(s[i])
            if x-i<=2:
                if i+2<n:
                    if x-i==1:
                        q=deque(A[i:i+3])
                        q.rotate(-1)
                        # print(q)
                        A[i:i+3]=list(q)
                        # print(A)
                    elif x-i==2:
                        q = deque(A[i:i + 3])
                        q.rotate(-2)
                        A[i:i + 3] = list(q)
                else:
                    return "NO"
            else:
                q=deque(A[x-2:x+1])
                q.rotate(-2)
                A[x-2:x+1]=list(q)
    return "YES"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)
        print(result)

    #     fptr.write(result + '\n')
    #
    # fptr.close()
