#https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
def hackerrankInString(s):
    st="hackerrank"
    pos=0
    for i in s:
        if i==st[pos]:
            pos+=1
        if pos==len(st):
            break
    # print(pos)
    return "YES" if pos==len(st) else "NO"

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)
        print(result)
