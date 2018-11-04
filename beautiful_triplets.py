#https://www.hackerrank.com/challenges/beautiful-triplets/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    triplets=0
    for i in arr:
        if i+d in arr and i+2*d in arr:
            triplets+=1
    return triplets
if __name__ == '__main__':

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    print(result)
