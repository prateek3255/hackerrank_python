#https://www.hackerrank.com/challenges/separate-the-numbers/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
def findFirstNo(s):
    if len(s)>=2:
        for i in range(1,len(s)):
            if 2*i<=len(s) and int(s[0:i])+1==int(s[i:i+i]):
                return int(s[0:i])
            elif 2*i+1<=len(s) and int(s[0:i])+1==int(s[i:i+i+1]):
                return int(s[0:i])
    else:
        return int(s)
    return None

def validate(s):
    return not s[0]=='0'

def separateNumbers(s):
    x=findFirstNo(s)
    step=len(str(x))
    # print(x)
    if x is not None:
        cur=0
        while(cur<=len(s)):
            if cur+2*step<=len(s) and int(s[cur:cur+step])+1==int(s[cur+step:cur+2*step]) and validate(s[cur+step:cur+2*step]):
                # print(s[cur:cur + step], s[cur + step:cur + 2 * step], cur+2*step,len(s))
                if cur+2*step==len(s):
                    break
                cur=cur+step


            elif (cur+2*step+1)<=len(s) and int(s[cur:cur+step])+1==int(s[cur+step:cur+2*step+1]) and validate(s[cur+step:cur+2*step+1]):
                # print(s[cur:cur + step], s[cur + step:cur + 2 * step + 1], (cur+2*step+1),len(s))
                if (cur+2*step+1)==len(s):
                    break
                cur=cur+step
                step+=1


            else:
                return "No"
        return "Yes "+str(x)
    return "No"




if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        print(separateNumbers(s))