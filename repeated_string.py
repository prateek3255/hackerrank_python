#https://www.hackerrank.com/challenges/repeated-string/problem
s=input()
n=int(input())

f=s.count('a')
no_of_strings=int(n/len(s))

chars_in_infinite=f*no_of_strings
rem=n%len(s)
rem_chars=s[0:rem].count('a')

print(chars_in_infinite+rem_chars)

