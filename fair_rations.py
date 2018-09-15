#https://www.hackerrank.com/challenges/fair-rations/problem
def fairRations(B):
    count=0
    for i in range(len(B)):
        if i+2<len(B):
            if B[i]%2!=0 and B[i+1]%2==0 and B[i+2]%2!=0:
                B[i]+=1
                B[i+1]+=2
                B[i+2]+=1
                count+=4
        if i+1<len(B):
            if B[i]%2!=0 and B[i+1]%2!=0:
                B[i]+=1
                B[i+1]+=1
                count+=2
    print(B)
    B=list(map(lambda a:a%2,B))
    if sum(B)==0:
        return count
    else:
        return "NO"

N = int(input())

B = list(map(int, input().rstrip().split()))

result = fairRations(B)

print(result)

