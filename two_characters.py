#https://www.hackerrank.com/challenges/two-characters/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
import itertools


# Complete the alternate function below.
def checkAlternate(s):
    chars=set(s)
    opp=chars.difference(set([s[0]]))
    for i in s:
        if i in opp:
            return False
        opp=chars.difference(opp)
    return True


def alternate(s):
    chars=set(s)
    comb=itertools.combinations(chars,r=len(chars)-2)
    m=0
    for i in list(comb):
        x=str(s)
        for j in i:
            x=x.replace(j,"")
        if checkAlternate(x) and len(x)>m:
            m=len(x)
    return m

if __name__ == '__main__':

    l = int(input().strip())

    s = input()

    result = alternate(s)

    print(result)