#https://www.hackerrank.com/challenges/lisa-workbook/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
    pages={}
    page=1
    for i in arr:
        cur_i=1
        while i!=0:
            if i-k>=0:
                pages[page]=[cur_i,cur_i+k]
                i=i-k
                cur_i+=k
            else:
                pages[page]=[cur_i,cur_i+i]
                i=0
            page+=1
    special=0
    for i in pages:
        if i in range(pages[i][0],pages[i][1]):
            special+=1
    return special

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    print(result)

