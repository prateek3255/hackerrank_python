#https://www.hackerrank.com/challenges/palindrome-index/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
def checkPalindrome(s):
    return s[::-1]==s

def palindromeIndex(s):
    i=0
    j=len(s)-1
    index=-1
    while(i!=j and abs(i-j)!=1):
        if(s[i]!=s[j]):
            x=s[:i]+s[i+1:]
            if checkPalindrome(x):
                index=i
            else:
                index=j
            break
        i += 1
        j -= 1
    return index




if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        print(result)
