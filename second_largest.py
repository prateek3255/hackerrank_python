if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l=list(arr)
    l.sort()
    m=l[n-1]
    m2=0
    l.reverse()
    for i in l:
        if i!=m:
            m2=i
            break
    print(m2)
