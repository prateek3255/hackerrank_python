#https://www.hackerrank.com/challenges/2d-array/problem?h_l=playlist&slugs%5B%5D=interview&slugs%5B%5D=interview-preparation-kit&slugs%5B%5D=arrays
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the hourglassSum function below.
def hourglassSum(arr):
    m = 0
    for i in range(4):
        for j in range(4):
            temp = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i + 1][j + 1] + arr[i+2][j] + arr[i + 2][j+1] + arr[i+2][j + 2];
            if m < temp:
                m = temp
    return m


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
    print(result)
