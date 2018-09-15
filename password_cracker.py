#https://www.hackerrank.com/challenges/password-cracker/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
import sys
import re

def passwordCracker(pas, attempt):
    # Complete this function
    pos=[]
    act_attempt=str(attempt)
    for i in pas:
        if i in attempt:
            l=[[m.start(),i] for m in re.finditer(i,act_attempt)]
            attempt=attempt.replace(i,"")
            pos=pos+l
    pos.sort(key= lambda x: x[0])
    pos=[p[1] for p in pos]
    print(attempt)
    if attempt=="":
        return " ".join(pos)
    else:
        return "WRONG PASSWORD"


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        pas = input().strip().split(' ')
        attempt = input().strip()
        result = passwordCracker(pas, attempt)
        print(result)