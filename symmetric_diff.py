n=input()
l1=input().split();
m=input();
l2=input().split();
s1=set(l1)
s2=set(l2)
s3=s1.union(s2)
s4=s1.intersection(s2)
s5=s3.difference(s4)
l=list(map(int,s5))
l.sort()
for i in l:
    print(i)