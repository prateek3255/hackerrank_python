#https://www.hackerrank.com/challenges/password-cracker/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
import sys
import re

def passwordCracker(pas, attempt,act_attempt,pos=[]):
    # Complete this function
    # pos=[]
    # act_attempt=str(attempt)
    # for i in pas:
    #     if i in attempt:
    #         l=[[m.start(),i] for m in re.finditer(i,act_attempt)]
    #         attempt=attempt.replace(i,"")
    #         pos=pos+l
    # pos.sort(key= lambda x: x[0])
    # pos=[p[1] for p in pos]
    # print(attempt)
    # if attempt=="":
    #     return " ".join(pos)
    # else:
    #     return "WRONG PASSWORD"
    if attempt=="":
        return pos

    res=False
    for i in pas:
        if i in attempt:
            l=[[m.start(),i] for m in re.finditer(i,act_attempt)]
            sub_res=passwordCracker(pas,attempt.replace(i,""),act_attempt,pos+l)

            if sub_res:
                res=sub_res
                break
    return res




if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        pas = input().strip().split(' ')
        attempt = input().strip()
        result = passwordCracker(pas, attempt,attempt)
        if result:
            result.sort(key= lambda x: x[0])
            result=[p[1] for p in result]
            print(" ".join(result))
        else:
            print("WRONG PASSWORD")