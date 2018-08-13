#https://www.hackerrank.com/challenges/string-construction/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
def stringConstruction(s):
    p=""
    cost=0
    i=0
    while(i<len(s)):
       if s[i] not in p:
           p+=s[i]
           cost+=1
           i+=1
       else:
            j=i+2
            while(s[i:j] in p and j<len(s)):
                j=j+1
            p+=s[i:j-1]
            i=j-1
    return cost
q = int(input())

for q_itr in range(q):
    s = input()

    result = stringConstruction(s)
    print(result)