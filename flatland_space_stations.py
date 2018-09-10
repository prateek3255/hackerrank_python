#https://www.hackerrank.com/challenges/flatland-space-stations/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=7-day-campaign
def flatlandSpaceStations(n, c):
    c.sort()
    cn=0
    stations=[]
    for i in range(n):
        if cn+1<len(c) and abs(i-c[cn])>abs(i-c[cn+1]):
            stations.append(abs(i-c[cn+1]))
            cn+=1
        else:
            stations.append(abs(i-c[cn]))
    return max(stations)

nm = input().split()
n = int(nm[0])

m = int(nm[1])

c = list(map(int, input().rstrip().split()))

result = flatlandSpaceStations(n, c)
print(result)


