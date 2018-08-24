#https://www.hackerrank.com/challenges/caesar-cipher-1/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
def caesarCipher(s, k):
    final=""
    for i in s:
        if (ord(i)>=65 and ord(i)<=90):
            pos=ord(i)-64
            pos=(pos+k)%26
            if pos==0:
                pos=26
            final=final+chr(pos+64)
        elif (ord(i)>=97 and ord(i)<=122):
            pos = ord(i) - 96
            pos = (pos + k) % 26
            if pos==0:
                pos=26
            final = final + chr(pos + 96)
        else:
            final+=i
    return final

if __name__ == '__main__':

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)
    print(result)