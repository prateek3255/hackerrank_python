#!/bin/python3

# https://www.hackerrank.com/challenges/plus-minus/problem
import sys

def plusMinus(arr):
    pos=0
    neg=0
    zer=0
    for i in arr:
        if i>0:
            pos+=1
        elif i<0:
            neg+=1
        else:
            zer+=1
    print(pos/len(arr))
    print(neg/len(arr))
    print(zer/len(arr))

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    plusMinus(arr)
