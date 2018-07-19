#https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
def minimumBribes(q):
    aq=[i for i in range(1,len(q)+1)]
    tm=0
    for i in range(len(q)):
        index=aq.index(q[i])
        if i<index:
            if index-i<=2:
                aq.insert(i,aq.pop(index))
                tm=tm+index-i
            else:
                return "Too chaotic"

    return tm

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))