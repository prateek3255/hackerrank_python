n=input()
def getMaxProjects(input):
    phases=list(input.split())
    proj=set()
    count=0
    i=0
    while i<len(phases):
        if i+6<=len(phases):
            if len(set(phases[i:i+6]))==6:
                count+=1
                i+=6
            else:
                i+=1
        else:
            break
    return count
print(getMaxProjects(n))