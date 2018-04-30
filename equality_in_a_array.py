#https://www.hackerrank.com/challenges/equality-in-a-array/problem

def equalizeArray(arr):
    s=set(arr)
    m=0
    e=0
    for i in s:
        if arr.count(i)>m:
            m=arr.count(i)
            e=i
    return (len(arr)-arr.count(e))
    
if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = equalizeArray(arr)
    print(result)
    

