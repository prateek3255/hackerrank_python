#https://www.hackerrank.com/challenges/kaprekar-numbers/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=7-day-campaign
import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    li=[]
    for i in range(p,q+1):
        n=len(str(i))
        sq=str(i**2)
        r=sq[-n:]
        l=sq[:-n]
        if l=='':
            l='0'
        if int(r)+int(l)==i:
            li.append(i)
    if li:
        print(" ".join(map(str,li)))
    else:
        print("INVALID RANGE")


if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)

