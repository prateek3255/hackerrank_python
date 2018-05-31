#https://www.hackerrank.com/challenges/mars-exploration/problem
s=input()
count=0
for i in range(0,len(s),3):
    if s[i:i+3]!="SOS":
        for j in range(3):
            if "SOS"[j]!=s[i+j]:
                count+=1
                
print(count)