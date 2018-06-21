s=input()
t=input()
k=int(input())
i=0
while i<len(s) and i<len(t) and s[0:i]==t[0:i]:
    i=i+1
delete=len(s)-i+1
append=len(t)-i+1
if k==(delete+append):
    print("Yes")
else:
    if k>(delete+append):
        if(k-i-1>0):
            print("Yes")
    else:
        print("No")

    

