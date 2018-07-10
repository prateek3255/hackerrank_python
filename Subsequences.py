import itertools
def buildSubsequences(s):
    subsequences=[]
    for i in range(1,len(s)+1):
       l=list(itertools.combinations(s,i))
       for j in l:
           subsequences.append(''.join(j))
    subsequences.sort()
    return subsequences

