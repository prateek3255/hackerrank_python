#https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
#!/bin/python3

# import os
# import sys

def climbingLeaderboard(scores, alice):
    scores=set(scores)
    scores=list(scores)
    scores.sort(reverse=True)
    ranks=[[j,i] for i,j in zip(scores,range(1,len(scores)+1))]
    result=[]
    for i in alice:
        for j in range(len(ranks)):
            if i<ranks[j][1]:
                if j==(len(ranks)-1):
#                     ranks.append([j+2,i])
                    result.append(j+2)
                    break
                else:
                    continue
            elif i==ranks[j][1]:
#                 ranks.insert(j,[j+1,i])
                result.append(j+1)
                break
            else:
#                 ranks.insert(j,[j+1,i])
                result.append(j+1)
                for k in range(j+1,len(ranks)):
                    ranks[k]=[ranks[k][0]+1,ranks[k][1]]
                break
                
    return result
                
            
            

if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)
    print(result)
# 
#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')
# 
#     fptr.close()
