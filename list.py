if __name__ == '__main__':
    n = int(input())
    lis=[]
    for i in range(0,n,1):
        s=input()
        l=s.split(" ")
        if l[0]=="insert":
            lis.insert(int(l[1]), int(l[2]))
        elif l[0]=="print":
            print(lis)
        elif l[0]=="remove":
            lis.remove(int(l[1]))
        elif l[0]=="append":
            lis.append(int(l[1]))
        elif l[0]=="sort":
            lis.sort()
        elif l[0]=="pop":
            lis.pop()
        else:
            lis.reverse()