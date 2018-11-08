#https://www.hackerrank.com/challenges/the-time-in-words/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign



# Complete the timeInWords function below.
def timeInWords(h, m):
    glos={
        1:"one",
        2:"two",
        3:"three",
        4:"four",
        5:"five",
        6:"six",
        7:"seven",
        8:"eight",
        9:"nine",
        10:"ten",
        11:"eleven",
        12:"twelve",
        13:"thirteen",
        14:"fourteen",
        16:"sixteen",
        17:"seventeen",
        18:"eighteen",
        19:"ninteen",
        20:"twenty"
    }
    s=""
    next=h+1 if h+1<=12 else 1
    if m<30:
        if m==0:
            s=glos[h]+" o' clock"
        elif m==15:
            s="quarter past "+glos[h]
        elif m==1:
            s="one minute past "+glos[h]
        else:
            if m>20:
                s="twenty "+glos[m-20]+" minutes past "+glos[h]
            else:
                s=glos[m]+" minutes past "+glos[h]
    elif m==30:
        s="half past "+glos[h]
    else:
        if m==45:
            s="quarter to "+glos[next]
        elif m==59:
            s="one minute to "+glos[next]
        else:
            rem=60-m
            if rem>20:
                s="twenty "+glos[rem-20]+" minutes to "+glos[next]
            else:
                s=glos[rem]+" minutes to "+glos[next]
    return s


if __name__ == '__main__':

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    print(result)