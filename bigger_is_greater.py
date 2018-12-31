#https://www.hackerrank.com/challenges/bigger-is-greater/problem


# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    if len(w)==1:
        return "no answer"
    i=len(w)-1
    while i>0:
        if w[i]<=w[i-1]:
            i-=1
        else:
            i-=1
            break
    if i==0 and w[0]>=w[1]:
        return "no answer"
    else:
        pivot = i
        rep=0
        for i in range(len(w)-1,0,-1):
            if w[i]>w[pivot]:
                rep=i
                break
        t=list(w)
        t[pivot],t[rep]=t[rep],t[pivot]
        w=''.join(t)
        res=w[:pivot+1]+''.join(sorted(w[pivot+1:]))
        return res



if __name__ == '__main__':

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        print(result)




