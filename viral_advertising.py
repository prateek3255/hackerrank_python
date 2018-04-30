#https://www.hackerrank.com/challenges/strange-advertising/problem

def viralAdvertising(n):
    total=0
    s=5
    for _ in range(1,n+1):
        l=int(s/2)
        total+=l
        s=l*3
    return total
        

if __name__ == "__main__":
    n = int(input().strip())
    result = viralAdvertising(n)
    print(result)