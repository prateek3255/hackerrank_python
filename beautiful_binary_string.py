def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count
def replaceAndReturnOcc(b,i):
    if b[i]=='0':
        b=b[:i]+'1'+b[i+1:]
    else:
        b=b[:i]+'0'+b[i+1:]
    return occurrences(b,"010")

def replace(b,i):
    if b[i]=='0':
        b=b[:i]+'1'+b[i+1:]
    else:
        b=b[:i]+'0'+b[i+1:]
    return b

def beautifulBinaryString(b):
    rep=0
    i=0
    while i<len(b):
        if i+3<=len(b) and b[i:i+3]=="010":
            l=[replaceAndReturnOcc(b,i),replaceAndReturnOcc(b,i+1),replaceAndReturnOcc(b,i+2)]
            rep+=1
            print()
            b=replace(b,i+l.index(min(l)))
            i=i+3
        else:
            i+=1
    return rep


if __name__ == '__main__':

    n = int(input())

    b = input()

    result = beautifulBinaryString(b)
    print(result)