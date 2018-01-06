if __name__ == '__main__':
    s = input()
    l=[False]*5
    for ch in s:
        if ch.isalnum():
            l[0]=True
        if ch.isalpha():
            l[1]=True
        if ch.isdigit():
            l[2]=True
        if ch.islower():
            l[3]=True
        if ch.isupper():
            l[4]=True
    for i in l:
        print(i)