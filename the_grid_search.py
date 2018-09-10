#https://www.hackerrank.com/challenges/the-grid-search/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
# Complete the gridSearch function below.
def gridSearch(G, P):
    R=len(G)
    C=len(G[0])
    r = len(P)
    c = len(P[0])
    i=0
    j=0
    flagFinal=False
    while(i+r<=R):
        j=0
        while (j+c<=C):
            flag=True
            for k in range(i,i+r):
                if G[k][j:j+c]!=P[k-i]:
                    flag=False
                    break
            if flag:
                flagFinal=True
                break
            j+=1
        if flagFinal:
            break
        i+=1
    return "YES" if flagFinal else "NO"




if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        print(result)
