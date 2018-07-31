#https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
import math
from collections import defaultdict
def nCr(n,r=2):
    f = math.factorial
    return f(n) // f(r) // f(n-r)
def sherlockAndAnagrams(s):
    letters=set(s)
    anagrams=0
    sub_list=[]
    anagramDict=defaultdict(int)
    for i in letters:
        if s.count(i)>1:
            anagrams+=nCr(s.count(i))
    for i in range(len(s)):
        for j in range(i+2,len(s)+1):
            sub_list.append(s[i:j])
    for i in sub_list:
        anagramDict[''.join(sorted(i))]+=1
    for key in anagramDict:
        if anagramDict[key]>1:
            anagrams+=nCr(anagramDict[key])
    return anagrams

q = int(input())

for q_itr in range(q):
    s = input()
    result = sherlockAndAnagrams(s)
    print(result)