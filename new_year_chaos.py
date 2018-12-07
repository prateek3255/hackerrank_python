#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def checkChaotic(q):
    for i in range(len(q),0,-1):
        if i-(q.index(i)+1)>2:
            return True
    return False


def minimumBribes(q):
    if checkChaotic(q):
        print("Too chaotic")
    else:
        i=len(q)

        count=0
        while(i>0):
            if(q.index(i)!=i-1):
                count=count+i-1-q.index(i)
                q.remove(i)
                q.insert(i-1,i)

            i=i-1

        print(count)



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
