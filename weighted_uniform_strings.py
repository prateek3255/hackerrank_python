#https://www.hackerrank.com/challenges/weighted-uniform-string/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
def calcWeight(buffer):
    c=buffer[0]
    return len(buffer)*(ord(c)-96)

def weightedUniformStrings(s, queries):
    d=[]
    for i in range(97,123):
        if chr(i) in s:
            for j in range(1,len(s)+1):
                if chr(i)*j in s:
                    d.append(calcWeight(chr(i)*j))
                else:
                    break
    result=[]
    for i in queries:
        if i in d:
            result.append('Yes')
        else:
            result.append('No')
    return result

if __name__ == '__main__':

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)
    print(result)