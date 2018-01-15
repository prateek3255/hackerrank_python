#https://www.hackerrank.com/challenges/grading/problem

# import sys

def solve(grades):
    result=[]
    for i in grades:
        if i>=38 and i<100:
            if (i+1)%5==0:
                result.append(i+1)
            elif (i+2)%5==0:
                result.append(i+2)
            else:
                result.append(i)
        else:
            result.append(i)
    result.sort()
    return result

        

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
    grades_t = int(input().strip())
    grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))