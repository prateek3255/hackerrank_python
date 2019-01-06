#https://www.hackerrank.com/challenges/countingsort1/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
    count=[]
    for i in range(100):
        count.append(arr.count(i))
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    print(result)



