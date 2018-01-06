def average(array):
    s=set(array)
    c=sum(s)
    print(s)
    return c/len(s)
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
    