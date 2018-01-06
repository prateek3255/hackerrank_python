import operator
if __name__ == '__main__':
    li=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l=[name,score]
        li.append(l)
    li.sort(key = operator.itemgetter(1,0))
    j=li[0][1]
    k=0
    for i in li:
        if j!=i[1]: 
            k=i[1]
            break
    
    for i in li:
        if i[1]==k:
            print(i[0])